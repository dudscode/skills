# Cenários para treino

Use no modo **Treinar**. Cada cenário entrega uma **estratégia já escolhida**. A tarefa não é escolher a melhor do mundo: é **habitar** aquela e descobrir o que ela implica, onde dói e quem reclama. Estratégia é músculo de consequência.

**Protocolo (20–30 min por cenário):**
1. Mostre só a situação e a estratégia dada. Nunca as perguntas e a leitura juntas.
2. Peça as **três primeiras consequências** — o que muda na segunda-feira depois do anúncio.
3. Faça as perguntas, uma ou duas por vez.
4. Peça: **quem fica bravo**, e o que ela diz para essa pessoa.
5. Só depois da resposta escrita (ou gravada), use a **leitura**: o que ela pegou, o que costuma faltar e faltou, e o nome técnico. Leitura não é gabarito: resposta diferente e bem defendida vale.

Não confirme palpite no meio. Responder em voz alta, gravando, vale o dobro.

---

## 1 — "A ponte que ninguém quer pagar"

**Situação.** O canal legado tem 70% do uso e 100% da receita atual. O modernizado tem 6 fluxos e é melhor em tudo, menos cobertura. O orçamento de modernização veio pela metade. O gestor pede: "me ajuda a decidir o que fazer com o que sobrou".

**Estratégia dada — "sangria controlada":** legado em congelamento funcional (só defeito e obrigação regulatória). Todo o orçamento vai para migrar fluxos na ordem de receita influenciada, um por vez.

**Perguntas.**
1. O diagnóstico implícito, na forma "o que nos impede é…".
2. O primeiro pedido de exceção: de quem? A resposta, e a regra definida **antes** para não decidir caso a caso.
3. Que sinal, em 90 dias, indicaria diagnóstico errado?
4. Como medir "receita influenciada" por fluxo sem virar ficção? De quem você precisa?

**Leitura.**
- Diagnóstico: "a capacidade está dividida entre manter o que vamos desligar e construir o substituto, e essa divisão torna os dois lentos." "Não temos orçamento" é **condição**, não obstáculo.
- Exceção vem de produto/negócio, com caso legítimo. Resposta não é "não": é regra prévia — "exceção só com aprovação do mesmo nível que aprovou o congelamento, e consome orçamento de migração equivalente". Exceção que custa a quem pede se autorregula; gratuita destrói a política em seis semanas.
- O que quase ninguém responde (3): fluxos migrados sem ganho de conversão, custo ou lead time → a lentidão vinha do processo ou do downstream, e congelar só produz dois sistemas ruins.
- Receita: atribuição por fluxo com premissa declarada, com alguém de negócio como **coautor** — trazer essa pessoa já é a jogada de influência.

---

## 2 — "Três squads, um BFF"

**Situação.** Três squads compartilham um BFF; o contrato cresce por acúmulo; ninguém responde pelo todo. Em 4 meses, três incidentes vieram de uma squad quebrar o consumo de outra. Você é chamada para "resolver a arquitetura".

**Estratégia dada — "um BFF por experiência, um dono por BFF":** divide-se por canal/experiência, cada um com time dono declarado; o comum vira biblioteca, não serviço compartilhado.

**Perguntas.**
1. Técnica ou organizacional? O que precisa ser verdade na estrutura de times?
2. O que custa, concretamente?
3. Abertura de três frases para o gestor que vai ouvir "vocês querem triplicar os serviços".
4. A sonda barata que testa antes de comprometer o trimestre.
5. Se a estrutura **não** puder mudar, qual a segunda melhor — e ela é honesta ou só adia?

**Leitura.**
- **Organizacional com cara de técnica.** Cada BFF precisa de time que responda por ele **na avaliação**, não só no organograma. Se todos seguem medidos só por feature, apodrece igual, em três lugares.
- Custo: duplicação de agregação, mais pipelines, mais tasks (infra), mais superfície de operação e plantão, risco de divergência de contrato com o mesmo downstream. Quem para em "duplicação" esqueceu operação — onde dói primeiro.
- Abertura começa pelo número de incidentes, não pela arquitetura, e termina pedindo a decisão sobre **quem passa a ser dono**.
- Sonda: separar **um**, o menos acoplado, e medir um trimestre de incidentes cruzados, lead time e custo.
- Segunda melhor: contrato explícito + testes de contrato + dono rotativo. Honesta **se** dita como mitigação, com a causa que permanece registrada. Mitigação vendida como solução é a origem do próximo incidente.

---

## 3 — "A plataforma mandou migrar"

