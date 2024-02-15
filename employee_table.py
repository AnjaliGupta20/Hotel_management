def create_employee_registration():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("create table employee_registration(serial_no int(2), Name varchar(20),Age int(2),Date_of_Birth date,Contact_no int(15),ID_proof varchar(20))")
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Employee table created")

def insert_empdetail():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("insert into employee_registration values(1,'Raj Kumar',21,'2000-04-12',998765432,'raj953')")
    mycur.execute("insert into employee_registration values(2,'Ankit Sharma',47,'1999-03-12',998724523,'ankit03')")
    mycur.execute("insert into employee_registration values(3,'Radhika Gupta',42,'1999-03-12',998765489,'radhika73')")
    mycur.execute("insert into employee_registration values(4,'Payal Goel',50,'1999-03-12',898765432,'payal9753')")
    mycur.execute("insert into employee_registration values(5,'Diksha Sharma',39,'1999-03-12',998765232,'diksha753')")
    mycur.execute("insert into employee_registration values(6,'Aashi Rai',19,'1999-03-12',998720987,'aashi0953')")
    mycur.execute("insert into employee_registration values(7,'Dev Patel',25,'1999-03-12',998765434,'dev953')")
    mycur.execute("insert into employee_registration values(8,'Ram Kathal',35,'1999-03-12',998765215,'ram12433')")
    mycur.execute("insert into employee_registration values(9,'Rajesh Rai',33,'1999-03-12',998769754,'rajesh79753')")
    mycur.execute("insert into employee_registration values(10,'Nishi Singh',36,'1999-03-12',998567323,'nishi703')")
    print("Employee record inserted")
    mydb.commit()
    mycur.close()
    mydb.close()

def add_employee_record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    serial_no=input("Enter Serial no.")
    Name=input("Enter employees name")
    Age=input("Enter age")
    Date_of_Birth=input("Enter DOB")
    Contact_no=input("Enter contact no.")
    ID_proof=input("Enter ID. proof ")
    b=("insert into employee_registration values(%s,%s,%s,%s,%s,%s)")
    a=(serial_no,Name,Age,Date_of_Birth,Contact_no,ID_proof)
    mycur.execute(b,a)
    print("New record inserted successfully")
    mydb.commit()
    mycur.close()
    mydb.close()
def employee_login_table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("create table employee_login(S_no int(3), Employee_id varchar(15),password int)")
    mydb.commit()
    mycur.close()
    mydb.close() 
    print("Employee login table created")
def insert_emplogin():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("insert into employee_login values(1,'anant',1234)")
    mycur.execute("insert into employee_login values(2,'ram',0000)")
    mycur.execute("insert into employee_login values(3,'Radhika Gupta',5489)")
    mycur.execute("insert into employee_login values(4,'Payal Goel',5432)")
    mycur.execute("insert into employee_login values(5,'Diksha Sharma',5232)")
    mycur.execute("insert into employee_login values(6,'Aashi Rai',0987)")
    mycur.execute("insert into employee_login values(7,'Dev Patel',5434)")
    mycur.execute("insert into employee_login values(8,'Ram Kathal',5215)")
    mycur.execute("insert into employee_login values(9,'Rajesh Rai',9754)")
    mycur.execute("insert into employee_login values(10,'Nishi Singh',7323)")
    print("Employee login's record inserted")
    mydb.commit()
    mycur.close()
    mydb.close()
def Employee_Login_record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    Employee_id=input("Enter Name of new employee ")
    password=input("Create ID. Password ")
    b=("insert into employee_login values(%s,%s)")
    a=(Employee_id,password)
    mycur.execute(b,a)
    print("New record inserted successfully")
    mydb.commit()
    mycur.close()
    mydb.close()  
def Employee_login():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    Employee_id=input("Enter Employee name:  ")
    password=input("enter Employee password:  ")
    a=("select * from employee_login where Employee_id=%s and password=%s")
    b=(Employee_id,password)
    mycur.execute(a,b)
    p=mycur.fetchall()
    if len(p)==0:
        print("Not an employee")
        exit()
    else:
        print("You successfully login")
def employee_updaterecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    ID_Proof=input("enter ID_proof")
    print("enter new data of the employee")
    serial_no=input("enter new serial no.:")
    Name=input("enter employee name :")
    Age=input("enter correct age :")
    DOB=input("enter correct Date_of_birth:")
    Contact_no=input("enter correct contact_no.:  ")
    ID_proof=input("enter correct ID_Proof:  ")
    a=("update employee_registration set serial_no=%s,Name=%s,Age=%s,Date_of_Birth=%s,Contact_no=%s,ID_proof=%s where ID_proof=%s")
    b=(serial_no,Name,Age,DOB,Contact_no,ID_proof,ID_Proof)
    mycur.execute(a,b)
    A=("select * from employee_registration where Name=%s")
    B=(Name,)
    mycur.execute(A,B)
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close() 
    print("Employee's record updated successfully")
def show_employee_record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("select * from employee_registration")
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close()  
    

def employee_delrecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    Name=input("enter name of employee to be deleted:-")
    A=("delete from employee_registration where Name=%s")
    B=(Name,)
    mycur.execute(A,B)
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Employee's record deleted successfully")

def employee_searchrecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    Name=input("Enter name of the employee to be searched:-")
    A=("select * from employee_registration where Name=%s")
    B=(Name,)
    mycur.execute(A,B)
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close() 
    print("Found Employee's record")

