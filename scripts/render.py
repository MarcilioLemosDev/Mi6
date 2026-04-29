#!/usr/bin/env python3
"""LOGUS render — reads PROJECT.md, generates /public/{status,sprint,health}.html"""

import re
import argparse
from pathlib import Path
from datetime import datetime
from html import escape

DEFAULT_ROOT = Path(__file__).parent.parent


def parse_sections(text: str) -> dict:
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


def html_escape(value) -> str:
    return escape(str(value or ""), quote=True)


def parse_tables(text: str) -> list:
    tables = []
    rows = []
    headers = []

    def flush():
        nonlocal rows, headers
        if headers:
            tables.append((headers, rows))
        rows = []
        headers = []

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            flush()
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not headers:
            headers = cells
        elif all(re.fullmatch(r":?-+:?", c) for c in cells if c):
            continue
        else:
            rows.append(dict(zip(headers, cells)))
    flush()
    return tables


def parse_table(text: str, required_headers=None) -> list:
    for headers, rows in parse_tables(text):
        if required_headers is None or all(header in headers for header in required_headers):
            return rows
    return []


def _scalar(section: str, label: str) -> str:
    for line in section.splitlines():
        if line.startswith(f"**{label}:**"):
            return line.replace(f"**{label}:**", "").strip().strip("`")
    return ""


# ── /status ──────────────────────────────────────────────────────────────────

