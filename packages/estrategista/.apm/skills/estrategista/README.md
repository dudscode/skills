# Skill `estrategista`

A apostila da trilha virou uma skill de agente: uma especialista em estratégia técnica que **aplica** o conteúdo em vez de só explicá-lo. Ela avalia, escreve, decide, prepara reunião, traduz e treina — sempre com a régua da trilha: **diga o que você deixa de fazer.**

## Como chamar

Dentro do `roadmap/`, no Claude Code:

```
/estrategista revise esta estratégia: <cole o texto>
/estrategista quero escrever o ADR do TTL do cache de saldo
/estrategista me treina com o cenário 4
/estrategista tenho 10 min no fórum para defender observabilidade
```

Ela também é acionada sem a barra, quando o pedido bate com a descrição (revisar estratégia, priorizar, traduzir impacto, preparar apresentação para liderança…).

No workspace de skills, ela vive em `packages/estrategista/.apm/skills/estrategista/` e é distribuída pelo pacote apm `estrategista`. No roadmap, é exposta ao Claude Code por um symlink em `roadmap/.claude/skills/estrategista`.

## Os modos

| Modo | Para quê |
|---|---|
| **Avaliar** | kernel de Rumelt + quatro sinais de má estratégia + checklist B.4 sobre qualquer texto — inclusive o PDI |
| **Escrever** | estratégia de uma página, ADR, OKR com trava, memo de uma página, parágrafo de impacto, premortem |
| **Decidir** | Cynefin, tipo 1/tipo 2, RICE × custo do atraso, quadro de quatro colunas — e termina numa recomendação |
| **Preparar a sala** | abertura em três frases, mapa de stakeholders, interesses × posições, BATNA |
| **Traduzir** | as quatro moedas, com intervalo, premissa e verificação |
| **Treinar** | os dez cenários da Parte IV, sem mostrar a leitura antes de você responder |
| **Revisar uma decisão** | autópsia pública, decisão × resultado, e o mecanismo que detecta mais cedo |
| **O que ler** | um ou dois itens da biblioteca, pelo problema que você tem agora |

## O que tem dentro

| Arquivo | Vem da apostila |
|---|---|
| [`SKILL.md`](SKILL.md) | os modos, as regras e o fluxo de cada modo |
| [`references/fundamentos.md`](references/fundamentos.md) | Parte I (Temas 1–5) + Tema 15 |
| [`references/ferramentas.md`](references/ferramentas.md) | Parte II (Temas 6–13) + Tema 14 |
| [`references/traducao.md`](references/traducao.md) | Tema 16 + a tabela de impacto do Tema 8 |
| [`references/modelos.md`](references/modelos.md) | Apêndice B + memo, abertura, mapa de stakeholders, quadro de decisão, revisão de decisão |
| [`references/cenarios.md`](references/cenarios.md) | Parte IV + Apêndice A |
| [`references/biblioteca.md`](references/biblioteca.md) | Parte V |

As referências são a apostila **condensada para uso**, não copiada: a apostila continua sendo o material de leitura; a skill é o que se usa na hora de decidir.

## O que ela não faz

- Não inventa número: o que não veio de você vira `‹a confirmar›`.
- Não escreve o artefato por você quando o objetivo é treino.
- Não trata a apostila como critério — o que conta são os três artefatos e as respostas em voz alta.
