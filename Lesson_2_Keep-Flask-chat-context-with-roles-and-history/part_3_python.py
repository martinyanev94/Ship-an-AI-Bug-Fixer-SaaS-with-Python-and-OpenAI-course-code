# already above: app = Flask(__name__)

# already above: client = OpenAI(api_key=...)

conversation_history = []



@app.route("/")

def index():

    return render_template("index.html")



@app.route("/get")

def get_bot_response():

    userText = request.args.get("msg")

    model_engine = "gpt-3.5-turbo"

    conversation_history.append(

        {"role": "user", "content": userText}

    )
