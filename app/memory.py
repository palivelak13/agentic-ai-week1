# def init_memory(goal: str) -> dict:
#     return {
#         "goal": goal,
#         "steps": [],
#         "completed": False
#     }

def init_memory(goal: str) -> dict:
    print("[MEMORY] Initializing memory")
 
    return {
        "goal": goal,
        "steps": [],
        "completed": False,
        "tool_retries": 0
    }
 