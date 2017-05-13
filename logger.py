#! /usr/bin/env
import psycopg2


def main():
    db = psycopg2.connect("dbname=news")

    # Question 1
    print "What are the most popular three articles of all time?"
    c = db.cursor()
    c.execute("SELECT title, count(*) as num FROM log "
              "JOIN articles ON slug = split_part(path, '/', 3) "
              "WHERE path != '/' GROUP BY title ORDER BY num DESC LIMIT 3")
    logs = c.fetchall()
    for l in logs:
        print l[0] + " - " + str(l[1])
    print ""

    # Question 2
    print "Who are the most popular article authors of all time?"
    c = db.cursor()
    c.execute("SELECT authors.name, count(*) as num FROM log "
              "JOIN articles ON slug = split_part(path, '/', 3) "
              "JOIN authors ON author = authors.id "
              "WHERE path != '/' GROUP BY authors.name ORDER BY num DESC")
    authors = c.fetchall()
    for a in authors:
        print a[0] + " - " + str(a[1]) + " views"
    print ""

    # Question 3
    print "On which days did more than 1% of requests lead to errors?"
    c = db.cursor()
    c.execute("SELECT date, (error / (ok + error) * 100) FROM "
              "(SELECT to_char(time, 'Mon DD, YYYY') as date, "
              "Sum(CASE WHEN status = '200 OK' THEN 1.0 ELSE 0.0 END) as ok, "
              "Sum(CASE WHEN status = '404 NOT FOUND' "
              "THEN 1.0 ELSE 0.0 END) as error "
              "FROM log GROUP BY date) as freq "
              "WHERE (error / (ok + error) * 100) > 1.0")
    days = c.fetchall()
    for d in days:
        print d[0] + " - " + str(d[1])
    print ""

    db.close()


if __name__ == '__main__':
    main()
