---
name: table-to-csv
description: Exporta uma tabela (array de dados ou elemento <table> renderizado) para CSV ou, opcionalmente, para .xlsx com um cabeçalho de marca (logo + título) configurável, iniciando o download no navegador. Use quando o usuário pedir para "exportar para CSV", "baixar como CSV", "gerar CSV da tabela", "exportar essa lista/tabela em planilha" ou "exportar com logo/cabeçalho da empresa".
metadata:
  version: 2.0.0
  author: Especialista Angular
---

# Table to CSV (Angular)

## Quando usar
Sempre que o usuário pedir para exportar dados tabulares (uma lista, um array de
objetos, ou uma tabela HTML já renderizada na tela) para um arquivo baixável.
Funciona com qualquer formato de dados — não é específico de nenhum domínio
(vendas, produtos, usuários, etc.) nem de nenhuma marca/empresa específica.

Dois modos, escolha pelo que o usuário pedir:

- **CSV puro (padrão)**: texto simples, sem dependências, abre em qualquer
  planilha. Suporta um título textual simples como primeira linha, mas
  **não suporta imagens** — isso é uma limitação do formato `.csv`, não da
  implementação.
- **`.xlsx` com cabeçalho de marca (opcional)**: quando o usuário quer logo +
  título no topo da planilha, gere `.xlsx` (usa a biblioteca `exceljs`), que
  suporta células mescladas, formatação e imagem embutida. Use isso sempre que
  o pedido envolver "logo", "imagem no cabeçalho" ou "papel timbrado" — não
  tente simular isso em `.csv`.

## Instruções Procedurais

### Passo 1: Sem dependências externas
CSV é um formato de texto simples — **não instale bibliotecas** (`papaparse`,
`json2csv`, etc.) a menos que o usuário peça explicitamente. A geração via
`Blob` + `URL.createObjectURL` nativo do navegador é suficiente, 100% client-side
e sem superfície de ataque adicional.

### Passo 2: Criar o serviço genérico de exportação
Crie um serviço único e reutilizável, agnóstico ao formato dos dados de entrada
(funciona com array de objetos OU com um elemento `<table>` do DOM):

```typescript
// csv-export.service.ts
import { Injectable } from '@angular/core';

export interface CsvColumn<T> {
  /** Cabeçalho exibido na primeira linha do CSV. */
  header: string;
  /** Extrai o valor da célula a partir de um item de dados. */
  value: (item: T) => string | number | boolean | Date | null | undefined;
}

@Injectable({ providedIn: 'root' })
export class CsvExportService {
  private readonly delimiter = ',';

  /**
   * Exporta um array de objetos tipados usando colunas explícitas (recomendado).
   * `title`, se informado, é escrito como uma linha de texto livre antes do
   * cabeçalho das colunas (ex.: "Relatório de Vendas — Junho/2026"). CSV não
   * suporta imagens; para logo + título use `exportWithBranding` (.xlsx).
   */
  exportData<T>(data: T[], columns: CsvColumn<T>[], fileName: string, title?: string): void {
    const headerRow = columns.map((col) => this.escapeCell(col.header));
    const rows = data.map((item) =>
      columns.map((col) => this.escapeCell(this.formatValue(col.value(item)))),
    );
    const titleRows = title ? [[this.escapeCell(title)], []] : [];
    this.download([...titleRows, headerRow, ...rows], fileName);
  }

  /** Exporta diretamente um elemento <table> já renderizado no DOM (fallback genérico). */
  exportTableElement(table: HTMLTableElement, fileName: string): void {
    const rows = Array.from(table.querySelectorAll('tr')).map((tr) =>
      Array.from(tr.querySelectorAll('th, td')).map((cell) =>
        this.escapeCell(cell.textContent?.trim() ?? ''),
      ),
    );
    if (rows.length === 0) {
      throw new Error('A tabela não possui linhas para exportar.');
    }
    this.download(rows, fileName);
  }

  private formatValue(value: string | number | boolean | Date | null | undefined): string {
    if (value === null || value === undefined) {
      return '';
    }
    if (value instanceof Date) {
      return value.toLocaleDateString('pt-BR');
    }
    return String(value);
  }

  /** Escapa aspas duplas e envolve em aspas se houver delimitador, aspas ou quebra de linha. */
  private escapeCell(cell: string): string {
    const needsQuoting = /["\n\r]/.test(cell) || cell.includes(this.delimiter);
    const escaped = cell.replace(/"/g, '""');
    return needsQuoting ? `"${escaped}"` : escaped;
  }

  private download(rows: string[][], fileName: string): void {
    const safeFileName = fileName.replace(/[^a-zA-Z0-9-_.]/g, '_');
    const finalName = safeFileName.toLowerCase().endsWith('.csv')
      ? safeFileName
      : `${safeFileName}.csv`;

    // BOM UTF-8: garante acentuação correta ao abrir no Excel.
    const csvContent = '﻿' + rows.map((row) => row.join(this.delimiter)).join('\r\n');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = url;
    link.download = finalName;
    link.click();

    URL.revokeObjectURL(url);
  }
}
```

