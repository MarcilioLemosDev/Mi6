# /auditoria-mecanizacao

Executa a auditoria interna do LOGUS quando um princípio escrito não foi disparado pelo fluxo.

## Gatilho

Use quando:
- o humano disser que sentiu falta de um desdobramento, checkpoint, decisão ou visualização
- a IA perceber que uma regra do `LOGUS.md`, `CLAUDE.md` ou `PROJECT.md` ficou dependente de memória
- uma falha de fluxo aparecer durante execução de sprint, auditoria ou render
- a IA encerrar um ciclo sem apresentar o próximo ponto de decisão humana

Exemplos:
- "senti falta de você guiar o fluxo"
- "isso não deveria ser automático?"
- "por que dependi da minha percepção?"
- "isso está no framework mas não aconteceu"

## Pergunta central

> O que no LOGUS ainda depende de memória, boa vontade ou interpretação da IA?

## Algoritmo

1. Leia `LOGUS.md`, `CLAUDE.md`, `PROJECT.md` e o comando/agente relacionado à falha.
2. Identifique o princípio escrito que não foi mecanizado.
3. Classifique onde faltou mecanismo:
   - gatilho
   - validação
   - artefato
   - checkpoint visual
   - ponto de peso humano
   - desdobramento natural direcionado
   - comando/agente
4. Produza um achado com:
   - princípio escrito
   - evidência da falha
   - risco
   - mecanização recomendada
   - ação aplicável agora
5. Se a ação for mecânica e segura, aplique imediatamente.
6. Gere `audits/MECHANIZATION-XXX.md`, sem substituir auditorias de sprint.
7. Ao final, apresente o próximo ponto de peso ao humano.
8. Se a falha envolveu ausência de desdobramento, atualize também a regra que encerra o ciclo afetado.
9. Se a mecanização necessária pertencer ao `logus-template` e a execução estiver ocorrendo em projeto-folha, encaminhe para `/retroalimentar` antes de encerrar.

## Regra de integridade

Não trate falha de mecanização como culpa humana. Se o humano precisou lembrar, o framework ainda não estava explícito o bastante.

Não encerre sem responder:

```text
Que regra ficou mais difícil de ignorar depois desta auditoria?
```

E não encerre sem apresentar:

```text
Próximo ponto de decisão humana:
```
