def decide_next_step(memory: dict) -> str:
    print("decide_next_step called, steps:", len(memory["steps"]))

    if memory["completed"]:
        print("Memory completed → stop")
        return "stop"

    if len(memory["steps"]) < 2:
        print("Calling LLM")
        return "call_llm"

    memory["completed"] = True
    print("Reached 2 steps → stopping")
    return "stop"
