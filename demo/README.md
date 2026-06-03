# Demo

Esta pasta contém uma demonstração conceitual de roteamento dinâmico com agentes.

A demo não depende de uma API real de LLM. Ela simula o comportamento de um coordenador que decide qual subagente deve receber a tarefa.

## Agentes

- `coordinator.py`: agente coordenador
- `researcher_agent.py`: agente de pesquisa
- `coding_agent.py`: agente de código
- `critic_agent.py`: agente crítico

## Como executar

Na raiz do repositório, rode:

```powershell
python demo/main.py
Objetivo

Mostrar, de forma simples, como um coordenador pode encaminhar tarefas para agentes especializados.
