---
name: print-to-pdf
description: Gera um PDF a partir do conteúdo HTML atualmente exibido na tela em uma aplicação Angular e inicia o download no navegador. Use quando o usuário pedir para "exportar para PDF", "baixar como PDF", "imprimir em PDF" ou "gerar PDF da tela atual".
metadata:
  version: 1.0.0
  author: Especialista Angular
---

# Print to PDF (Angular)

## Instruções Procedurais

### Passo 1: Escolha da Biblioteca (Simplicidade + Segurança)
Use `html2pdf.js` (combina `html2canvas` + `jsPDF` em uma única API simples). Ela é totalmente client-side: o HTML nunca é enviado para servidores externos.

```bash
npm install html2pdf.js
npm audit
```

- **Fixe a versão** no `package.json` (evite `^`/`~` em projetos sensíveis) e rode `npm audit` regularmente.
- Se o `npm audit` reportar vulnerabilidade alta/crítica sem correção, avalie alternativa (`jspdf` + `html2canvas` separados, com versões corrigidas) antes de prosseguir.

### Passo 2: Criar o Serviço de Exportação
Crie um serviço único e reutilizável:

```typescript
// pdf-export.service.ts
import { Injectable } from '@angular/core';
import html2pdf from 'html2pdf.js';

@Injectable({ providedIn: 'root' })
export class PdfExportService {
  exportElement(elementId: string, fileName = 'documento.pdf'): void {
    const element = document.getElementById(elementId);
    if (!element) {
      throw new Error(`Elemento #${elementId} não encontrado`);
    }

    const safeFileName = fileName.replace(/[^a-zA-Z0-9-_.]/g, '_');

    const options = {
      margin: 10,
      filename: safeFileName,
      image: { type: 'jpeg', quality: 0.98 },
      html2canvas: { scale: 2, useCORS: true },
      jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' },
    };

    html2pdf().set(options).from(element).save();
  }
}
```

### Passo 3: Uso no Componente
1. Envolva o conteúdo a ser exportado em um elemento com `id` fixo.
2. Adicione um botão que chame o serviço.

```html
<div id="conteudo-para-pdf">
  <!-- conteúdo a ser exportado -->
</div>

<button (click)="exportarPdf()">Baixar PDF</button>
```

```typescript
constructor(private pdfExportService: PdfExportService) {}

exportarPdf(): void {
  this.pdfExportService.exportElement('conteudo-para-pdf', 'relatorio.pdf');
}
```

### Passo 4: Checklist de Segurança (CRÍTICO)
Antes de considerar a tarefa concluída, verifique:

1. **Dados sensíveis ocultos:** Campos como senhas, tokens, números de cartão ou dados de outros usuários NÃO podem aparecer no PDF. Oculte-os via classe CSS (ex: `.no-print { display: none; }`) aplicada ao elemento antes da captura.
2. **`useCORS` apenas para origens confiáveis:** A opção `html2canvas: { useCORS: true }` deve ser usada apenas se as imagens vierem de domínios confiáveis/mesma origem, para evitar "canvas tainting" ou exfiltração de recursos.
3. **Nome de arquivo sanitizado:** Sempre aplique a regex de sanitização (`replace(/[^a-zA-Z0-9-_.]/g, '_')`) no `fileName`, especialmente se ele vier de dados do usuário.
4. **Sem HTML não confiável:** Não capture conteúdo inserido via `innerHTML`/`bypassSecurityTrustHtml` sem sanitização prévia (risco de XSS refletido no PDF).
5. **Geração 100% client-side:** Não envie o HTML/conteúdo para serviços externos de conversão de PDF sem autorização explícita do usuário.
6. **Dependência auditada:** Confirme que `npm audit` não acusa vulnerabilidades não corrigidas para `html2pdf.js`/`jspdf`/`html2canvas`.

## Exemplos
**Entrada do Usuário:** "Adiciona um botão para exportar essa tela de relatório em PDF."
**Ação do Claude:** Instala `html2pdf.js`, cria `PdfExportService`, envolve o conteúdo do relatório com `id="conteudo-para-pdf"`, adiciona o botão `exportarPdf()` e aplica o checklist de segurança (oculta campos sensíveis com `.no-print`, sanitiza o nome do arquivo).

## Solução de Problemas
- **PDF em branco ou cortado:** Verifique se o elemento alvo está totalmente visível/renderizado no DOM antes de chamar `exportElement` (evite chamar durante carregamento assíncrono).
- **Imagens não aparecem:** Confirme CORS das imagens ou use `useCORS: true` apenas para domínios confiáveis.
- **Tabelas cortadas entre páginas:** Use a opção `pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }` do `html2pdf.js`.

## Notas de Performance
- `html2canvas: { scale: 2 }` melhora a qualidade, mas aumenta tempo de processamento e uso de memória; reduza para `1` em telas muito grandes.
- Prefira capturar apenas o contêiner necessário, evitando capturar a página inteira (menus, sidebars, etc.).

## Encerramento do Fluxo (Avaliação)
Quando toda a implementação solicitada no prompt atual estiver concluída (ou seja, quando esta for a última resposta do fluxo, não logo após implementar a exportação), ative a Skill `feedback-avaliacao` (pacote `validate`) para convidar o usuário a preencher a pesquisa de satisfação.
