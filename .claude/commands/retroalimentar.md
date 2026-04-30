# /retroalimentar

Executa o Dialogo VIII do Framework LOGUS: retorno de escala folha -> tronco.

Use quando uma falha observada em projeto-folha indicar melhoria reutilizavel no `logus-template`.

## Pre-condicao

Leia:
- `dialogos/VIII-retroalimentacao-de-escala.md`
- `PROJECT.md`
- `LOGUS.md`
- `CLAUDE.md`
- comando, auditoria ou arquivo relacionado a falha

Se a falha pertencer so ao produto, nao execute retorno de escala. Registre no `BACKLOG` normal.

## Algoritmo

1. Classifique a origem:
   - `Produto`: pertence so ao projeto-folha.
   - `Framework`: deve melhorar o `logus-template`.
   - `Misto`: produto sofre o sintoma; framework precisa de correcao.

2. Se a classificacao for `Produto`, pare e proponha item de BACKLOG de produto.

3. Se for `Framework` ou `Misto`, gere um artefato local versionado:

   ```text
   audits/framework/FRAMEWORK-FEEDBACK-XXX.md
   ```

4. Use o formato:

   ```md
   # FRAMEWORK-FEEDBACK-XXX - <titulo curto>

   **Data:** YYYY-MM-DD
   **Origem:** <sprint, auditoria, task ou conversa>
   **Projeto-folha:** <repo/nome>
   **Tronco alvo:** logus-template
   **Status:** aberto | pr-aberto | mergeado | recusado
   **Link remoto:** <issue ou PR>

   ## Evidencia local

   <o que aconteceu na folha>

   ## Principio LOGUS afetado

   <regra, dialogo, comando, validacao ou documento>

   ## Risco

   <o que continua dependendo de memoria, boa vontade ou interpretacao>

   ## Correcao proposta no tronco

   <mudanca esperada no logus-template>

   ## Fechamento

   Item so fecha quando o PR for mergeado, ou quando houver decisao explicita de recusa.
   ```

5. Atualize `PROJECT.md` na subsecao:

   ```md
   ### Pendencias no framework

   - [ ] FRAMEWORK-FEEDBACK-XXX - <titulo> - status: aberto - PR/issue: <link>
   ```

   Se a subsecao nao existir, crie dentro de `## BACKLOG`, sem criar nova secao `##`.

6. Prepare a acao remota no tronco, sem publicar automaticamente:
   - se a correcao for clara, prepare corpo de PR;
   - se ainda houver incerteza, prepare corpo de issue;
   - liste arquivos provaveis do `logus-template`;
   - liste validacoes necessarias.

7. So abra PR ou issue remoto se o humano confirmar explicitamente:
   - `abrir PR`
   - `abrir issue`
   - outra autorizacao equivalente e inequívoca

8. Se a execucao estiver acontecendo dentro do proprio `logus-template`, aplique a correcao local quando aprovada, mas ainda nao publique PR sem confirmacao humana.

## Corpo minimo de PR ou issue

```md
## Origem

<projeto-folha, sprint, auditoria ou conversa>

## Evidencia

<resumo objetivo da falha>

## Correcao proposta

<o que muda no logus-template>

## Arquivos provaveis

- `LOGUS.md`
- `dialogos/...`
- `.claude/commands/...`
- `scripts/validate.py`
- `PROJECT.md`
- `CLAUDE.md`
- `README.md`

## Fechamento local

Atualizar `PROJECT.md` da folha para status `pr-aberto`, `mergeado` ou `recusado`.
```

## Regra de integridade

Nao trate retorno de escala como backlog comum de produto.

Nao publique PR ou issue sem confirmacao humana explicita.

Nao marque item local como `[x]` enquanto o status nao for `mergeado` ou `recusado`.

## Saida obrigatoria

```text
Evidencia local: <arquivo>
Acao remota preparada: <PR/issue>
Estado no PROJECT.md: <item em Pendencias no framework>
Proximo ponto de decisao humana: abrir PR, abrir issue, aplicar correcao local provisoria, aguardar tronco ou pausar?
```
