from __future__ import print_function
from django.test import TestCase
import os
import psycopg2


def updateScore(index, rightScore, wrongScore, isCorrect):
    if isCorrect:
        rightScore = rightScore + 1
    else:
        wrongScore = wrongScore + 1

    try:
        conn = psycopg2.connect(("dbname='eng_game' user='postgres' host='35.195.186.40' password='softball'"))
        cur = conn.cursor()
        cur = conn.cursor()
        cur.execute("""
            UPDATE word
            SET correct=%s, wrong=%s
            WHERE id=%s
            """, (rightScore, wrongScore, index))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    updateScore(5, 1, 2, 1)
