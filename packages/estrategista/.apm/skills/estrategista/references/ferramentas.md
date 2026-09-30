# Ferramentas — cada uma pelo problema que a fez existir

Use nos modos **Decidir**, **Preparar a sala** e **Revisar uma decisão**. Toda ferramenta aqui vem com o modo de falha: apresente os dois juntos.

## Qual ferramenta, em qual camada

O erro comum não é escolher a ferramenta ruim; é usar a certa na camada errada.

| Camada | Pergunta | Ferramenta certa | Errada aqui |
|---|---|---|---|
| Por que estamos indo para lá? | qual é o obstáculo real? | kernel, Wardley, 5 porquês | SMART (não tem diagnóstico) |
| O que perseguir neste ciclo? | qual resultado, e como sabemos? | OKR, North Star | SMART sozinha (vira lista de tarefas) |
| Como a meta está escrita? | é verificável e tem dono? | SMART | OKR (grosso demais para uma frase) |
| O que fazer primeiro? | qual a ordem? | RICE, custo do atraso, tipo 1/2 | qualquer das de cima |
| Qual método serve? | dá para analisar ou precisa sondar? | Cynefin | — |

## SMART — ortografia de meta

**Problema de origem:** Doran, 1981, *"There's a S.M.A.R.T. way to **write** management's goals"*. Gerentes escreviam objetivos que ninguém conseguia verificar.

| Letra | Pergunta real |
|---|---|
| S | o que exatamente muda? |
| M | qual número, medido como, por qual fonte? |
| A | no original era **Assignable**: de quem é? (a versão moderna, *Achievable*, perdeu a pergunta mais útil) |
| R | importa para alguém além de quem escreveu? |
| T | até quando, com qual checkpoint no meio? |

**Resolve:** ambiguidade de enunciado. Torna o resultado defensável: um número que existia antes e existe depois.

**Não é — os quatro limites:**
1. Ortografia, não escolha: dá para escrever em SMART impecável uma meta inútil ("migrar 12 telas até junho" que ninguém usa).
2. O A e o R empurram para baixo: onde meta vira avaliação, escreve-se a meta que já se sabe que vai bater (*sandbagging*).
3. O M favorece o fácil de medir: "fazer 3 cursos" é atividade, não resultado.
4. Individual e estática: sem cadência, sem jeito de matar meta que perdeu sentido.

**Uso certo:** régua de acabamento. Escolha o que perseguir com kernel + OKR; use SMART para a frase final não ser ambígua. Reescreva atividade como resultado: não "fazer o curso de system design", mas "conduzir um desenho de sistema de ponta a ponta numa discussão real, com estimativa e gargalo nomeados, e a decisão registrada em ADR".

## OKR — o objetivo que aceita falhar

**Problema de origem:** Andy Grove, Intel, anos 70. Milhares de pessoas batendo metas bem escritas, cada uma otimizando o seu pedaço, e a empresa perdendo mercado. Alinhamento em escala com ambição preservada. Doerr levou ao Google em 1999.

Estrutura: um objetivo qualitativo, memorável, sem número; 2 a 4 KRs numéricos.

**Duas regras culturais que fazem funcionar:**
1. KR é resultado, nunca atividade. "Lançar a lib v3" é tarefa; "70% dos novos componentes vêm da lib" é resultado.
2. Objetivo ambicioso pode falhar sem punição (0,7 é bom num *stretch*). Só funciona **desacoplado da avaliação de desempenho** — onde a maioria das implementações quebra.

**KR em tensão (a trava):** um KR que impede bater os outros do jeito errado. Sem trava, o jeito ótimo e horrível de subir conversão é remover validação. É a defesa embutida contra Goodhart.

| Modo de falha | Reconhece-se por | Correção |
|---|---|---|
| to-do list | todo KR é entregável com data | reescrever como número que muda |
| sandbagging | todos fecham em 100% | desacoplar da avaliação; celebrar o 0,7 |
| cascata literal | KR do chefe vira objetivo do time 4 níveis abaixo | cascatear **contexto**; o time propõe o KR |
| excesso | 6 objetivos, 25 KRs | 1 a 3 objetivos; o resto é operação |
| órfão | ninguém olha até a revisão | 20 min quinzenais com nível de confiança |
| OKR de operação | "manter o sistema no ar" | isso é KPI |

