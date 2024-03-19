from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

from src.llmtoolkit import LLMToolkit
from src.chat_completion import rate_consolation

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/userinput", methods=["POST"])
def userinput():
    # get the body as json
    data = request.get_json()
    chathistory = data["chathistory"]
    character = data["character"]
    llm = LLMToolkit(character)
    response = llm.user_input(data["chathistory"])
    rating = rate_consolation(character, chathistory)
    return jsonify({
        "message":response,
        "progress": rating
    })

if __name__ == '__main__':
    app.run(debug=True)