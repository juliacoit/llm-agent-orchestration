from agents.coordinator import CoordinatorAgent


def main():
    coordinator = CoordinatorAgent()

    examples = [
        "Pesquise o que é o padrão Orchestrator-Workers.",
        "Crie um exemplo de código em Python.",
        "Revise essa resposta e encontre possíveis problemas.",
        "Explique o que é roteamento dinâmico com LLMs."
    ]

    for request in examples:
        print("=" * 80)
        print(f"Usuário: {request}")
        print("-" * 80)
        response = coordinator.route(request)
        print(f"Resposta: {response}")
        print()


if __name__ == "__main__":
    main()
