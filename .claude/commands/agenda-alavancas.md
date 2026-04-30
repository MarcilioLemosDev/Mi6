# /agenda-alavancas

Executa o Dialogo IX do Framework LOGUS: agenda derivada de alavancas de maior retorno composto.

Use quando houver mais de um caminho plausivel, fim de sprint, fim de auditoria, fim de ciclo operacional ou decisao estrategica entre produto, performance, engenharia, mecanizacao e estrategia.

## Pre-condicao

Leia:
- `dialogos/IX-agenda-de-alavancas.md`
- `PROJECT.md`
- auditorias em `audits/`
- `audits/framework/`, se existir
- diff atual, somente como evidencia auxiliar

Nao trate a agenda como fonte de verdade. A agenda recomenda; o humano decide peso.

## Algoritmo

1. Extraia o estado declarado:
   - NORTE
   - MAPA
   - SPRINT ATUAL
   - PROXIMOS
   - BACKLOG
   - AUDITORIAS

2. Leia achados recentes:
   - ultimo `AUDIT-SXX.md`;
   - ultimas `MECHANIZATION-XXX.md`;
   - `FRAMEWORK-FEEDBACK-XXX.md` aberto ou recem-fechado.

3. Classifique ate uma alavanca por eixo:

   | Eixo | Pergunta |
   |------|----------|
   | Produto | O que torna o software mais util, vendavel ou essencial? |
   | Performance | O que torna o software mais rapido, barato, confiavel ou escalavel? |
   | Engenharia | O que reduz fragilidade, ambiguidade, debito ou retrabalho? |
   | Mecanizacao | O que ainda depende de memoria humana e deve virar regra, comando, validacao ou artefato? |
   | Estrategia | O que aproxima a Awake de uma vantagem composta e defensavel? |

4. Para cada eixo com alavanca real, apresente:

   ```text
   Eixo:
   Alavanca:
   Evidencia:
   Retorno esperado:
   Custo/risco:
   Destino possivel:
   ```

5. Escolha uma recomendacao LOGUS.

   Criterios:
   - vantagem composta para a Awake;
   - maior retorno esperado;
   - menor dependencia externa;
   - maior desbloqueio de trabalho futuro;
   - maior reducao de memoria humana;
   - maior alinhamento ao NORTE.

   Quando duas alavancas competirem, prefira a que melhora o projeto atual e tambem aumenta capacidade futura do tronco, do time, do metodo ou do sistema.

6. Se a recomendacao alterar escopo, proponha edicao no `PROJECT.md` antes de executar.

7. Se a recomendacao for do framework, encaminhe para `/retroalimentar`.

8. Se a recomendacao for falha de fluxo, encaminhe para `/auditoria-mecanizacao`.

## Regra de integridade

Nao crie backlog paralelo.

Nao altere sprint, task ou backlog sem decisao humana.

Nao apresente lista longa. A agenda deve caber em cinco alavancas e uma recomendacao.

## Saida obrigatoria

```text
Agenda de alavancas:
- Produto: ...
- Performance: ...
- Engenharia: ...
- Mecanizacao: ...
- Estrategia: ...

Recomendacao LOGUS: ...
Proximo ponto de decisao humana: aprovar, corrigir, transformar em sprint, mover para backlog, abrir auditoria, retroalimentar ou pausar?
```
