---
name: estrategista
description: Processa solicitações de estratégia técnica — avaliar ou escrever uma estratégia, criticar um plano ou meta, priorizar iniciativas, preparar uma apresentação para liderança, traduzir impacto técnico em negócio, escrever ADR/OKR ou treinar pensamento estratégico com cenários.
---

# Estrategista
## Visão Geral
Esta Skill é ativada quando o usuário pede para "revisar esta estratégia", "escrever um ADR/OKR", "priorizar essas iniciativas", "preparar a apresentação para a liderança", "defender um investimento técnico", "comunicar o impacto" ou "treinar com um cenário". Ela torna explícito, escrito e mensurável o raciocínio estratégico da pessoa, sempre com a régua: **diga o que você deixa de fazer.**

## Fluxo de Trabalho
1. **Detecção da Necessidade:** O agente identifica que a tarefa envolve uma decisão técnica que alguém vai ter que bancar.
2. **Ativação da Skill:** Ativa `estrategista`, que define os modos (Avaliar, Escrever, Decidir, Preparar a sala, Traduzir, Treinar, Revisar uma decisão, O que ler) e carrega só a referência do modo em uso.
3. **Execução:** Aplica o fluxo do modo — kernel de Rumelt e sinais de má estratégia, modelos de artefato, ferramentas de decisão, preparação de stakeholders ou conversão para dinheiro, risco, tempo e reputação.
4. **Verificação:** Antes de entregar, confere as regras obrigatórias (diagnóstico antes de solução, nenhum número inventado, estimativa com intervalo/premissa/verificação, o que está sólido, informação interna generalizada).

## Exemplos
- **Entrada do Usuário:** "Revise esta estratégia: <texto>."
  **Ação do Claude:** Ativa `estrategista` no modo Avaliar, devolve veredito em uma frase, o que está sólido, os problemas com trecho + sinal + pergunta que desarma e uma reescrita do trecho mais fraco.
- **Entrada do Usuário:** "Tenho 10 minutos no fórum para defender observabilidade."
  **Ação do Claude:** Ativa `estrategista` no modo Preparar a sala, monta o mapa de stakeholders, a abertura em três frases, o memo de uma página e as três objeções prováveis com resposta.
