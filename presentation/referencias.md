# Referências

## Frameworks e materiais para estudo

- OpenAI Agents SDK
- LangChain — Multi-agent systems
- Microsoft AutoGen
- CrewAI
- LangGraph
- Anthropic — Building effective agents

## Conceitos relacionados

- Agent orchestration
- Tool calling
- Handoffs
- Multi-agent systems
- Planner-Executor
- Reflection pattern
- Blackboard architecture
- Debate-based agents

As melhores fontes para essa parte são as **documentações oficiais dos frameworks** e alguns textos técnicos de referência. Eu organizaria sua pesquisa assim:

## 1. Fonte principal para padrões gerais: Anthropic

A melhor fonte para entender **Orchestrator-Workers**, **Routing** e **Reflection/Critic** é o artigo da Anthropic **“Building Effective AI Agents”**. Ele explica padrões como routing, orchestrator-workers e evaluator-optimizer, que é muito próximo da ideia de um agente gerador + agente crítico/revisor. ([Anthropic][1])

Use essa fonte para estudar:

* Orchestrator-Workers;
* diferença entre workflows e agents;
* quando usar agentes e quando manter fluxos simples;
* trade-offs de complexidade;
* Reflection/Critic, conectando com o padrão evaluator-optimizer.

Para a apresentação, essa pode ser sua **fonte teórica principal**.

---

## 2. Fonte principal para `transfer_to_agent`, handoffs e agents-as-tools: OpenAI Agents SDK

A documentação da OpenAI Agents SDK é muito boa para explicar **handoffs**, ou seja, quando um agente delega a tarefa para outro agente. A própria documentação explica que handoffs permitem que um agente delegue tarefas a outro agente especializado e que isso aparece como uma ferramenta para o LLM, por exemplo `transfer_to_refund_agent`. ([OpenAI GitHub][2])

Também vale usar a página de orquestração da OpenAI, porque ela trata diretamente de **handoffs** e **agents-as-tools** em sistemas com múltiplos agentes. ([OpenAI Desenvolvedores][3])

Use essa fonte para estudar:

* `transfer_to_agent`;
* handoff;
* agents-as-tools;
* agente coordenador;
* subagentes especializados.

Mesmo que essa parte seja mais da pessoa 1 ou 3, ela ajuda você a conectar sua parte de arquitetura com a demo.

---

## 3. Fonte principal para supervisor, hierarquia e agente coordenador: LangChain / LangGraph

A documentação da LangChain explica sistemas multiagente com a ideia de **supervisor**, em que um agente central coordena agentes especializados. A página de subagentes descreve esse padrão como uma arquitetura em que um supervisor central coordena workers especializados, especialmente quando a tarefa exige diferentes tipos de expertise. ([LangChain Docs][4])

A referência do LangGraph Supervisor também é útil porque fala explicitamente de criar um agente supervisor para orquestrar múltiplos agentes especializados e de handoff baseado em ferramentas. ([reference.langchain.com][5])

Use essa fonte para estudar:

* hierarquia;
* coordenador + subagentes;
* supervisor pattern;
* tool-based handoff;
* agentes especializados.

Essa é provavelmente a melhor fonte para sua parte de **Hierarquia** e também ajuda com **Orchestrator-Workers**.

---

## 4. Fonte principal para Group Chat / Debate: Microsoft AutoGen

Para **Group Chat / Debate**, a melhor fonte é a documentação do AutoGen. A documentação descreve AutoGen como um framework de conversas multiagente, em que agentes podem conversar entre si para realizar tarefas coletivamente. ([Microsoft GitHub][6])

A página específica de Group Chat do AutoGen também define group chat como um padrão em que um grupo de agentes compartilha uma thread comum de mensagens, publicando e recebendo mensagens no mesmo tópico. ([Microsoft GitHub][7])

Use essa fonte para estudar:

* Group Chat;
* debate entre agentes;
* moderador;
* conversa multiagente;
* colaboração por mensagens.

Essa fonte é especialmente boa porque o AutoGen ficou conhecido justamente por popularizar a ideia de múltiplos agentes conversando.

---

## 5. Fonte complementar para workflows e agentes: LangGraph

A documentação de workflows e agents do LangGraph é boa para explicar a diferença entre **workflows com caminhos predeterminados** e **agents mais dinâmicos**, que definem seus próprios processos e uso de ferramentas. ([LangChain Docs][8])

Use essa fonte para estudar:

* Planner-Executor;
* workflows;
* diferença entre fluxo fixo e agente dinâmico;
* execução em etapas;
* sistemas mais controláveis.

Para sua apresentação, essa fonte ajuda a explicar que nem tudo precisa ser “100% agente autônomo”; às vezes um workflow planejado é mais previsível.

---

