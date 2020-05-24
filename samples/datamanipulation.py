import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_domain_by_id(conn, domainid):
    """ Select all rows from domain table with the domainid filter
    """
    # open a cursor
    cur = conn.cursor()
    # sql
    sql = "select * from domain where domainid > ?"
    # execute the sql with bind parameters
    cur.execute(sql,  (domainid,))
    # result of the query. The result is a list of rows
    # example [(1, 'domain1', 'daily'), (2, 'domain2', 'daily')]
    rows = cur.fetchall()
    return rows

def create_domain ( conn, domain):

    # open cursor
    cur = conn.cursor()
    sql = "insert into domain values (?,?,?)"
    cur.execute(sql, domain)

def main():
    database = r'../data/pcf.db'

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Select from domain")
        domainrows = select_domain_by_id(conn, 0)
        # print the number of row of the list
        print(len(domainrows))
        # print each row
        for row in domainrows:
            print(row)

        # insert into domain
        print ("2. Insert into domain ")
        #
        newdomain=(len(domainrows) + 1, 'domain' + str(len(domainrows) + 1), 'daily')
        print(newdomain)

        create_domain(conn, newdomain)

        # select from domain after insert
        print("3. Select from domain after insert")
        print(select_domain_by_id(conn, 0))

if __name__ == '__main__':
    main()