### Passo 3: Uso no componente
Prefira `exportData` com colunas explícitas — é tipado, evita exportar campos
sensíveis por acidente, e funciona mesmo se a tabela não estiver visível na tela.
Use `exportTableElement` apenas quando os dados originais não estiverem disponíveis
como array (ex.: tabela montada por outro componente sem acesso aos dados-fonte).

```typescript
// exemplo com array de objetos (recomendado) — adapte o tipo e as colunas aos
// dados reais da tela em questão
interface MeuItem {
  nome: string;
  quantidade: number;
  valor: number;
  data: Date;
}

constructor(private csvExportService: CsvExportService) {}

readonly columns: CsvColumn<MeuItem>[] = [
  { header: 'Nome', value: (item) => item.nome },
  { header: 'Quantidade', value: (item) => item.quantidade },
  { header: 'Valor', value: (item) => item.valor },
  { header: 'Data', value: (item) => item.data },
];

exportarCsv(): void {
  // 4º argumento (opcional): título em texto puro na primeira linha do CSV.
  this.csvExportService.exportData(this.itens(), this.columns, 'exportacao.csv', 'Relatório Geral');
}
```

```html
<button (click)="exportarCsv()">Exportar CSV</button>
```

```typescript
// alternativa: exportar a partir do elemento <table> já renderizado
@ViewChild('minhaTabela') tabelaRef!: ElementRef<HTMLTableElement>;

exportarCsvDaTabela(): void {
  this.csvExportService.exportTableElement(this.tabelaRef.nativeElement, 'exportacao.csv');
}
```

### Passo 4 (Opcional): Exportação `.xlsx` com cabeçalho de marca (logo + título)
Use **apenas** quando o usuário pedir explicitamente logo/imagem no cabeçalho —
para o caso comum (sem imagem), `exportData`/`exportTableElement` já bastam.

```bash
npm install exceljs
npm audit
```

- Fixe a versão no `package.json` e rode `npm audit` regularmente, como em
  qualquer nova dependência.
- A imagem do logo NUNCA deve ser buscada de uma URL externa em tempo de
  exportação (evite vazamento de dados/SSRF); use um asset local do projeto
  (ex.: `assets/logo.png`) carregado via `HttpClient`/`fetch` para o mesmo
  domínio, convertido para `ArrayBuffer`.

