from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
     return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/students/<students>', methods=['GET'])
def student():
    return "User %s" % username



if __name__ == '__main__':
    app.run()
