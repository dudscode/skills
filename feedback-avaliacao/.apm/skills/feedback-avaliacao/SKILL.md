---
name: feedback-avaliacao
description: Solicita ao usuário o preenchimento de uma pesquisa de avaliação ao final de um fluxo de trabalho que utilizou o cnpj-validator ou o print-to-pdf. NÃO deve ser usada logo após a execução dessas skills, apenas quando toda a implementação/tarefa solicitada pelo usuário no prompt for concluída.
metadata:
  version: 1.0.0
  author: Especialista em Compliance
---

# Solicitação de Avaliação

## Quando Ativar
Esta Skill é ativada **somente ao final de todo o fluxo de trabalho** de um prompt que, em algum momento, acionou a Skill `cnpj-validator` e/ou `print-to-pdf` (lista configurável em `scripts/feedback-triggers.json`).

- **NÃO ative** logo após a execução de `scripts/validate.py` (cnpj-validator) ou logo após implementar/usar a exportação de PDF (print-to-pdf).
- **Ative** apenas depois que todas as demais tarefas solicitadas pelo usuário no mesmo prompt (implementação, edições, respostas, etc.) tiverem sido concluídas e a resposta final estiver prestes a ser enviada ao usuário.
- Caso a skill-gatilho seja acionada, mas o usuário ainda continue a conversa pedindo novas tarefas dentro do mesmo fluxo, aguarde até que esse fluxo seja efetivamente encerrado para então ativar esta Skill.
- Ative apenas **uma vez** por fluxo, mesmo que mais de uma skill-gatilho tenha sido usada.

## Instruções Procedurais

### Passo 1: Concluir o Fluxo Principal
Finalize normalmente toda a implementação ou resposta solicitada pelo usuário, incluindo o resultado da validação de CNPJ.

### Passo 2: Convite para Avaliação
Ao final da resposta final do fluxo, adicione um convite breve e não intrusivo para o usuário avaliar o atendimento, incluindo o link do formulário:

> Antes de encerrar: se puder, deixe sua avaliação sobre este atendimento neste formulário rápido: https://forms.office.com/r/z1k6WMbCfM

### Passo 3: Respeitar a Resposta do Usuário
- Não insista nem repita o convite caso o usuário não responda ou recuse.
- Não bloqueie nem condicione a entrega do trabalho ao preenchimento do formulário.

## Exemplos
**Entrada do Usuário:** "Valide este CNPJ: 12.345.678/0001-95 e depois crie um relatório com o resultado."
**Ação do Claude:** Ativa `cnpj-validator`, valida o CNPJ, gera o relatório solicitado e, somente ao final de toda a resposta, ativa `feedback-avaliacao` para convidar o usuário a preencher o formulário de avaliação.

**Entrada do Usuário:** "Adiciona um botão para exportar essa tela de relatório em PDF."
**Ação do Claude:** Ativa `print-to-pdf`, implementa a exportação e, somente ao final de toda a resposta, ativa `feedback-avaliacao` para convidar o usuário a preencher o formulário de avaliação.

## Notas de Performance
- Esta Skill não interfere no resultado da validação nem no fluxo principal da tarefa.
- O convite deve ser curto (uma linha) para não desviar a atenção do resultado entregue.

## Instalação Opcional (Hook de Reforço - Nível 3)
Para projetos que queiram garantir o convite mesmo se o modelo esquecer, esta skill inclui um hook `Stop` pronto em `scripts/`:

- `scripts/feedback-trigger.py`: hook que verifica, ao final da resposta, se a Skill `cnpj-validator` (ou outras listadas em `scripts/feedback-triggers.json`) foi usada na sessão e, em caso positivo, instrui o agente a adicionar o convite de avaliação uma única vez por sessão.
- `scripts/feedback-triggers.json`: lista de skills-gatilho + URL do formulário. Adicione novos nomes de skill aqui para que também disparem o convite.

Para habilitar no projeto que consome esta skill, copie a pasta `scripts/` para dentro do projeto (ex: `.claude/feedback-avaliacao/`) e registre o hook em `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/feedback-avaliacao/feedback-trigger.py\""
          }
        ]
      }
    ]
  }
}
```

Adicione `.claude/.feedback-state/` ao `.gitignore` do projeto consumidor (estado por sessão, não deve ser versionado).
