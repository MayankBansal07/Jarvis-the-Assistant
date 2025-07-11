from flask import Flask, request, jsonify
from flask_cors import CORS
from main import listen_for_command, speak

app = Flask(__name__)
CORS(app)

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    command = data.get("command", "")
    speak(f"You said: {command}")
    return jsonify({"response": f"Command '{command}' received and processed."})

if __name__ == "__main__":
    app.run(debug=True)
