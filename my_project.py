import sqlite3
import time
conn=sqlite3.connect("fourth.db")
c=conn.cursor()

def create_table():               #creates table if not present
    c.execute("CREATE TABLE IF NOT EXISTS hisaab(date BLOB,item TEXT,quantity INTEGER,price INTEGER,total_price INTEGER)")
    
    
                        #NAME OF TABLE IS hisaab :-)
def dynamic_data_entry():         #takes data from user at run time
        print("enter every thing in lower case for future purpose")
        dte=input("Enter Today's date: ")
        itm=input("Enter Name of Item: ")
        qnty=int(input("Enter quantity: "))
        prce=int(input("Enter Price per piece of Item: "))
        totl_price=qnty*prce
        c.execute("INSERT INTO hisaab(date,item,quantity,price,total_price) VALUES(?,?,?,?,?)",
                  (dte,itm,qnty,prce,totl_price))
        conn.commit()
        
def total_kharcha():    #to check total expenses
    c.execute("SELECT SUM(total_price) FROM hisaab")
    sum_all=c.fetchone()[0] #PROBLEM HERE (DID NOT KNOW THE PROPER FUNCTIONING OF THIS)
    print("\nTotal Kharcha till now is : ",sum_all)
    conn.commit()
        
        
def read_from_db():                #funtion to read from Database 
    c.execute('SELECT * FROM hisaab')
    data = c.fetchall()
    #print(data)
    for row in data:
        print(row)
    time.sleep(2)
    
def delete_all_db():                #delete funtion to clear whole data base
    c.execute('DELETE FROM hisaab')
    conn.commit()
    
def delete_some_db():               #delete funtion to clear particular ITEM
    del_itm=input("\nEnter Name of Item You want to delete from storage: ")
    c.execute("DELETE FROM hisaab WHERE item=?",(del_itm,)) #MOST IMPORTANT SYNTAX   
    conn.commit()
    
def entry():                        #funtion to make entry in DB multiple times as user requires    
    num=int(input("Enter number of Items you want to Enter: ")) 
    for i in range(num):
        dynamic_data_entry()

        
def main_func():                    #main function to execute other funtions        
    print("MENU")
    print("\n 1. Data Entry             (Press 1)")
    print(" 2. Check Existing Entry   (Press 2)")
    print(""" 3. Delete a Item from 
    Memory                 (Press 3)  
    (Remember everything 
    related to that Item 
    will be Deleted)""")
    print(" 4. Delete all the DATA    (Press 4)")
    print(" 5. Check Total Kharcha    (Press 5)")
    print(" 6. EXIT                   (Press 6)")
    
    ch=int(input('Choice: '))                   
    print("\n")
    if(ch==1):
        create_table()
        entry()
    elif(ch==2):
        read_from_db()
    elif(ch==3):
        delete_some_db()
    elif(ch==4):
        delete_all_db()
    elif(ch==5):
        total_kharcha()
    elif(ch==6):
        print("Thankyou!")    
        
    else:
        print("Wrong Choice Try Again!")



print("""Application made by - ANUSHIV SHUKLA
      Languages used - Python 3 and Sqlite 3
      
      Application will Run after 5 secs""")

time.sleep(5)        

main_func()

time.sleep(2)

while True:                 #to stop termination of program without asking USER
    print("\nWhat to do Now? Final Exit or Continue")
    print("\n1. Continue       (Press 1)")
    print("\n2. Final Exit     (Press 2)")

    ch2=int(input("Choice: "))

    if(ch2==1):
        main_func()
    elif(ch2==2):
        c.close()
        conn.close()
        break   
    else:
        print("Wrong Choice Try Again")
        
        
        
        