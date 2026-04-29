# MECHANIZATION-002 — Auditoria de Mecanização LOGUS

**Data:** 2026-04-29
**Origem:** O humano apontou que não quer lembrar o fluxo; espera que o trabalho se desdobre naturalmente até checkpoints e decisões inevitáveis.
**Pergunta central:** O que no LOGUS ainda depende de memória, boa vontade ou interpretação da IA?

---

## Achado

| Impacto | Tipo | Princípio escrito | Evidência da falha | Risco | Mecanização aplicada | Destino |
|---------|------|-------------------|--------------------|-------|----------------------|---------|
| alto | desdobramento natural direcionado | A IA executa regra mecânica; o humano decide peso. Todo ciclo deve terminar apontando o próximo ponto de decisão humana. | O humano precisou explicar que deseja conferir andamento, dar `ok` no terminal e ser conduzido a decisões, sem lembrar que faltou etapa. | O fluxo vira fiscalização manual; checkpoints e decisões dependem da memória do humano, quebrando o próprio controle de trajetória. | Adicionada identidade macro/micro; criado invariante de próximo ponto de decisão; atualizado gatilho de fim de task; criado gatilho de fim de ciclo operacional; comandos passam a terminar com decisão concreta; validação bloqueia linguagem aspiracional no protocolo. | task-próximo-sprint |

---

## Correções aplicadas

- `LOGUS.md`: explicita que o LOGUS é operação, não linguagem aspiracional; adiciona identidade macro/micro e invariantes de desdobramento natural direcionado.
- `PROJECT.md`: template passa a exigir checkpoint de fim de task com `ok` e gatilho de fim de ciclo operacional.
- `CLAUDE.md`: instruções do Claude passam a exigir desdobramento natural direcionado e próximo ponto explícito.
- `.claude/commands/cadencia-curta.md`: a saída agora apresenta a próxima task e pede decisão concreta.
- `.claude/commands/auditoria-sprint.md`: fechamento reforçado com próximo ponto obrigatório.
- `.claude/commands/auditoria-mecanizacao.md`: ausência de desdobramento vira gatilho explícito.
- `scripts/validate.py`: validação passa a exigir o gatilho `Fim de ciclo operacional` e bloqueia termos aspiracionais em arquivos de protocolo.
- `README.md`: documentação pública registra desdobramento natural direcionado como parte do framework.

---

## Resumo

- **Crítico:** 0
- **Alto:** 1
- **Médio:** 0
- **Baixo:** 0

**Regra que ficou mais difícil de ignorar:** todo ciclo operacional deve terminar colocando o humano diante do próximo ponto de decisão.

**Próximo ponto de decisão humana:** confirmado pelo humano o nome `Desdobramento natural direcionado` para o princípio fundador que fecha ciclos LOGUS.
