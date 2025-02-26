from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
students = []
def calculate_risk(marks, attendance):
    risk = 100 - (marks * 0.5 + attendance * 0.5)
    return min(max(risk, 0), 100)  
@app.route('/')
def index():
    return render_template('index.html', students=students)
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    marks = float(request.form['marks'])
    attendance = float(request.form['attendance'])
    risk = calculate_risk(marks, attendance)
    students.append({'name': name, 'marks': marks, 'attendance': attendance, 'risk': risk})
    return redirect(url_for('index'))
@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    if 0 <= student_id < len(students):
        students.pop(student_id)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
