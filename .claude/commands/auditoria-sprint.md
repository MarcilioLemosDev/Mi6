# /auditoria-sprint

Executa a cadência longa do Framework LOGUS — Diálogos II e IV.

## Pré-condição

Leia `PROJECT.md` e extraia:
- `Sprint` (ex: S01)
- `Conquista`
- `Início` e `Fim`
- `Baseline` (commit ou tag validado no início do sprint)
- Tabela "Gatilhos deste sprint" (para respeitar regra vs peso)
- Tabela "Receita de auditoria" (profundidade de cada subagent)
- Tabela "Tasks" (para verificadores de spec e trajetória)

Antes de disparar subagents, execute:

```bash
python scripts/validate.py --mode project
```

Se a validação falhar, pare e reporte os itens ao humano. Não audite estado inválido.

Se qualquer campo obrigatório for placeholder (`[...]`), pare imediatamente com mensagem:
> "Sprint não definido em PROJECT.md. Preencha SPRINT ATUAL (conquista, datas, baseline, receita de auditoria) antes de rodar auditoria."

Não invente valores. Não assuma defaults.

---

## Algoritmo

### 1. Disparo paralelo dos 5 subagents

Dispare em **paralelo** via Agent tool, cada um com contexto isolado:

- **sentinela** — profundidade conforme receita. Escopo: código do sprint atual.
- **cacador** — sempre profundo. Escopo: código do sprint atual.
- **otimizador** — profundidade conforme receita. Escopo: código do sprint atual.
- **verificador-spec** — sempre profundo. Escopo: tasks do sprint + critérios de aceite do PROJECT.md.
- **verificador-trajetoria** — sempre profundo. Escopo: estado atual vs. Baseline declarado no início do sprint.

Aguarde todos terminarem antes de prosseguir.

### 2. Consolide achados

Agrupe todos os achados numa lista unificada ordenada por impacto:
`crítico → alto → médio → baixo`

Para cada achado: impacto | categoria | subagent | localização | descrição | sugestão

### 3. Proponha destino por classificação (Diálogo VI — regra mecânica)

Para cada achado, proponha default:
- **crítico** → `task-próximo-sprint`
- **alto** → *(pergunta ao humano — não decide)*
- **médio** → *(pergunta ao humano — não decide)*
- **baixo** → `aceita`

Apresente lista completa com defaults propostos:

```
| # | Impacto | Descrição | Destino proposto |
|---|---------|-----------|-----------------|
| 1 | crítico | ...       | task-próximo-sprint |
| 2 | alto    | ...       | ⚠ AGUARDA HUMANO |
| 3 | baixo   | ...       | aceita |
```

Pergunte ao humano:
> "Confirma os destinos acima? Responda 'ok' para confirmar em lote, ou liste os números que quer alterar com o novo destino."

**Se o humano não responder, pause. Não decida sozinho. Peso de julgamento permanece humano — Diálogo VI.**

### 4. Após confirmação humana

Produza `audits/AUDIT-S{NN}.md` com:
- Sprint, data, conquista auditada
- Receita executada (subagent + profundidade)
- Tabela de achados com destino final (não proposto — final, após confirmação)
- Resumo: crítico X, alto X, médio X, baixo X
- Campo `Decisor:` em branco para humano preencher

Onde `{NN}` = número do sprint inferido do `PROJECT.md` (S01 → AUDIT-S01.md).

### 5. Atualize PROJECT.md

Adicione linha na tabela `AUDITORIAS`:

```
| S{NN} | YYYY-MM-DD | <crítico> | <alto> | <médio> | <baixo> |
```

### 6. Reporte ao humano

Informe:
- Arquivo gerado: `audits/AUDIT-S{NN}.md`
- Linha adicionada em `PROJECT.md` seção AUDITORIAS
- Estado visual atualizado em `/health`
- Próximo ponto de peso: qual conquista entra no próximo sprint?

Apresente as opções já declaradas em `PRÓXIMOS` e uma recomendação objetiva. Não encerre a auditoria sem colocar essa decisão na frente do humano.

### 7. Próximo ponto obrigatório

Depois do relatório, a saída deve terminar com uma decisão operacional explícita:

```
Próximo ponto de decisão: qual conquista entra no próximo sprint?
Opções declaradas em PROJECT.md:
- S02: ...
- S03: ...

Recomendação LOGUS: ...
Responda com a sprint escolhida, ajuste de escopo ou pausa.
```

Se houver achado crítico destinado a `task-próximo-sprint`, destaque que ele concorre com a conquista planejada. O humano decide peso; a IA apresenta o conflito.

---

## Regras de integridade

- Nunca sobrescreva um AUDIT existente. Se `audits/AUDIT-S{NN}.md` já existir, pare e pergunte ao humano.
- Nunca edite `/public/` diretamente.
- Nunca altere a tabela AUDITORIAS sem confirmação humana dos destinos.
