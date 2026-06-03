# Hierarchical Agents

## Ideia principal

A arquitetura hierárquica organiza agentes em níveis.

Um agente coordenador fica no topo e controla subagentes especializados.

## Como funciona

O coordenador recebe a tarefa principal, decide quais subagentes devem atuar e combina os resultados.

## Exemplo

```text
Coordenador Geral
│
├── Agente de Pesquisa
├── Agente de Código
├── Agente de Revisão
└── Agente de Documentação
Vantagens
Organização clara.
Boa separação de responsabilidades.
Facilita a divisão de tarefas.
Desvantagens
O coordenador pode virar um ponto único de falha.
Se o coordenador decidir errado, o fluxo inteiro pode ser prejudicado.
Pode aumentar a complexidade.
Quando usar

Quando o sistema possui várias responsabilidades e precisa de uma estrutura organizada em níveis.
