from __future__ import print_function
from django.test import TestCase
import os
import psycopg2


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
        cur.execute(query, (str(index)))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        raise Exception(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    updateScore(1, 1, 1, 1)
