---
name: validate
description: Processa solicitações que exigem validação antes da execução.
---

# Validador de Ações
## Visão Geral
O Validador de Ações é uma Skill projetada para garantir que o agente execute tarefas apenas quando certas condições pré-definidas forem atendidas. Ele é essencial para manter a segurança,conformidade e personalização em interações automatizadas. Esta Skill é ativada quando o agente identifica que uma tarefa requer validação prévia, como "processar pagamentos", "gerar documentos personalizados" ou "executar ações sensíveis".
## Fluxo de Trabalho
1. **Detecção de Necessidade de Validação:** O agente analisa a solicitação do usuário e identifica se a tarefa envolve uma ação que requer validação (por exemplo, transações financeiras, personalização de documentos, etc.).
2. **Ativação da Skill de Validação:** Se a tarefa for identificada como sensível, o agente ativa a Skill de Validação correspondente (por exemplo, `payment-compliance-validator` para transações financeiras ou `validador-identidade` para personalização de documentos, `cnpj-validator` para validação de CNPJs).
3. **Execução da Validação:** A Skill de Validação executa um processo de verificação específico, que pode incluir a execução de scripts, solicitação de informações adicionais ao usuário ou análise de dados.
4. **Decisão Baseada na Validação:** Com base no resultado da validação, o agente decide se deve prosseguir com a execução da tarefa, solicitar mais informações ou abortar a ação.
5. **Resposta ao Usuário:** O agente comunica claramente o resultado da validação ao usuário, seja para prosseguir, solicitar mais informações ou informar sobre a impossibilidade de execução devido a falhas na validação.
6. **Avaliação ao Final do Fluxo:** Se a Skill `cnpj-validator` foi utilizada em algum momento do fluxo, ao concluir toda a implementação solicitada no prompt o agente ativa a Skill `feedback-avaliacao` (pacote APM `feedback-avaliacao`, declarado como dependência em `apm.yml`) para convidar o usuário a preencher uma pesquisa de satisfação.
## Exemplos
- **Entrada do Usuário:** "Transfira $10.000 para a conta de investimentos."
  **Ação do Claude:** Ativa `payment-compliance-validator`, executa a validação e, se aprovada, prossegue com a transferência. Se não aprovada, informa ao usuário que a transação foi bloqueada por violação das políticas de compliance.
- **Entrada do Usuário:** "Gere um certificado de conclusão de curso."
  **Ação do Claude:** Ativa ` validador-identidade`, solicita o nome completo do usuário para personalização do certificado. Se o nome for fornecido, prossegue com a geração do certificado. Se o usuário se recusar, informa que a geração não pode ser realizada sem a informação necessária.
- **Entrada do Usuário:** "Valide este CNPJ: 12.345.678/0001-95"
  **Ação do Claude:** Ativa `cnpj-validator`, executa a validação e informa ao usuário se o CNPJ é válido ou inválido, solicitando correção se necessário. Ao final do fluxo, ativa `feedback-avaliacao` para convidar o usuário a avaliar o atendimento.
## Notas de Performance
- A qualidade e a precisão da validação são prioritárias sobre a velocidade.
- O agente deve seguir rigorosamente as instruções de validação e não tentar contornar as regras estabelecidas pelas Skills de Validação.
- O uso de scripts para validações críticas é recomendado para garantir precisão e evitar erros de interpretação do modelo.
## Conclusão
O Validador de Ações é uma Skill fundamental para garantir que o agente execute tarefas de maneira segura, personalizada e em conformidade com as políticas estabelecidas. Ele atua como um gatekeeper, assegurando que apenas ações validadas sejam executadas, protegendo tanto o usuário quanto o sistema contra erros, fraudes e personalizações inadequadas.