## 6. Fonte para Blackboard Pattern

Para o **Blackboard Pattern**, talvez você encontre menos material diretamente ligado a LLMs, porque ele é um padrão clássico de sistemas multiagente e IA simbólica, anterior aos LLMs. Para apresentar, você pode explicar o padrão de forma conceitual e conectar com a ideia moderna de **memória compartilhada**, **estado compartilhado** ou **shared workspace** entre agentes.

A fonte do AutoGen sobre Group Chat ajuda parcialmente, porque fala de agentes compartilhando uma thread comum de mensagens. ([Microsoft GitHub][7])

A documentação do LangGraph também ajuda porque LangGraph trabalha com workflows/agents e controle de estado, persistência e debugging, o que conversa bem com a ideia de um espaço compartilhado de informação. ([LangChain Docs][8])

Para apresentar, você pode dizer:

> “O Blackboard Pattern é um padrão clássico em que agentes colaboram escrevendo e lendo de um espaço comum. Em sistemas modernos com LLMs, essa ideia aparece como memória compartilhada, estado compartilhado ou uma thread comum onde os agentes acumulam informações.”

---

# Minha recomendação de fontes por padrão

| Padrão               | Melhor fonte para pesquisar                        | Por quê                                                                           |
| -------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------- |
| Orchestrator-Workers | Anthropic + LangChain                              | A Anthropic explica o padrão; LangChain mostra implementação com supervisor       |
| Planner-Executor     | LangGraph + Anthropic                              | Ajuda a explicar workflows, planejamento e execução em etapas                     |
| Reflection / Critic  | Anthropic                                          | O padrão evaluator-optimizer é muito próximo de gerador + crítico                 |
| Blackboard Pattern   | LangGraph + AutoGen + conceito clássico            | Mais difícil achar fonte moderna direta; conecte com estado/memória compartilhada |
| Group Chat / Debate  | Microsoft AutoGen                                  | É a fonte mais direta para conversa multiagente                                   |
| Hierarquia           | LangChain/LangGraph Supervisor + OpenAI Agents SDK | Explica supervisor, subagentes, handoffs e agents-as-tools                        |

---

# Ordem de estudo recomendada

Eu estudaria nesta ordem:

1. **Anthropic — Building Effective AI Agents**
   Para entender os padrões principais e os trade-offs.

2. **LangChain/LangGraph — Supervisor e workflows**
   Para entender coordenador, workers, hierarquia e execução controlada.

3. **OpenAI Agents SDK — Handoffs e agents-as-tools**
   Para conectar os padrões com a demo do grupo.

4. **Microsoft AutoGen — Group Chat**
   Para explicar debate e colaboração entre agentes.

5. **Blackboard Pattern**
   Pesquise por último, porque ele é mais conceitual e você pode apresentar como “memória/estado compartilhado”.

---

# Como colocar isso na apresentação

Você pode falar assim:

> “Para estudar esses padrões, usei principalmente documentações de frameworks atuais de agentes, como OpenAI Agents SDK, LangChain/LangGraph e Microsoft AutoGen, além do artigo técnico da Anthropic sobre construção de agentes efetivos. Essas fontes são interessantes porque não explicam apenas o conceito teórico, mas também mostram como esses padrões aparecem em implementações reais.”

E para fechar sua parte:

> “Apesar de cada framework usar nomes um pouco diferentes, os padrões se repetem: um agente pode coordenar outros, planejar etapas, revisar respostas, compartilhar estado ou participar de uma conversa coletiva. A diferença principal está em como o fluxo de informação e responsabilidade é organizado.”

[1]: https://www.anthropic.com/research/building-effective-agents?utm_source=chatgpt.com "Building Effective AI Agents"
[2]: https://openai.github.io/openai-agents-python/handoffs/?utm_source=chatgpt.com "Handoffs - OpenAI Agents SDK"
[3]: https://developers.openai.com/api/docs/guides/agents/orchestration?utm_source=chatgpt.com "Orchestration and handoffs | OpenAI API"
[4]: https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant?utm_source=chatgpt.com "Build a personal assistant with subagents"
[5]: https://reference.langchain.com/python/langgraph-supervisor?utm_source=chatgpt.com "LangGraph Multi-Agent Supervisor"
[6]: https://microsoft.github.io/autogen/0.2/docs/Use-Cases/agent_chat?utm_source=chatgpt.com "Multi-agent Conversation Framework | AutoGen 0.2"
[7]: https://microsoft.github.io/autogen/stable//user-guide/core-user-guide/design-patterns/group-chat.html?utm_source=chatgpt.com "Group Chat — AutoGen"
[8]: https://docs.langchain.com/oss/python/langgraph/workflows-agents?utm_source=chatgpt.com "Workflows and agents - Docs by LangChain"

