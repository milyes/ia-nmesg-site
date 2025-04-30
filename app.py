from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("message", "")
    if "bonjour" in question.lower():
        reply = "Bonjour ! Je suis IA_NETMSG."
    elif "analyse" in question.lower():
        reply = "Analyse en cours de votre environnement..."
    else:
        reply = "Je suis IA_NETMSG, assistant IA local prêt à vous aider."
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
