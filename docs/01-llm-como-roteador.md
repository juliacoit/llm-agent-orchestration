# LLM como roteador

Um LLM pode ser usado como roteador quando ele interpreta a solicitação do usuário e decide qual agente, ferramenta ou fluxo deve ser acionado.

Em vez de seguir apenas regras fixas, o modelo analisa a intenção do pedido e escolhe o caminho mais adequado.

## Exemplo

Se o usuário escreve:

> "Revise esse código e veja se tem erro."

O roteador pode encaminhar a tarefa para um agente de programação ou para um agente crítico.

Se o usuário escreve:

> "Pesquise sobre arquiteturas multiagente."

O roteador pode encaminhar a tarefa para um agente pesquisador.

## Comparação com regras fixas

Em um sistema determinístico, a decisão geralmente depende de condições explícitas:

```python
if "código" in pergunta:
    chamar_agente_de_codigo()
elif "pesquise" in pergunta:
    chamar_agente_pesquisador()
Em um sistema com LLM como roteador, o modelo interpreta a intenção geral da mensagem, mesmo que palavras específicas não apareçam.

Vantagens
Mais flexibilidade
Melhor interpretação de linguagem natural
Capacidade de lidar com ambiguidade
Melhor adaptação a tarefas variadas
Desvantagens
Menor previsibilidade
Maior custo
Mais difícil de debugar
Pode escolher o caminho errado
