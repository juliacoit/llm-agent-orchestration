# Reflection / Critic

## Ideia principal

O padrão Reflection ou Critic adiciona um agente responsável por revisar a saída de outro agente.

## Como funciona

1. Um agente gera uma resposta inicial.
2. Um agente crítico analisa a resposta.
3. O sistema corrige, melhora ou aprova a saída.
4. A resposta final é entregue ao usuário.

## Exemplo

Um agente gera um código em Python.

Depois, um agente crítico verifica:

- se o código funciona;
- se atende ao enunciado;
- se possui erros;
- se poderia ser mais claro.

## Vantagens

- Melhora a qualidade da resposta.
- Ajuda a encontrar erros.
- É útil em código, textos e análises técnicas.

## Desvantagens

- O crítico também pode errar.
- Aumenta custo e tempo.
- Pode gerar revisões excessivas.

## Quando usar

Quando a qualidade da resposta é importante e vale a pena revisar antes de entregar.
