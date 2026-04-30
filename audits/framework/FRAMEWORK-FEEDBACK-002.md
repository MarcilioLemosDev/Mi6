# FRAMEWORK-FEEDBACK-002 - Baseline antes da execucao da sprint

**Data:** 2026-04-30
**Origem:** AUDIT-S01, achado 3 do Verificador de Trajetoria
**Projeto-folha:** Mi6
**Tronco alvo:** logus-template
**Status:** mergeado
**Link remoto:** https://github.com/MarcilioLemosDev/logus-template/commit/84e5eff8fd1aeb5a9870724c48a9ee1626003d78

---

## Evidencia local

O achado 3 da `AUDIT-S01` registrou:

```text
O baseline declarado aponta para um estado ainda em template; a declaracao de NORTE/MAPA/SPRINT/TASKS e a execucao da S01 ficaram no mesmo intervalo de diff, reduzindo a nitidez entre plano aprovado e mudanca durante execucao.
```

Na folha, isso virou item planejado para S02 como `MECHANIZATION-003` sobre baseline de sprint.

## Principio LOGUS afetado

Baseline congela o estado validado no inicio do sprint.

## Risco

Se o baseline for registrado antes da declaracao real da sprint, a auditoria compara execucao contra template, nao contra plano aprovado. A fronteira entre planejamento, execucao e mutacao fica borrada.

## Correcao proposta no tronco

Mecanizar no `logus-template` que o baseline deve ser registrado depois de `NORTE`, `MAPA`, `STACK`, `SPRINT ATUAL`, tasks e receita de auditoria estarem preenchidos e aprovados, antes de qualquer execucao da sprint.

Arquivos provaveis:

- `LOGUS.md`
- `CLAUDE.md`
- `.claude/commands/cadencia-curta.md`
- `.claude/commands/auditoria-sprint.md`
- `PROJECT.md`
- `README.md`
- `scripts/validate.py`, se houver regra verificavel contra Git.

## Fechamento

Fechado pelo commit `84e5eff8fd1aeb5a9870724c48a9ee1626003d78` no `logus-template`.