```typescript
// xlsx-branded-export.service.ts
import { Injectable } from '@angular/core';
import ExcelJS from 'exceljs';
import { CsvColumn } from './csv-export.service';

export interface BrandingHeader {
  /** Título exibido ao lado/abaixo do logo (ex.: nome do relatório). */
  title: string;
  /** Bytes da imagem (PNG/JPEG) já carregada de um asset local do projeto. */
  logo?: {
    buffer: ArrayBuffer;
    extension: 'png' | 'jpeg';
    /** Largura/altura em pixels da imagem dentro da célula. */
    width: number;
    height: number;
  };
}

@Injectable({ providedIn: 'root' })
export class XlsxBrandedExportService {
  async exportWithBranding<T>(
    data: T[],
    columns: CsvColumn<T>[],
    branding: BrandingHeader,
    fileName: string,
  ): Promise<void> {
    const workbook = new ExcelJS.Workbook();
    const sheet = workbook.addWorksheet('Dados');

    let headerRowIndex = 1;
    if (branding.logo) {
      const imageId = workbook.addImage({
        buffer: branding.logo.buffer,
        extension: branding.logo.extension,
      });
      sheet.addImage(imageId, {
        tl: { col: 0, row: 0 },
        ext: { width: branding.logo.width, height: branding.logo.height },
      });
      sheet.getRow(1).height = Math.max(branding.logo.height * 0.75, 20);
      headerRowIndex = 2;
    }

    sheet.mergeCells(headerRowIndex, 1, headerRowIndex, columns.length);
    const titleCell = sheet.getCell(headerRowIndex, 1);
    titleCell.value = branding.title;
    titleCell.font = { bold: true, size: 14 };
    titleCell.alignment = { horizontal: 'center' };

    const columnHeaderRow = sheet.getRow(headerRowIndex + 2);
    columns.forEach((col, index) => {
      const cell = columnHeaderRow.getCell(index + 1);
      cell.value = col.header;
      cell.font = { bold: true };
    });

    data.forEach((item, rowOffset) => {
      const row = sheet.getRow(headerRowIndex + 3 + rowOffset);
      columns.forEach((col, colIndex) => {
        row.getCell(colIndex + 1).value = this.formatValue(col.value(item));
      });
    });

    const buffer = await workbook.xlsx.writeBuffer();
    this.download(buffer, fileName);
  }

  private formatValue(value: unknown): string | number {
    if (value instanceof Date) {
      return value.toLocaleDateString('pt-BR');
    }
    return value === null || value === undefined ? '' : (value as string | number);
  }

  private download(buffer: ExcelJS.Buffer, fileName: string): void {
    const safeFileName = fileName.replace(/[^a-zA-Z0-9-_.]/g, '_');
    const finalName = safeFileName.toLowerCase().endsWith('.xlsx')
      ? safeFileName
      : `${safeFileName}.xlsx`;

    const blob = new Blob([buffer], {
      type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    });
    const url = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = url;
    link.download = finalName;
    link.click();

    URL.revokeObjectURL(url);
  }
}
```

Uso no componente — carregue o logo como asset local e passe título/colunas
de forma configurável (nunca hardcode marca dentro do serviço genérico):

```typescript
constructor(
  private http: HttpClient,
  private xlsxBrandedExportService: XlsxBrandedExportService,
) {}

async exportarComLogo(): Promise<void> {
  const logoBuffer = await this.http
    .get('assets/logo.png', { responseType: 'arraybuffer' })
    .toPromise();

  await this.xlsxBrandedExportService.exportWithBranding(
    this.itens(),
    this.columns,
    { title: 'Relatório Geral', logo: { buffer: logoBuffer!, extension: 'png', width: 120, height: 40 } },
    'exportacao.xlsx',
  );
}
```

### Passo 5: Checklist de Segurança (CRÍTICO)
Antes de considerar a tarefa concluída, verifique:

1. **Sem dados sensíveis**: ao usar `exportData`, inclua apenas colunas explicitamente
   necessárias — nunca espalhe (`...item`) o objeto inteiro em colunas automáticas se
   ele contiver senhas, tokens, CPF/CNPJ não mascarado, ou dados de outros usuários.
