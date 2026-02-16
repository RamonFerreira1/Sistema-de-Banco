
```markdown
# 💳 TrustBank - Simulador de Gestão Financeira

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

O **TrustBank** é um simulador de terminal desenvolvido em Python que gerencia operações bancárias essenciais. O foco deste projeto foi a implementação de uma lógica rigorosa para o uso de cheque especial e a integridade dos dados financeiros.

---

## 🛠️ Funcionalidades

* **Autenticação Simples:** Sistema de cadastro e verificação de senha numérica para acesso.
* **Gestão de Saldo e Extrato:** Consulta em tempo real do saldo real, dívida acumulada e limite disponível.
* **Saque com Limite Inteligente:** Permite saques além do saldo real, utilizando o cheque especial de forma acumulativa.
* **Depósito com Quitação de Dívida:** Prioriza o pagamento do limite utilizado antes de aumentar o saldo positivo.
* **Pagamento de Boletos:** Integração com o saldo e limite para quitação de contas.

---

## 📊 Regras de Negócio Implementadas

O sistema segue regras estritas para simular um ambiente bancário real:

1. **Cálculo de Limite:** O limite do cheque especial é definido no primeiro depósito:
   * Depósitos até R$ 500,00 $\rightarrow$ Limite fixo de R$ 50,00.
   * Depósitos acima de R$ 500,00 $\rightarrow$ Limite de 50% do valor depositado.
2. **Taxa de Utilização:** Aplicação de uma taxa de 20% sobre o valor depositado caso o usuário esteja utilizando o cheque especial:
   $$valor_{final} = valor_{deposito} \times 0.80$$
3. **Segurança de Entrada:** Proteção contra a inserção de valores negativos ou caracteres inválidos em operações financeiras.




---

Desenvolvido por **Ramon Ferreira**.

```
