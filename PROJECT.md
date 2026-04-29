# PROJECT.md — Fonte Única da Verdade

> Framework LOGUS · Awake Software
> Este arquivo é a verdade do projeto. Tudo o que não está aqui ainda não foi decidido.

---

## NORTE

<!-- PREENCHA: O que este projeto entrega, para quem, e por quê agora. Uma ou duas frases. -->

**Produto:** `[nome do produto]`
**Cliente:** `[nome do cliente ou "interno"]`
**Objetivo central:** `[o que o projeto entrega de concreto ao mundo]`
**Restrição principal:** `[o maior limitante — prazo, orçamento, tecnologia]`

---

## MAPA

<!-- PREENCHA: Épicos do projeto em ordem lógica. Status: [ ] pendente, [~] em andamento, [x] concluído. -->

| # | Épico | Status |
|---|-------|--------|
| E1 | `[nome do épico]` | [ ] |
| E2 | `[nome do épico]` | [ ] |
| E3 | `[nome do épico]` | [ ] |

---

## STACK

<!-- PREENCHA: Tecnologias escolhidas e por quê. Seja específico — versão importa. -->

- **Linguagem:** `[ex: Python 3.12]`
- **Framework:** `[ex: FastAPI 0.111]`
- **Banco:** `[ex: PostgreSQL 16]`
- **Infra:** `[ex: Railway / Render / VPS]`
- **Repo:** `[URL do repositório]`
- **Deploy:** `[URL de produção]`

---

## SPRINT ATUAL

<!-- PREENCHA: Conquista do sprint em uma frase. Tasks com critério de aceite objetivo. -->

**Sprint:** S01
**Conquista:** `[o que ao fim deste sprint existe que antes não existia]`
**Início:** `[YYYY-MM-DD]`
**Fim:** `[YYYY-MM-DD]` *(3 dias a partir do início)*
**Baseline:** `[commit ou tag validado no início do sprint]`

### Gatilhos deste sprint

| Evento | Tipo | Agente | Ação |
|--------|------|--------|------|
| Início de sessão | regra | IA | `/cadencia-curta` |
| Início de task | regra | IA | confirmar hipótese antes de tocar código |
| Fim de task | regra | IA | validar, renderizar, mostrar checkpoint visual e pedir `ok` para seguir |
| Fim de ciclo operacional | regra | IA | apresentar desdobramento natural direcionado para próxima decisão humana |
| Fim de sprint | regra | IA | sugerir `/auditoria-sprint` |
| Fim de auditoria | regra | IA | apresentar próximo ponto de peso ao humano |
| Falha de fluxo percebida | regra | IA | rodar `/auditoria-mecanizacao` |
| Destino de achado | peso | humano | task-próximo-sprint / aceita / backlog |
| Mutação macro | peso | humano | ajustar MAPA, BACKLOG ou SPRINT ATUAL |

### Receita de auditoria deste sprint

| Subagent | Profundidade | Justificativa |
|----------|-------------|---------------|
| Sentinela | leve / profundo | `[motivo]` |
| Caçador | profundo | sempre profundo |
| Otimizador | leve / profundo | `[profundo se sprint ≥ S03 ou mexeu em DB]` |
| Verificador de Spec | profundo | sempre profundo |
| Verificador de Trajetória | profundo | sempre profundo |

### Tasks

| ID | Task | Critério de aceite | Status |
|----|------|--------------------|--------|
| T01 | `[descrição]` | `[como saber que terminou]` | todo |
| T02 | `[descrição]` | `[como saber que terminou]` | todo |

<!-- Status: todo / doing / done / bloqueado -->

---

## PRÓXIMOS

<!-- PREENCHA: Sprints planejados após o atual. Conquista por sprint. Não detalhe tasks ainda. -->

| Sprint | Conquista planejada |
|--------|---------------------|
| S02 | `[conquista]` |
| S03 | `[conquista]` |

---

## BACKLOG

<!-- PREENCHA: Itens identificados mas não priorizados. Sem ordem obrigatória. -->

- `[item]`
- `[item]`

---

## AUDITORIAS

<!-- Atualizado automaticamente ao fim de cada sprint. Não editar manualmente. -->
<!-- render.py lê esta tabela para gerar /health. Manter formato exato. -->

| Sprint | Data | Crítico | Alto | Médio | Baixo |
|--------|------|---------|------|-------|-------|
| S00 | 2026-04-28 | 0 | 0 | 0 | 0 |

---

## GLOSSÁRIO

<!-- PREENCHA: Termos do domínio do cliente que têm significado específico neste projeto. -->

| Termo | Significado no projeto |
|-------|----------------------|
| `[termo]` | `[definição]` |

---

## CLIENTE

<!-- PREENCHA: Dados de contato e preferências de comunicação. -->

**Nome:** `[nome]`
**Email:** `[email]`
**Telefone/WhatsApp:** `[número]`
**Preferência de atualização:** `[ex: link /status toda sexta-feira]`
**URL /status para o cliente:** `[URL do deploy público]`