**Situação.** Padronização em um orquestrador só, em 12 meses. Sua gerência tem 4 aplicações, 2 críticas. Sem recurso extra. Prazo inegociável; o **como** é.

**Estratégia dada — "a mais barata primeiro, a mais crítica por último, com o aprendizado indo junto":** ordem crescente de risco; cada migração produz um artefato reutilizável (pipeline, módulo, runbook) antes da próxima.

**Perguntas.**
1. O risco embutido nessa ordem?
2. A estratégia oposta (crítica primeiro): quando é a certa?
3. Duas maiores incertezas → quatro cenários → qual ação é robusta nos quatro?
4. Premortem: é daqui a 12 meses e falhou. Cinco razões.
5. O que pedir à plataforma em vez de recurso? (Interesse, não posição.)

**Leitura.**
- Risco: chegar às críticas com prazo estourando e paciência no fim. Mitigação: **prova de conceito antecipada** do pedaço mais assustador da crítica, em paralelo desde o início.
- Crítica primeiro é certa quando o risco é de **viabilidade** (pode simplesmente não caber no alvo). Execução → crescente; viabilidade → crítica primeiro.
- Ação robusta: o artefato reutilizável. Vale em todos os futuros, inclusive no de cancelamento.
- Premortem, o que ninguém escreve antes: plataforma sobrecarregada; característica não mapeada da crítica (estado local, job, conexão persistente); sem ambiente de teste comparável; perda de duas pessoas; e a mais comum — a migração competiu com produto e perdeu toda sexta-feira.
- Pedir: prioridade de suporte nomeada, ambiente de referência, e ser o **caso-piloto documentado** deles. O interesse deles é provar que a padronização funciona; o seu, ter suporte.

---

## 4 — "O pico e a tentação da reescrita"

**Situação.** No pico do mês o p99 do BFF estoura e o erro sobe. O time aposta no modelo de threads bloqueantes e propõe migrar para reativo. Muito entusiasmo, nenhum dado.

**Estratégia dada — "nenhuma reescrita antes de um número":** nada estrutural sem experimento que isole a causa; o trimestre vai para instrumentação e teste de carga reproduzível.

**Perguntas.**
1. Que evidência específica confirma ou refuta a hipótese? O que olhar, onde?
2. Custo político: desanima um time motivado. Como conduzir sem parecer que barra inovação?
3. Quando a oposta ("aprove, o time aprende fazendo") seria a certa?
4. Cinco outras causas do mesmo sintoma (Ishikawa).
5. Cynefin: complicado ou complexo? O que muda no método?

**Leitura.**
- Evidência: saturação do pool de threads, tempo em fila × tempo em I/O, p99 **por dependência** (não agregado), correlação com o pico. Threads bloqueadas esperando downstream → o modelo importa. CPU saturada ou downstream como gargalo → reescrever não muda nada.
- Conduzir: não barrar, **redirecionar para a pergunta** — "topo, e o caminho mais rápido de aprovar é o dado. Quem quer construir o teste de carga?".
- Oposta é certa quando experimentar custa menos que investigar e o aprendizado vale além da decisão (serviço pequeno, não crítico).
- Outras causas: pool de conexões HTTP/banco subdimensionado; falta de timeout acumulando requests; pausa de GC; cache frio no pico (efeito manada); autoscaling lento para a rampa; downstream degradando só no pico.
- **Complicado**: causa determinável por análise com especialista e instrumentação. Sondar às cegas aqui é desperdício.

---

## 5 — "Cinco times, uma tela"

**Situação.** Um canal novo, cinco times. Aplicação única com contribuição ou microfrontends com deploy autônomo? Três semanas em "qual é melhor".

**Estratégia dada — "autonomia de entrega acima de consistência de experiência":** microfrontends com contrato explícito; cada time entrega quando quiser; consistência via lib de design versionada com atualização obrigatória por trimestre.

**Perguntas.**
1. O lado sacrificado e **como** vai doer, concretamente.
2. A condição organizacional sem a qual falha.
3. Inconsistência visível em um ano = falha? Como definir antes o limite?
4. O problema como pergunta de negócio, sem a palavra "microfrontend".

**Leitura.**
- Sacrificado: coerência de experiência e eficiência de runtime — bundle duplicado, divergência visual, depuração entre fronteiras, versões da lib em convivência. "Microfrontend desacopla" e parar ali é resposta sem preço.
- Condição: deploy **realmente** independente (pipeline, ambiente, autorização próprios). Deploy coordenado por um time central às quintas = pagou a autonomia sem comprá-la.
- Inconsistência prevista é o preço sendo pago; falha é passar do limite definido antes ("nenhuma divergência em identidade e formulário; tolerada em layout interno"). Isso transforma briga de gosto em política.
- Pergunta de negócio: *"quanto estamos dispostos a pagar em consistência para que cinco times entreguem sem esperar uns pelos outros?"* — vai para quem deve decidir, e você sai do papel de defensora de tecnologia.

