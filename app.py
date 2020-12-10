from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gosha/py/hw8/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.app = app
db.init_app(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    bitrhday = db.Column(db.Text)

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    q_fool = db.Column(db.Text)
    q_walla = db.Column(db.Text)
    q_def = db.Column(db.Text)

@app.route('/stats')
def stats():
    return render_template("stats.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey')
def survey():
    questions = Questions.query.all()
    return render_template(
        'survey.html',
        questions=questions
    )

@app.route('/process', methods=['get'])
def answer_process():
    if not request.args:
        return redirect(url_for('survey'))
    name = request.args.get('name')
    birthday = request.args.get('birthday')
    user = User(
        birthday=birthday,
        name=name,
    )
    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)
    q_fool = request.args.get('q_fool')
    q_walla = request.args.get('q_walla')
    q_def = request.args.get('q_def')
    answer = Answers(id=user.id, q_fool=q_fool, q_walla=q_walla, q_def=q_def)
    db.session.add(answer)
    db.session.commit()
    return 'Ok'

if __name__ == '__main__':
    app.run(debug=True)
