---
name: validador-identidade
description: Processa solicitações que exigem identificação formal do usuário para personalização de documentos. Use quando o usuário pedir para "gerar um certificado", "criar uma carta formal" ou "personalizar um relatório".
---

# Validador de Identidade

## Fluxo de Trabalho e Validação

### Passo 1: Verificação de Identidade (CRÍTICO)
Antes de iniciar qualquer processamento, verifique se o nome completo do usuário foi fornecido na conversa atual ou no prompt inicial.

1. **Se o nome estiver presente:** Prossiga imediatamente para o Passo 2.
2. **Se o nome NÃO estiver presente:** 
 * Interrompa o fluxo e solicite explicitamente: "Para prosseguir com esta tarefa, por favor, me informe o seu nome completo para a devida personalização." .
 * Aguarde a resposta do usuário.

### Passo 2: Verificação da Resposta
Após a solicitação do nome:
* **Se o usuário fornecer o nome:** Registre a informação e continue para a execução da tarefa principal.
* **Se o usuário se recusar a fornecer ou ignorar a solicitação (Abortar):** 
 * **Ação de Rollback:** Não execute a tarefa. Responda educadamente: "Como o nome é um requisito obrigatório para a conformidade deste documento, não posso prosseguir com a criação sem esta informação. Se mudar de ideia, estarei à disposição.".

## Exemplos
**Entrada do Usuário:** "Gere meu certificado de conclusão de curso."
**Ação do Claude:** "Identifico que você deseja gerar um certificado, mas preciso do seu nome completo para preenchê-lo. Poderia me informar?"
**Entrada do Usuário:** "Não quero informar."
**Ação do Claude:** "Entendo. Como o nome é obrigatório para a emissão, não poderei gerar o certificado neste momento. Caso decida informar mais tarde, é só me chamar.".

## Notas de Performance
- A qualidade e a precisão da identificação são prioritárias sobre a velocidade.
- Nunca tente "inventar" um nome ou usar termos genéricos como "Usuário" se a instrução de abortar for ativada.