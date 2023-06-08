from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension 
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chickens1'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses = []

@app.route('/')
def home():
    '''Home Page'''
    #current_question_no = len(responses)
    #questions = satisfaction_survey.questions
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title = title, instructions = instructions, responses = responses)

@app.route('/questions/<int:question_no>')
def display_questions(question_no):
    '''Display question'''
    current_question_no = len(responses)

    if current_question_no < question_no or current_question_no > question_no:
        flash("You're trying to access an invalid question")
        return redirect ('/questions/' + str(current_question_no))
    
    question = satisfaction_survey.questions[question_no].question

    return render_template('questions.html', question = question, current_question_no = current_question_no, question_no = question_no)

@app.route('/answer', methods=["POST"])
def track_answer():
    ans = request.form['yes_no']
    responses.append(ans)
    if len(responses) == 1:
        return redirect ('/questions/1')
    elif len(responses) == 2:
        return redirect ('/questions/2')    
    elif len(responses) == 3:
        return redirect ('/questions/3')
    else:
        return render_template ('thank_you.html', responses = responses)
    