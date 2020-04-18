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



def get_name():
    con = create_connection()
    cur = con.cursor()
    #insert into tablename values('question', 'answert')
    query = "select value from memory where name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(new_name):
    con = create_connection()
    cur = con.cursor()
    #insert into tablename values('question', 'answert')
    query = "update memory set value = '"+new_name+"' where name = 'assistant_name'"
    cur.execute(query)
    con.commit()


def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    #insert into tablename values('question', 'answert')
    query = "update memory set value = '"+str(last_seen_date)+"' where name = 'last_seen_date'"
    cur.execute(query)
    con.commit()

def get_last_seen():
    con = create_connection()
    cur = con.cursor()

    query = "select value from memory where name = 'last_seen_date'"
    cur.execute(query)
    return str(cur.fetchall()[0][0])

update_last_seen("324324")

