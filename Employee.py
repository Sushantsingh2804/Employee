import sqlite3

conn = sqlite3.connect("Company.db")
conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE (
                    EMPLOYEE_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT,
                    DESIGNATION TEXT,
                    SALARY INTEGER,
                    COMPANY_NAME TEXT,
                    MOBILE_NUMBER TEXT);
    ''')

print(" Table Creation Successful ")

getName = input("Enter the Name-")
getDes = input("Enter the Designation-")
getSal = input("Enter the Salary-")
getComp = input("Enter the Company Name-")
getMob = input("Enter the Mobile Number-")

conn.execute("INSERT INTO EMPLOYEE (NAME,DESIGNATION,SALARY,COMPANY_NAME,MOBILE_NUMBER) VALUES('"+getName+"','"+getDes+"',"+getSal+",'"+getComp+"','"+getMob+"')")
conn.commit()
conn.close()
print("Entry successful")