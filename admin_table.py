def create_Admin_table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("create table admin_login(s_no int(3), admin_id varchar(15),password int(6))")
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Admin table created")
def insert_admlogin():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("insert into admin_login values(1, 'saurav',1111)")
    mycur.execute("insert into admin_login values(2, 'anjali',2222)")
    print("Admin record inserted")
    mydb.commit()
    mycur.close()
    mydb.close()
def insert_admin():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    admin_id=input("enter admin id.   ")
    password=input("enter admin password    ")
    qry=("insert into admin_login values(%s,%s)")
    data=(admin_id,password)
    mycur.execute(qry,data)
    print("Admin's record inserted succssfully")
    mydb.commit()
    mycur.close()
    mydb.close()
def admin_login():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    admin_id=input("Enter your Admin Id:-  ")
    password=input("Enter your password:-  ")
    a=("select s_no from admin_login where admin_id=%s and password=%s")
    b=(admin_id,password)
    mycur.execute(a,b)
    p=mycur.fetchall()
    if len(p)==0:
        print("Not an Admin")
        exit()
    else:
        print("Entered succesfully")
def show_admin_record():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("select * from admin_login")
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close()  
def admin_delrecord():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    admin_id=input("Enter admin id to be deleted:-")
    A=("delete from admin_login where admin_id=%s")
    B=(admin_id,)
    mycur.execute(A,B)
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Record deleted successfully")
    if p is None:
        print("Not an Admin")
    else:
        print("Entered succesfully")
