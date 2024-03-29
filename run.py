from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "123Fe$#"
socketio = SocketIO(app)

@app.route("/", methods=['GET', 'POST'])
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on("message")
def handle_messages(json, methods=['GET','POST']):
    print("received my event: " + str(json))
    socketio.emit("response", json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)
