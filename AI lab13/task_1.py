questions = [
    "What is my name?",
    "Which university do I study in?",
    "What is my favorite programming language?",
    "What am I studying?",
    "Where am I currently living?"
]
user_info = {}
def chatbot_answer(question):
    question = question.lower()
    if "name" in question:
        return user_info.get("name", "I don't know for sure")
    elif "university" in question:
        return user_info.get("university", "I haven’t heard which university you attend.")
    elif "programming language" in question:
        return user_info.get("programming_language", "You didn’t say anything about that.")
    elif "studying" in question:
        return user_info.get("study", "I don’t know your major.")
    elif "living" in question:
        return user_info.get("living", "You haven’t shared that information with me yet.")
    else:
        return "I don't understand the question."

print("BEFORE INFORMATION:")
for question in questions:
    print(f"Question: {question}")
    print(f"Answer  : {chatbot_answer(question)}\n")
user_info = {
    "name": "KHUBAIB NAEEM",
    "university": "KIET",
    "programming_language": "PYTHON",
    "study": "SOFTWARE ENGINEERING",
    "living": "KARACHI"
}
print("AFTER INFORMATION:")
for question in questions:
    print(f"Question: {question}")
    print(f"Answer  : {chatbot_answer(question)}\n")