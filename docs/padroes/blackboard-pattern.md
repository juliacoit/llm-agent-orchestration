# Blackboard Pattern

## Ideia principal

O Blackboard Pattern usa um espaço compartilhado de informação, como um quadro, onde vários agentes podem ler e escrever.

## Como funciona

Os agentes não precisam conversar diretamente o tempo todo. Eles colaboram por meio de uma memória compartilhada.

Cada agente pode adicionar informações, hipóteses, resultados parciais ou correções.

## Exemplo

Um sistema precisa diagnosticar um problema em um servidor.

- Agente de logs adiciona erros encontrados.
- Agente de rede adiciona dados de conexão.
- Agente de banco adiciona falhas relacionadas ao banco.
- Agente coordenador observa o quadro e decide a conclusão.

## Vantagens

- Facilita colaboração.
- Permite memória compartilhada.
- Útil para problemas com várias fontes de informação.

## Desvantagens

- Pode gerar conflitos.
- Pode acumular informação irrelevante.
- Exige controle sobre o que entra no quadro.

## Quando usar

Quando vários agentes precisam contribuir com informações complementares para uma solução comum.
