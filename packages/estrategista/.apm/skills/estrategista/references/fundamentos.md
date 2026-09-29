# Fundamentos — o que é estratégia e como reconhecer uma ruim

Use no modo **Avaliar** e sempre que precisar explicar por que algo não é estratégia.

## Por que a palavra existe

*Strategós*: o comandante com menos soldados, menos informação e menos tempo do que gostaria, escolhendo onde concentrar força sabendo que concentrar aqui é ficar descoberto ali.

Estratégia só existe quando há **ao mesmo tempo**:

| Condição | Sem ela, o que sobra |
|---|---|
| **Escassez** — não dá para fazer tudo | execução |
| **Incerteza** — o resultado não é conhecido antes | planejamento / otimização |
| **Oposição ou fricção** — concorrente, legado, inércia | uma lista |

Frase que seria verdadeira em qualquer cenário ("a estratégia é entregar valor ao cliente") não corre risco de estar errada, logo não é estratégia.

## A escada que todo mundo embaralha

| Degrau | O que é | Exemplo |
|---|---|---|
| Missão | por que a organização existe; não muda com o trimestre | "ser o banco da pequena e média empresa" |
| Visão | estado futuro concreto o bastante para saber se chegou | "em 2 anos, todo fluxo de contratação PJ roda no canal modernizado" |
| **Estratégia** | **como** ir daqui até lá, dado que não dá para fazer tudo | "modernizamos por fluxo de maior receita, um por vez, e congelamos feature nova no legado" |
| Meta | o resultado numérico esperado | "6 fluxos migrados até dezembro" |
| Tática | ações com nome e data | "migrar cadastro em outubro" |

A confusão mais cara é entre estratégia e meta. Meta só se avalia no fim do prazo. Estratégia se avalia **hoje**: dá para dizer "esse diagnóstico está errado" ou "essas ações não decorrem dessa política".

## O kernel (Rumelt, *Good Strategy / Bad Strategy*)

Três partes, **nesta ordem**:

1. **Diagnóstico** — a natureza do problema, simplificada num obstáculo nomeável. Bom diagnóstico é **falsificável** e normalmente **desconfortável**: aponta um mecanismo, e o mecanismo sugere o tratamento. "O time é pequeno" quase nunca é diagnóstico. "Nenhum dos 4 squads é dono do fluxo inteiro, então toda mudança de ponta a ponta precisa de três alinhamentos e morre de espera" é.
2. **Política norteadora** — uma regra de decisão, não um plano. Resolve antecipadamente uma classe de discussões e **fecha portas**. Deixa gente irritada — é assim que se sabe que é real.
3. **Ações coerentes** — ações que se **reforçam**. Se dá para remover uma sem enfraquecer as outras, é lista, não estratégia.

**As três perguntas que expõem uma estratégia vazia:**
1. Qual é o diagnóstico? (se a resposta é uma lista de ambições, não há)
2. O que a política **proíbe**? (se nada, não há)
3. As ações se reforçam? (se são projetos independentes com donos diferentes, não há)

Fazer essas perguntas numa sala, com educação, **é** influência em decisão estratégica.

**Provocação útil:** um diagnóstico errado se sente tão confortável quanto um certo. Pergunte sempre: se estiver errado, quanto tempo leva para descobrir, e o que dá para instrumentar hoje para encurtar isso?

## Os quatro sinais de má estratégia

