---
name: print-to-pdf
description: Processa solicitações para exportar/imprimir o conteúdo atual de uma tela Angular em PDF para download.
---

# Print to PDF
## Visão Geral
Esta Skill é ativada quando o usuário pede para "exportar para PDF", "baixar como PDF", "gerar PDF da tela atual", "imprimir em PDF" ou similar em uma aplicação Angular. Ela orienta a implementação de uma funcionalidade simples e segura de captura do conteúdo exibido e geração de um arquivo PDF para download no navegador.

## Fluxo de Trabalho
1. **Detecção da Necessidade:** O agente identifica que a tarefa envolve gerar um PDF a partir de conteúdo renderizado na tela.
2. **Ativação da Skill:** Ativa `print-to-pdf`, que define a biblioteca recomendada, a implementação (serviço + componente) e o checklist de segurança obrigatório.
3. **Implementação:** Cria/ajusta o serviço de exportação e o botão/ação de download conforme o padrão do projeto.
4. **Verificação de Segurança:** Antes de finalizar, confere o checklist de segurança (dados sensíveis ocultos, versão da lib auditada, nome de arquivo sanitizado).

## Exemplos
- **Entrada do Usuário:** "Quero um botão para baixar essa tela de relatório como PDF."
  **Ação do Claude:** Ativa `print-to-pdf`, instala/usa `html2pdf.js`, cria `PdfExportService` e adiciona o botão que chama `exportElement(...)`, aplicando o checklist de segurança.
