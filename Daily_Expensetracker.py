from tkinter import*
import tkinter.ttk as ttk
import oracledb
import tkinter.messagebox as messagebox
import python_projects.Expensetracker_db as bk
from tkcalendar import DateEntry
import sys



class Main():
    
    #Ex_id=bk.cal_expense_id()
    def __init__(self,root):
        self.root=root
        self.frame1=Frame(root,height=600,width=400,relief=GROOVE,bg='light green',border=2)
        self.frame1.pack(side=LEFT)
        self.lb1=Label(self.frame1,text='MENU',font=('times',15,'bold'),bg='light green')
        self.lb1.place(x=180,y=10)
        self.frame1.pack_propagate(0)

                 #-----------------label and entry-------------
        self.Date=Label(self.frame1,text='Date',font=('times',15,'bold'),bg='light green')
        self.Date.place(x=20,y=50)      
        self.Date_field=DateEntry(self.frame1,date_pattern='dd-mm-yyyy',font=('times',15,'bold'),width=23)
        self.Date_field.place(x=120,y=50)
        self.Details=Label(self.frame1,text='Details',font=('times',15,'bold'),bg='light green')
        self.Details.place(x=20,y=80)      
        self.Details_field=Entry(self.frame1,font=('times',15,'bold'),width=25)
        self.Details_field.place(x=120,y=80)
        self.Cost=Label(self.frame1,text='Cost',font=('times',15,'bold'),bg='light green')
        self.Cost.place(x=20,y=110)      
        self.Cost_field=Entry(self.frame1,font=('times',15,'bold'),width=25)
        self.Cost_field.place(x=120,y=110)
        self.Total=Label(self.frame1,text='Total Expense',font=('times',15,'bold'),bg='light green')
        self.Total.place(x=20,y=140)
        self.Total=Label(self.frame1,text='From',font=('times',15,'bold'),bg='light green')
        self.Total.place(x=100,y=170)
        self.Total_field=DateEntry(self.frame1,date_pattern='dd-mm-yyyy',font=('times',15,'bold'),width=18)
        self.Total_field.place(x=162,y=170)
        self.Total_to=Label(self.frame1,text='To',font=('times',15,'bold'),bg='light green')
        self.Total_to.place(x=130,y=200)
        self.Total_to_field=DateEntry(self.frame1,date_pattern='dd-mm-yyyy',font=('times',15,'bold'),width=18)
        self.Total_to_field.place(x=162,y=200)
        
            #------------------Buttons--------------
            
        
        self.Add=Button(self.frame1,text='Add',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=self.Add)
        self.Add.place(x=60,y=290)
        self.Select=Button(self.frame1,text='View Selected',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=self.Select)
        self.Select.place(x=60,y=330)
        self.Update=Button(self.frame1,text='Update',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=self.Update)
        self.Update.place(x=60,y=370)
        self.Delete=Button(self.frame1,text='Delete',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=self.Delete)
        self.Delete.place(x=60,y=410)
        self.Total_bt=Button(self.frame1,text='Total',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=self.Total_cost)
        self.Total_bt.place(x=60,y=450)
        self.Clear=Button(self.frame1,text='Clear',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=self.Clear)
        self.Clear.place(x=60,y=490)
        self.Exit=Button(self.frame1,text='Exit',font=('times',15,'bold'),width=20,bg='green2',bd=4,command=root.quit)
        self.Exit.place(x=60,y=530)

        #_----------show data--------
        
        self.table=Frame(root,height=650,width=400,relief=GROOVE,bd=30,bg='white')
        self.table.pack(side=RIGHT)
        self.sc=ttk.Scrollbar(self.table,orient=VERTICAL)
        self.sc.pack(side=RIGHT,fill=Y)
        Main.Show_tree_view(self)
    def Show_tree_view(self):     
        self.tree=ttk.Treeview(self.table,columns=('c1','c2','c3','c4','c5'),show='headings',height=25)
        self.tree.column('#1',anchor=CENTER,width=60)
        self.tree.heading('#1',text='Ex_id')
        self.tree.column('#2',anchor=CENTER,width=120)
        self.tree.heading('#2',text='Date')
        self.tree.column('#3',anchor=CENTER,width=320)
        self.tree.heading('#3',text='Details')
        self.tree.column('#4',anchor=CENTER,width=120)
        self.tree.heading('#4',text='Cost')
        self.tree.column('#5',anchor=CENTER,width=120)
        self.tree.heading('#5',text='Total')
        data1=bk.show_expense()
        for readdata in data1:
            self.tree.insert('',index=END,values=(readdata[0],readdata[1],readdata[2],readdata[3]))
        self.tree.pack()
    


    def Add(self):
        if self.Date_field.get()!=''and self.Details_field.get() !='' and self.Cost_field.get() !='':
            #Ex_id=self.Ex_id_field.get()
            Date=self.Date_field.get()
            Details=self.Details_field.get() 
            Cost=self.Cost_field.get()
            bk.add_expense(Date,Details,Cost)
            latest=bk.find_latest()
            for a in latest:
                self.tree.insert('',index=END,values=(a[0],a[1],a[2],a[3]))
  
            
            
            #Ex_id+=1
            #self.Ex_id_field.delete(0,END)
            self.Date_field.delete(0,END)
            self.Details_field.delete(0,END)
            self.Cost_field.delete(0,END)

            
        else:
            messagebox.showinfo('message','please fill all field')
    def Select(self):
        #self.Ex_id_field.delete(0,END)
        self.Date_field.delete(0,END)
        self.Details_field.delete(0,END)
        self.Cost_field.delete(0,END)
        selected=self.tree.focus()
        values=self.tree.item(selected,'values')
        #messagebox.showinfo('Message',values[0])
        #self.Ex_id_field.insert(0,values[0])
        self.Date_field.insert(0,values[1])
        self.Details_field.insert(0,values[2])
        self.Cost_field.insert(0,values[3])


    


    def Delete(self):
        self.Date_field.delete(0,END)  
        self.Details_field.delete(0,END)  
        self.Cost_field.delete(0,END) 
        selected=self.tree.focus()
        values=self.tree.item(selected,'values') 
        print(values[0])    

        item=self.tree.selection()
        print(item)
        del_item=self.tree.delete(item)
        bk.delete_expense(values[0]) 

    def Update(self):

        selected=self.tree.focus()
        values=self.tree.item(selected,'values') 
        #print(values[0])
        Ex_id=values[0]
        
        Date=self.Date_field.get()
        Details=self.Details_field.get()
        Cost=self.Cost_field.get()
        item=self.tree.selection()[0]
        print("Total : ",Ex_id,Date,Details,Cost)
        self.tree.item(item,values=(values[0],Date,Details,Cost))
        bk.edit_expense(Ex_id,Date,Details,Cost)
        self.Date_field.delete(0,END)  
        self.Details_field.delete(0,END)  
        self.Cost_field.delete(0,END)

    def Clear(self):
        #self.Ex_id_field.delete(0,END)
        self.Date_field.delete(0,END)  
        self.Details_field.delete(0,END)  
        self.Cost_field.delete(0,END) 
        self.Total_field.delete(0,END)
        self.Total_to_field.delete(0,END)
        self.Total_exp.place_forget() 
        self.Total_exp1.place_forget() 

 



    def Total_cost(self):
        date_f=self.Total_field.get() 
        date_t=self.Total_to_field.get()
        sum=bk.total_expense(date_f,date_t)
        
        self.Show_total(sum)
        

    def Show_total(self,sum):
        print('i got:',sum)
        self.Total_exp=Label(self.frame1,text='TOTAL Expense =',font=('times',15,'bold'),bg='light green')
        self.Total_exp.place(x=20,y=240)
        self.Total_exp1=Label(self.frame1,text=sum,font=('times',15,'bold'),bg='light green',fg='red')
        self.Total_exp1.place(x=190,y=240)
        

               

     



root=Tk()
root.title('EXPENSE TRACKER')
root.resizable(False,False)
root.geometry('1200x650')
frame=Frame(root,height=70,width=1200,bg='green3',relief=GROOVE,border=8)
frame.pack()
lb=Label(frame,text='EXPENSE TRACKER',width=1200,font="arial 24 bold",bg='green3')
lb.pack()

tracker=Main(root)
root.mainloop()
