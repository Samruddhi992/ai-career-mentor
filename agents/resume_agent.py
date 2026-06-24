from agents.gemini_agent import ask_gemini

def get_resume_advice():
    prompt = "Give resume improvement tips for a student in simple points"
    return ask_gemini(prompt)