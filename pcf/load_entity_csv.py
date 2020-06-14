import pandas as pd
from pcf.common.dbconnect import connect
from sqlite3 import Error


def create_connection():
    """ create a database connection to the SQLite database
    """
    conn = None
    try:
        conn = connect()
    except Error as e:
        print(e)

    return conn


def load_entity(fname='../data/entity.csv'):
    dfentity_csv = pd.read_csv(fname)
    #    print(dfentity_csv.head())

    conn = create_connection()
    dfentity_sql = pd.read_sql("select * from entity", conn)
    print(dfentity_sql.head())

    #    print("start iteration")
    #    df = dfentity_sql.assign(rn=dfentity_sql.sort_values('entityId', ascending=False)
    #                                            .groupby(['entityName'])
    #                                            .cumcount() +1)

    dfentity_sql_rnk1 = dfentity_sql.assign(rn=dfentity_sql.sort_values(['entityId'], ascending=False) \
                             .groupby(['entityName']) \
                             .cumcount() + 1) \
        .query('rn == 1 ')

    #print(df_sql_rnk1)

    df = pd.merge(dfentity_csv, dfentity_sql_rnk1 , how='left' , left_on=['entityName'] , right_on=['entityName'])
    print(df)


"""
    # using itertulples to iterate the csv dataframe. when a match is found the flag column will be updated.
    for row in dfentity_csv.itertuples():
        print(getattr(row,'entityName'))
        #if getattr(row,'entityName') in dfentity_sql['entityName'].values:
        #    print ("exists" + str(dfentity_sql['entityId'].values) )
        if dfentity_sql.isin(getattr(row,'entityName')):
            print
        else:
            print("does not exist")
"""

load_entity()
