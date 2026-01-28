# # # def print_tool(text: str) -> str:
# # #     print("[TOOL] Printing output:")
# # #     print(text)
# # #     return "printed"

# # #AGENT 1: MARKET CONCEPT EXPLAINER
# # # def print_tool(text: str) -> str:
# # #     print("[TOOL] NEWS SUMMARY:")
# # #     print(text)
# # #     return "printed"

# # #AGENT 2: MARKET CONCEPT EXPLAINER

# # # def print_tool(text: str) -> str:
# # #     print("[TOOL] MARKET EXPLANATION:")
# # #     print(text)
# # #     return "printed"
# # import requests
 
# # def fetch_joke_tool() -> str:
# #     print("[TOOL] Calling external Joke API")
 
# #     response = requests.get(
# #         "https://official-joke-api.appspot.com/random_joke",
# #         timeout=5
# #     )
 
# #     if response.status_code != 200:
# #         print("[TOOL] API failed")
# #         return "TOOL_FAILED"
 
# #     data = response.json()
# #     joke = f"{data['setup']} — {data['punchline']}"
 
# #     print("[TOOL] Joke fetched successfully")
# #     return joke

# # import requests
# # import random
 
# # def fetch_joke_tool() -> str:
# #     print("[TOOL] Calling external Joke API")
 
# #     # Simulate failure sometimes (for learning)
# #     if random.choice([True, False]):
# #         print("[TOOL] Simulated tool failure")
# #         return "TOOL_FAILED"
 
# #     response = requests.get(
# #         "https://official-joke-api.appspot.com/random_joke",
# #         timeout=5
# #     )
 
# #     if response.status_code != 200:
# #         print("[TOOL] API error")
# #         return "TOOL_FAILED"
 
# #     data = response.json()
# #     joke = f"{data['setup']} — {data['punchline']}"
# #     print("[TOOL] Joke fetched successfully")
# #     return joke
 
# #practice agent
# import random

# MOVIE_TICKETS = [
#     {"movie": "Inception", "price": 12.5, "currency": "USD"},
#     {"movie": "Interstellar", "price": 15.0, "currency": "USD"},
#     {"movie": "Avatar", "price": 10.0, "currency": "USD"}
# ]

# def fetch_ticket_tool() -> dict:
#     print("[TOOL] Fetching movie ticket data")

#     # Simulate failure sometimes (for learning)
#     if random.choice([True, False]):
#         print("[TOOL] Simulated tool failure")
#         return {"status": "FAILED"}

#     ticket = random.choice(MOVIE_TICKETS)
#     print("[TOOL] Ticket fetched successfully")
#     return {
#         "status": "SUCCESS",
#         "data": ticket
#     }


# def market_explainer_tool(text: str) -> str:
#     print("\n[TOOL] MARKET EXPLANATION:")
#     print(text)
#     return "EXPLANATION_PRESENTED"

#week 2 assignment 3

def read_notice(file_path="app/notice.txt"):
    with open(file_path, "r") as file:
        return file.read()

def explain_notice(notice_text):
    return (
        "All students are informed that the school will remain closed on Monday due to a staff meeting. "
        "Regular classes will resume from Tuesday."
    )
