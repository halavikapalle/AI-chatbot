# ============================================================
#  DecodeLabs | Project 1 | Rule-Based AI Chatbot
#  Backend: Python + Flask
# ============================================================

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── KNOWLEDGE BASE ───────────────────────────────────────────
RESPONSES = {
    "hello":             "Hey there! I'm DecoBot. How can I help you today?",
    "hi":                "Hi! Great to see you. What's on your mind?",
    "hey":               "Hey! I'm here and ready to chat. What do you need?",
    "good morning":      "Good morning! Hope you have a productive day ahead.",
    "good evening":      "Good evening! How can I assist you tonight?",
    "who are you":       "I'm DecoBot — a rule-based AI chatbot built at DecodeLabs.",
    "what are you":      "I'm a rule-based chatbot. I respond using predefined logic, not deep learning.",
    "your name":         "My name is DecoBot! Built with pure Python + Flask.",
    "what can you do":   "I can answer predefined questions and have a basic conversation!",
    "help":              "Try: hello, who are you, what is ai, tell me a joke, or bye.",
    "how are you":       "I'm just code, but running perfectly! How about you?",
    "what's up":         "Not much — just waiting for your next input!",
    "are you human":     "Nope! I'm 100% programmatic. No neurons, just conditions.",
    "do you sleep":      "Never! I run in a continuous loop — always awake.",
    "what is ai":        "AI stands for Artificial Intelligence — machines simulating human decision-making.",
    "what is python":    "Python is a high-level programming language — the one I'm built with!",
    "what is a chatbot": "A chatbot is a program that simulates conversation with users — like me!",
    "what is ml":        "ML stands for Machine Learning — AI that learns from data. I use rules instead!",
    "what is decodelabs":"DecodeLabs is an industrial training platform helping interns build real AI projects.",
    "what is nlp":       "NLP is Natural Language Processing — how machines understand human language.",
    "tell me a joke":    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "another joke":      "Why did the AI go to school? To improve its learning rate!",
    "one more joke":     "What do you call a sleeping AI? Artificial unintelligence!",
    "quote":             "An LLM without rules is a hallucination engine. — DecodeLabs",
    "bye":               "Goodbye! It was great chatting with you. See you next time!",
    "goodbye":           "Take care! Keep building great things.",
    "see you":           "See you around! Come back anytime.",
    "thanks":            "You're welcome! Always happy to help.",
    "thank you":         "Anytime! That's what I'm here for.",
}

EXIT_COMMANDS = {"exit", "quit", "stop", "end", "close"}

# ── PHASE 1: SANITIZATION ────────────────────────────────────
def sanitize(raw_input):
    return raw_input.lower().strip()

# ── PHASE 2: IF-ELSE LOGIC ───────────────────────────────────
def get_response(clean_input):
    for key in RESPONSES:
        if key in clean_input:
            return RESPONSES[key]
    return "I don't understand that. Type 'help' to see what I can do!"

# ── ROUTES ───────────────────────────────────────────────────
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data        = request.get_json()
    user_msg    = data.get("message", "")
    clean       = sanitize(user_msg)

    if clean in EXIT_COMMANDS:
        return jsonify({"reply": "Goodbye! Session ended.", "exit": True})

    reply = get_response(clean)
    return jsonify({"reply": reply, "exit": False})

# ── RUN ──────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)