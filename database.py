import sqlite3

def create_connection():

    connection = sqlite3.connect("memory.db")
    return connection


def get_questions_and_answers():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM questionsAndAnswers")

    return cur.fetchall()


def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()
    #insert into tablename values('question', 'answert')
    query = "INSERT INTO questionsAndAnswers values('"+question+"', '"+answer+"')"
    cur.execute(query)
    con.commit()

    

def get_answer_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break

    return answer


