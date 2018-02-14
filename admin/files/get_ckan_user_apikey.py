#! /usr/bin/python
import getopt
import psycopg2
import sys


def main(argv):

    username = ''
    conn_string = ''

    try:
        opts, args = getopt.getopt(
            argv, "hu:c:", ["username=", "connection-string="])
    except getopt.GetoptError:
        print('-u <username> -c <connection-string>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-u', '--username'):
            username = arg
        if opt in ('-c', '--connection-string'):
            conn_string = arg

    if not conn_string or not username:
        print('-u <username> -c <connection-string>')
        sys.exit(2)

    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    cur.execute(
        "SELECT apikey FROM public.user WHERE name = '{0}'".format(username))

    rows = cur.fetchall()
    try:
        print(rows[0][0])
    except IndexError:
        print(None)


if __name__ == "__main__":
    main(sys.argv[1:])
