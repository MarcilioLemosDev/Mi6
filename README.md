# logus-template

Template de repositório para projetos usando o **Framework LOGUS** — Awake Software.

---

## O que é este template

Ponto de partida para qualquer projeto Awake. Contém a estrutura completa do framework: especificação algorítmica, fonte única de verdade, sistema de auditoria adaptativa com cinco subagents, e render automático das três vistas HTML.

Baseado nos sete diálogos fundadores do LOGUS.

---

## Como usar

### 1. Clone ou use como template

```bash
git clone <este-repo> meu-projeto
cd meu-projeto
```

Ou clique em **Use this template** no GitHub.

### 2. Preencha o PROJECT.md

Leia `LOGUS.md` se quiser entender o algoritmo antes de operar o template.

Abra `PROJECT.md` e preencha os campos marcados com `<!-- PREENCHA: ... -->`:

- **NORTE** — o que o projeto entrega, para quem, e por quê
- **MAPA** — épicos em ordem lógica
- **STACK** — tecnologias e versões
- **SPRINT ATUAL** — conquista do primeiro sprint, baseline e tasks com critério de aceite
- **CLIENTE** — dados de contato

As demais seções são preenchidas ao longo do projeto.

### 3. Gere as páginas

```bash
python scripts/validate.py --mode auto
python scripts/render.py
```

Abre `/public/status.html`, `/public/sprint.html`, `/public/health.html` no browser.

Use `python scripts/validate.py --mode project` antes de auditar um projeto real. Esse modo exige campos preenchidos, baseline, sprint de 3 dias, gatilhos, receita de auditoria e tasks válidas.

### 4. Configure o deploy automático

No GitHub: **Settings → Pages → Source → GitHub Actions**.

A partir daí, cada push que toca `PROJECT.md` ou `audits/` regenera e publica as três páginas.

---

## Estrutura do repositório

```
├── PROJECT.md                    # Fonte única da verdade
├── LOGUS.md                      # Especificação algorítmica do framework
├── audits/
│   └── AUDIT-S00.md             # Auditoria por sprint (gerada ao fim de cada um)
├── .claude/agents/
│   ├── sentinela.md              # Segurança e estabilidade
│   ├── cacador.md                # Bugs, débito técnico e edge cases
│   ├── otimizador.md             # Performance, eficiência e clareza
│   ├── verificador-spec.md       # Critérios de aceite
│   └── verificador-trajetoria.md # Mutações não declaradas
├── scripts/
│   ├── render.py                 # Gera /public/ a partir do PROJECT.md
│   └── validate.py               # Valida estrutura e estado LOGUS antes do render/auditoria
└── .github/workflows/
    └── render.yml                # Dispara render a cada push relevante
```

`/public/` não entra no repositório — é gerada e publicada pelo GitHub Actions.

---

## Ciclo de um sprint

```
1. Preenche SPRINT ATUAL no PROJECT.md (conquista + datas + baseline + tasks + receita de auditoria)
2. Desenvolve
3. Ao fim do sprint, roda os cinco subagents em contextos isolados
4. Consolida achados em audits/AUDIT-SXX.md
5. Atualiza tabela AUDITORIAS no PROJECT.md
6. Decide destino de cada achado (task / aceita / backlog)
7. Push → páginas regeneram automaticamente
```

---

## As três vistas

| Vista | URL | Leitor | Pergunta respondida |
|-------|-----|--------|---------------------|
| `/status` | `/public/status.html` | Cliente | Onde estamos? |
| `/sprint` | `/public/sprint.html` | Dev | O que rola agora? |
| `/health` | `/public/health.html` | Dev | Como é a tendência? |

---

## Auditoria de mecanização

Se o humano precisar lembrar um princípio do LOGUS, isso não é falha humana; é falha de mecanização.

Quando acontecer, rode `/auditoria-mecanizacao` e transforme a descoberta em gatilho, validação, artefato, checkpoint visual ou comando.

---

## Checkpoint visual

Ao fim de cada task, rode validação e render, então abra as vistas relevantes:

```bash
python scripts/validate.py --mode project
python scripts/render.py
```

O humano deve ver o avanço em `/sprint` e, quando afetar percepção externa, também em `/status`.

---

## Cadência curta (entre tasks)

No início de cada sessão, antes de tocar código, o Claude Code lê o PROJECT.md e pergunta:

> *A hipótese que entrou nesta task ainda é verdade?*

Se sim, segue. Se não, pausa e atualiza o PROJECT.md antes de continuar.

## Desdobramento natural direcionado

O LOGUS não depende do humano lembrar o fluxo. Todo ciclo deve terminar em desdobramento natural direcionado: seguir a task, corrigir o `PROJECT.md`, pausar, aceitar mutação, mover algo para backlog ou escolher o próximo sprint.

Se o humano precisar lembrar que faltou desdobramento, checkpoint ou decisão, rode `/auditoria-mecanizacao` e transforme a falha em gatilho, validação, comando ou ponto de peso explícito.

---

## Referência — vocabulário LOGUS

| Termo | Significado |
|-------|-------------|
| Artefato | Documento, código ou registro que tornou consciente um algoritmo |
| Sprint atômico | Pacote entregável de 3 dias, indivisível |
| Cadência curta | Checagem entre tasks ou no início de cada sessão |
| Cadência longa | Auditoria ao fim de cada sprint |
| Mutação | Mudança detectada na varredura entre estado atual e último estado validado |
| Baseline | Commit ou tag que congela o estado validado no início do sprint |
| Auditoria adaptativa | Cinco varreduras com profundidade ajustada ao sprint |
| PROJECT.md | Fonte única da verdade do projeto |
| Render automático | Três páginas HTML geradas do PROJECT.md |
| Desdobramento natural direcionado | O fim de um ciclo aponta naturalmente a próxima decisão necessária |