**OKR é para mudança; KPI é para saúde.** Disponibilidade é KPI com limite, não OKR. Ligação com SLO: SLO é o KPI de saúde, error budget é o risco que se pode gastar, OKR é o que se faz com a capacidade que sobra. Política pronta: *"enquanto o error budget está no azul, o time trabalha nos OKRs; quando estoura, trabalha em confiabilidade até voltar."*

## Métricas que aguentam pressão

**Goodhart** (formulação de Strathern): *quando uma medida se torna um alvo, deixa de ser uma boa medida.* Não é cinismo, é mecânico: a métrica mede um proxy, pessoas otimizam o proxy, a folga é explorada sem ninguém ser desonesto. Cobertura sem asserção; deploy vazio; inflação de story points; chamado fecha e reabre; bug que não é registrado não existe.

| Tipo | O que é | Serve para |
|---|---|---|
| Vaidade | sobe sempre, não muda decisão (commits, acumulado de usuários). Teste: se dobrar amanhã, eu faço algo diferente? | nada |
| Antecedente (*leading*) | move antes do resultado e é influenciável: p95, taxa de erro, tempo de review | dirigir |
| Consequente (*lagging*) | confirma depois: receita, NPS, churn, conversão | provar |

Só antecedente é ativismo sem resultado; só consequente é autópsia. A ponte é uma **hipótese escrita**, com o que a refutaria:

> "Acreditamos que reduzir o p75 de carregamento na contratação aumenta a conclusão do funil, porque o abandono concentra-se na primeira tela e em 4G. Se o p75 cair 40% e a conclusão não subir 5 pontos, a hipótese estava errada e revisamos o diagnóstico."

**DORA** (*Accelerate*): frequência de deploy, lead time, taxa de falha de mudança, tempo de restauração. Velocidade e estabilidade **não são trade-off** — os melhores times são melhores nas quatro. Munição contra "qualidade vai nos deixar lentos". Mede o sistema de entrega, nunca pessoa.
**SPACE:** existe porque usaram DORA para avaliar indivíduo. Cinco dimensões; nunca uma sozinha, nunca por indivíduo.
**North Star:** a métrica única de valor; o valor dela é alinhar. Mal escolhida, é Goodhart em escala industrial.

**As cinco perguntas para qualquer número, nesta ordem:**
1. Definição operacional? ("erro" conta 4xx? timeout do cliente?)
2. Denominador? (onde mora a maior parte das mentiras)
3. Média ou percentil? (média de latência esconde a cauda)
4. Intervalo e variação natural? (oscila 15% por semana → não sustenta decisão sobre 8%)
5. O que ela ignora de propósito?

Quem define a métrica define a realidade percebida — escolher percentil e denominador é escolha estratégica.

## Diagnóstico — cinco ferramentas

| Situação | Ferramenta | Modo de falha |
|---|---|---|
| um incidente, uma causa provável | **5 porquês** (Toyota) | produz uma cadeia linear; pessoas diferentes chegam a raízes diferentes. Use como abridor, com duas pessoas de áreas diferentes, e compare. Quase sempre começa técnico e termina organizacional. |
| problema recorrente, causas múltiplas | **Ishikawa** — categorias: código, dados, infra, processo, pessoas, terceiros | o valor não é o desenho; é olhar categorias que você não olharia sozinha |
| liderança pediu SWOT | **SWOT com cruzamento obrigatório** | sem mecanismo de escolha vira quatro listas de adjetivos. Cada item só entra numa frase que cruza dois quadrantes **e** diz "deixando de fazer B" |
| construir × comprar, investimento de plataforma, descomissionar | **Wardley Map** | a mais trabalhosa; mapa mal feito é discutível ao infinito |
| iniciativa grande sem conexão com resultado | **Árvore de impacto** (Adzic): por quê → quem → como (comportamento) → o quê | a pergunta que vale: qual comportamento precisa mudar? Costuma revelar que a feature não muda nenhum |

**Wardley, em uma página:** eixo vertical = cadeia de valor (em cima o que o usuário vê, embaixo o que sustenta, ligados por dependência). Eixo horizontal = evolução: gênese → custom → produto → commodity. O mapa mostra:
1. onde você **constrói commodity** (peça à direita mantida em casa) — argumento de custo visual em 30 segundos;
2. que **tudo se move para a direita** (orquestração de contêiner era gênese em 2014);
3. que **o método muda com a posição**: à esquerda experimenta e aceita desperdício; à direita padroniza e corta custo. Método de commodity numa peça de gênese mata a inovação; o contrário queima dinheiro.

