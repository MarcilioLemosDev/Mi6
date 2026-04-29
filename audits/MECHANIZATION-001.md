# MECHANIZATION-001 — Auditoria de Mecanização LOGUS

**Data:** 2026-04-29
**Origem:** O humano percebeu que, após fechamento de uma auditoria de sprint, a IA não guiou o próximo ponto de decisão.
**Pergunta central:** O que no LOGUS ainda depende de memória, boa vontade ou interpretação da IA?

---

## Achado

| Impacto | Tipo | Princípio escrito | Evidência da falha | Risco | Mecanização aplicada | Destino |
|---------|------|-------------------|--------------------|-------|----------------------|---------|
| alto | ponto de peso humano | Regra é mecânica; peso é julgamento humano. A IA deve apresentar o próximo ponto de peso. | Após uma auditoria de sprint, a IA reportou fechamento, mas não apresentou a decisão do próximo sprint até o humano apontar. | O framework avança por execução, mas perde condução estratégica; descobertas dependem da percepção do humano. | Adicionados gatilhos `Fim de auditoria` e `Falha de fluxo percebida`; criado `/auditoria-mecanizacao`; atualizado `/auditoria-sprint` para não encerrar sem próxima decisão. | task-próximo-sprint |

---

## Correções aplicadas

- `LOGUS.md`: adicionados gatilhos de fim de auditoria e falha de fluxo percebida.
- `PROJECT.md`: template atualizado com os gatilhos de meta-fluxo.
- `scripts/validate.py`: validação passa a exigir esses gatilhos em modo project.
- `.claude/commands/auditoria-mecanizacao.md`: novo comando operacional.
- `.claude/commands/auditoria-sprint.md`: fechamento agora deve apresentar o próximo ponto de peso.
- `CLAUDE.md` e `README.md`: falha de mecanização documentada como evento oficial.

---

## Resumo

- **Crítico:** 0
- **Alto:** 1
- **Médio:** 0
- **Baixo:** 0

**Regra que ficou mais difícil de ignorar:** se o humano precisou lembrar um princípio do LOGUS, a IA deve rodar auditoria de mecanização antes de continuar o projeto.
