# from app.agent import run_agent

# if __name__ == "__main__":
#     goal = "Explain what LLM in simple word?"
#     run_agent(goal)



#AGENT 1: MARKET CONCEPT EXPLAINER

# from app.agent import run_agent

# if __name__ == "__main__":
#     goal = "Summarize current technology trends"
#     run_agent(goal)


#AGENT 2: MARKET CONCEPT EXPLAINER

# from app.agent import run_agent
from app.agent import run_agent
if __name__ == "__main__":
    goal = "Explain why humor helps in communication"
    run_agent(goal)
 
def decide_next_step(memory: dict) -> str:
    print("\n[CONTROL] Current memory:", memory)
 
    if memory["completed"]:
        return "stop"
 
    
 