# Dialogo IX - Agenda de Alavancas

**Prateleira:** LOGUS / Dialogos / IX / Agenda -> Decisao
**Comando:** `/agenda-alavancas`
**Natureza:** radar de retorno, nao backlog paralelo.

**Principio:** a IA nao puxa apenas a proxima task; ela mantem uma leitura ativa das alavancas de maior retorno composto e coloca o humano diante da melhor decisao seguinte.

---

## Dialogo

**Construtor:**
Se eu so puxo tasks, posso terminar o sprint e ainda deixar valor maior na mesa.

**Pensador:**
Entao nao opere so como fila. Opere como agenda. A task diz o que foi combinado; a agenda pergunta qual alavanca aumenta mais resultado agora e mais capacidade depois.

**Construtor:**
Mas isso nao cria outra fonte de verdade?

**Pensador:**
Nao. A agenda nao decide e nao guarda verdade. Ela deriva de `PROJECT.md`, auditorias, backlog, feedbacks e estado atual. Depois apresenta peso ao humano.

**Construtor:**
Entao a IA recomenda, mas nao troca o plano sozinha.

**Pensador:**
Exato. Agenda sem decisao humana vira impulso. Task sem agenda vira execucao cega. O LOGUS precisa das duas: contrato e alavanca.

---

## Execucao

1. Ler as fontes oficiais

   A agenda deriva de:
   - `PROJECT.md`;
   - `audits/AUDIT-SXX.md`;
   - `audits/MECHANIZATION-XXX.md`;
   - `audits/framework/FRAMEWORK-FEEDBACK-XXX.md`, quando existir;
   - diff atual, somente como evidencia auxiliar.

   A agenda nao cria verdade nova. Toda decisao final precisa virar sprint, task, backlog, auditoria, feedback de framework ou pausa declarada.

2. Separar por eixo conceitual

   Classifique alavancas em cinco eixos:

   | Eixo | Pergunta |
   |------|----------|
   | Produto | O que torna o software mais util, vendavel ou essencial? |
   | Performance | O que torna o software mais rapido, barato, confiavel ou escalavel? |
   | Engenharia | O que reduz fragilidade, ambiguidade, debito ou retrabalho? |
   | Mecanizacao | O que ainda depende de memoria humana e deve virar regra, comando, validacao ou artefato? |
   | Estrategia | O que aproxima a Awake de uma vantagem composta e defensavel? |

3. Avaliar retorno esperado

   Para cada eixo, apresente no maximo uma alavanca forte:

   ```text
   Eixo: <produto | performance | engenharia | mecanizacao | estrategia>
   Alavanca: <movimento concreto>
   Evidencia: <arquivo, auditoria, backlog ou diff>
   Retorno esperado: <por que isso muda resultado>
   Custo/risco: <friccao, dependencia ou tradeoff>
   Destino possivel: sprint | task | backlog | auditoria | retroalimentar | pausa
   ```

4. Recomendar proxima decisao

   Depois de listar as alavancas, a IA recomenda uma decisao unica:

   ```text
   Recomendacao LOGUS: <alavanca escolhida>
   Motivo: <comparacao objetiva entre retorno, urgencia e dependencia>
   Proximo ponto de decisao humana: aprovar, corrigir, transformar em sprint, mover para backlog, abrir auditoria, retroalimentar ou pausar?
   ```

   Criterio superior: quando duas alavancas competirem, prefira a que gera vantagem composta para a Awake. Vantagem composta e o movimento que melhora o projeto atual e tambem aumenta capacidade futura do tronco, do time, do metodo ou do sistema.

5. Nao substituir o sprint

   Se a alavanca escolhida mudar escopo, nao execute direto. Primeiro proponha a edicao em `PROJECT.md`.

   Se a alavanca for do framework, encaminhe para `/retroalimentar`.

   Se a alavanca for falha de fluxo, encaminhe para `/auditoria-mecanizacao`.

6. Hooks minimos

   Em fim de auditoria:

   ```text
   Apos apresentar destinos e proximo sprint, apresente tambem a agenda de alavancas ou sugira /agenda-alavancas.
   ```

   Em fim de ciclo operacional:

   ```text
   Se ha mais de um caminho plausivel, use a agenda de alavancas para ordenar as opcoes antes de pedir decisao humana.
   ```

7. Saida obrigatoria

   `/agenda-alavancas` encerra com:

   ```text
   Agenda de alavancas:
   - Produto: ...
   - Performance: ...
   - Engenharia: ...
   - Mecanizacao: ...
   - Estrategia: ...

   Recomendacao LOGUS: ...
   Proximo ponto de decisao humana: ...
   ```
