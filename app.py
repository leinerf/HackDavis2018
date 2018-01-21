from flask import Flask, render_template, redirect, url_for
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
	links = [{"name":"Freniel","link":"/students/Freniel"},{"name":"Brianna","link":"/students/Brianna"},{"name":"Marty","link":"/students/Marty"},{"name":"Nathan","link":"/students/Nathan"}]
	return render_template("home.html",items=links)
	

@app.route('/graph', methods=['GET'])
def graph():
    return render_template("example.html")


@app.route('/students/<student>', methods=['GET'])
def student(student):
	subject_grades = {"Math":43,"Englise":37,"Science":10}
	links = [{"name":"Math","link":"/students/"+student + "/Math"},{"name":"English","link":"/students/"+student + "/English"},{"name":"Science","link":"/students/"+student + "/Science"}]
	return render_template("student-profile.html",student= student, items= links,progress = subject_grades)

@app.route('/students/<student>/<course>', methods=['GET'])
def studentCourses(student,course):
		if(course == "Math"):
			subject_grades = {"Adding":23,"Subtracting":37,"Multiplication":10, "Division":30}
			links = [{"name":"Adding","link":"/students/"+student + "/"+ course + "/Adding"},{"name":"Subtracting","link":"/students/"+student + "/"+ course + "/Subtracting"},{"name":"Division","link":"/students/"+student + "/"+ course + "/Division"},{"name":"Multiplication","link":"/students/"+student + "/"+ course + "/Multiplication"}]
			return render_template("student-profile.html",student= student, items= links,progress = subject_grades)
		elif(course == "English"):
			subject_grades = {"Grammar":23,"Comprehension":37}
			links = [{"name":"Grammar","link":"/students/"+student + "/"+ course + "/Grammar"},
			{"name":"Comprehension","link":"/students/"+student + "/"+ course + "/Comprehension"}]
			return render_template("student-profile.html",student= student, items= links,progress = subject_grades)
		return redirect(url_for('student'))



@app.route('/students/<student>/<course>/<subject>', methods=['GET'])
def studentSubjects(student,course,subject):
	return "{} {} {} ".format(student,course,subject)



if __name__ == '__main__':
    app.run()
