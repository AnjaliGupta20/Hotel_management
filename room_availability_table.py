def create_room_availability_table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("create table Room_Availability(Room_no int,Room_Type varchar(20),Bed_Type varchar(10),Room_Rate int(10),Included_Breakfast varchar(5))")
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Room Availability table created")

def insert_room():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("insert into Room_Availability values(101,'NON-AC','SINGLE',2000,'NO')")
    mycur.execute("insert into Room_Availability values(105,'AC','DOUBLE',4500,'YES')")              
    mycur.execute("insert into Room_Availability values(107,'AC','DOUBLE',10000,'YES')")
    mycur.execute("insert into Room_Availability values(110,'NON-AC','SINGLE',1500,'NO')")
    mycur.execute("insert into Room_Availability values(115,'NON-AC','DOUBLE',3000,'YES')")
    mycur.execute("insert into Room_Availability values(117,'NON-AC','SINGLE',3500,'NO')")
    mycur.execute("insert into Room_Availability values(120,'AC','TRIPLE',15000,'NO')")
    mycur.execute("insert into Room_Availability values(125,'AC','DOUBLE',2500,'YES')")
    mycur.execute("insert into Room_Availability values(128,'NON-AC','DOUBLE',4000,'YES')")
    mycur.execute("insert into Room_Availability values(130,'AC','TRIPLE',20000,'YES')")            
    print("Room Availability record inserted")
    mydb.commit()
    mycur.close()
    mydb.close()

def show_room():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753",database="hotel_management")
    mycur=mydb.cursor()
    mycur.execute("select * from Room_Availability")
    record=mycur.fetchall()
    for x in record:
        print(x)
    mydb.commit()
    mycur.close()
    mydb.close()  

