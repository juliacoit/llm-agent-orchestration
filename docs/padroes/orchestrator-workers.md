# Orchestrator-Workers

## Ideia principal

O padrão Orchestrator-Workers usa um agente central para coordenar vários agentes especializados.

## Como funciona

O orquestrador recebe a tarefa principal, divide em subtarefas e encaminha cada parte para um worker. Depois, ele reúne os resultados em uma resposta final.

## Exemplo

Um usuário pede a criação de um chatbot educacional.

- Worker 1: define o conteúdo.
- Worker 2: cria exemplos.
- Worker 3: revisa a resposta.
- Orquestrador: junta tudo.

## Vantagens

- Boa divisão de responsabilidades.
- Funciona bem para tarefas complexas.
- Permite usar agentes especializados.

## Desvantagens

- Mais chamadas ao LLM.
- Maior custo.
- Mais difícil de debugar.

## Quando usar

Quando a tarefa pode ser dividida em partes menores e cada parte pode ser resolvida por um agente especializado.
