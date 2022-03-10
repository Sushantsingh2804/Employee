import sqlite3

conn = sqlite3.connect("Company.db")
getEmp = input("Enter the Employee code- ")
cursor = conn.execute("DELETE FROM EMPLOYEE WHERE EMPLOYEE_CODE="+getEmp)
conn.commit()
print("Record deleted successfully")
cursor = conn.execute("SELECT * FROM EMPLOYEE")
for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Designation-", i[2])
    print("Salary-", i[3])
    print("Company Name-", i[4])
    print("Mobile Number-", i[5])
    print("------------------------------------------------------")