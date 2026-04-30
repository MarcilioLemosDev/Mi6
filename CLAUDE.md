# LOGUS — Instruções para o Claude Code

Este projeto opera sob o **Framework LOGUS** (Awake Software). Leia antes de qualquer ação técnica.

Para a especificação algorítmica completa, consulte `LOGUS.md`.

---

## Vocabulário

| Termo | Significado |
|-------|-------------|
| Artefato | Documento, código ou registro que tornou consciente um algoritmo |
| Sprint atômico | Pacote entregável indivisível; em datas usa `Fim = Início + 3 dias` |
| Cadência curta | Checagem entre tasks ou no início de cada sessão — uma pergunta |
| Cadência longa | Auditoria ao fim do sprint — cinco varreduras |
| Mutação | Mudança detectada na comparação entre estado atual e último estado validado |
| Baseline | Commit ou tag registrado depois da declaração aprovada do sprint e antes da execução |
| Auditoria adaptativa | Cinco varreduras com profundidade ajustada ao sprint |
| Regra | Gatilho mecânico executável por instrução clara: se A, então B |
| Peso | Decisão que exige julgamento humano de contexto, cliente ou custo |
| Desdobramento natural direcionado | Obrigação da IA de transformar o fim de um ciclo no próximo ponto explícito de decisão humana |
| Retorno de escala | Falha observada em projeto-folha que precisa subir como correção reutilizável para o `logus-template` |
| Modo operacional | Forma atual de executar um artefato; não é invariante de identidade |
| Agenda de alavancas | Radar derivado dos artefatos oficiais para recomendar o maior retorno composto sem virar backlog paralelo |

---

## Regras de operação

### Fonte única
- `PROJECT.md` é a única fonte de verdade. Toda decisão mora aqui.
- `/public/` é derivada — nunca editar. Se algo está errado, corrija o markdown, não o HTML.
- Se algo não está no `PROJECT.md`, ainda não foi decidido.

### Baseline de sprint
- Baseline só é válido depois que `NORTE`, `MAPA`, `STACK`, `SPRINT ATUAL`, tasks e receita de auditoria foram preenchidos e aprovados.
- Registre o baseline antes de tocar execução do sprint.
- Se o baseline apontar para template ou estado anterior à declaração aprovada do sprint, trate como falha de mecanização ou retorno de escala.

### Identidade e modo operacional
- Ao definir agente, processo ou serviço, separe identidade estável de modo operacional da sprint.
- Invariantes pertencem à identidade permanente; ferramenta, execução manual, agendamento, runner ou cadência pertencem ao modo operacional.
- Regra transitória só vira invariante quando o humano decidir que ela deve sobreviver à mudança de ferramenta, agenda ou executor.

### Desdobramento natural direcionado
- O LOGUS não depende do humano lembrar o fluxo. Se o humano precisou lembrar, trate como falha de mecanização.
- Todo ciclo operacional termina com um próximo ponto explícito de decisão humana.
- Desdobramento natural direcionado significa que o trabalho flui para a próxima decisão necessária sem o humano precisar lembrar a etapa.
- Ao fim de sessão, task, checkpoint, auditoria ou correção de fluxo, apresente a decisão necessária: seguir, corrigir, pausar, aceitar mutação, mover para backlog ou abrir próximo sprint.
- Não descreva o LOGUS como tentativa, intenção ideal ou orientação vaga. Descreva como operação, regra, evidência, decisão e mecanização.

### Retroalimentação de escala
- Os Diálogos vivem em `dialogos/` e descrevem princípios operacionais do framework.
- Se uma falha encontrada em projeto-folha apontar para regra, comando, validação, template, documentação ou agente reutilizável, trate como retorno de escala.
- Retorno de escala não é backlog comum de produto. Rode `/retroalimentar` para registrar evidência local, amarrar `PROJECT.md` e preparar PR ou issue para o `logus-template`.
- `/retroalimentar` prepara ação remota por padrão. Só abra PR ou issue depois de confirmação humana explícita.

### Agenda de alavancas
- A IA não puxa apenas a próxima task. Ela mantém leitura ativa de alavancas derivadas de `PROJECT.md`, auditorias, backlog, feedbacks e estado atual.
- A agenda separa Produto, Performance, Engenharia, Mecanização e Estratégia.
- Quando duas alavancas competirem, prefira a que gera vantagem composta para a Awake: melhora o projeto atual e aumenta capacidade futura do tronco, do time, do método ou do sistema.
- Agenda não é fonte de verdade e não altera escopo. Ela recomenda; o humano decide peso.
- Em fim de auditoria, fim de sprint ou quando houver mais de um caminho plausível, rode ou sugira `/agenda-alavancas`.

### Cadência curta — executa no início de cada sessão
Antes de tocar qualquer código ou arquivo de projeto:
1. Leia `PROJECT.md` seção `SPRINT ATUAL`
2. Liste as tasks com status `todo` ou `doing`
3. Confirme se `Baseline` está preenchido e foi registrado depois da declaração aprovada do sprint
4. Pergunte ao humano: *"A hipótese dessas tasks ainda é verdade? [task X: <critério de aceite>]"*
5. Se o humano disser "não" para qualquer task, pause. Proponha edição no `PROJECT.md` antes de continuar.
6. Se o humano confirmar, apresente a próxima task e peça `ok` para iniciar ou continuar.
7. Só então prossiga com o trabalho.

Atalho: `/cadencia-curta`

### Cadência longa — ao fim de sprint
Se a data atual for igual ou posterior à data de fim do sprint em `PROJECT.md`:
- Informe o humano que o sprint chegou ao fim
- Sugira executar `/auditoria-sprint` usando o `Baseline` registrado no sprint

Não rode a auditoria sem o humano pedir.

### Agentes de auditoria
Ao rodar qualquer subagent de auditoria, respeite a profundidade declarada na tabela "Receita de auditoria" do sprint atual no `PROJECT.md`. Não improvise profundidade.
Antes de auditoria, rode `python scripts/validate.py --mode project`. Se falhar, corrija o estado declarado antes de auditar.

---

## Slash commands disponíveis

| Comando | Quando usar |
|---------|-------------|
| `/cadencia-curta` | Início de sessão, início de nova task |
| `/auditoria-sprint` | Fim de sprint — dispara os 5 subagents e consolida AUDIT-SXX.md |
| `/auditoria-mecanizacao` | Quando um princípio do LOGUS precisou ser lembrado pelo humano ou ficou dependente de memória |
| `/retroalimentar` | Quando um projeto-folha revelar correção reutilizável para o `logus-template` |
| `/agenda-alavancas` | Quando houver múltiplos caminhos e for preciso escolher a alavanca de maior retorno composto |

### Falha de mecanização
Se o humano apontar que um desdobramento, checkpoint, decisão ou visualização deveria ter acontecido pelo framework, trate como falha de mecanização. Rode `/auditoria-mecanizacao` antes de continuar o projeto.

### Retorno de escala
Se a falha de mecanização ou achado de auditoria pertencer ao framework e não apenas ao produto, rode `/retroalimentar` antes de encerrar o ciclo.