---

## 6 — "A meta que te deram"

**Situação.** Meta pronta: "melhorar a performance do canal em 30%". Performance não está definida, 30% soa bem, e a maior parte da latência vem de uma dependência que não é sua.

**Estratégia dada — "renegociar a métrica, não o esforço":** não discutir o tamanho; discutir **qual número** representa a experiência, com a parte fora do controle explicitada.

**Perguntas.**
1. A contraproposta em SMART, com o indicador justificado.
2. O interesse por trás do "30%" e a pergunta que o descobre.
3. Como tratar a dependência externa sem parecer desculpa antecipada.
4. A trava.
5. Se for "30% e ponto": BATNA e o que fazer no dia seguinte.

**Leitura.**
- Indicador centrado no usuário e sensível ao que você controla: p75 de LCP nas 3 telas de maior tráfego, no RUM, segmentado por rede, com a fatia da dependência externa **reportada à parte desde o início**. Não reduziu a ambição; tornou o número interpretável.
- Interesse: quase sempre um compromisso anterior (promessa ao comitê, reclamação de cliente grande). Pergunta: *"esse 30% está amarrado a algum compromisso que você já assumiu? Quero que o que eu entregar sirva para aquela conversa."* Aliança, não desafio.
- Dependência externa entra **agora**, medida e separada, com compromisso: "reporto essa fatia mensalmente e levo ao time responsável". Troca desculpa futura por transparência presente.
- Trava: sem regressão de erro; sem reduzir o conteúdo da primeira tela (o jeito rápido de carregar mais rápido é entregar menos).
- BATNA quase nunca é conflito: é **documentar** no dia seguinte o entendimento, a métrica reportada e a premissa. Em seis meses é a diferença entre "não bateu" e "bateu o possível e avisou em janeiro".

---

## 7 — "Dez minutos no fórum"

**Situação.** Dez minutos no fórum de arquitetura para defender um trimestre de observabilidade, que não entrega funcionalidade. Depois de você, alguém pede o mesmo tempo de time para uma feature com receita estimada.

**Estratégia dada — "vender diagnóstico, não solução":** nada de ferramenta, dashboard ou arquitetura. O custo atual da cegueira em números, e a decisão que a organização não consegue tomar por falta de dado.

**Perguntas.**
1. Abertura de três frases, com o pedido.
2. Três números, e de onde tirar cada um **hoje**.
3. Analogia para não técnicos — e o risco de ser boa demais.
4. Resposta a "não dá para fazer aos poucos, junto com as features?".
5. Com uma folha circulada antes: o que vai na folha e o que fica na fala?

**Leitura.**
- A primeira frase custa dinheiro: horas gastas diagnosticando incidentes que levariam minutos, e incidentes sem causa até hoje. Termina pedindo a **decisão de alocar**, não discussão de ferramenta.
- Números obteníveis com o que existe: tempo médio de resolução (chamados); pessoas × horas por incidente (calendário, canal de guerra); **decisões pendentes por falta de dado** — o que mais impressiona, porque ninguém tinha contado.
- "Painel do carro" leva a "então é acessório". Melhor para audiência financeira: **é auditoria** — não gera receita e ninguém opera sem.
- "Aos poucos?": "sim, em parte" honesto + o limite — o fatiável já está sendo fatiado; o resto exige mexer no caminho crítico de todos ao mesmo tempo, porque trilha pela metade não responde a pergunta de um incidente.
- Folha circulada transforma os dez minutos em discussão de objeções — onde a decisão acontece.

---

## 8 — "O token de inovação"

**Situação.** Tecnologia nova em todas as conversas. Três squads querem adotar, cada uma do seu jeito; dois pilotos rodam sem ninguém saber direito. Liderança animada. Perguntam a você o que fazer.

**Estratégia dada — "um token, um caso, um dono, um prazo":** gasta-se **um** token de inovação: um caso com valor mensurável, um time dono, um trimestre, critério definido antes. Os outros pilotos param.

**Perguntas.**
1. Como escolher **o** caso? Critérios, em ordem.
2. "Os outros param" custa capital político. Vale? O que oferecer em troca?
3. Critério de sucesso não auto-realizável.
4. Onde está no eixo de Wardley, e o que isso muda na gestão?
5. O risco de **não** gastar o token, sem apelar para medo.

