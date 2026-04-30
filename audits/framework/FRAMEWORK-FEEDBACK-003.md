# FRAMEWORK-FEEDBACK-003 - Invariante do agente vs modo de operacao

**Data:** 2026-04-30
**Origem:** AUDIT-S01, achado 5 do Verificador de Trajetoria
**Projeto-folha:** Mi6
**Tronco alvo:** logus-template
**Status:** mergeado
**Link remoto:** https://github.com/MarcilioLemosDev/logus-template/commit/84e5eff8fd1aeb5a9870724c48a9ee1626003d78

---

## Evidencia local

O achado 5 da `AUDIT-S01` registrou:

```text
A regra `Execute apenas o processo solicitado manualmente pelo humano no terminal` esta em invariantes do agente, mas e regra do modo manual de S01. Se houver agendamento futuro, essa regra exigira reescrita do contrato do agente.
```

O humano calibrou esse achado como medio porque uma regra de modo foi promovida a invariante de identidade.

## Principio LOGUS afetado

Invariantes devem descrever identidade estavel. Modo operacional de sprint deve ficar separado da identidade do artefato.

## Risco

Projetos-folha podem cristalizar restricoes temporarias como invariantes. Depois, evolucoes naturais como agendamento, runner ou automacao parecem violar o contrato do agente, mesmo quando deveriam apenas mudar o modo de operacao.

## Correcao proposta no tronco

Adicionar orientacao ao `logus-template` para separar:

- identidade e limites permanentes do agente;
- modo operacional vigente no sprint;
- regras transitorias da execucao manual;
- condicoes para promover regra temporaria a invariante.

Arquivos provaveis:

- `LOGUS.md`
- `CLAUDE.md`
- `README.md`
- futuro template de agente, se o tronco passar a fornecer um.

## Fechamento

Fechado pelo commit `84e5eff8fd1aeb5a9870724c48a9ee1626003d78` no `logus-template`.
