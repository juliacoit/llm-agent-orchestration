# LLM Agent Orchestration

Este repositório reúne o material do **Encontro 2: Roteamento Dinâmico com LLMs**.

O objetivo é estudar como LLMs podem atuar como roteadores inteligentes em sistemas com múltiplos agentes, comparando abordagens determinísticas com decisões baseadas em linguagem natural e explorando padrões de orquestração multiagente.

## Tema central

**Roteamento Dinâmico com LLMs e Arquiteturas Multiagente**

## Temas abordados

- LLM como roteador
- Roteamento dinâmico vs condicional determinístico
- `transfer_to_agent`
- `escalate`
- `tool` vs `agent_as_tool`
- Orchestrator-Workers
- Planner-Executor
- Reflection / Critic
- Blackboard Pattern
- Group Chat / Debate
- Hierarquia com coordenador e subagentes
- Trade-offs: custo, previsibilidade e debugabilidade
- Demo com coordenador LLM e subagentes

## Estrutura do repositório

- `presentation/`: material da apresentação, roteiro, slides e divisão do grupo.
- `docs/`: conteúdo teórico do encontro.
- `docs/padroes/`: explicação dos padrões multiagente.
- `demo/`: código da demonstração prática.
- `diagrams/`: diagramas usados na apresentação.
- `assets/`: imagens e recursos auxiliares.

## Divisão do grupo

| Pessoa | Responsabilidade |
|---|---|
| Pessoa 1 | Fundamentos do roteamento dinâmico com LLM |
| Pessoa 2 | Padrões de arquitetura multiagente |
| Pessoa 3 | Trade-offs e demo prática |

## Objetivo da demo

A demo apresenta um agente coordenador capaz de encaminhar tarefas para subagentes especializados, mostrando a ideia de roteamento, transferência de responsabilidade e agentes usados como ferramentas.
