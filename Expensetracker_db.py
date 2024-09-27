import sys
import cx_Oracle
from tabulate import tabulate
import pandas as pd
import string
from tkinter import*
import tkinter.messagebox as messagebox

from database_properties import Util
def show_manu_1():
    while True:
        print('== Expense Tracker ==')
        choice = input('[1] Show Expense Details \n[2] Add Expense \n[3] Edit Expense\n[4] Delete\n[5] Exit \nYour choice: ')

        if choice == '1':
            try:
                obj=Util()
                cursor_data,con=obj.test_a() 
                cursor_data.execute('select expense_id,expense_details,cost,sum(cost) over() Total from expense_tracker')
                a=cursor_data.fetchall()
                
                pan=pd.DataFrame(a)
                firstrows=['No','Id','Desc','Cost','Total']
                print(tabulate(pan, headers = firstrows, tablefmt = 'grid'))

            except cx_Oracle.DatabaseError as e:
                print("There is a problem with Oracle", e)  

            finally:
                if cursor_data:
                   cursor_data.close()
                if con:
                   con.close()    
                 
                
            show_manu_1()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            edit_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':    
            sys.exit()
        else:
            print('Enter a correct number')

def add_expense(date,expense,cost):
    print('\n[ADD EXPENSE]')
    
    try:
        obj=Util()
        cursor_data,con=obj.test_a() 
        sql_query="insert into  expense_tracker (expense_id,expense_date,expense_details,cost) values(seq2.nextval,to_date(:name2,'DD/MM/YYYY'),:name,:name1)"
        print('sql_query::Insert::',sql_query)
        print(date,expense,cost)
        cursor_data.execute(sql_query,{'name2':date,'name':expense,'name1':cost})

        con.commit()

        #Add()
        #show_manu_1()

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)  

    finally:
       if cursor_data:
          cursor_data.close()
       if con:
          con.close()
def show_expense():
    try:
        obj=Util()
        cursor_data,con=obj.test_a() 
        sql_query="select EXPENSE_ID,to_char(EXPENSE_DATE,'DD-MM-YYYY'),EXPENSE_DETAILS,COST from expense_tracker order by 1"
        cursor_data.execute(sql_query)
        data=cursor_data.fetchall()
        print(data)
        for readdata in data:
            print(readdata[1])

        return data

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)  

    finally:
       if cursor_data:
          cursor_data.close()
       if con:
          con.close() 

def find_latest():
    try:
        obj=Util()
        cursor_data,con=obj.test_a() 
        sql_query="select EXPENSE_ID,to_char(EXPENSE_DATE,'DD-MM-YYYY'),EXPENSE_DETAILS,COST from(select *from expense_tracker order by expense_id desc) where rownum=1"
        cursor_data.execute(sql_query)
        latest=(cursor_data.fetchall())        
        return latest

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)  

    finally:
       if cursor_data:
          cursor_data.close()
       if con:
          con.close()






def edit_expense(Ex_id,Date,Details,Cost):
    print('\n[EDIT EXPENSE]')
    ch_id=Ex_id
    print(Ex_id,Date,Details,Cost)
    ch_date=Date
    ch_expense = Details
    ch_cost= Cost

    try:
      
        obj=Util()
        cursor_data,con=obj.test_a() 
        sql_q="update expense_tracker set expense_date=to_date(:n3,'DD-MM-YYYY'),expense_details=:n,cost=:n1 where expense_id=:n2"
        cursor_data.execute(sql_q,{'n3':ch_date,'n':ch_expense,'n1':ch_cost,'n2':ch_id})
        print(sql_q)
        con.commit()
       # show_manu_1()

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)  

    finally:
        if cursor_data:
            cursor_data.close()
        if con:
            con.close()   

def delete_expense(item):
    print('\n[DELETE EXPENSE]')
    de_expense_id=item
    print(item)
    #de_expense = input('what is the expense brief? ')
    #de_cost= input('how much cost you spent? ')

    try:
        obj=Util()
        cursor_data,con=obj.test_a() 
        sql_qr='delete from expense_tracker where expense_id=:id'
        cursor_data.execute(sql_qr,{'id':de_expense_id})
        con.commit()
       # show_manu_1()

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)  

    finally:
        if cursor_data:
            cursor_data.close()
        if con:
            con.close()

def total_expense(date_f,date_t):
    date_from= date_f
    date_to= date_t 
    try:
        obj=Util()
        cursor_data,con=obj.test_a()
        sql_q="select sum(cost) from expense_tracker where expense_date between to_date(:n,'DD-MM-YYYY') and to_date(:n2,'DD-MM-YYYY')"
        cursor_data.execute(sql_q,{'n':date_from,'n2':date_to})
        sum=cursor_data.fetchone()
        print(sql_q,sum)
        con.commit()
        print('expecsum===',sum[0])
        return sum[0]
       # show_manu_1()

    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)  

    finally:
        if cursor_data:
            cursor_data.close()
        if con:
            con.close()               


#show_expense()

#show_manu_1()

#total_expense()