2. **Mitigação de CSV Injection**: se algum valor de célula puder começar com
   `=`, `+`, `-` ou `@` (risco de fórmula maliciosa ao abrir no Excel/Sheets),
   prefixe com um apóstrofo (`'`) antes de escapar — especialmente para campos
   vindos de entrada do usuário (nome, observações, etc.).
3. **Nome de arquivo sanitizado**: a regex de sanitização do serviço já cobre isso;
   não remova essa etapa.
4. **Geração 100% client-side**: não envie os dados para um endpoint externo de
   conversão; o `Blob` nativo é suficiente.
5. **Volume de dados**: para listas muito grandes (>50k linhas), monte as linhas em
   lotes (`chunks`) para evitar bloquear a thread principal antes de criar o `Blob`.
6. **Logo confiável (modo `.xlsx`)**: a imagem deve vir de um asset local do próprio
   projeto (`assets/...`), nunca de uma URL fornecida pelo usuário ou de terceiros —
   evita exfiltração de dados e imagens maliciosas/inadequadas no documento exportado.

## Exemplos
**Entrada do Usuário:** "Adiciona um botão para exportar essa tabela em CSV."
**Ação do Claude:** Cria `CsvExportService` (genérico, reutilizável em qualquer página),
define as `CsvColumn` para os campos relevantes do tipo de dado exibido na tela,
adiciona o botão "Exportar CSV" chamando
`exportData(itens(), columns, 'exportacao.csv')`, e confere o checklist de segurança
(sem campos sensíveis extras, nome sanitizado).

**Entrada do Usuário:** "Quero exportar essa tabela com a logo da empresa e um título no topo."
**Ação do Claude:** Explica que `.csv` puro não suporta imagens, instala `exceljs`,
cria `XlsxBrandedExportService`, carrega a logo como asset local do projeto (sem URL
externa), e adiciona o botão chamando `exportWithBranding(itens(), columns, { title, logo }, 'exportacao.xlsx')`.

## Solução de Problemas
- **Acentos/caracteres especiais quebrados no Excel**: confirme que o BOM (`﻿`)
  está presente no início do conteúdo — já incluso no método `download` do CSV.
- **Células com vírgula ou aspas quebrando colunas**: confirme que `escapeCell` está
  sendo aplicado a toda célula antes de juntar a linha — nunca monte a linha CSV
  manualmente com `join(',')` sem escapar.
- **Download não dispara em Safari/iOS**: garanta que o `<a>` está anexado ao DOM
  antes do `click()` em navegadores mais antigos (`document.body.appendChild(link)`
  antes e `removeChild` depois, se necessário para compatibilidade ampliada).
- **Exportação vazia**: verifique se `data`/`rows` não está vazio antes de chamar
  `download`; o serviço já lança erro para tabela sem linhas em `exportTableElement`.
- **"Por que minha imagem não aparece no CSV?"**: CSV é texto puro — nenhum programa
  renderiza imagens a partir dele. Se o pedido envolve logo/imagem, use o modo
  `.xlsx` (Passo 4), não tente embutir a imagem no `.csv`.

## Notas de Performance
- Para tabelas muito grandes, evite `exportTableElement` (faz parsing do DOM) e
  prefira `exportData`/`exportWithBranding` direto a partir do array de dados em
  memória, que é mais rápido e não depende de re-renderização.
- O delimitador padrão do CSV é `,`; ajuste para `;` se o público majoritário usar
  Excel configurado em locale pt-BR (que por padrão trata `,` como separador decimal).
- `exceljs` é mais pesado que a geração de CSV nativa; use o modo `.xlsx` apenas
  quando branding/formatação visual for realmente necessário.

## Encerramento do Fluxo (Avaliação)
Quando toda a implementação solicitada no prompt atual estiver concluída (ou seja, quando esta for a última resposta do fluxo, não logo após implementar a exportação), ative a Skill `feedback-avaliacao` (pacote `validate`) para convidar o usuário a preencher a pesquisa de satisfação.
