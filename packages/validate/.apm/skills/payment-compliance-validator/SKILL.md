---
name: payment-compliance-validator
description: Valida transações financeiras contra regras de conformidade, limites de valor e listas de sanções. Use obrigatoriamente antes de "processar pagamentos", "transferir fundos" ou "aprovar faturas".
metadata:
  version: 1.1.0
  compliance_level: strict
---

# Validador de Conformidade Financeira

## Fluxo de Trabalho (Conformidade antes da Ação) [1, 8]

### Passo 1: Coleta de Dados da Transação
Antes de qualquer processamento, extraia os seguintes dados:
- Identificação do destinatário (ID ou Nome).
- Valor total e moeda.
- Jurisdição de origem e destino.

### Passo 2: Validação Determinística (CRÍTICO) [2, 9]
Execute o script de validação para garantir precisão técnica que instruções de linguagem podem omitir:
`bash: python3 scripts/check_compliance.py --amount {valor} --recipient {id}`

### Passo 3: Portão de Decisão [8]
Analise o resultado do script:
1. **SE o script retornar "APPROVED":** Prossiga para a ferramenta de pagamento solicitada pelo usuário.
2. **SE o script retornar "FLAGGED" ou "DENIED":** 
   - **Interrompa o processo imediatamente.** [8]
   - Não tente contornar a regra ou pedir desculpas para prosseguir.
   - Responda: "Esta transação foi bloqueada por violação das políticas de compliance: [motivo do script]".

## Exemplos [3, 10]
**Entrada do Usuário:** "Transfira $50.000 para a conta de Investimentos Internacionais."
**Ação do Claude:** Ativa `payment-compliance-validator`, executa o script de checagem, identifica que o valor excede o limite diário sem aprovação manual e informa ao usuário que a tarefa foi abortada por segurança.

## Notas de Performance [2]
- **Qualidade sobre Velocidade:** O agente deve levar o tempo necessário para validar cada campo.
- **Confiabilidade:** O uso do script na pasta `scripts/` é obrigatório para evitar erros de interpretação do modelo. [2, 11]
Por que esta Skill é considerada uma boa prática:
Validação antes da Ação: Ela implementa o princípio de "Conformidade antes da ação", garantindo que o agente não execute uma tarefa perigosa sem uma verificação prévia
.
Uso de Scripts (Nível 3): Para validações críticas (como cálculos de impostos ou listas de sanções), as fontes recomendam scripts em vez de apenas texto, pois o código é determinístico e não consome tokens desnecessários da janela de contexto
.
Rollback Explícito: A Skill define uma instrução de "abortar" clara, o que é essencial para fluxos de automação onde o agente deve parar se os requisitos de segurança não forem atingidos
.
Divulgação Progressiva: O modelo só carrega as regras detalhadas de compliance no momento em que uma transação é mencionada, mantendo o sistema leve
