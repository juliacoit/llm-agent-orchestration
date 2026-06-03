from agents.researcher_agent import ResearcherAgent
from agents.coding_agent import CodingAgent
from agents.critic_agent import CriticAgent


class CoordinatorAgent:
    def __init__(self):
        self.researcher = ResearcherAgent()
        self.coder = CodingAgent()
        self.critic = CriticAgent()

    def route(self, user_request: str) -> str:
        """
        Simula um LLM como roteador.

        Em uma implementação real, um LLM analisaria a intenção do usuário.
        Aqui usamos regras simples apenas para demonstrar o fluxo.
        """

        request = user_request.lower()

        if "pesquise" in request or "o que é" in request:
            return self.transfer_to_agent("researcher", user_request)

        if "código" in request or "python" in request:
            return self.transfer_to_agent("coder", user_request)

        if "revise" in request or "problemas" in request:
            return self.transfer_to_agent("critic", user_request)

        return "Coordenador: consigo responder diretamente, sem transferir para outro agente."

    def transfer_to_agent(self, agent_name: str, task: str) -> str:
        """
        Simula o conceito de transfer_to_agent.
        """

        if agent_name == "researcher":
            return self.researcher.run(task)

        if agent_name == "coder":
            return self.coder.run(task)

        if agent_name == "critic":
            return self.critic.run(task)

        return "Nenhum agente adequado foi encontrado."
