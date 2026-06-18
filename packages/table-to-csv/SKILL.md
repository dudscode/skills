---
name: table-to-csv
description: Processa solicitações para exportar uma tabela ou lista de dados de uma tela Angular para CSV ou, opcionalmente, para .xlsx com cabeçalho de marca (logo + título).
---

# Table to CSV
## Visão Geral
Esta Skill é ativada quando o usuário pede para "exportar para CSV", "baixar como CSV", "gerar CSV da tabela", "exportar essa lista/tabela em planilha" ou "exportar com logo/cabeçalho da empresa" em uma aplicação Angular. Ela orienta a implementação de uma funcionalidade simples e segura de exportação de dados tabulares para um arquivo `.csv` baixável (sem dependências externas) ou, quando o usuário pedir explicitamente logo/imagem no cabeçalho, para um `.xlsx` com cabeçalho de marca.

## Fluxo de Trabalho
1. **Detecção da Necessidade:** O agente identifica que a tarefa envolve exportar dados tabulares (array de objetos ou tabela renderizada) e se há pedido de logo/cabeçalho de marca.
2. **Ativação da Skill:** Ativa `table-to-csv`, que define a implementação (serviço genérico de CSV, e opcionalmente o serviço `.xlsx` com branding) e o checklist de segurança obrigatório.
3. **Implementação:** Cria/ajusta o serviço de exportação e o botão/ação de download conforme o padrão do projeto.
4. **Verificação de Segurança:** Antes de finalizar, confere o checklist de segurança (sem dados sensíveis, mitigação de CSV injection, nome de arquivo sanitizado, logo apenas de asset local quando aplicável).

## Exemplos
- **Entrada do Usuário:** "Adiciona um botão para exportar essa tabela em CSV."
  **Ação do Claude:** Ativa `table-to-csv`, cria `CsvExportService` e adiciona o botão que chama `exportData(...)`, aplicando o checklist de segurança.
- **Entrada do Usuário:** "Quero exportar essa tabela com a logo da empresa e um título no topo."
  **Ação do Claude:** Ativa `table-to-csv`, explica que `.csv` não suporta imagens, instala `exceljs`, cria `XlsxBrandedExportService` usando um asset local de logo e adiciona o botão que chama `exportWithBranding(...)`.
