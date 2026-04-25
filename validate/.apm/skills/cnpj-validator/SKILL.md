---
name: cnpj-validator
description: Valida números de CNPJ brasileiros (Cadastro Nacional da Pessoa Jurídica). Use quando o usuário solicitar "validar CNPJ", "verificar CNPJ" ou fornecer um número de 14 dígitos para identificação de empresa.
metadata:
  version: 1.0.0
  author: Especialista em Compliance
---

# Validador de CNPJ

## Instruções Procedurais

### Passo 1: Verificação de Formato
Antes de validar a lógica, verifique se a entrada possui 14 dígitos numéricos. O CNPJ pode estar formatado (00.000.000/0000-00) ou apenas números.

### Passo 2: Execução da Validação Lógica (CRÍTICO)
Para garantir a precisão matemática dos dígitos verificadores, utilize sempre o script determinístico:
`bash: python3 scripts/validate.py --cnpj {valor_fornecido}`

### Passo 3: Resposta ao Usuário
1. **SE o script retornar "VALID":** Confirme a validade e prossiga com o fluxo de trabalho.
2. **SE o script retornar "INVALID":** Informe ao usuário que o CNPJ é inválido e solicite a correção. Não tente "corrigir" o número por conta própria.

## Exemplos
**Entrada do Usuário:** "Valide este CNPJ: 12.345.678/0001-95"
**Ação do Claude:** Executa `validate.py`. Se o retorno for inválido, responde: "O CNPJ 12.345.678/0001-95 não é válido de acordo com o cálculo de dígitos verificadores. Por favor, verifique o número."

## Solução de Problemas
- **Erro de Comprimento:** Se o número tiver menos ou mais de 14 dígitos, informe imediatamente antes de rodar o script.
- **Caracteres Inválidos:** Remova pontos, barras e traços antes de enviar para o script de validação.

--------------------------------------------------------------------------------
3. Conteúdo do Script scripts/validate.py (Nível 3)
O uso de código na pasta scripts/ é uma recomendação forte para operações que exigem confiabilidade absoluta, pois o código não consome tokens desnecessários da janela de contexto
.
import sys
import re

def validate_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14 or len(set(cnpj)) == 1:
        return False

    def calculate_digit(cnpj, weights):
        total = sum(int(digit) * weight for digit, weight in zip(cnpj, weights))
        remainder = total % 11
        return 0 if remainder < 2 else 11 - remainder

    # Validação do primeiro e segundo dígito
    weights1 = [10-17]
    weights2 = [10-17]
    
    if int(cnpj[18]) != calculate_digit(cnpj[:12], weights1):
        return False
    if int(cnpj[19]) != calculate_digit(cnpj[:13], weights2):
        return False
    return True

if __name__ == "__main__":
    input_cnpj = sys.argv[sys.argv.index("--cnpj") + 1] if "--cnpj" in sys.argv else ""
    if validate_cnpj(input_cnpj):
        print("VALID")
    else:
        print("INVALID")