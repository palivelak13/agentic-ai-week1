# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import init_memory
# from app.tools import fetch_joke_tool
 
# def run_agent(goal: str):
#     memory = init_memory(goal)
 
#     print("\n[AGENT] Starting agent")
#     print("[AGENT] Goal:", goal)
 
#     while True:
#         print("\n[AGENT] Loop iteration started")
#         step = decide_next_step(memory)
#         print("[AGENT] Control decided:", step)
 
#         if step == "call_llm":
#             response = call_llm(goal)
#             memory["steps"].append(response)
#             print("[AGENT] LLM Response:", response)
 
#         elif step == "use_tool":
#             result = fetch_joke_tool()
#             memory["steps"].append(result)
#             print("[AGENT] Tool Result:", result)
 
#         elif step == "stop":
#             print("[AGENT] Agent stopped cleanly")
#             break

# from app.control import decide_next_step
# from app.llm import call_llm
# from app.memory import init_memory
# from app.tools import fetch_joke_tool
 
# def run_agent(goal: str):
#     memory = init_memory(goal)
 
#     print("\n[AGENT] Starting agent")
#     print("[AGENT] Goal:", goal)
 
#     while True:
#         print("\n[AGENT] Loop iteration")
#         step = decide_next_step(memory)
#         print("[AGENT] Control decided:", step)
 
#         if step == "call_llm":
#             response = call_llm(goal)
#             memory["steps"].append(response)
#             print("[AGENT] LLM Response:", response)
 
#         elif step == "use_tool":
#             result = fetch_joke_tool()
#             memory["steps"].append(result)
#             print("[AGENT] Tool Result:", result)
 
#         elif step == "stop":
#             print("[AGENT] Agent stopped cleanly")
#             break
  #practice agent


from app.control import decide_next_step
from app.llm import call_llm
from app.memory import init_memory
from app.tools import fetch_ticket_tool

def run_agent(goal: str):
    memory = init_memory(goal)

    print("\n[AGENT] Starting agent")
    print("[AGENT] Goal:", goal)

    while True:
        print("\n[AGENT] Loop iteration")

        step = decide_next_step(memory)
        print("[AGENT] Control decided:", step)

        if step == "call_llm":
            response = call_llm(goal)
            memory["steps"].append(response)
            print("[AGENT] LLM Response:", response)

        elif step == "use_tool":
            result = fetch_ticket_tool()
            memory["steps"].append(result)

            if isinstance(result, dict) and result.get("status") == "SUCCESS":
                ticket = result["data"]
                # Print directly without formatter
                print("\n🎬 Movie Ticket Info")
                print("-------------------")
                print(f"Movie Name : {ticket['movie']}")
                print(f"Price      : {ticket['price']} {ticket['currency']}\n")
            else:
                print("[AGENT] Tool failed, no ticket data")

        elif step == "stop":
            print("[AGENT] Agent stopped cleanly")
            print("[AGENT] Final memory:", memory)
            break
