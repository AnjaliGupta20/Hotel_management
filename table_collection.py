import admin_table
import employee_table
import visitor_table
import table_collection
import room_availability_table

def Admin():
        
        print("1. LOGIN FOR ADMIN ")
        print("2. EXIT")
        print("===================================================================================================================================================================")
        choice=int(input("enter choice between 1 to 2 ------:"))
        if choice==1:
                admin_table.admin_login()
                table_collection.Slide2()
        elif choice==2:
                print()
                

def employee():
        print("1. LOGIN FOR EMPLOYEE ")
        print("2. EXIT")
        print("===================================================================================================================================================================")
        choice=int(input("enter choice between 1 to 2 ------:"))
        if choice==1:
                employee_table.employee_login()
                table_collection.Slide3()
        elif choice==2:
                print()


def Slide1():
        print('''                                                        *** LOGIN TO HOTEL MANAGEMENT RECORD ***                        ''')
        print("===================================================================================================================================================================")
        print("1. LOGIN AS ADMIN")
        print("2. LOGIN AS EMPLOYEE")
        print("3. CHECK ROOM AVAILABILITY")
        print("4. Exit")
        print()
        print("===================================================================================================================================================================")
        choice=int(input("Enter your Login choice:-"))
        if choice==1:
            admin_table.admin_login()
            table_collection.Slide2()
        elif choice==2:
            employee_table.Employee_login()
            table_collection.Slide3()
        elif choice==3:
            table_collection.Slide4()
        elif choice==4:
            print("you are out of the system")                
        
            
def Slide2():
        while True:
                
                print('''                                                        *** WELCOME TO HOTEL MANAGEMENT SYSTEM ***       ''')
                print("1. FOR VISITOR INFORMATION")
                print("2. FOR EMPLOYEEE INFORMATION")
                print("3. FOR ADMIN INFORMATION")
                print("4.EXIT")
                print("===================================================================================================================================================================")
                choice=int(input("Enter choice between 1 to 4 :-"))
                if choice==1:
                        table_collection.Slide3()
                      
                elif choice==2:
                        table_collection.Slide5()
               
                elif choice==3:
                        table_collection.Slide6()
                elif choice==4:
                        break

                

def Slide3():
        while True:
                print('''                                                        *** WELCOME TO HOTEL MANAGEMENT SYSTEM ***       ''')
        
                print("1. ADD NEW VISITOR RECORD")
                print("2. DISPLAY ALL VISITOR RECORD")
                print("3. SEARCH ONE VISITOR RECORD")
                print("4. UPDATE VISITOR RECORD")
                print("5. DELETE VISITOR RECORD")
                print("6. EXIT")
                print("===================================================================================================================================================================")
                choice=int(input("enter choice between 1 to 6 ------:"))
                if choice==1:
                        visitor_table.add_visitor_record()
                      
                elif choice==2:
                        visitor_table.visitor_record()
               
                elif choice==3:
                        visitor_table.visitor_searchrecord()
                
                elif choice==4:
                        visitor_table.visitor_updaterecord()
                
                elif choice==5:
                        visitor_table.visitor_delrecord()
                elif choice==6:
                        break
                    
def Slide4():
        while True:
                print('''                                                        *** WELCOME TO HOTEL MANAGEMENT SYSTEM ***    ''')
        
                print("1. ROOM AVAILABILITY")
                print("2. EXIT")
                print("===================================================================================================================================================================")
                choice=int(input("enter choice between 1 or 2 ------:"))
                if choice==1:
                    room_availability_table.show_room()    
                elif choice==2:
                        break
def Slide5():
        while True:
                print('''                                                        *** WELCOME TO HOTEL MANAGEMENT SYSTEM ***    ''')
        
                print("1. ADD NEW EMPLOYEE RECORD")
                print("2. DISPLAY ALL EMPLOYEE RECORD")
                print("3. SEARCH ONE EMPLOYEE RECORD")
                print("4. UPDATE EMPLOYEE RECORD")
                print("5.DELETE EMPLOYEE RECORD")
                print("6.EXIT")
                print("===================================================================================================================================================================")
                choice=int(input("enter choice between 1 to 6 ------:"))
                if choice==1:
                        employee_table.add_employee_record()
                        
                elif choice==2:
                        employee_table.show_employee_record()
               
                elif choice==3:
                        employee_table.employee_searchrecord()
                
                elif choice==4:
                        employee_table.employee_updaterecord()
                
                elif choice==5:
                        employee_table.employee_delrecord()
                        
                elif choice==6:
                        break
def Slide6():
        while True:
                print('''                                                        *** WELCOME TO HOTEL MANAGEMENT SYSTEM ***    ''')
        
                print("1. ADD ADMIN ID")
                print("2. DISPLAY ALL ADMIN")
                print("3. DELETE ADMIN RECORD")
                print("4. EXIT")
                print("===================================================================================================================================================================")
                choice=int(input("enter choice between 1 to 4------:"))
                if choice==1:
                        admin_table.insert_admin()
                      
                elif choice==2:
                        admin_table.show_admin_record()
               
                elif choice==3:
                        admin_table.admin_delrecord()
                
                elif choice==4:
                        break
def information():
        admin_table.create_Admin_table()
        admin_table.insert_admlogin()
        employee_table.create_employee_registration()
        employee_table.insert_empdetail()
        employee_table.employee_login_table()
        employee_table.insert_emplogin()
        visitor_table.create_visitor_registration()
        visitor_table.insert_visdetail()
        room_availability_table.create_room_availability_table()
        room_availability_table.insert_room()
def createdatabase():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="9753")
    mycur=mydb.cursor()
    mycur.execute("create database hotel_management")
    mydb.commit()
    mycur.close()
    mydb.close()
    print("Database created")
def Optional():
    print("")
    print("1. FOR COMMERCIAL PURPOSE")
    print("2. FOR ADMINISTRATION PURPOSE")
    print("3. FOR EMPLOYEE'S USE")
    print("4. EXIT")
    print("===================================================================================================================================================================")
    choice=int(input("Enter choice between 1 to 4 :-"))
    if choice==1:
        table_collection.Slide1()
        return
    elif choice==2:
        table_collection.Admin()
        return
    elif choice==3:
        table_collection.employee()
    elif choice==4:
        print("Good Bye")
        return
        
