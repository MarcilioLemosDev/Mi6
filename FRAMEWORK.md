# LOGUS — Framework

> Fonte única do framework LOGUS aplicado a este repositório.
> Mantido pela Awake Software. Este arquivo é artefato de referência —
> não editar sem revisão consciente do que está sendo mutado.

---

## O que é

LOGUS é a espinha dorsal técnica e metodológica da Awake Software: um framework para construir software com IA como acelerador, mantendo auditabilidade até o último centímetro e substituindo cerimônia humana por varredura automatizada.

Este repositório (Mi6 — agentes digitais) é o **projeto-piloto real** do framework. O que funcionar aqui vira padrão. O que quebrar aqui revela mutação no próprio LOGUS.

---

## Vocabulário oficial

**Artefato** — qualquer documento, código, diagrama ou registro que tornou consciente um algoritmo que antes operava em silêncio. Cada artefato é a forma material de uma decisão que saiu da cabeça e ganhou o mundo. PROJECT.md, AUDIT-S0X.md, diálogos, código entregue — todos são artefatos.

**Algoritmo** — sequência lógica de passos posta em consciência, com intenção declarada. Algoritmizar é tornar consciente o que já operava em silêncio.

**Sprint atômico** — pacote entregável de 3 dias. Não é caixa de tempo, é unidade de conquista visível.

**Cadência curta** — checagem entre tasks ou no início de sessão. Pergunta única: *"a hipótese que entrou nesta task ainda é verdade?"*

**Cadência longa** — auditoria de fim de sprint. Cinco varreduras:
- **Sentinela** — segurança
- **Caçador** — débito técnico
- **Otimizador** — performance e clareza
- **Verificador** — spec compliance
- **Verificador de Trajetória** — mutação revelada

**Mutação** — qualquer mudança detectada na varredura entre estado atual e último estado validado. Não classificada na entrada por tamanho, classificada na saída por impacto. Resultado da varredura tem 3 destinos: vira task no próximo sprint, aceita e segue, ou vai pro backlog.

**Auditoria adaptativa** — profundidade de cada varredura é definida no Sprint Plan, baseada no que o sprint vai mexer. Sentinela profundo se mexer auth. Otimizador profundo a cada 3 sprints. Verificador e Caçador sempre profundos.

**PROJECT.md** — fonte única da verdade do projeto. Mora no repo. 9 seções: NORTE, MAPA, STACK, SPRINT ATUAL, PRÓXIMOS, BACKLOG, AUDITORIAS, GLOSSÁRIO, CLIENTE.

**Render automático** — três páginas HTML geradas do PROJECT.md a cada commit: `/status` (mapa de épicos, cliente vê), `/sprint` (kanban interno), `/health` (gráfico de tendência).

---

## Princípios fundadores

1. **Trajeto no dia 1** — mapa completo definido antes do código. Mutação é função, não exceção.
2. **Sprint atômico de 3 dias** — pacote entregável, não caixa de tempo.
3. **Auditoria adaptativa** — substituiu retrospectiva humana por varredura automatizada.
4. **Fonte única no repo** — PROJECT.md edita, render gera, IA / humano / cliente veem o mesmo.
5. **Verdade aparece** — sistema é auditável até o último centímetro. Sem zona cega.

---

## Stack padrão por tipo de projeto

- **Site / landing:** Astro + Tailwind + Cloudflare Pages
- **Webapp / SaaS:** Next.js + Supabase + Vercel
- **Mobile:** React Native + Expo
- **Desktop:** Tauri (Rust + web)
- **Transversal:** TypeScript, Tailwind, Stripe, Resend, Better Auth, Vitest + Playwright

> Para este repo (Mi6 / agentes), a stack ainda não está definida — é uma das perguntas a responder antes do PROJECT.md.

---

## Critério fixo de diálogo

Conversar de igual para igual, com franqueza. Foco em chegar à verdade pelo diálogo, não em despejar respostas. Discordar quando necessário. Calibrar com perguntas honestas. Evoluir a ideia em conjunto. Inteligência multiplicada.

Respostas curtas e calibradas. Uma decisão por turno. Aplicar o framework no próprio diálogo: se está virando rodeio, simplificar.

---

## Como trabalhar dentro de um repo LOGUS

**Toda sessão de desenvolvimento começa com:**
> "Leia PROJECT.md. Confirme sprint atual e próxima task. Use plan mode antes de tocar código."

**Toda sessão termina com:**
> "Atualize PROJECT.md: tasks concluídas, bloqueios, notas relevantes."

**Fim de sprint:**
> "Rode auditoria conforme receita. Gere /audits/AUDIT-S0X.md. Atualize tabela de auditorias."

---

## Status do framework (snapshot)

- ✓ Diálogo I — Sobre o que é Algoritmo
- ◐ Diálogo II — Sobre Trajeto e Mutação
- ○ Diálogo III — Sobre Sprint Atômico
- ○ Diálogo IV — Sobre Auditoria como Substituta de Cerimônia
- ○ Diálogo V — Sobre a Fonte Única
- ○ Diálogo VI — Sobre Quem Dispara
- ○ Diálogo VII — Sobre o Render
