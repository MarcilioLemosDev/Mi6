# FRAMEWORK-FEEDBACK-001 - Convencao de sprint de 3 dias

**Data:** 2026-04-30
**Origem:** AUDIT-S01 / backlog de encerramento da S01
**Projeto-folha:** Mi6
**Tronco alvo:** logus-template
**Status:** mergeado
**Link remoto:** https://github.com/MarcilioLemosDev/logus-template/commit/84e5eff8fd1aeb5a9870724c48a9ee1626003d78

---

## Evidencia local

O `PROJECT.md` da folha usa:

```text
Inicio: 2026-04-30
Fim: 2026-05-03
```

O `scripts/validate.py` do LOGUS valida esse intervalo porque exige `Fim - Inicio == 3 dias`.

A ambiguidade apareceu no backlog da S01: "decidir e mecanizar a convencao de duracao do sprint atomico: manter `Fim = Inicio + 3 dias` como 4 dias de calendario e declarar explicitamente no LOGUS, ou alterar `validate.py` conforme a convencao escolhida."

## Principio LOGUS afetado

Sprint atomico de 3 dias.

## Risco

Cada projeto-folha pode interpretar "3 dias" de forma diferente: tres dias inclusivos, tres noites, ou `Fim = Inicio + 3 dias`. A validacao mecaniza uma interpretacao, mas a linguagem do protocolo ainda permite duvida.

## Correcao proposta no tronco

Declarar explicitamente no `logus-template` a convencao operacional:

- `Inicio` e `Fim` sao datas de limite do sprint;
- sprint atomico de 3 dias usa `Fim = Inicio + 3 dias`;
- a regra representa janela operacional validada por `scripts/validate.py`.

Arquivos provaveis:

- `LOGUS.md`
- `PROJECT.md`
- `README.md`
- `scripts/validate.py` se a convencao escolhida mudar.

## Fechamento

Fechado pelo commit `84e5eff8fd1aeb5a9870724c48a9ee1626003d78` no `logus-template`.