def build_status(sections: dict) -> str:
    mapa_rows = parse_table(sections.get("MAPA", ""), ["#", "Épico", "Status"])

    epics_html = ""
    for row in mapa_rows:
        status_val = row.get("Status", "[ ]").strip()
        if status_val == "[x]":
            cls, label = "done", "concluído"
        elif status_val == "[~]":
            cls, label = "progress", "em andamento"
        else:
            cls, label = "pending", "pendente"
        num = html_escape(row.get("#", ""))
        name = html_escape(row.get("Épico", ""))
        epics_html += (
            f'<div class="epic {cls}">'
            f'<span class="num">{num}</span>'
            f'<span class="name">{name}</span>'
            f'<span class="badge">{label}</span>'
            f'</div>\n'
        )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Status do Projeto</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f8f9fa;color:#1a1a2e;min-height:100vh}}
  .header{{background:#1a1a2e;color:#fff;padding:2rem}}
  .header h1{{font-size:1.5rem;font-weight:600;margin-bottom:.25rem}}
  .header p{{font-size:.875rem;opacity:.6}}
  .content{{max-width:640px;margin:2rem auto;padding:0 1rem}}
  .section-title{{font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:#888;margin-bottom:1rem}}
  .epic{{display:flex;align-items:center;gap:.75rem;padding:1rem;background:#fff;border-radius:8px;margin-bottom:.5rem;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
  .epic.done{{border-left:3px solid #22c55e}}
  .epic.progress{{border-left:3px solid #3b82f6}}
  .epic.pending{{border-left:3px solid #e2e8f0}}
  .num{{font-size:.75rem;color:#aaa;min-width:2rem}}
  .name{{flex:1;font-size:.95rem}}
  .badge{{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;padding:.2rem .5rem;border-radius:4px}}
  .done .badge{{background:#dcfce7;color:#15803d}}
  .progress .badge{{background:#dbeafe;color:#1d4ed8}}
  .pending .badge{{background:#f1f5f9;color:#94a3b8}}
  .footer{{text-align:center;padding:2rem;font-size:.75rem;color:#ccc}}
</style>
</head>
<body>
<div class="header">
  <h1>Status do Projeto</h1>
  <p>Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} · Framework LOGUS</p>
</div>
<div class="content">
  <p class="section-title">Mapa de Épicos</p>
  {epics_html}
</div>
<div class="footer">logus-template · awake software</div>
</body>
</html>"""


# ── /sprint ───────────────────────────────────────────────────────────────────

def build_sprint(sections: dict) -> str:
    sprint_section = sections.get("SPRINT ATUAL", "")
    sprint_id = html_escape(_scalar(sprint_section, "Sprint"))
    conquista = html_escape(_scalar(sprint_section, "Conquista"))

    tasks = parse_table(sprint_section, ["ID", "Task", "Critério de aceite", "Status"])
    cols = {"todo": [], "doing": [], "bloqueado": [], "done": []}
    for t in tasks:
        status = t.get("Status", "todo").strip().lower()
        if status not in cols:
            status = "todo"
        cols[status].append(t)

    def col_html(title, color, tasks_list):
        items = ""
        for t in tasks_list:
            tid = html_escape(t.get("ID", ""))
            task_name = html_escape(t.get("Task", ""))
            aceite = html_escape(t.get("Critério de aceite", ""))
            items += (
                f'<div class="card">'
                f'<div class="card-id">{tid}</div>'
                f'<div class="card-name">{task_name}</div>'
                f'<div class="card-aceite">{aceite}</div>'
                f'</div>\n'
            )
        count = len(tasks_list)
        return (
            f'<div class="col">'
            f'<div class="col-header" style="border-top:3px solid {color}">'
            f'<span>{title}</span><span class="count">{count}</span></div>'
            f'{items}</div>'
        )

    board = (
        col_html("A fazer", "#e2e8f0", cols["todo"]) +
        col_html("Em andamento", "#3b82f6", cols["doing"]) +
        col_html("Bloqueado", "#ef4444", cols["bloqueado"]) +
        col_html("Concluído", "#22c55e", cols["done"])
    )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sprint {sprint_id}</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f0f2f5;color:#1a1a2e;min-height:100vh}}
  .header{{background:#1a1a2e;color:#fff;padding:1.5rem 2rem}}
  .header h1{{font-size:1.25rem;font-weight:600}}
  .header p{{font-size:.875rem;opacity:.5;margin-top:.25rem}}
  .conquista{{background:#fff;border-left:4px solid #3b82f6;margin:1.5rem 2rem;padding:.875rem 1rem;border-radius:0 8px 8px 0;font-size:.9rem;color:#334155}}
  .board{{display:flex;gap:1rem;padding:0 1.5rem 2rem;overflow-x:auto}}
  .col{{min-width:220px;flex:1}}
  .col-header{{background:#fff;padding:.75rem 1rem;border-radius:8px 8px 0 0;display:flex;justify-content:space-between;align-items:center;font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:#64748b}}
  .count{{background:#f1f5f9;color:#94a3b8;font-size:.7rem;padding:.1rem .4rem;border-radius:10px}}
  .card{{background:#fff;border-radius:0 0 6px 6px;margin-bottom:.5rem;padding:.75rem 1rem;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
  .card-id{{font-size:.65rem;color:#aaa;font-weight:600;margin-bottom:.25rem}}
  .card-name{{font-size:.875rem;color:#1e293b;margin-bottom:.375rem}}
  .card-aceite{{font-size:.75rem;color:#94a3b8;font-style:italic}}
</style>
</head>
<body>
<div class="header">
  <h1>Sprint {sprint_id}</h1>
  <p>Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
</div>
<div class="conquista">Conquista: {conquista}</div>
<div class="board">
  {board}
</div>
</body>
</html>"""


# ── /health ───────────────────────────────────────────────────────────────────

def build_health(sections: dict) -> str:
    rows = parse_table(sections.get("AUDITORIAS", ""), ["Sprint", "Data", "Crítico", "Alto", "Médio", "Baixo"])

    def to_int(val):
        try:
            return int(val or 0)
        except (ValueError, TypeError):
            return 0

    totals = [
        to_int(r.get("Crítico")) + to_int(r.get("Alto")) +
        to_int(r.get("Médio")) + to_int(r.get("Baixo"))
        for r in rows
    ]
    max_total = max(totals or [1], default=1)
    if max_total == 0:
        max_total = 1

    bars_html = ""
    for r, total in zip(rows, totals):
        sprint = html_escape(r.get("Sprint", ""))
        date = html_escape(r.get("Data", ""))
        critico = to_int(r.get("Crítico"))
        alto = to_int(r.get("Alto"))
        medio = to_int(r.get("Médio"))
        baixo = to_int(r.get("Baixo"))
        height = max(4, int((total / max_total) * 160))

        segs = ""
        for val, color, lbl in [
            (critico, "#ef4444", "crítico"),
            (alto, "#f97316", "alto"),
            (medio, "#eab308", "médio"),
            (baixo, "#94a3b8", "baixo"),
        ]:
            if val and total:
                h = max(1, int((val / total) * height))
                segs += f'<div title="{val} {lbl}" style="height:{h}px;background:{color};width:100%"></div>'

        if not segs:
            segs = '<div style="height:4px;background:#e2e8f0;width:100%"></div>'

        bars_html += (
            f'<div class="bar-wrap">'
            f'<div class="bar-col">{segs}</div>'
            f'<div class="bar-label">{sprint}</div>'
            f'<div class="bar-date">{date}</div>'
            f'</div>'
        )

    legend = "".join(
        f'<span class="leg-item"><span class="leg-dot" style="background:{c}"></span>{l}</span>'
        for c, l in [("#ef4444", "crítico"), ("#f97316", "alto"), ("#eab308", "médio"), ("#94a3b8", "baixo")]
    )

    total_sprints = len(rows)
    sum_critico = sum(to_int(r.get("Crítico")) for r in rows)
    sum_alto = sum(to_int(r.get("Alto")) for r in rows)
    early_note = (
        '<p class="note">A curva começa a revelar tendência a partir do sprint 4.</p>'
        if total_sprints < 4 else ""
    )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Saúde do Projeto</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f8f9fa;color:#1a1a2e;min-height:100vh}}
  .header{{background:#1a1a2e;color:#fff;padding:2rem}}
  .header h1{{font-size:1.5rem;font-weight:600;margin-bottom:.25rem}}
  .header p{{font-size:.875rem;opacity:.6}}
  .content{{max-width:800px;margin:2rem auto;padding:0 1rem}}
  .chart{{background:#fff;border-radius:12px;padding:2rem;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
  .chart-title{{font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;color:#888;margin-bottom:1.5rem}}
  .bars{{display:flex;align-items:flex-end;gap:.75rem;min-height:180px;border-bottom:1px solid #f1f5f9;padding-bottom:.5rem}}
  .bar-wrap{{display:flex;flex-direction:column;align-items:center;gap:.25rem;flex:1}}
  .bar-col{{width:100%;display:flex;flex-direction:column-reverse;border-radius:4px 4px 0 0;overflow:hidden;min-height:4px}}
  .bar-label{{font-size:.7rem;font-weight:600;color:#64748b}}
  .bar-date{{font-size:.6rem;color:#cbd5e1}}
  .legend{{display:flex;gap:1rem;margin-top:1rem;flex-wrap:wrap}}
  .leg-item{{display:flex;align-items:center;gap:.35rem;font-size:.75rem;color:#64748b}}
  .leg-dot{{width:8px;height:8px;border-radius:50%}}
  .note{{margin-top:1rem;font-size:.75rem;color:#94a3b8;font-style:italic}}
  .stats{{display:flex;gap:1rem;margin-top:1.5rem}}
  .stat{{background:#fff;border-radius:8px;padding:1rem 1.25rem;flex:1;box-shadow:0 1px 3px rgba(0,0,0,.06)}}
  .stat-val{{font-size:1.5rem;font-weight:700;color:#1a1a2e}}
  .stat-label{{font-size:.75rem;color:#94a3b8;margin-top:.25rem}}
</style>
</head>
<body>
<div class="header">
  <h1>Saúde do Projeto</h1>
  <p>Gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')} · Framework LOGUS</p>
</div>
<div class="content">
  <div class="chart">
    <p class="chart-title">Achados por Sprint</p>
    <div class="bars">{bars_html}</div>
    <div class="legend">{legend}</div>
    {early_note}
  </div>
  <div class="stats">
    <div class="stat"><div class="stat-val">{total_sprints}</div><div class="stat-label">sprints auditados</div></div>
    <div class="stat"><div class="stat-val">{sum_critico}</div><div class="stat-label">críticos acumulados</div></div>
    <div class="stat"><div class="stat-val">{sum_alto}</div><div class="stat-label">altos acumulados</div></div>
  </div>
</div>
</body>
</html>"""


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Render LOGUS pages from PROJECT.md.")
    parser.add_argument("--root", default=DEFAULT_ROOT, help="Directory containing PROJECT.md.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    project_md = root / "PROJECT.md"
    public = root / "public"

    if not project_md.exists():
        raise FileNotFoundError(f"PROJECT.md não encontrado em {project_md}")

    text = project_md.read_text(encoding="utf-8")
    sections = parse_sections(text)

    public.mkdir(exist_ok=True)

    (public / "status.html").write_text(build_status(sections), encoding="utf-8")
    (public / "sprint.html").write_text(build_sprint(sections), encoding="utf-8")
    (public / "health.html").write_text(build_health(sections), encoding="utf-8")

    print("OK status.html")
    print("OK sprint.html")
    print("OK health.html")
    print(f"-> /public/ gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')}")


if __name__ == "__main__":
    main()
