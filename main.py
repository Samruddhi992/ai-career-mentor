from agents.gemini_agent import ask_gemini

print("\n" + "="*60)
print("        🚀 AI CAREER MENTOR SYSTEM 🚀")
print("="*60 + "\n")

print("\n=== AI Scholarship & Career Mentor ===\n")

name = input("Enter your name: ")
print("Welcome", name)

while True:
    user = input("\nAsk anything (type exit to stop): ")

    if user.lower() == "exit":
        print("\nGoodbye! 🚀 Keep learning.")
        break

    prompt = f"""
You are an expert AI Career Mentor.

User query: {user}

Give response in:
- Short bullet points
- Simple English
- Resume + roadmap + portfolio focused
- Practical advice only
"""

    response = ask_gemini(prompt)

    print("\nAI Response:\n")
    print(response)