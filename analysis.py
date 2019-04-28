#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

#What are the most popular three articles of all time?
def top_three_articles():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        """SELECT title, count(*) as num
        FROM articles, log
        WHERE log.status = '200 OK'
        AND log.path LIKE '%'
        AND articles.slug = substr(log.path,10)
        GROUP BY articles.title
        ORDER BY num desc limit 3
        """)
    articles = cursor.fetchall()
    print("\n")
    print("1. What are the most popular three articles of all time?")
    print(" ========================================================")
    for el in articles:
        print("   -{} -- {} views".format(el[0], el[1]))
    print("\n")
    db.close()

#Who are the most popular authors of all time?
def top_three_authors():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        """SELECT name, count(*) as num 
        FROM authors, articles, log
        WHERE log.status = '200 OK'
        AND log.path LIKE '%'
        AND articles.slug = substr(log.path,10)
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY num DESC
        """)
    authors = cursor.fetchall()
    print("2. Who are the most popular authors of all time?")
    print(" ========================================================")
    for el in authors:
        print("   -{} -- {} views".format(el[0], el[1]))
    print("\n")
    db.close()

#On which day did more than 1% of requests lead to errors?
def error_date():
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        """SELECT date,error_rate from
        (SELECT date(time) as date,round(100.0*sum(
                    case log.status when '200 OK' then 0 else 1 end)/count(*),1
                    ) as error_rate 
        FROM log 
        GROUP BY date
        ORDER BY error_rate DESC) as errors
        WHERE error_rate > 1
        """)
    errors = cursor.fetchall()
    print("3. On which day did more than 1% of requests lead to errors?")
    print(" ========================================================")
    for el in errors:
        print("   -{} -- {}% errors".format(el[0], el[1]))
    print("\n")
    db.close()

#Runs Log Analysis results
top_three_articles()
top_three_authors()
error_date()