A pergunta de especialista: **qual peça está na posição errada?**

## Priorizar e escolher

**RICE** (Intercom): (Reach × Impact × Confidence) ÷ Effort. O valor não é o ranking; é o **C** — declarar confiança transforma opinião em discussão de evidência. Falha: esforço subestimado, impacto superestimado por quem propôs, e penaliza sistematicamente o estruturante (fundação nunca ganha de feature pequena).

**Custo do atraso / CD3** (Reinertsen; = WSJF do SAFe): custo do atraso ÷ duração. Pergunta "quanto custa esperar mais um trimestre?". Captura o que o RICE perde: débito técnico, risco regulatório, migração com fim de suporte. Frase:

> "Não estou pedindo para priorizar porque é mais valioso. É a única coisa na lista cujo preço **sobe** se a gente esperar."

**Tipo 1 × tipo 2** (Bezos, carta de 2015):

| | Tipo 1 | Tipo 2 |
|---|---|---|
| natureza | porta de mão única | porta de vaivém |
| exemplos | banco central, API pública, contratar | flag, layout, lib de datas |
| como decidir | devagar, consulta, registro (ADR) | rápido, por quem está perto, e ajusta |
| erro comum | decidir rápido demais | **decidir devagar demais** — o mais caro em empresa grande |

Frase de liderança visível: *"isso é tipo 2 — decidam e sigam."*

**Quadro de decisão:** item · custo de esperar · reversível? · quem fica bravo se sim · quem fica bravo se não. As duas últimas colunas não estão em framework nenhum e são as que decidem em organização grande.

## Decidir sob incerteza

**Cynefin** (Snowden) — usar o método errado para o tipo de problema é o modo de falha mais comum da gestão.

| Domínio | Causa-efeito | Método | Exemplo |
|---|---|---|---|
| Claro | óbvia | sentir → categorizar → responder | certificado vencido |
| Complicado | existe, pede especialista | sentir → **analisar** → responder | dimensionar cache, desenhar arquitetura, achar causa de latência no pico |
| Complexo | só em retrospecto | **sondar** → sentir → responder | adoção de padrão por 4 squads; comportamento de usuário |
| Caótico | não há | **agir** → sentir → responder | incidente grave agora |
| Confuso | não se sabe | descobrir o domínio primeiro | a maioria das reuniões |

No complexo, análise só produz atraso com cara de rigor: rode uma **sonda segura** — pequena, reversível, com critério de leitura definido antes ("uma squad, uma tela, quatro semanas; se abrirem menos de 2 issues de bloqueio e não pedirem fork, escala"). No caótico, estancar antes de entender.

**Premortem** (Klein, HBR 2007): "é daqui a um ano, o projeto falhou de forma constrangedora; cada um escreve sozinho, cinco minutos, por quê". Imaginar retrospectivamente aumenta a identificação de causas; e legitima a dúvida onde levantar risco parece falta de comprometimento. 30 minutos, sem pedir autorização. Roteiro em [modelos.md](modelos.md).

**Planejamento por cenários** (Shell, Pierre Wack): não é prever, é ensaiar.
1. As duas incertezas mais impactantes e menos controláveis.
2. Cruze em quatro quadrantes; nomeie cada cenário.
3. Em cada um: o que seria verdade? o que teríamos feito cedo que agora importa?
4. Ações **robustas** — valem nos quatro. Comece por elas.
5. **Sinais precoces** de cada cenário. É o passo que transforma exercício em ferramenta.

**Apostas** (Annie Duke, *Thinking in Bets*): decisão ≠ resultado. Julgar decisão pelo resultado é *resulting*. Duas práticas: falar em probabilidade ("~70% de confiança de que cabe no trimestre") e **registrar a previsão antes** — a maior fonte de autoridade técnica é abrir um documento de seis meses atrás.

## Influência — a estratégia sobreviver à sala

Comunicação de decisão tem regras diferentes da de ensino. Ensinar constrói (contexto → conclusão); decidir inverte.

