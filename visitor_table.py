def create_visitor_registration():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("create table visitor_registration(serial_no int, Name varchar(30),Arrival_date date,Departure_date date,Contact_no int(15),No_of_person int,Room_no int(5))")
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Visitor Table created")

def insert_visdetail():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("insert into visitor_registration values(1,'Mr.Anant Raj','2022-02-15','2022-02-19',885648734,3,102)")
    mycur.execute("insert into visitor_registration values(2,'Mr.Shiv Varma','2022-02-12','2022-02-17',947453786,2,103)")
    mycur.execute("insert into visitor_registration values(3,'Mr.Vikram Seth','2022-02-08','2022-02-18',963619654,1,104)")
    mycur.execute("insert into visitor_registration values(4,'Mrs.Esha Singh','2022-02-13','2022-02-20',785409748,4,106)")
    mycur.execute("insert into visitor_registration values(5,'Mr.Rajendra Kaurav','2022-02-15','2022-02-22',789643674,2,108)")
    mycur.execute("insert into visitor_registration values(6,'Mrs.Nina Ahuja','2022-02-11','2022-02-19',965784537,1,109)")
    mycur.execute("insert into visitor_registration values(7,'Mr.Nandan Tripathi','2022-02-14','2022-02-18',963827842,3,111)")
    mycur.execute("insert into visitor_registration values(8,'Mr.Om Panday','2022-02-16','2022-02-23',982617648,3,113)")
    print("Visitors record inserted")
    mydb.commit()
    mycur.close()
    mydb.close()

def add_visitor_record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    serial_no=input("Enter Serial no.")
    Name=input("Enter visitor name")
    Arrival_date=input("Enter arrival date")
    Departure_date=input("Enter departure date")
    Contact_no=input("Enter contact no.")
    No_of_person=input("Enter No. of persons ")
    Room_no=input("Enter Room no")
    b=("insert into visitor_registration values(%s,%s,%s,%s,%s,%s,%s)")
    a=(serial_no,Name,Arrival_date,Departure_date,Contact_no,No_of_person,Room_no)
    mycur.execute(b,a)
    print("New record inserted successfully")
    mydb.commit()
    mycur.close()
    mydb.close()
    
def visitor_record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("select * from visitor_registration")
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close()  
    

def visitor_delrecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    Room_no=input("Enter Room_no of visitor to be deleted:--")
    a=("delete from visitor_registration where Room_no=%s")
    b=(Room_no,)
    mycur.execute(a,b)
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Record deleted successfully")

def visitor_searchrecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    Name=input("Enter Name of the visitor to be searched:-")
    a=("select * from visitor_registration where Name=%s")
    b=(Name,)
    mycur.execute(a,b)
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close() 
    print("Visitor record is found")

def visitor_updaterecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    room_no=input("enter Room_no of the visitor to be updated.....")
    print("enter new data of the visitor")
    serial_no=input("Enter Serial no.")
    Name=input("Enter visitor name")
    Arrival_date=input("Enter arrival date")
    Departure_date=input("Enter departure date")
    Contact_no=input("Enter contact no.")
    No_of_person=input("Enter No. of persons ")
    Room_no=input("Enter Room no")
    a=("update visitor_registration set serial_no=%s,Name=%s,Arrival_date=%s,Departure_date=%s,Contact_no=%s,No_of_person=%s,Room_no=%s where Room_no=%s")
    b=(serial_no,Name,Arrival_date,Departure_date,Contact_no,No_of_person,Room_no,room_no)
    mycur.execute(a,b)
    c=("select * from visitor_registration where Room_no=%s")
    d=(Name,)
    mycur.execute(c,d)
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close() 
    print("visitor record updated successfully")

