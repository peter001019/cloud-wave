import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host='lab-edu-rds-aurora-instance-1.cv2us808e5ws.ap-northeast-2.rds.amazonaws.com',
        database='trip_advisor',
        user='user',
        password='qwer1234'
    )
    return conn