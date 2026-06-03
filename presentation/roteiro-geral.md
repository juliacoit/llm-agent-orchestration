# Roteiro Geral da Apresentação

## Introdução

Neste encontro, vamos falar sobre **roteamento dinâmico com LLMs** e **arquiteturas multiagente**.

A ideia principal é mostrar que um sistema baseado em LLM não precisa seguir apenas regras fixas. Ele pode interpretar a solicitação do usuário e decidir dinamicamente qual agente, ferramenta ou fluxo deve ser acionado.

## Parte 1 — Fundamentos do roteamento dinâmico

Nesta parte, explicamos o que significa usar um LLM como roteador.

Em sistemas tradicionais, muitas decisões são feitas usando condicionais determinísticas, como `if/else`.

Já em um sistema com LLM como roteador, o modelo interpreta a intenção do usuário com base no contexto. Isso permite lidar melhor com ambiguidades, linguagem natural e pedidos mais complexos.

Também são apresentados os conceitos de `transfer_to_agent`, `escalate`, `tool` e `agent_as_tool`.

## Parte 2 — Padrões de arquitetura multiagente

Nesta parte, apresentamos formas de organizar vários agentes trabalhando juntos.

Os principais padrões são:

- Orchestrator-Workers
- Planner-Executor
- Reflection / Critic
- Blackboard Pattern
- Group Chat / Debate
- Hierarquia com coordenador e subagentes

Esses padrões ajudam a definir quem coordena, quem executa, quem revisa e como as informações circulam entre os agentes.

## Parte 3 — Trade-offs e demo

Por fim, discutimos os principais trade-offs de sistemas multiagente:

- custo;
- previsibilidade;
- debugabilidade;
- complexidade;
- tempo de execução.

Depois, apresentamos uma demo conceitual com um agente coordenador e três subagentes: pesquisador, programador e crítico.

## Conclusão

Sistemas multiagente com LLMs são poderosos porque permitem dividir tarefas, usar especialistas e revisar resultados. Porém, essa flexibilidade também traz desafios, como maior custo, menor previsibilidade e maior dificuldade de depuração.
