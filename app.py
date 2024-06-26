from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from src.roles import roles
from src.simple_characters import characters

load_dotenv()

from src.llmtoolkit import LLMToolkit
from src.convince_me_toolkit import ConvinceMeToolkit
from src.imaginarium_toolkit import ImaginariumToolkit
from src.character_toolkit import CharacterToolkit
from src.chat_completion import rate_consolation, rate_convincing

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/consoleme")
def consoleme():
    return render_template("consoleme.html", roles= roles)

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

@app.route("/convinceme")
def convinceme():
    return render_template("convinceme.html")

@app.route("/convinceme_input", methods=["POST"])
def convinceme_input():
    # get the body as json
    data = request.get_json()
    chathistory = data["chathistory"]
    llm = ConvinceMeToolkit()
    response = llm.user_input(data["chathistory"])
    rating, convinced = rate_convincing(chathistory)
    return jsonify({
        "message":response,
        "progress": rating,
        "convinced": convinced
    })

@app.route("/imaginarium")
def imaginarium():
    return render_template("imaginarium.html")

@app.route("/imaginarium_input", methods=["POST"])
def imaginarium_input():
    data = request.get_json()
    chathistory = data["chathistory"]
    world = data["world"]
    imaginarium_toolkit = ImaginariumToolkit(world)
    response = imaginarium_toolkit.user_input(chathistory)
    return jsonify({
        "message":response,
    })

@app.route("/character/<character>")
def character(character):
    return render_template(
        "character.html",
        character = characters[character]
    )

@app.route("/character_input/<character>", methods=["POST"])
def character_input(character):
    data = request.get_json()
    chathistory = data["chathistory"]
    poet_toolkit = CharacterToolkit(characters[character]["role"])
    response = poet_toolkit.user_input(chathistory)
    return jsonify({
        "message":response,
    })

if __name__ == '__main__':
    app.run(debug=True)