# Planner-Executor

## Ideia principal

O padrão Planner-Executor separa o planejamento da execução.

Um agente cria o plano e outro agente executa as etapas.

## Como funciona

1. O usuário faz uma solicitação.
2. O Planner divide a tarefa em etapas.
3. O Executor realiza cada etapa.
4. O sistema retorna o resultado final.

## Exemplo

Pedido do usuário:

> "Crie uma aplicação simples com backend, frontend e banco de dados."

O Planner pode definir:

1. Levantar requisitos.
2. Criar o modelo do banco.
3. Implementar a API.
4. Criar a interface.
5. Testar o sistema.

O Executor segue esse plano.

## Vantagens

- Melhor organização.
- Bom para tarefas longas.
- Ajuda a evitar respostas impulsivas.

## Desvantagens

- Se o plano inicial for ruim, a execução pode ser prejudicada.
- Pode aumentar o número de etapas.
- Pode ser lento.

## Quando usar

Quando o problema exige uma sequência clara de passos.
