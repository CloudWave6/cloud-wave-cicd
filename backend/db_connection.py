import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='lab-edu-rds-aurora.cluster-cr8yyiy2wzm2.ap-northeast-2.rds.amazonaws.com',
        database='trip_advisor',
        user='user',
        password='qwer1243'
    )
    return conn