from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def root():
     return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/graph', methods=['GET'])
def graph():
    return render_template("example.html")


@app.route('/students/<student>', methods=['GET'])
def student(student):
    return render_template("student-profile.html",student = student)


if __name__ == '__main__':
    app.run()
