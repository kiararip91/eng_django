import psycopg2


class Word:
    def __init__(self, id, english, italian, sentence, type, importance, right, error):
        self.id = id
        self.english = english.replace("'", "---") // FIXME
        self.italian = italian.replace("'", "---")
        self.sentence = sentence.replace("'", "---").replace("\n", " _ ")
        self.type = type
        self.importance = importance
        self.right = right
        self.error = error


def rowToWord(row):
    parsedWord = Word(id=row[0], english=row[1], italian=row[2], sentence=row[3], type=row[4], importance=row[5], right=row[6], error=row[7])
    return parsedWord


def updateScore(index, rightScore, wrongScore, isCorrect):

    if isCorrect:
        query = """
            UPDATE word
            SET correct=correct + 1
            WHERE id=%s
            """
    else:
        query = """
            UPDATE word
            SET wrong=wrong + 1
            WHERE id=%s
            """

    try:
        conn = psycopg2.connect(("dbname='eng_game' user='postgres' host='35.195.186.40' password='softball'"))
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute(query, [index])
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception(error)
    finally:
        if conn is not None:
            conn.close()


def getWordFromDb(importance):
    conn = None
    word = None
    try:
        conn = psycopg2.connect(("dbname='eng_game' user='postgres' host='35.195.186.40' password='softball'"))
        cur = conn.cursor()
        cur.execute("SELECT * FROM word WHERE importance = %s ORDER BY (wrong+0.1)/(correct+0.1) DESC LIMIT 10", str(importance))
        wordList = []

        for word in cur:
            parsedWord = rowToWord(word)
            newWord = {
                'id': parsedWord.id,
                'english': parsedWord.english,
                'italian': parsedWord.italian,
                'sentence': parsedWord.sentence,
                'correct': parsedWord.right,
                'wrong': parsedWord.error}
            wordList.append(newWord)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return wordList


def getAcronymusFromDb():
    conn = None
    acronymus = None
    try:
        conn = psycopg2.connect(("dbname='eng_game' user='postgres' host='35.195.186.40' password='softball'"))
        cur = conn.cursor()
        cur.execute("SELECT * FROM acronym ORDER BY RANDOM() LIMIT 1")
        row = cur.fetchone()
        acronymus = {
            'id': row[0],
            'name': row[1],
            'explanation': row[2]
        }
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return acronymus
