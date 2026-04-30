# LOGUS — Especificação Algorítmica

> Awake Software
> O LOGUS é um sistema de controle de trajetória baseado em artefatos, comparação de estados e decisão humana explícita.

---

## Tese

O projeto já executa algoritmos antes de escrevê-los: hipóteses, decisões, atalhos, critérios, medos e acordos tácitos. O LOGUS existe para tirar esses algoritmos do silêncio e transformá-los em artefatos comparáveis.

```text
silêncio -> artefato -> execução -> evidência -> decisão -> novo artefato
```

O framework inteiro é essa operação repetida em escalas diferentes.

O LOGUS não é linguagem aspiracional. Ele opera quando obriga o trabalho a passar por artefato, comparação, evidência e decisão humana explícita. Se esse fluxo não acontece, a falha não é conceitual; é falha de mecanização.

O desdobramento natural direcionado é a regra que fecha cada ciclo: ao concluir uma etapa, a IA apresenta o próximo movimento necessário de decisão humana — seguir, corrigir, pausar, aceitar mutação, mover para backlog ou abrir novo sprint.

---

## Diálogos

Os Diálogos são peças constitutivas do framework. Eles vivem em `dialogos/` na raiz do repositório, no mesmo nível de protocolo de `LOGUS.md`.

Um Diálogo não substitui comando, validação ou template. Ele nomeia o princípio operacional que depois precisa ser mecanizado.

---

## Identidade macro/micro

O mesmo algoritmo LOGUS opera em todas as escalas:

| Escala | Artefato | Evidência | Decisão |
|--------|----------|-----------|---------|
| Sessão | cadência curta | tasks e baseline lidos | seguir ou corrigir hipótese |
| Task | critério de aceite | validação e checkpoint visual | aprovar, corrigir ou bloquear |
| Sprint | PROJECT.md + baseline | auditoria adaptativa | destino dos achados e próximo sprint |
| Projeto | MAPA + auditorias | tendência em `/health` | ajustar trajetória |
| Empresa | princípios + templates | falhas de mecanização | atualizar o protocolo |

A escala muda; o algoritmo não.

---

## Máquina de estados

| Estado | Nome | Definição | Artefato |
|--------|------|-----------|----------|
| S0 | intuído | ainda está na cabeça ou na prática informal | nenhum |
| S1 | declarado | foi escrito como intenção validada | PROJECT.md |
| S2 | em execução | está sendo implementado no sprint | código, commits, testes |
| S3 | mutado | mudou em relação ao estado validado | diff, observação, feedback |
| S4 | auditado | foi varrido por evidência | AUDIT-S0X.md |
| S5 | decidido | recebeu destino humano | AUDIT-S0X.md |
| S6 | validado | virou novo ponto de referência | PROJECT.md + Baseline |

Transições:

```text
algoritmizar: S0 -> S1
executar:     S1 -> S2
comparar:     S2 -> S3
auditar:      S3 -> S4
julgar:       S4 -> S5
registrar:    S5 -> S6
```

---

## Invariantes

1. `PROJECT.md` é a única fonte de verdade.
2. `/public/` é derivada; nunca é editada manualmente.
3. Todo sprint tem conquista observável, datas, baseline, tasks e critérios de aceite.
4. Sprint atômico de 3 dias usa `Fim = Início + 3 dias`; `Fim` é limite de encerramento do ciclo, não dia adicional de trabalho.
5. Baseline é registrado depois da declaração aprovada do sprint e antes de qualquer execução.
6. Mutação não é classificada na entrada; é revelada por comparação e classificada na saída.
7. A IA executa regra mecânica; o humano decide peso.
8. O caminho até a resposta é privado; só a decisão final vira artefato.
9. Auditoria gera evidência, não cerimônia.
10. Invariante descreve identidade estável; regra transitória de modo operacional fica separada do contrato permanente.
11. Todo ciclo operacional termina em desdobramento natural direcionado: próximo ponto de decisão humana explícito.
12. O LOGUS não depende do humano lembrar o fluxo; se dependeu, houve falha de mecanização.
13. Quando uma folha revela falha reutilizável do framework, a evidência fica na folha e a correção sobe para o tronco.
14. A IA mantém agenda de alavancas derivada dos artefatos oficiais; agenda recomenda pelo maior retorno composto, humano decide peso.

---

## Identidade e modo operacional

Ao definir agente, processo, serviço ou outro artefato operacional, separe:

| Camada | Conteúdo | Onde declarar |
|--------|----------|---------------|
| Identidade | papel estável, limites permanentes e responsabilidade do artefato | contrato do artefato |
| Modo operacional | forma atual de execução, ferramenta, cadência ou restrição da sprint | SPRINT ATUAL, processo ou seção de modo |
| Regra transitória | condição temporária usada para provar uma hipótese | task, critério de aceite ou nota de sprint |

