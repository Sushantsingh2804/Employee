import sqlite3

conn = sqlite3.connect("Company.db")
getEmp = input("Enter the Employee code- ")

getName = input("Enter the Name-")
getDes = input("Enter the Designation-")
getSal = input("Enter the Salary-")
getComp = input("Enter the Company Name-")
getMob = input("Enter the Mobile Number-")
cursor = conn.execute("UPDATE EMPLOYEE SET NAME='"+getName+"',DESIGNATION='"+getDes+"',SALARY="+getSal+",COMPANY_NAME='"+getComp+"',MOBILE_NUMBER='"+getMob+"' WHERE EMPLOYEE_CODE="+getEmp)
conn.commit()
print("Record Updated successfully")
cursor = conn.execute("SELECT * FROM EMPLOYEE WHERE EMPLOYEE_CODE="+getEmp)
for i in cursor:
    print("id-", i[0])
    print("Name-", i[1])
    print("Designation-", i[2])
    print("Salary-", i[3])
    print("Company Name-", i[4])
    print("Mobile Number-", i[5])
    print("------------------------------------------------------")