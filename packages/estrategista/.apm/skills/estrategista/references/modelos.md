# Modelos prontos

Use no modo **Escrever**. Todos cabem em uma página, de propósito. As seções marcadas com ⛔ não podem ficar vazias — se a pessoa não sabe preencher, isso é a primeira pergunta, não um campo a pular.

## B.1 — Estratégia de uma página

```markdown
# Estratégia — <assunto> — <período>

## Diagnóstico
<3 a 5 linhas, em prosa, com pelo menos um número. Sem verbo de ação.>
O que nos impede é: <uma frase>.

## Política norteadora
<1 a 2 linhas. Uma regra de decisão que exclui alternativas.>

## Ações coerentes
1. <ação> — <dono>, <prazo>.  Torna possível: <qual das outras>
2. <ação> — <dono>, <prazo>.  Depende de: <qual>
3. <ação> — <dono>, <prazo>.

## O que isto significa não fazer   ⛔
<2 linhas. Nomeie o que sai, e quem vai sentir falta.>

## Como saberemos que está errado   ⛔
<Sinal observável + prazo de revisão.>
```

**Testes antes de entregar:**
- Diagnóstico termina em "o que nos impede é X", e X é obstáculo, não condição.
- Política: resolve antecipadamente uma classe de discussões? Alguém consegue violá-la sem querer, ou é vaga demais para ser violada?
- Ações: tirando uma, as outras enfraquecem? Cada uma tem dono e prazo?
- "Não fazer": alguém real vai sentir falta?
- "Errado": existe um número e uma data?

### Exemplo completo

> **Estratégia de resiliência do BFF — Q4**
>
> **Diagnóstico.** Nos últimos 90 dias, 4 dos 6 incidentes do canal começaram fora do nosso código: uma API downstream degradou e o BFF segurou as conexões até o timeout do gateway, devolvendo 504 em massa. Cada um custou de 20 a 50 minutos de indisponibilidade parcial da contratação. **O que nos impede não é falta de monitoramento — é que o BFF trata toda dependência como se fosse confiável e igualmente essencial.**
>
> **Política norteadora.** Toda dependência é *essencial* ou *enriquecedora*. Nenhuma enriquecedora pode impedir a resposta: timeout menor, circuit breaker e caminho degradado definido. Na dúvida, é enriquecedora.
>
> **Ações coerentes.**
> 1. Classificar as 11 dependências e registrar em ADR — [dono], 2 semanas. (Torna as outras possíveis.)
> 2. Timeout por dependência, sempre menor que o do chamador, com a cadeia documentada — [dono], 3 semanas. (Depende de 1.)
> 3. Resposta degradada com indicação na interface para as enriquecedoras — [dono], 4 semanas. (Depois de 1 e 2.)
>
> **O que isto significa não fazer.** O cache de segundo nível sai do trimestre. E a tela de contratação vai exibir, às vezes, um bloco vazio em vez de dado — produto precisa aceitar isso explicitamente, ou a estratégia não existe.
>
> **Como saberemos que está errado.** Se em 90 dias a maioria dos incidentes continuar vindo de fora e sendo total em vez de parcial, o diagnóstico está errado — provavelmente é capacidade, não isolamento. Checkpoint: revisão do quarto mês, mesma contagem.

O parágrafo do "não fazer" é o que faz a liderança acreditar no resto: prova que o preço foi entendido.

## B.2 — ADR com peso estratégico

```markdown
# ADR <n> — <decisão em uma frase>

## Status
<Proposto | Aceito | Substituído por ADR n> — <data>

## Contexto
<O diagnóstico: restrição, número, o que acontece hoje.>

## Decisão
<A política, em uma frase que exclui alternativas.>

## Alternativas consideradas
- <alternativa> — recusada porque <motivo real, não "é ruim">
- <alternativa> — recusada porque <...>

## Consequências
### Positivas
### Negativas              ⛔ ADR sem consequência negativa é propaganda
### O que passa a ser proibido
### Quando revisar          ⛔ sinal + data
```

Merece ADR quando é tipo 1: desfazer custa mais que tomar. Contexto = diagnóstico; decisão = política; consequências = o que se deixou de fazer.

## B.3 — OKR com trava

```markdown
Objetivo: <qualitativo, sem número, memorável>

KR1 <métrica> de <X> para <Y>
KR2 <métrica> de <X> para <Y>
KR3 (trava) <métrica que impede bater os outros do jeito errado>   ⛔

Confiança inicial: <0 a 10>   ·   Revisão: quinzenal, 20 min
Se a confiança cair abaixo de 5, a conversa é sobre <o quê>, não sobre esforço.
```

