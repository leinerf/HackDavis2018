from flask import Flask, render_template, redirect, url_for, request
from generation import generate
#from pymongo import MongoClient
#import pprint

app = Flask(__name__)
app.debug = True
#db = client['test-database']
def createPost(**kwargs):
	return kwargs    

#client = MongoClient('mongodb://localhost:27017/')


@app.route('/', methods=['GET'])
def root():
     return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
	links = [{"name":"Freniel","link":"/students/Freniel"},{"name":"Briana","link":"/students/Briana"},{"name":"Marty","link":"/students/Marty"},{"name":"Aziz","link":"/students/Aziz"}]
	return render_template("home.html",items=links,title="Homepage")
	

@app.route('/graph', methods=['GET'])
def graph():
    return render_template("example.html")


@app.route('/students/<student>', methods=['GET'])
def student(student):
	subject_grades = {"Math":43,"English":37,"Science":10}
	links = [{"name":"Math","link":"/students/"+student + "/course/Math"},{"name":"English","link":"/students/"+student + "/course/English"},{"name":"Science","link":"/students/"+student + "/course/Science"}]
	return render_template("student-profile.html",student= student, items= links,progress = subject_grades,title=student)

@app.route('/students/<student>/course/<course>', methods=['GET'])
def studentCourses(student,course):
		generate(10)
		if(course == "Math"):
			subject_grades = {"Adding":23,"Subtracting":37,"Multiplication":10, "Division":30}
			links = [{"name":"Adding","link":"/students/"+student + "/course/"+ course + "/Adding"},{"name":"Subtracting","link":"/students/"+student + "/course/"+ course + "/Subtracting"},{"name":"Division","link":"/students/"+student + "/course/"+ course + "/Division"},{"name":"Multiplication","link":"/students/"+student + "/course/"+ course + "/Multiplication"}]
			return render_template("subject_page.html",student= student, items= links,progress = subject_grades,title=student,course = True)
		elif(course == "English"):
			subject_grades = {"Grammar":23,"Comprehension":37}
			links = [{"name":"Grammar","link":"/students/"+student + "/"+ course + "/Grammar"},
			{"name":"Comprehension","link":"/students/"+student + "/"+ course + "/Comprehension"}]
			return render_template("subject_page.html",student= student, items= links,progress = subject_grades,title=student,course = True)
		return redirect(url_for('student'))


@app.route('/students/<student>/course/<course>/subject/<subject>', methods=['GET'])
def studentSubjects(student,course,subject):
	return "{} {} {} ".format(student,course,subject)

@app.route('/students/<student>/<course>/subject/<subject>/practice', methods=['GET'])
def quiz(student,course,subject):
	return "Hello World"

if __name__ == '__main__':
    app.run()
