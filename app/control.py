# # # def decide_next_step(memory: dict) -> str:
# # #     print("\n[CONTROL] Current memory:", memory)
 
# # #     if memory["completed"]:
# # #         print("[CONTROL] completed=True → STOP")
# # #         return "stop"
 
# # #     if len(memory["steps"]) == 0:
# # #         print("[CONTROL] First step → CALL LLM")
# # #         return "call_llm"
 
# # #     if len(memory["steps"]) == 1:
# # #         print("[CONTROL] Second step → USE TOOL")
# # #         return "use_tool"
 
# # #     print("[CONTROL] All steps done → STOP")
# # #     memory["completed"] = True
# # #     return "stop"
 
 

# # def decide_next_step(memory: dict) -> str:
# #     print("\n[CONTROL] Current memory:", memory)
 
# #     if memory["completed"]:
# #         return "stop"
 
# #     # Step 1: Ask LLM
# #     if len(memory["steps"]) == 0:
# #         print("[CONTROL] First step → CALL LLM")
# #         return "call_llm"
 
# #     # Step 2: Use external tool
# #     if len(memory["steps"]) == 1:
# #         print("[CONTROL] Second step → USE TOOL")
# #         return "use_tool"
 
# #     # Step 3: Stop
# #     print("[CONTROL] All steps done → STOP")
# #     memory["completed"] = True
# #     return "stop"


# def decide_next_step(memory: dict) -> str:
#     print("\n[CONTROL] Current memory:", memory)
 
#     if memory["completed"]:
#         return "stop"
 
#     # Step 1: Call LLM
#     if len(memory["steps"]) == 0:
#         print("[CONTROL] First step → CALL LLM")
#         return "call_llm"
 
#     # Step 2: Use tool
#     if len(memory["steps"]) == 1:
#         print("[CONTROL] Second step → USE TOOL")
#         return "use_tool"
 
#     # Handle tool failure
#     last_step = memory["steps"][-1]
#     if last_step == "TOOL_FAILED":
#         if memory["tool_retries"] < 1:
#             memory["tool_retries"] += 1
#             print("[CONTROL] Tool failed → RETRY")
#             return "use_tool"
#         else:
#             print("[CONTROL] Tool failed again → STOP")
#             memory["completed"] = True
#             return "stop"
 
#     # Successful execution → stop
#     print("[CONTROL] Tool succeeded → STOP")
#     memory["completed"] = True
#     return "stop"

# def decide_next_step(memory: dict) -> str:
#     print("\n[CONTROL] Current memory:", memory)
 
#     if memory["completed"]:
#         return "stop"
 
#     # Step 1: Get explanation from LLM
#     if len(memory["steps"]) == 0:
#         return "call_llm"
 
#     # Step 2: Present explanation using tool
#     if len(memory["steps"]) == 1:
#         return "use_tool"
 
#     # Step 3: Stop agent
#     memory["completed"] = True
#     return "stop"
 
#assignment week 2 -3

from app.tools import read_notice, explain_notice



def run_agent():
    # Step 1: Read notice
    notice = read_notice()

    # Step 2: Explain notice
    explanation = explain_notice(notice)

    # Step 3: Present explanation
    print("Original Notice:\n")
    print(notice)

    print("\nSimple Explanation:\n")
    print(explanation)

    # Step 4: Stop
    return
