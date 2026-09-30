# Traduzir técnica em dinheiro, risco, tempo e reputação

Use no modo **Traduzir** e na parte de impacto de qualquer artefato.

## O problema

O erro padrão é apresentar **a solução** ("vamos adotar circuit breaker") ou **a métrica técnica** ("o p95 caiu 40%") a quem não tem como avaliar nenhuma das duas. A audiência não é desinteressada: ela responde por outra coisa, e o que foi trazido não está na moeda dela.

## As quatro moedas

| Moeda | Pergunta que responde | Como converter |
|---|---|---|
| **Dinheiro** | quanto entra ou deixa de sair? | receita influenciada, custo de infra, horas de time, custo de chamado |
| **Risco** | o que pode dar muito errado? | indisponibilidade, exposição regulatória, incidente de segurança, dependência de fornecedor |
| **Tempo** | quando, e o que atrasa? | time to market, lead time, capacidade liberada |
| **Reputação** | o que os outros vão ver? | NPS, imagem em incidente público, avaliação de auditoria |

Antes de converter, descubra a moeda de **quem vai ouvir**, não a sua.

## As conversões

**Latência → dinheiro.** Latência → abandono → conversão → receita. Número público ancora (há relatos públicos de grandes varejistas sobre perda de receita por cada 100 ms), mas o argumento forte é o **próprio funil**: "na coorte de 4G, quem espera mais de 3s abandona 2,4× mais; são N sessões/mês; recuperando metade, são X contratos".

**Disponibilidade → dinheiro e risco.** 99,9% ≈ 43 min/mês fora; 99,95% ≈ 22 min. A conversa útil não é "mais um nove", é *"nesses 43 minutos, quantas contratações não acontecem e quantos chamados isso gera?"*.

**Débito técnico → tempo.** A mais poderosa e a menos usada: débito não é feio, é **lento**. "Toda alteração na contratação toca 3 repositórios e 2 times: ~9 dias de lead time contra ~2 no modernizado. 7 dias × ~30 alterações/ano ≈ 210 dias-pessoa/ano." Agora há um número comparável ao custo de arrumar.

**Confiabilidade → risco quantificado (error budget).** *"O SLO nos dá 43 minutos por mês. Gastamos 38 em julho. Mais uma dependência síncrona no caminho crítico gasta o orçamento inteiro."* Discussão de arquitetura vira discussão de orçamento — a língua nativa de quem decide.

**Custo de infra → dinheiro direto.** A mais fácil: preço de task, de NAT gateway, de tráfego entre AZs. "Isso custa R$ X/mês" pesa mais que "isso é caro" em qualquer sala.

## O erro simétrico: traduzir demais

Prometer número sem base ("vai aumentar a conversão em 15%") é dívida que vence no trimestre seguinte e destrói credibilidade técnica.

**O formato honesto, sempre em três partes:**

> "Minha estimativa é entre 3 e 6 pontos, com confiança média — **assumindo** que o abandono na primeira tela seja por latência, que os dados sugerem mas não provam. O jeito mais barato de verificar antes de investir é [sonda]."

Intervalo, premissa, verificação. Isso **aumenta** a autoridade; número seco e errado a destrói. Precisão inclui ser precisa sobre o que não se sabe.

## A tabela de impacto (antes de escrever qualquer parágrafo de resultado)

Preencha com a pessoa. Célula vazia é exatamente a lacuna que faz um avaliador dizer "faltou mensuração":

| Campo | Resposta |
|---|---|
| Número **antes** | |
| Número **depois** | |
| Fonte (ferramenta, query) | |
| O que mais mudou no período e pode explicar | |
| Qual seria a evidência de que **não** funcionou | |
| Quanto vale em dinheiro, risco, tempo ou reputação | |

A quinta linha é a mais rara e a que mais convence: quem diz o que falsificaria o próprio resultado é quem a sala acredita.

Com a tabela cheia, escreva o **parágrafo de impacto** (B.6 em [modelos.md](modelos.md)).

## Previsto não é realizado

- Economia "prevista" é previsão; marque assim.
- Elo causal não medido (ex.: lead time → NPS) é premissa; declare.
- "Ajudei muito" não é resultado. Número antes/depois com fonte é.
- Se a pessoa não tem o número, a primeira ação recomendada é **como obter o número**, não um parágrafo sem ele.