| Sinal | Como soa | Teste | A pergunta que desarma |
|---|---|---|---|
| **1. Fluff** | "cultura de excelência, orientada a dados, centrada no cliente" | troque as palavras difíceis pelas simples — sobra algo? Alguém competente e de boa-fé defenderia o contrário? | "O que a gente faria diferente amanhã se isso fosse verdade?" |
| **2. Não enfrentar o problema** | só metas e iniciativas, nenhum obstáculo nomeado | existe um slide "o que está no nosso caminho é isto"? | "Na sua leitura, **o que está nos impedindo** hoje?" |
| **3. Meta como estratégia** | "a estratégia é crescer 20%"; 20 prioridades, todas prioritárias (*dog's dinner of goals*) | diz **como**? | "Esse é o resultado. **Qual é o mecanismo** que produz ele?" |
| **4. Objetivo ruim** | objetivos impossíveis com os recursos, ou genéricos demais para orientar decisão | "para isso eu preciso deixar de fazer o quê?" | "Se eu só pudesse entregar duas, quais duas?" |

Por que o sinal 2 é comum em empresa grande: nomear o problema costuma significar nomear uma área, um processo ou uma pessoa. Aspiração é mais segura.

Uma lista de 20 prioridades é uma lista de 0: a liderança não escolheu e empurrou a escolha para baixo — para quem tem menos contexto, no meio do sprint, às seis da tarde.

## Porter — decidir o que não fazer

"What Is Strategy?" (HBR, 1996): *a essência da estratégia é escolher o que não fazer.*

- **Eficácia operacional** (fazer o mesmo, melhor) é necessária e **insuficiente**: boas práticas difundem, a competição converge, a diferenciação vira preço.
- **Posicionamento**: escolher clientes, necessidades ou acessos e desenhar as atividades para eles.
- **Trade-off**: a posição só é defensável se escolhê-la **impede** outra. Se dá para ter as duas, é feature.
- **Encaixe (*fit*)**: vantagem vem do sistema de atividades que se reforçam — o mesmo conceito das ações coerentes.

Em tecnologia:

| Eficácia operacional (não é estratégia) | Estratégia técnica (escolhe e exclui) |
|---|---|
| subir cobertura de 40% para 70% | "testamos por risco de fluxo: contratação tem E2E, telas internas não — e aceitamos o bug lá" |
| adotar X porque o mercado adotou | "ficamos em ECS mesmo com EKS disponível, porque o gargalo é gente que entenda o runtime" |
| reduzir tempo de build | "investimos no caminho de deploy antes de features; isso atrasa dois meses de roadmap, aceito" |

"Nossa arquitetura otimiza para autonomia de squad e paga com duplicação" é trade-off. "Nossa arquitetura é escalável, segura, barata e flexível" é fluff.

**Provocação:** se um concorrente tivesse o código inteiro, o que ele ainda não teria? Se nada, a vantagem está em distribuição, marca, dado ou regulação — e isso muda onde vale investir engenharia (refatoração × pipeline de dados).

## Onde mora a estratégia técnica

**Estratégia técnica é a ponte entre uma restrição do sistema e um objetivo do negócio.** Só restrição = engenharia. Só objetivo = planejamento.

```
ESTRATÉGIA DE NEGÓCIO   ── restringe ──▼   ▲── habilita / bloqueia
ESTRATÉGIA DE PRODUTO   ── restringe ──▼   ▲
ESTRATÉGIA TÉCNICA
```

A seta de subida é a que quase ninguém desenha: a estratégia técnica informa o que é possível, o que é caro, e o que só é caro por uma escolha antiga.

**Os quatro tipos de decisão técnica com peso estratégico:**

| Tipo | Por que pesa | Exemplo |
|---|---|---|
| Fronteira | define quem muda o quê sem pedir licença | borda entre BFF e microfrontend; um BFF por canal ou compartilhado |
| Dependência | acoplamento de longo prazo | lib proprietária no core; provedor de identidade |
| Investimento | consome capacidade que não volta | reescrever legado; construir lib de componentes |
| Risco | muda o perfil de perda | retry e idempotência; onde ficam dados sensíveis |

**Teste:** uma decisão é estratégica quando **desfazê-la custa mais do que tomá-la**. É o mesmo critério de "merece ADR?" e de "é tipo 1?".

**O papel do especialista:** gerência responde por o quê, prazo e recursos; arquitetura, por padrões e coerência; o especialista, por **tornar a decisão possível de tomar** — traz a informação que ninguém tem, nomeia o trade-off, quantifica o custo, diz o que vai quebrar. A autoridade vem de **ser a pessoa cuja previsão se confirma** — e previsão só conta se foi escrita antes.

**Primeira contribuição estratégica barata e visível:** listar três decisões técnicas dos últimos 12 meses, classificar nos quatro tipos, e perguntar para cada uma: quem decidiu de fato? existe registro do porquê? quem quiser desfazer daqui a 2 anos vai achar o raciocínio? Onde não houver registro, começar a escrever ADR — sem precisar de mandato.

## Decisões de código que já são estratégia (o caso do BFF)

Útil para mostrar que a pessoa **já** decide estrategicamente e só falta nome e registro.

| Decisão | Por que é estratégica | O kernel / o preço |
|---|---|---|
| cache com TTL no saldo | troca consistência por latência e carga no downstream | política: dado que muda devagar não vai ao downstream na request · preço: usuário vê dado velho por N segundos |
| timeouts em cascata (gateway > BFF > downstream) | define quem falha primeiro e como o erro aparece | política: nenhuma camada espera mais que a de cima · preço: cortamos requests que talvez completassem |
| um único tradutor de exceção | superfície de erro num lugar auditável | política: nenhum controller decide status · preço: acoplamento central |
| health aberto, resto do actuator restrito | operabilidade × exposição | política: o que o orquestrador precisa é público · preço: um endpoint a menos protegido |
| build multi-stage | superfície de ataque e tamanho de imagem | política: nada de build no runtime · preço: build mais difícil de entender |

**Provocação:** se você sair de férias por um mês, quais decisões a pessoa que mexer vai **desfazer sem perceber que eram decisões**? ("TTL vira 60s porque causava inconsistência.") Cada reversão silenciosa é uma estratégia morrendo por falta de registro. E só se delega o que está escrito.

## Frases de uma linha, para devolver na hora certa

| Tema | A frase |
|---|---|
| A palavra | Estratégia existe porque os recursos acabam antes das ideias. |
| Kernel | Sem diagnóstico, o resto é decoração. |
| Má estratégia | "Crescer 20%" é o pedido, não o plano. |
| Porter | Fazer melhor não é estratégia. Fazer diferente, e abrir mão, é. |
| Onde mora | Estratégia técnica é a ponte entre uma restrição do sistema e um objetivo de negócio. |
| SMART | SMART é ortografia de meta, não escolha de meta. |
| OKR | Se o KR pode ser marcado como feito, é tarefa. |
| Métricas | Toda métrica vira alvo e, ao virar alvo, deixa de medir. |
| Diagnóstico | Diagnóstico bom dói: ele acusa alguém, inclusive você. |
| Priorizar | Reversível se decide rápido; irreversível, devagar. |
| Incerteza | Em ambiente complexo, sonde antes de planejar. |
| Influência | A conclusão vem primeiro; o raciocínio é para quem pedir. |
| Execução | Estratégia morre de atrito e de todo mundo estar ocupado. |
| Escrever | Cinco design docs antes de uma estratégia; cinco estratégias antes de uma visão. |
| Código | Um timeout escolhido com justificativa escrita já é artefato de estratégia. |
| Traduzir | Negócio tem quatro moedas: dinheiro, risco, tempo e reputação. |
