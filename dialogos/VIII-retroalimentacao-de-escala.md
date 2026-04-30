# Dialogo VIII - Retroalimentacao de escala

**Prateleira:** LOGUS / Dialogos / VIII / Folha -> Tronco
**Comando:** `/retroalimentar`
**Natureza:** roteamento de escala, nao nova lente de auditoria.

**Principio:** quando uma folha revela falha do framework, a evidencia fica na folha e a correcao sobe para o tronco.

---

## Dialogo

**Construtor:**
Achei uma falha que nao pertence so a este projeto. Se eu corrigir aqui, resolvo o sintoma local, mas o framework continua esquecendo.

**Pensador:**
Entao nao trate como backlog de produto. Trate como retorno de escala. A folha guarda a evidencia; o tronco recebe a correcao.

**Construtor:**
Preciso abrir PR direto no `logus-template`?

**Pensador:**
So com confirmacao humana explicita. Primeiro gere o artefato local, amarre no `PROJECT.md` da folha e prepare a acao remota. O humano decide se sobe como PR, issue ou pausa.

**Construtor:**
Entao o Markdown local nao substitui o PR.

**Pensador:**
Exato. Markdown sem PR ou issue vira aviso ignorado. PR sem Markdown vira correcao sem memoria local. O ciclo fecha com os dois: evidencia na folha, mecanismo no tronco.

---

## Execucao

1. Detectar retorno de escala

   Use `/retroalimentar` quando uma falha encontrada na folha apontar para regra, comando, validacao, template, documentacao ou agente do LOGUS.

   Exemplos:
   - regra do `LOGUS.md` dependeu de memoria;
   - `/auditoria-sprint` ou `/auditoria-mecanizacao` precisou de hook novo;
   - `PROJECT.md` exigiu campo, secao ou status nao previsto;
   - `scripts/validate.py` deveria bloquear ou exigir algo;
   - `CLAUDE.md` nao orientou a IA a agir mecanicamente.

2. Separar produto de framework

   Antes de registrar, classifique:

   ```text
   Produto: pertence so ao projeto-folha.
   Framework: deve melhorar o logus-template.
   Misto: produto sofre o sintoma; framework precisa de correcao.
   ```

   Se for produto, segue o `BACKLOG` normal. Se for framework ou misto, continue este dialogo.

3. Criar artefato local na folha

   Registre em Markdown versionado no projeto-folha, em formato estavel:

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

   Local sugerido na folha:

   ```text
   audits/framework/FRAMEWORK-FEEDBACK-XXX.md
   ```

4. Amarrar ao `PROJECT.md` da folha

   Registre referencia local em `## BACKLOG`, dentro da subsecao padronizada:

   ```md
   ### Pendencias no framework

   - [ ] FRAMEWORK-FEEDBACK-001 - <titulo> - status: aberto - PR/issue: <link>
   ```

   O item so pode ser marcado como `[x]` quando o PR no tronco estiver mergeado ou a issue tiver decisao explicita de recusa.

5. Preparar acao remota no tronco

   Por padrao, `/retroalimentar` prepara o corpo de PR ou issue, mas nao publica nada sem confirmacao humana explicita.

   O PR ou issue deve conter:
   - problema observado na folha;
   - link para o Markdown local, se acessivel;
   - arquivos provaveis do tronco;
   - validacao esperada;
   - condicao de fechamento do item local.

   Se a correcao for clara, recomende PR. Se ainda houver incerteza, recomende issue.

6. Escopo provavel da correcao no tronco

   A correcao pode tocar:
   - `LOGUS.md`, se o principio ainda nao existe;
   - `dialogos/`, se um dialogo precisar nascer ou mudar;
   - `CLAUDE.md`, se a IA precisa receber uma regra operacional;
   - `.claude/commands/*.md`, se o fluxo precisa de comando ou hook;
   - `scripts/validate.py`, se a regra deve ser bloqueada mecanicamente;
   - `PROJECT.md`, se o template precisa carregar novo campo, tabela ou subsecao;
   - `README.md`, se a operacao publica do framework mudou.

7. Hooks minimos

   Em `/auditoria-sprint`:

   ```text
   Ao consolidar achados, se algum achado indicar falha reutilizavel do framework, nao classifique apenas como backlog de produto. Sinalize como retorno de escala e pergunte se deve executar /retroalimentar.
   ```

   Em `/auditoria-mecanizacao`:

   ```text
   Se a mecanizacao necessaria pertencer ao logus-template e a execucao estiver ocorrendo em projeto-folha, encaminhe para /retroalimentar antes de encerrar.
   ```

8. Validacao

   `scripts/validate.py` deve aceitar a subsecao `### Pendencias no framework` dentro de `BACKLOG`, sem alterar a lista fechada de secoes `##`.

   Em modo `project`, se existir item de framework marcado como `[x]`, o status deve ser `mergeado` ou `recusado`.

9. Caso zero

   A primeira aplicacao esperada deste dialogo vem dos achados observados no Mi6:

   - `FRAMEWORK-FEEDBACK-001` - convencao de sprint de 3 dias;
   - `FRAMEWORK-FEEDBACK-002` - baseline antes da sprint;
   - `FRAMEWORK-FEEDBACK-003` - invariante vs modo.

   Esses artefatos pertencem ao projeto-folha onde a evidencia nasceu. O `logus-template` recebe a correcao por PR ou issue confirmado pelo humano.

10. Encerramento

   `/retroalimentar` nunca encerra so dizendo que registrou.

   A saida obrigatoria e:

   ```text
   Evidencia local: <arquivo>
   Acao remota preparada: <PR/issue>
   Estado no PROJECT.md: <item em Pendencias no framework>
   Proximo ponto de decisao humana: abrir PR, abrir issue, aplicar correcao local provisoria, aguardar tronco ou pausar?
   ```
