#!/usr/bin/env python3
"""Validate LOGUS project structure before render or audit."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


DEFAULT_ROOT = Path(__file__).parent.parent

OFFICIAL_SECTIONS = [
    "NORTE",
    "MAPA",
    "STACK",
    "SPRINT ATUAL",
    "PRÓXIMOS",
    "BACKLOG",
    "AUDITORIAS",
    "GLOSSÁRIO",
    "CLIENTE",
]

VALID_TASK_STATUS = {"todo", "doing", "done", "bloqueado"}
VALID_EPIC_STATUS = {"[ ]", "[~]", "[x]"}
VALID_TRIGGER_TYPES = {"regra", "peso"}
VALID_DEPTHS = {"leve", "profundo"}

REQUIRED_AGENTS = {
    "Sentinela",
    "Caçador",
    "Otimizador",
    "Verificador de Spec",
    "Verificador de Trajetória",
}

REQUIRED_TRIGGERS = {
    "Início de sessão": ("regra", "IA"),
    "Início de task": ("regra", "IA"),
    "Fim de task": ("regra", "IA"),
    "Fim de ciclo operacional": ("regra", "IA"),
    "Fim de sprint": ("regra", "IA"),
    "Fim de auditoria": ("regra", "IA"),
    "Falha de fluxo percebida": ("regra", "IA"),
    "Destino de achado": ("peso", "humano"),
    "Mutação macro": ("peso", "humano"),
}

PROTOCOL_FILES = [
    "LOGUS.md",
    "CLAUDE.md",
    "README.md",
    ".claude/commands/cadencia-curta.md",
    ".claude/commands/auditoria-sprint.md",
    ".claude/commands/auditoria-mecanizacao.md",
]

WEAK_PROTOCOL_TERMS = {"tenta", "tentar", "tentamos", "idealmente"}


def parse_sections(text):
    sections = {}
    current = None
    lines = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                sections[current] = "\n".join(lines).strip()
            current = line[3:].strip()
            lines = []
        elif current:
            lines.append(line)
    if current:
        sections[current] = "\n".join(lines).strip()
    return sections


def parse_tables(text):
    tables = []
    headers = []
    rows = []

    def flush():
        nonlocal headers, rows
        if headers:
            tables.append((headers, rows))
        headers = []
        rows = []

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            flush()
            continue

        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not headers:
            headers = cells
        elif all(re.fullmatch(r":?-+:?", cell) for cell in cells if cell):
            continue
        else:
            rows.append(dict(zip(headers, cells)))

    flush()
    return tables


def table_with_headers(text, required_headers):
    for headers, rows in parse_tables(text):
        if all(header in headers for header in required_headers):
            return rows
    return []


def scalar(section, label):
    prefix = f"**{label}:**"
    for line in section.splitlines():
        line = line.strip()
        if line.startswith("- "):
            line = line[2:].strip()
        if line.startswith(prefix):
            return line.replace(prefix, "", 1).strip()
    return ""


def bracket_placeholders(value):
    placeholders = []
    for match in re.findall(r"\[([^\]]*)\]", value or ""):
        content = match.strip()
        if content in {"", "~", "x"}:
            continue
        placeholders.append(match)
    return placeholders


def is_blank_or_placeholder(value):
    return not str(value or "").strip() or bool(bracket_placeholders(str(value)))


def first_date(value):
    match = re.search(r"\d{4}-\d{2}-\d{2}", value or "")
    if not match:
        return None
    try:
        return datetime.strptime(match.group(0), "%Y-%m-%d").date()
    except ValueError:
        return None


def normalize(value):
    return re.sub(r"\s+", " ", str(value or "").strip())


def collect_template_fields(sections):
    values = []

    for label in ["Produto", "Cliente", "Objetivo central", "Restrição principal"]:
        values.append(scalar(sections.get("NORTE", ""), label))

    for label in ["Linguagem", "Framework", "Banco", "Infra", "Repo", "Deploy"]:
        values.append(scalar(sections.get("STACK", ""), label))

    sprint = sections.get("SPRINT ATUAL", "")
    for label in ["Conquista", "Início", "Fim", "Baseline"]:
        values.append(scalar(sprint, label))

    for row in table_with_headers(sections.get("MAPA", ""), ["#", "Épico", "Status"]):
        values.append(row.get("Épico", ""))

    for row in table_with_headers(sprint, ["ID", "Task", "Critério de aceite", "Status"]):
        values.append(row.get("Task", ""))
        values.append(row.get("Critério de aceite", ""))

    for label in ["Nome", "Email", "Telefone/WhatsApp", "Preferência de atualização", "URL /status para o cliente"]:
        values.append(scalar(sections.get("CLIENTE", ""), label))

    return values


def is_template_skeleton(sections):
    values = collect_template_fields(sections)
    return bool(values) and all(is_blank_or_placeholder(value) for value in values)


def require_present(errors, location, value, label):
    if is_blank_or_placeholder(value):
        errors.append(f"{location}: preencha `{label}`.")


def validate_sections(sections, errors):
    found = list(sections)
    missing = [section for section in OFFICIAL_SECTIONS if section not in sections]
    extras = [section for section in found if section not in OFFICIAL_SECTIONS]

    for section in missing:
        errors.append(f"PROJECT.md: seção obrigatória ausente: `{section}`.")
    for section in extras:
        errors.append(f"PROJECT.md: seção não oficial em nível ##: `{section}`.")

    ordered_found = [section for section in found if section in OFFICIAL_SECTIONS]
    expected_order = [section for section in OFFICIAL_SECTIONS if section in sections]
    if ordered_found != expected_order:
        errors.append("PROJECT.md: as 9 seções oficiais devem manter a ordem LOGUS.")


def validate_norte_stack_cliente(sections, strict, errors):
    if not strict:
        return

    for label in ["Produto", "Cliente", "Objetivo central", "Restrição principal"]:
        require_present(errors, "NORTE", scalar(sections.get("NORTE", ""), label), label)

    for label in ["Linguagem", "Framework", "Banco", "Infra", "Repo", "Deploy"]:
        require_present(errors, "STACK", scalar(sections.get("STACK", ""), label), label)

    for label in ["Nome", "Email", "Telefone/WhatsApp", "Preferência de atualização", "URL /status para o cliente"]:
        require_present(errors, "CLIENTE", scalar(sections.get("CLIENTE", ""), label), label)


def validate_mapa(sections, strict, errors):
    rows = table_with_headers(sections.get("MAPA", ""), ["#", "Épico", "Status"])
    if not rows:
        errors.append("MAPA: tabela com cabeçalhos `# | Épico | Status` não encontrada.")
        return

    for index, row in enumerate(rows, start=1):
        status = normalize(row.get("Status", ""))
        if status not in VALID_EPIC_STATUS:
            errors.append(f"MAPA linha {index}: status `{status}` inválido; use [ ], [~] ou [x].")
        if strict and is_blank_or_placeholder(row.get("Épico", "")):
            errors.append(f"MAPA linha {index}: preencha o épico.")


def validate_sprint(sections, strict, errors):
    sprint = sections.get("SPRINT ATUAL", "")

    sprint_id = normalize(scalar(sprint, "Sprint"))
    if not re.fullmatch(r"S\d{2,}", sprint_id):
        errors.append("SPRINT ATUAL: `Sprint` deve usar formato S01, S02, ...")

    for label in ["Conquista", "Início", "Fim", "Baseline"]:
        value = scalar(sprint, label)
        if strict:
            require_present(errors, "SPRINT ATUAL", value, label)

    start_date = first_date(scalar(sprint, "Início"))
    end_date = first_date(scalar(sprint, "Fim"))
    if strict:
        if not start_date:
            errors.append("SPRINT ATUAL: `Início` deve usar YYYY-MM-DD.")
        if not end_date:
            errors.append("SPRINT ATUAL: `Fim` deve usar YYYY-MM-DD.")
        if start_date and end_date and end_date - start_date != timedelta(days=3):
            errors.append("SPRINT ATUAL: `Fim` deve estar 3 dias após `Início`.")


def validate_triggers(sections, strict, errors):
    rows = table_with_headers(sections.get("SPRINT ATUAL", ""), ["Evento", "Tipo", "Agente", "Ação"])
    if not rows:
        errors.append("SPRINT ATUAL: tabela `Gatilhos deste sprint` não encontrada.")
        return

    seen = {}
    for index, row in enumerate(rows, start=1):
        event = normalize(row.get("Evento", ""))
        trigger_type = normalize(row.get("Tipo", "")).lower()
        agent = normalize(row.get("Agente", ""))

        if trigger_type not in VALID_TRIGGER_TYPES:
            errors.append(f"Gatilhos linha {index}: tipo `{trigger_type}` inválido; use regra ou peso.")
        if strict and is_blank_or_placeholder(row.get("Ação", "")):
            errors.append(f"Gatilhos linha {index}: preencha a ação.")
        if event:
            seen[event] = (trigger_type, agent)

    if strict:
        for event, (expected_type, expected_agent) in REQUIRED_TRIGGERS.items():
            if event not in seen:
                errors.append(f"Gatilhos: evento obrigatório ausente: `{event}`.")
                continue
            actual_type, actual_agent = seen[event]
            if actual_type != expected_type:
                errors.append(f"Gatilhos `{event}`: tipo deve ser `{expected_type}`.")
            if actual_agent.lower() != expected_agent.lower():
                errors.append(f"Gatilhos `{event}`: agente deve ser `{expected_agent}`.")


def validate_recipe(sections, strict, errors):
    rows = table_with_headers(sections.get("SPRINT ATUAL", ""), ["Subagent", "Profundidade", "Justificativa"])
    if not rows:
        errors.append("SPRINT ATUAL: tabela `Receita de auditoria` não encontrada.")
        return

    agents = {normalize(row.get("Subagent", "")): row for row in rows}
    missing = REQUIRED_AGENTS - set(agents)
    for agent in sorted(missing):
        errors.append(f"Receita de auditoria: subagent obrigatório ausente: `{agent}`.")

    if strict:
        for agent, row in agents.items():
            depth = normalize(row.get("Profundidade", "")).lower()
            if depth not in VALID_DEPTHS:
                errors.append(f"Receita de auditoria `{agent}`: escolha `leve` ou `profundo`.")
            if is_blank_or_placeholder(row.get("Justificativa", "")):
                errors.append(f"Receita de auditoria `{agent}`: preencha a justificativa.")


def validate_tasks(sections, strict, errors):
    rows = table_with_headers(sections.get("SPRINT ATUAL", ""), ["ID", "Task", "Critério de aceite", "Status"])
    if not rows:
        errors.append("SPRINT ATUAL: tabela `Tasks` não encontrada.")
        return

    for index, row in enumerate(rows, start=1):
        task_id = normalize(row.get("ID", ""))
        status = normalize(row.get("Status", "")).lower()
        if not re.fullmatch(r"T\d{2,}", task_id):
            errors.append(f"Tasks linha {index}: ID `{task_id}` inválido; use T01, T02, ...")
        if status not in VALID_TASK_STATUS:
            errors.append(f"Tasks linha {index}: status `{status}` inválido.")
        if strict:
            require_present(errors, f"Tasks linha {index}", row.get("Task", ""), "Task")
            require_present(errors, f"Tasks linha {index}", row.get("Critério de aceite", ""), "Critério de aceite")


def validate_audits(sections, errors):
    rows = table_with_headers(sections.get("AUDITORIAS", ""), ["Sprint", "Data", "Crítico", "Alto", "Médio", "Baixo"])
    if not rows:
        errors.append("AUDITORIAS: tabela com histórico de auditorias não encontrada.")
        return

    for index, row in enumerate(rows, start=1):
        sprint_id = normalize(row.get("Sprint", ""))
        if not re.fullmatch(r"S\d{2,}", sprint_id):
            errors.append(f"AUDITORIAS linha {index}: sprint `{sprint_id}` inválido.")
        if not first_date(row.get("Data", "")):
            errors.append(f"AUDITORIAS linha {index}: data deve usar YYYY-MM-DD.")
        for label in ["Crítico", "Alto", "Médio", "Baixo"]:
            value = normalize(row.get(label, ""))
            if not re.fullmatch(r"\d+", value):
                errors.append(f"AUDITORIAS linha {index}: `{label}` deve ser inteiro >= 0.")


def validate_public_derivative(gitignore, errors):
    if not gitignore.exists():
        errors.append(".gitignore: arquivo ausente; `/public/` deve ser ignorado.")
        return
    ignored = {line.strip() for line in gitignore.read_text(encoding="utf-8").splitlines()}
    if "/public/" not in ignored and "public/" not in ignored:
        errors.append(".gitignore: adicione `/public/` para manter HTML como derivada.")


def validate_protocol_language(root, errors):
    for relative_path in PROTOCOL_FILES:
        path = root / relative_path
        if not path.exists():
            continue
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            normalized = line.casefold()
            for term in WEAK_PROTOCOL_TERMS:
                if re.search(rf"\b{re.escape(term)}\b", normalized):
                    errors.append(
                        f"{relative_path}:{line_number}: termo aspiracional `{term}` em arquivo de protocolo; "
                        "descreva o LOGUS como operação, regra, evidência ou mecanização."
                    )


def validate(root, mode):
    project_md = root / "PROJECT.md"
    gitignore = root / ".gitignore"

    if not project_md.exists():
        return ["PROJECT.md: arquivo não encontrado."], "missing"

    text = project_md.read_text(encoding="utf-8")
    sections = parse_sections(text)
    errors = []

    validate_sections(sections, errors)

    strict = mode == "project"
    detected_template = False
    if mode == "auto":
        detected_template = is_template_skeleton(sections)
        strict = not detected_template

    validate_norte_stack_cliente(sections, strict, errors)
    validate_mapa(sections, strict, errors)
    validate_sprint(sections, strict, errors)
    validate_triggers(sections, strict, errors)
    validate_recipe(sections, strict, errors)
    validate_tasks(sections, strict, errors)
    validate_audits(sections, errors)
    validate_public_derivative(gitignore, errors)
    validate_protocol_language(root, errors)

    effective_mode = "template" if mode == "template" or detected_template else "project"
    return errors, effective_mode


def main():
    parser = argparse.ArgumentParser(description="Validate LOGUS PROJECT.md.")
    parser.add_argument(
        "--mode",
        choices=["auto", "template", "project"],
        default="auto",
        help="auto keeps the empty template valid, project enforces filled fields.",
    )
    parser.add_argument("--root", default=DEFAULT_ROOT, help="Directory containing PROJECT.md.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors, effective_mode = validate(root, args.mode)
    if errors:
        print("LOGUS validate: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"LOGUS validate: OK ({effective_mode})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
