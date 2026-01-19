# def decide_next_step(memory: dict) -> str:
#     print("\n[CONTROL] Current memory:", memory)
 
#     if memory["completed"]:
#         print("[CONTROL] completed=True → STOP")
#         return "stop"
 
#     if len(memory["steps"]) == 0:
#         print("[CONTROL] First step → CALL LLM")
#         return "call_llm"
 
#     if len(memory["steps"]) == 1:
#         print("[CONTROL] Second step → USE TOOL")
#         return "use_tool"
 
#     print("[CONTROL] All steps done → STOP")
#     memory["completed"] = True
#     return "stop"
 
 

from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import fetch_joke_tool
 
def run_agent(goal: str):
    memory = init_memory(goal)
 
    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)
 
    while True:
        print("\n[AGENT] Loop iteration started")
        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)
 
        if step == "call_llm":
            response = call_llm(goal)
            memory["steps"].append(response)
            print("[AGENT] LLM Response:", response)
 
        elif step == "use_tool":
            result = fetch_joke_tool()
            memory["steps"].append(result)
            print("[AGENT] Tool Result:", result)
 
        elif step == "stop":
            print("[AGENT] Agent stopped cleanly")
            break