# /cadencia-curta

Executa a cadência curta do Framework LOGUS — Diálogo II.

## Algoritmo

1. Leia `PROJECT.md` seção `SPRINT ATUAL`
2. Extraia todas as tasks com status `todo` ou `doing`
3. Se não houver sprint definido (campos ainda são placeholder), informe: "Sprint não definido em PROJECT.md. Preencha SPRINT ATUAL antes de executar cadência curta." Pare.
4. Se `Baseline` estiver vazio ou placeholder, informe: "Baseline não definido. Registre o commit ou tag validado no início do sprint antes de tocar código." Pare.
5. Leia a tabela "Gatilhos deste sprint" para respeitar a divisão entre regra e peso.
6. Para cada task, exiba: ID, descrição, critério de aceite, status atual
7. Pergunte ao humano:

   > A hipótese dessas tasks ainda é verdade? Para cada uma, confirme (s) ou sinalize que mudou (n + o que mudou).

8. Se o humano confirmar tudo:
   - responda "Cadência curta OK. Hipóteses validadas."
   - apresente a próxima task `todo` ou `doing`
   - pergunte: "Próximo ponto de decisão: iniciar/continuar esta task agora? Responda `ok` para seguir, ou indique correção."
   - aguarde o humano
9. Se o humano sinalizar mudança em alguma task:
   - Liste o que mudou
   - Proponha edição específica no `PROJECT.md` (critério de aceite, descrição, ou remoção da task)
   - Aguarde aprovação
   - Edite `PROJECT.md` conforme aprovado
   - Confirme: "PROJECT.md atualizado. Estado validado."
   - apresente o próximo ponto de decisão antes de encerrar

## Regra de tempo

Deve completar em menos de 2 minutos de interação. Se as mudanças forem complexas, sinalize: "Mudança grande detectada — pode ser mutação de escopo. Considere registrar no BACKLOG antes de ajustar o sprint."

## Regra de desdobramento

Não encerre a cadência curta com uma autorização genérica. A saída deve deixar o humano diante de uma decisão concreta: seguir a task atual, corrigir o `PROJECT.md`, pausar ou mover a mudança para backlog.
