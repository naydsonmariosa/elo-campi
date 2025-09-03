# Desafio Clean Code com Fila e API de Cotação

## 🧠 Objetivo

Você deve criar um microserviço que:

1. Criar a lógica de cálculo da cotação de um pedido.
2. Usar a resposta da **BrasilAPI** para converter BRL para outra moeda.
3. Publicar a resposta formatada em uma fila (presente no projeto).
4. Aplicar boas práticas de código limpo e testabilidade.

---


## ⚖️ Regras de Negócio

1.  Todos os dias possuem 3 registros com a propriedade tipo_cotacao igual a **INTERMEDIÁRIO**
- Quando o tipo de boletim da mensagem de entrada for INTERMEDIÁRIO, o cálculo da cotação do pedido deverá considerar a média de valor dos registros intermediários do dia.

---

## 🧱 Estrutura entregue no desafio

O repositório inicial já contém:

- 🔗 Chamada à BrasilAPI implementada
- ✅ Modelos de entrada/saída já definidos (ou a serem criados)
- ❌ **Lógica de cálculo não implementada**
- ❌ **MessageHandler ausente**
- ❌ **Testes ausentes**

---

## 🧩 O que devem entregar

- Implementação da classe que processa a mensagem (`MessageHandler`)
- Aplicação das regras de negócio baseadas no tipo de boletim
- Cálculo correto do valor convertido com base na cotação recebida
- Mensagem de resposta formatada corretamente
- Testes automatizados (mínimo esperado)

---


## Mensagem de entrada

Veja abaixo exemplos de retorno da API:

```json
{
  "numeroPedido": "13213213221",
  "valor": "10.00",
  "moedaCotacao": "USD",
  "dataPedido": "2025-01-01",
  "tipo_boletim": "INTERMEDIÁRIO"
}
```

## Resposta esperada

```json
{
  "numeroPedido": "13213213221",
  "valor": "10.00",
  "moedaCotacao": "USD",
  "dataPedido": "2025-01-01",
  "valorCotacaoMoeda": "5.67",
  "valorCotacaoPedido": "56.70",
  "tipo_boletim": "INTERMEDIÁRIO"
}
```

## Avaliação

- Código limpo e bem estruturado
- Nomes claros e responsabilidades separadas
- Testes para funções críticas
- Uso correto da API e tratamento de erros

## Rodando

```bash
pip install -r requirements.txt
python main.py
```

## Testando

```bash
pytest
```
