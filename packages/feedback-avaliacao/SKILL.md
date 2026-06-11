---
name: feedback-avaliacao
description: Solicita ao usuário o preenchimento de uma pesquisa de avaliação ao final de fluxos de trabalho que utilizaram skills-gatilho (ex: cnpj-validator, print-to-pdf).
---

# Feedback de Avaliação
## Visão Geral
Esta Skill é um pacote independente, declarado como dependência por outras skills (ex: `validate`, `print-to-pdf`). Ela é ativada apenas ao final de todo o fluxo de trabalho de um prompt que, em algum momento, acionou uma das skills-gatilho configuradas, convidando o usuário a preencher uma pesquisa de satisfação.

## Fluxo de Trabalho
1. **Detecção:** Durante o processamento do prompt, alguma skill que declara `feedback-avaliacao` como dependência é utilizada (ex: `cnpj-validator`, `print-to-pdf`).
2. **Conclusão do Fluxo Principal:** O agente finaliza toda a implementação/resposta solicitada.
3. **Convite para Avaliação:** Apenas na resposta final do fluxo, ativa `feedback-avaliacao`, que adiciona um convite breve com o link do formulário.
4. **Sem Insistência:** Se o usuário não responder ou recusar, o convite não é repetido nem condiciona a entrega.

## Exemplos
- **Entrada do Usuário:** "Valide este CNPJ: 12.345.678/0001-95 e depois crie um relatório com o resultado."
  **Ação do Claude:** Ativa `cnpj-validator`, valida o CNPJ, gera o relatório e, somente ao final de toda a resposta, ativa `feedback-avaliacao`.
- **Entrada do Usuário:** "Adiciona um botão para exportar essa tela de relatório em PDF."
  **Ação do Claude:** Ativa `print-to-pdf`, implementa a exportação e, somente ao final de toda a resposta, ativa `feedback-avaliacao`.
