from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools

from dotenv import load_dotenv
load_dotenv()

#criação de um agente de pesquisa
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile",temperature=0.0),
    tools=[TavilyTools()],
        instructions=(
        "Quando chamar ferramentas, siga estritamente o schema: "
        "passe números sem aspas para campos numéricos (ex.: max_results=5, não '5'). "
        "Prefira omitir parâmetros opcionais se o default já servir."
    )
    #,debug_mode=True
)
agent.print_response("Voce é um agente de viagens especialista na Andaluzia, Espanha."
  "Use suas ferramentas e me diga  apenas em Celsius Qual a temperatura minima e maxima em Sevilla," 
  "Espanha para os dias: Sexta, Sabado e Domingo. Monte um roteiro diario dizendo: temperatura minima e maxima do dia em celsius,"
  "  Que roupas devo levar? Quais atividades posso fazer considerando as condicoes climaticas? Monte um pequeno roteiro.")
