
# Postgres database interaction
import psycopg2

# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Test password=dani user=postgres")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results

# Uploads a score into the highscore table
def upload_score(name, score):
    interact_with_database("UPDATE score SET score = {} WHERE name = '{}'"
                           .format(score, name))

# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM score")

# Downloads the questions
def download_questions():
    return interact_with_database("Select * FROM mult_questions")

# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM score ORDER BY score")
    return result
# Download a single question
def download_singlequestion(nr):
    variable = str(nr)
    result = interact_with_database("SELECT question From mult_question WHERE "+variable+" = nr")
    return result
# Download option A
def download_singlequestionoptionA(nr):
    variable = str(nr)
    result = interact_with_database("SELECT a From mult_question WHERE "+variable+" = nr")
    return result
# Download option B
def download_singlequestionoptionB(nr):
    variable = str(nr)
    result = interact_with_database("SELECT b From mult_question WHERE "+variable+" = nr")
    return result
# Download option C
def download_singlequestionoptionC(nr):
    variable = str(nr)
    result = interact_with_database("SELECT c From mult_question WHERE "+variable+" = nr")
    return result
# Download the right answer
def download_question_answer(nr):
    variable = str(nr)
    result = interact_with_database("SELECT correct_answer FROM mult_question WHERE "+variable+" = nr")
    return result
# Get (almost) everything from a question
def download_alot_question(nr):
    variable = str(nr)
    result = interact_with_database("Select question,a,b,c,correct_answer FROM mult_question WHERE "+variable+" = nr")
    return result
# Store in a list
def seperate_question(nr):
    questionlist = []
    questionlist.append(download_singlequestion(nr))
    questionlist.append(download_singlequestionoptionA(nr))
    questionlist.append(download_singlequestionoptionB(nr))
    questionlist.append(download_singlequestionoptionC(nr))
    questionlist.append(download_question_answer(nr))
    return questionlist
