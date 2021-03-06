from chatbot import get_answer

from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=['GET'])
def get_bot_response():
    question = request.args.get('msg')
    return get_answer(question)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