Regras: o objetivo não tem número; nenhum KR pode ser marcado como "feito"; pelo menos uma trava. Exemplo de trava para OKR pessoal de especialista: "nenhuma decisão tomada sem ADR publicado", "sem aumento no meu tempo em reunião".

Exemplo de produto:
> **Objetivo:** a contratação no canal deixa de ser um funil que vaza.
> KR1 conclusão sobe de 54% para 68% · KR2 p75 até a primeira interação cai de 3,4s para 2,0s · **KR3 (trava)** 5xx no BFF ≤ 0,3% · **KR4 (trava)** nenhum aumento de chamados de suporte do fluxo.

## B.4 — Checklist de má estratégia

Rode em qualquer apresentação, plano, PDI — inclusive no próprio rascunho.

- [ ] Existe um **diagnóstico**, ou só metas e iniciativas?
- [ ] A frase central tem **oposto defensável**, ou é fluff?
- [ ] A política **proíbe** alguma coisa?
- [ ] As ações **se reforçam**, ou são projetos paralelos?
- [ ] Está dito o que **deixa de ser feito**?
- [ ] Existe um sinal que indicaria que o diagnóstico está **errado**?
- [ ] Alguma decisão **tipo 2** está sendo tratada como tipo 1?
- [ ] A estrutura de times **permite** o que está sendo proposto?

## B.5 — Roteiro de premortem (30 min)

1. **2 min** — enquadramento: "é daqui a <prazo>, o projeto falhou de forma clara e constrangedora."
2. **5 min** — cada pessoa escreve sozinha, em silêncio. Sem falar.
3. **10 min** — cada uma lê **uma** razão por vez, em rodadas, sem debate.
4. **8 min** — agrupar e escolher as 3 mais prováveis × mais graves.
5. **5 min** — para cada uma: qual é o **sinal precoce**, e quem observa?

Saída obrigatória: três sinais precoces com dono. Sem isso, foi terapia.

## B.6 — Parágrafo de impacto

Para avaliação, banca, PDI, LinkedIn. Preencha antes a tabela de impacto de [traducao.md](traducao.md).

```
<O que mudou, sem jargão — uma frase.>
<Número antes → número depois, com a fonte.>
<A conversão: dinheiro, risco, tempo ou reputação.>
<A premissa que sustenta a conversão.>
<O que ainda não está provado.>   ⛔
```

Cinco linhas. Legível por um gestor sem background técnico.

## Memo de uma página (pedir uma decisão)

```
1. A situação (diagnóstico)            3–5 linhas, com um número
2. O que está no nosso caminho         2–3 linhas, nomeado
3. A recomendação (política)           1–2 linhas, do que exclui
4. O que isso significa não fazer      2 linhas — nomeie algo que alguém vai sentir falta   ⛔
5. Como saberemos se deu certo         2 linhas, métrica e prazo
6. O que eu preciso de vocês           1 linha
```

Circule **antes** da reunião. Mande primeiro para uma pessoa de confiança, depois para quem decide.

## Abertura em três frases (BLUF)

```
Recomendo <a decisão, em uma frase>.
Por três motivos: <1>, <2>, <3>.            ← cada um com número, se houver
O que eu preciso desta reunião é <decisão | ciência | ajuda para destravar X>.
```

## Mapa de stakeholders

| Pessoa/área (por papel) | O que ganha | O que perde | Como é avaliada | Decidir, ser ouvida ou só saber? |
|---|---|---|---|---|

## Quadro de decisão

| Item | Custo de esperar | Reversível? (tipo 1/2) | Quem fica bravo se sim | Quem fica bravo se não |
|---|---|---|---|---|

## Revisão de decisão (autópsia pública)

```markdown
# Revisão — <decisão> — <data original> → <hoje>

## O que eu sabia na época
## O que eu assumi
## O que se provou falso
## Era previsível? (decisão ruim × resultado ruim)
## O que eu mudaria
## O sinal que eu deveria ter monitorado   ⛔
## O mecanismo daqui para frente           ⛔ sinal + limite + data de revisão
```

Sem autoflagelo (vira sobre você) e sem defesa disfarçada (a sala percebe em dois parágrafos). Na avaliação, entra como "conduzi, revisei, corrigi e instituí o mecanismo que detecta mais cedo".
