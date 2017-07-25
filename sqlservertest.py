import pymssql

def main():
    print('hello world')
    conn = pymssql.connect(server='LVTEST-DB', database='labvantage')
    cursor = conn.cursor()
    cursor.execute('select * from s_qcbatch')
    row = cursor.fetchone()
    while row:
        print(str(row[0]) + ' ' + str(row[1]) + ' ' + str(row[2]) + ' ' + str(row[4]))
        row = cursor.fetchone()

    print('ok')


if __name__ == "__main__": main()