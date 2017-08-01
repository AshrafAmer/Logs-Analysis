#!/usr/bin/env python
# import DB library we are using..
import psycopg2


# Create most_popularArticles class to answer the 1st Question..
# What are the most popular three articles of all time?
def most_popularArticles():
    # 1. connect to the DB.
    try:
        conn = psycopg2.connect("dbname=news")
    except:
        print "Unable to connect to the database."
    # 2.Create cursor object to run Queries and fetch results.
    cursor = conn.cursor()
    # 3.used cursor object to run my Query.
    try:
        cursor.execute("""
            SELECT title, count(*) AS nom
            FROM articles, log
            WHERE log.path = '/article/'||articles.slug
            group by title
            order by nom desc limit(3);
            """)
    except:
        print "Unable to execute the Query."
    # 4.Save results by fetch it all.
    results = cursor.fetchall()
    # 5.Print Out results on screen..
    print "\n the most popular three articles of all time:\n"
    # Loop to read data from table, row by row
    for row in results:
        # Python function to convert a list to a string for display
        # Reference : https://www.decalage.info/en/python/print_list
        print '"' + ('" - '.join(map(str, row))) + ' views'
    # Finally, close the Connection
    conn.close()


# Create most_popularAuthors class to answer the 2nd Question..
# Who are the most popular article authors of all time?
def most_popularAuthors():
    try:
        conn = psycopg2.connect("dbname=news")
    except:
        print "Unable to connect to the database."
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT name, nom
            FROM authors, ArticlesView
            WHERE authors.id = ArticlesView.author
            order by nom desc;
            """)
    except:
        print "Unable to execute the Query."
    results = cursor.fetchall()
    print "\n the most popular article authors of all time:\n"
    for row in results:
        print(' - '.join(map(str, row))) + ' views'
    conn.close()


# Create requestsError class to answer the 3rd Question..
# On which days did more than 1% of requests lead to errors?
def requestsError():
    try:
        conn = psycopg2.connect("dbname=news")
    except:
        print "Unable to connect to the database."
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT requests_no.date, 100.0*nom/sum_all AS per
            FROM requests_no , requests_con
            where requests_no.date = requests_con.date
            and requests_no.status !='200 OK'
            and (100.0*nom/sum_all)  > 1;
            """)
    except:
        print "Unable to execute the Query."
    results = cursor.fetchall()
    print "\n Which days did more than 1% of requests lead to errors? \n"
    for row in results:
        print(' - '.join(map(str, row))) + ' % errors'
    conn.close()


# Call functions to RUN..
if __name__ == "__main__":
    most_popularArticles()
    most_popularAuthors()
    requestsError()
