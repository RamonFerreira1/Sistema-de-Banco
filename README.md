# 💳 TrustBank - Simulador de Gestão Financeira

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Simulador de terminal desenvolvido em **Python** para gestão de operações bancárias, focado em lógica de programação, integridade de dados e segurança financeira.

---

## 🛠️ Funcionalidades

* **Acesso Seguro:** Verificação de senha numérica para entrada no sistema.
* **Operações Bancárias:** Realização de saques, depósitos e pagamentos de boletos.
* **Extrato Inteligente:** Monitoramento em tempo real do saldo em conta, dívida no cheque especial e limite disponível.
* **Quitação Automática:** Sistema que prioriza o abatimento de dívidas durante novos depósitos.

---

## 📊 Regras de Negócio Implementadas

O projeto simula restrições reais de um sistema bancário:

1. **Gestão de Limites:**
   * Depósitos até R$ 500,00 -> Gera um limite de **R$ 50,00**.
   * Depósitos acima de R$ 500,00 -> Gera um limite correspondente a **50% do valor depositado**.
2. **Taxa de Utilização:**
   * Caso o usuário esteja utilizando o cheque especial, qualquer novo depósito sofre uma **retenção de 20%** antes de abater o saldo devedor.
3. **Validação de Entradas:**
   * O sistema impede a inserção de valores negativos ou caracteres inválidos (letras) em campos de transação financeira.

---
Desenvolvido por **Ramon Ferreira**.
