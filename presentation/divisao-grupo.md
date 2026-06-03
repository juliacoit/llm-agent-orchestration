# Divisão do Grupo

## Pessoa 1 — Fundamentos do roteamento dinâmico

Responsável por explicar:

- LLM como roteador
- Roteamento com LLM vs condicional determinístico
- `transfer_to_agent`
- `escalate`
- `tool` vs `agent_as_tool`

Arquivos principais:

- `docs/01-llm-como-roteador.md`
- `docs/02-transfer-escalate.md`
- `docs/03-tool-vs-agent-as-tool.md`

## Pessoa 2 — Padrões de arquitetura multiagente

Responsável por explicar:

- Orchestrator-Workers
- Planner-Executor
- Reflection / Critic
- Blackboard Pattern
- Group Chat / Debate
- Hierarquia: coordenador + subagentes

Arquivos principais:

- `docs/04-padroes-multiagente.md`
- `docs/padroes/orchestrator-workers.md`
- `docs/padroes/planner-executor.md`
- `docs/padroes/reflection-critic.md`
- `docs/padroes/blackboard-pattern.md`
- `docs/padroes/group-chat-debate.md`
- `docs/padroes/hierarchical-agents.md`

## Pessoa 3 — Trade-offs e demo prática

Responsável por explicar:

- custo
- previsibilidade
- debugabilidade
- demonstração com coordenador e subagentes
- uso conceitual de `transfer_to_agent`
- uso conceitual de `agent_as_tool`

Arquivos principais:

- `docs/05-trade-offs.md`
- `demo/README.md`
- `demo/main.py`
- `demo/agents/`
- `demo/tools/`