**Leitura.**
- Critérios em ordem: resultado mensurável em semanas; caso real com dono que se importa; prejuízo contido se falhar; aprendizado transferível. Erro comum: o caso mais empolgante, que falha no 1 e no 3.
- Alternativa que preserva capital: os outros seguem como **exploração declarada, com prazo**, sem promessa de produção e sem consumir suporte de plataforma. Mata-se a expectativa de virar produção por inércia, não a curiosidade.
- Sucesso não pode ser adoção nem satisfação do time. Precisa ser mudança observável **fora** do time: tempo de tarefa real, erro, custo, uso sem treinamento.
- Está na **gênese**: gestão por experimento, desperdício aceito, critério de encerramento. Método de commodity (plano detalhado, estimativa firme, meta de adoção) mata e depois "não funciona aqui".
- Não gastar é custo de **tempo**: "quando virar padrão de mercado, aprendemos sob pressão, com prazo de terceiro" — não depende de a tecnologia ser boa.

---

## 9 — "A pessoa que virou gargalo"

**Situação.** Você virou referência; toda decisão relevante passa por você. Agenda é reunião; trabalho profundo acontece à noite. Reclamar parece ingratidão; recusar, desinteresse.

**Estratégia dada — "escrever em vez de responder":** toda pergunta recebida pela segunda vez vira documento. 20% da semana bloqueados para escrever; recusar convites sem decisão; responder com link.

**Perguntas.**
1. O custo de curto prazo e como atravessar as primeiras semanas.
2. O critério de delegar, em uma frase.
3. Sinal de delegar cedo demais; e tarde demais.
4. Como tornar visível um trabalho que aparece menos (sem "confiar que vão perceber").
5. De qual papel abrir mão, e o que se perde.

**Leitura.**
- Custo: parecer menos disponível. Atravessa-se **anunciando** o método no fórum certo — "vou responder mais com link e menos com reunião". Anunciado vira método; não anunciado vira distância.
- *Delega-se o que é reversível e ensinável; faz-se o que é irreversível e ainda não está escrito.* (Tipo 1/2 aplicado a si.)
- Cedo demais: a pessoa volta mais de uma vez à mesma decisão, e ela é tipo 1. Tarde demais: você é a única que sabe, e isso já não é mérito — é falta de oportunidade dos outros. O segundo é mais difícil de ver porque é confortável.
- Visibilidade = artefato com o seu nome (ADR, estratégia, registro de progresso), circulado pedindo crítica, com relato em cadência. Especialista é assimétrico: quando dá certo, nada acontece — só o registro transforma "nada aconteceu" em "nada aconteceu **por causa disto**".
- Sem resposta certa. A honesta costuma ser: o papel mais gostoso de largar é o mais visível; o mais necessário é o que dá identidade.

---

## 10 — "A estratégia que era sua e deu errado"

**Situação.** Uma decisão que você defendeu e conduziu há oito meses se mostrou subótima; o time convive com o custo. Ninguém cobrou. Vem a avaliação.

**Estratégia dada — "autópsia pública, sem autoflagelo":** escrever e circular a revisão: o que sabia, o que assumiu, o que se provou falso, o que mudaria e **qual sinal deveria ter monitorado e não monitorou**.

**Perguntas.**
1. Por que aumenta a autoridade em vez de diminuir? Quando faria o contrário?
2. Decisão ruim ou resultado ruim? Como demonstrar sem parecer defesa?
3. Que mecanismo detecta o mesmo erro mais cedo?
4. Como entra na avaliação sem virar autossabotagem?
5. Você **conseguiria** escrever isso hoje no seu ambiente? Se não, o problema é seu, do ambiente, ou dos dois?

**Leitura.**
- Autoridade vem de **calibração demonstrada**, não de acerto. Faz o contrário se for autoflagelo (constrange a sala) ou defesa disfarçada (percebida em dois parágrafos).
- Reconstruir o que era **conhecível na época**. Previsível → decisão ruim, diga. Não previsível → decisão boa, resultado ruim; o aprendizado é de monitoramento.
- Mecanismo: sinal monitorado, com limite e data — o desenho de um SLO aplicado a uma decisão. "Revisamos em 90 dias; se Y não se mover, reabrimos."
- Na avaliação: "conduzi, revisei, corrigi, instituí o mecanismo". Autossabotagem é o erro sem correção e sem mecanismo; com os dois, é a história mais forte num comitê.
- Em muitos ambientes a resposta honesta é "não conseguiria". Isso é dado sobre o ambiente. Começa-se por uma versão menor, circulada para duas pessoas de confiança.
