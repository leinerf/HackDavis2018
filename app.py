from flask import Flask, render_template, redirect, url_for
#from pymongo import MongoClient
#import pprint

app = Flask(__name__)
app.debug = True
#db = client['test-database']
def createPost(math,english,science):
	post = {

	 "Math": math, 
	 "English": english,
	 "Science": science
	}
	return post 
    

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
	subject_grades = createPost(40,30,30)
	links = [{"name":"Math","link":"/students/"+student + "/Math"},{"name":"English","link":"/students/"+student + "/English"},{"name":"Science","link":"/students/"+student + "/Science"}]
	return render_template("student-profile.html",student= student, items= links,progress = subject_grades)

@app.route('/students/<student>/<course>', methods=['GET'])
def studentCourses(student,course):
	subject_grades = createPost(23,32,32)
	links = [{"name":"Adding","link":"/students/"+student + "/"+ course + "/Adding"},{"name":"Subtracting","link":"/students/"+student + "/"+ course + "/Subtracting"},{"name":"Division","link":"/students/"+student + "/"+ course + "/Division"},{"name":"Multiplication","link":"/students/"+student + "/"+ course + "/Multiplication"}]
	return render_template("student-profile.html",student= student, items= links,progress = subject_grades)



@app.route('/students/<student>/<course>/<subject>', methods=['GET'])
def studentSubjects(student,course,subject):
	return "{} {} {} ".format(student,course,subject)



if __name__ == '__main__':
    app.run()
