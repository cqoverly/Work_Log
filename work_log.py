# work_log.py

import os

import pyodbc

DRIVER = '{ODBC Driver 17 for SQL Server}'
SERVER = 'MSI'
DATABSE = 'Work_Log'



def get_topic_dict():
    try:
        conn = pyodbc.connect(
                                f'DRIVER={DRIVER};'
                                f'SERVER={SERVER};'
                                f'DATABASE={DATABSE};'
                                'TRUSTED_CONNECTION=yes'
        )
        
        cur = conn.cursor()
        cur.execute('SELECT * FROM topic')
        topic_dict = {}
        for t_id, t_desc in cur:
            topic_dict[t_desc] = t_id

        print('Topics collected')
        return topic_dict
    except pyodbc.DatabaseError as err:
        raise err

    return True

def add_log_entry(entry_topic, entry_text):
    sql = '''INSERT INTO work_log (topic, log_entry)
            VALUES (?, ?)'''
    try:
        conn = pyodbc.connect(
                                f'DRIVER={DRIVER};'
                                f'SERVER={SERVER};'
                                f'DATABASE={DATABSE};'
                                'TRUSTED_CONNECTION=yes'
        )
        
        cur = conn.cursor()
        cur.execute(sql,(entry_topic,entry_text))
        conn.commit()
        conn.close()

        print('Entry successfully added.')
    except pyodbc.DatabaseError as err:
        raise err

    return True

def create_entry():
    topic_dict = get_topic_dict()
    for d, i in topic_dict.items():
        print(f'{i}: {d} {type(i)}')
    topic = 0
    while int(topic) not in topic_dict.values():
        topic = input('Enter the number for the topic you would like to use: ')
    text = ''
    while not text:
        text = input('Type in your entry: ')

    add_log_entry(int(topic), text)
    return True


if __name__ == '__main__':

    create_entry()