**BLUF / Pirâmide de Minto:** recomendação no topo, três porquês, evidência embaixo. Abertura em três frases:

> "**Recomendo que a gente pare de criar tela nova no legado a partir de outubro.** Por três motivos: [custo 1,8× maior], [adia o descomissionamento, onde está a economia], [perdemos a janela de contexto do time]. **O que eu preciso desta reunião é a decisão sobre outubro** — os detalhes estão no documento."

O terceiro elemento é o mais esquecido: **dizer o que se quer da reunião** (decisão, ciência, ajuda para destravar).

**Interesses, não posições** (*Getting to Yes*): posição é o que a pessoa pede ("em novembro"); interesse é o que ela precisa ("não posso chegar ao comitê de dezembro sem nada"). Posições colidem; interesses têm várias soluções. Pergunta de descoberta: *"Me ajuda a entender o que acontece com você se isso não sair em novembro?"*

**BATNA:** o que acontece se não houver acordo. Saber o seu evita ceder demais e travar por orgulho. Internamente, costuma ser "o assunto volta em três meses com mais dívida" — vale dizer em voz alta.

**Mapa de stakeholders:** pessoa/área · o que ganha · o que perde · **como é avaliada** · precisa decidir, ser ouvida ou só saber? "Como é avaliada" explica o comportamento que parece irracional: ninguém apoia o que piora o próprio número. Tratar quem precisa **ser ouvido** como quem só precisa **saber** cria oposição por processo, não por mérito.

**Memo de uma página** (inspirado nos memos da Amazon: prosa expõe raciocínio frouxo que bullet esconde). Circulado **antes**, faz as objeções chegarem por escrito e a reunião virar discussão de objeções. Modelo em [modelos.md](modelos.md).

**Discordar e se comprometer** só é posição forte quando as duas metades estão escritas. Discordância sem registro é memória; memória não conta em avaliação.

## Execução — por que estratégia morre

Estratégia raramente morre por estar errada; morre porque nada muda no dia seguinte.

**As três lacunas de Bungay** (*The Art of Action*):

| Lacuna | Entre | Reação instintiva | Por que piora |
|---|---|---|---|
| Conhecimento | o que se sabe × o que se gostaria | mais análise | atrasa; o que falta é sobre o futuro |
| Alinhamento | o plano × o que entenderam | detalhar mais a instrução | tira julgamento de quem está perto |
| Efeito | a ação × o resultado | mais controle e report | consome o tempo de quem faria |

**Auftragstaktik:** dê a **intenção** (o quê e o porquê), não a instrução; deixe o como. Peça o *back-briefing* — a pessoa reexplica com as palavras dela. Para especialista sem autoridade formal, é o único modo disponível: a qualidade do seu porquê é a alavanca inteira.

**Cadência mínima:**

| Ritmo | O quê | Tempo |
|---|---|---|
| semanal | os antecedentes se movem? | 15 min |
| quinzenal | confiança por KR e **por que mudou** | 30 min |
| trimestral | a política ainda vale? o diagnóstico mudou? | 2 h |
| semestral | **o que paramos de fazer, de fato?** | 1 h |

Se ninguém nomeia o que parou, a estratégia não foi implementada — foi **adicionada**.

**Conway** (1967): organizações desenham sistemas que copiam sua estrutura de comunicação. Três squads num BFF sem dono → nenhuma arquitetura conserta. **Manobra inversa**: mude a estrutura para obter a arquitetura (*Team Topologies*: times de fluxo, plataforma, habilitadores, subsistema complicado; interações de colaboração, *X-as-a-Service*, facilitação). Frase de especialista: *"essa arquitetura exige que alguém seja dono do contrato, e hoje ninguém é; enquanto isso não mudar, a proposta não se sustenta."*

**Três perguntas sobre qualquer iniciativa anunciada:** o que parou por causa dela? qual a cadência de revisão e quando foi a última? exige mudança de estrutura de times, e ela aconteceu?

## Escrever a estratégia

Will Larson: **cinco design docs antes de uma estratégia; cinco estratégias antes de uma visão.** A estratégia emerge do padrão visto nos casos concretos; escrita sem eles é adivinhação sobre qual é o problema.

Estratégia não escrita não pode ser discutida, herdada nem **atribuída a quem a fez**. Estrutura e exemplo completo em [modelos.md](modelos.md).
