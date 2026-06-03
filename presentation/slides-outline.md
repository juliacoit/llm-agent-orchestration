# Estrutura dos Slides

## Slide 1 — Título

**Roteamento Dinâmico com LLMs e Arquiteturas Multiagente**

- Encontro 2
- Tema: como LLMs podem coordenar agentes e ferramentas de forma dinâmica

## Slide 2 — Problema

- Sistemas simples usam regras fixas
- Sistemas mais complexos precisam decidir dinamicamente o próximo passo
- LLMs podem interpretar intenção, contexto e ambiguidade

## Slide 3 — LLM como roteador

- O LLM recebe a solicitação do usuário
- Analisa a intenção
- Decide qual agente, ferramenta ou fluxo deve ser acionado

## Slide 4 — Condicional determinístico vs roteamento com LLM

- Condicional determinístico: regras fixas com `if/else`
- LLM Router: decisão baseada em linguagem natural e contexto
- Mais flexível, porém menos previsível

## Slide 5 — `transfer_to_agent` e `escalate`

- `transfer_to_agent`: transfere a tarefa para outro agente especializado
- `escalate`: encaminha para um nível superior ou mais especializado quando o agente atual não consegue resolver

## Slide 6 — `tool` vs `agent_as_tool`

- `tool`: função específica chamada pelo agente
- `agent_as_tool`: outro agente é usado como ferramenta especializada

## Slide 7 — O que são arquiteturas multiagente?

- Sistemas compostos por agentes com papéis diferentes
- Cada agente pode executar uma parte da tarefa
- A arquitetura define como eles interagem

## Slide 8 — Orchestrator-Workers

- Um agente coordenador distribui tarefas
- Workers executam subtarefas
- O orquestrador combina os resultados

## Slide 9 — Planner-Executor

- Um agente cria o plano
- Outro agente executa o plano
- Útil para tarefas longas e sequenciais

## Slide 10 — Reflection / Critic

- Um agente produz uma resposta
- Outro agente revisa, critica ou corrige
- Ajuda a melhorar qualidade e reduzir erros

## Slide 11 — Blackboard, Group Chat e Hierarquia

- Blackboard: agentes compartilham um espaço comum de informações
- Group Chat/Debate: agentes discutem entre si
- Hierarquia: coordenador controla subagentes

## Slide 12 — Trade-offs

- Custo
- Previsibilidade
- Debugabilidade
- Tempo de execução
- Complexidade da arquitetura

## Slide 13 — Demo prática

- Coordenador LLM
- Subagentes especializados
- Exemplo com agente de pesquisa, agente de código e agente crítico

## Slide 14 — Conclusão

- LLMs podem atuar como roteadores inteligentes
- Multiagentes permitem especialização e colaboração
- A escolha da arquitetura depende do problema