Regra de modo só vira invariante quando o humano decide que ela deve sobreviver à mudança de ferramenta, agenda ou executor.

---

## Agenda de alavancas

Agenda de alavancas é radar, não backlog paralelo. Ela deriva de `PROJECT.md`, auditorias, feedbacks de framework, backlog e estado atual para apresentar o movimento de maior retorno composto.

| Eixo | Pergunta |
|------|----------|
| Produto | o que torna o software mais útil, vendável ou essencial? |
| Performance | o que torna o software mais rápido, barato, confiável ou escalável? |
| Engenharia | o que reduz fragilidade, ambiguidade, débito ou retrabalho? |
| Mecanização | o que ainda depende de memória humana e deve virar regra, comando, validação ou artefato? |
| Estratégia | o que aproxima a Awake de vantagem composta e defensável? |

A agenda não altera sprint, backlog ou escopo sozinha. Ela apresenta alavancas e recomenda uma decisão; o humano transforma isso em sprint, task, backlog, auditoria, retroalimentação ou pausa.

Critério superior: quando duas alavancas competirem, prefira a que gera vantagem composta para a Awake, melhorando o projeto atual e aumentando capacidade futura do tronco, do time, do método ou do sistema.

---

## Loop operacional

```text
1. Declarar NORTE, MAPA, STACK e SPRINT ATUAL no PROJECT.md
2. Aprovar o sprint e registrar Baseline antes de qualquer execução
3. Executar cadência curta antes de tocar código ou iniciar nova task
4. Implementar apenas o que está declarado
5. Validar o estado LOGUS antes de render ou auditoria
6. Ao fim do sprint, rodar auditoria adaptativa
7. Humano decide destino dos achados
8. Registrar AUDIT-S0X.md e atualizar AUDITORIAS no PROJECT.md
9. Render regenerado apresenta a verdade em /status, /sprint e /health
10. IA apresenta o desdobramento natural direcionado antes de encerrar o ciclo
```

---

## Gatilhos

| Evento | Tipo | Agente | Ação |
|--------|------|--------|------|
| Início de sessão | regra | IA | executar `/cadencia-curta` |
| Início de sprint | peso | humano | aprovar conquista, datas, receita e baseline pós-declaração |
| Início de task | regra | IA | perguntar se a hipótese ainda é verdade |
| Fim de task | regra | IA | validar, renderizar, mostrar checkpoint visual e pedir `ok` para seguir |
| Fim de ciclo operacional | regra | IA | apresentar desdobramento natural direcionado para próxima decisão humana |
| Fim de sprint | regra | IA | sugerir `/auditoria-sprint` e, se houver múltiplos caminhos, `/agenda-alavancas` |
| Fim de auditoria | regra | IA | apresentar próximo ponto de peso e agenda de alavancas |
| Falha de fluxo percebida | regra | IA | rodar auditoria de mecanização do LOGUS |
| Retorno de escala percebido | regra | IA | sugerir `/retroalimentar` |
| Destino de achado | peso | humano | escolher `task-próximo-sprint`, `aceita` ou `backlog` |
| Mutação macro | peso | humano | ajustar MAPA, BACKLOG ou SPRINT ATUAL |
| Push relevante | regra | GitHub Actions | regenerar `/public/` |

Pergunta-teste: se a instrução pode ser escrita como `se A, então B`, é regra. Se exige ponderar contexto, cliente ou custo de oportunidade, é peso.

---

## Auditoria

As cinco varreduras existem para produzir evidência independente:

| Subagent | Pergunta |
|----------|----------|
| Sentinela | isto pode quebrar, vazar ou expor? |
| Caçador | isto falha no mundo real ou acumula débito técnico? |
| Otimizador | isto desperdiça tempo, clareza ou recurso? |
| Verificador de Spec | o prometido foi entregue? |
| Verificador de Trajetória | o que mudou sem ser declarado? |

Achado não é decisão. Achado vira decisão quando recebe destino humano.

---

## Mecanização

Sempre que um princípio do LOGUS for lembrado pelo humano, mas não tiver sido disparado pelo framework, isso é uma falha de mecanização.

```text
princípio escrito -> gatilho ausente -> falha de fluxo -> auditoria de mecanização -> correção do protocolo
```

Pergunta da auditoria:

```text
O que ainda depende de memória, boa vontade ou interpretação da IA?
```

Toda falha de mecanização deve produzir um artefato em `audits/` e virar mecanismo: gatilho, validação, checkpoint, comando ou ponto de peso explícito.

---

## Render

O render não cria informação. Ele apresenta faces diferentes da mesma verdade:

| Vista | Leitor | Pergunta |
|-------|--------|----------|
| `/status` | cliente | onde estamos? |
| `/sprint` | dev | o que está rolando agora? |
| `/health` | dev no tempo | qual é a tendência? |

Uma quarta vista só entra se responder uma quarta pergunta operacional distinta.
