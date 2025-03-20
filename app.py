from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from utils.main import capitalise
import webbrowser

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/format", methods=['POST'])
def formatter():
    data = request.json
    formatted_text = capitalise(data['text'])
    return jsonify({'formatted_text':formatted_text })

if __name__=="__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    socketio.run(app, debug=True)