from ast import And
import tkinter as tk
import userManagement_oracledb as um
import EncryptDecrypt as ed


class UserLogin():
    def __init__(self,main_window):
        self.main_window=main_window
        self.main_window.title('Project2')
        self.main_window.resizable(False,False)
        self.main_window.geometry('800x600')
        self.heading_frame=tk.Frame(self.main_window,height=100,width=800,bg='chocolate2',bd=30)
        self.heading_frame.pack(side=tk.TOP,fill=tk.X) #place(x=0,y=0)
        self.heading_label=tk.Label(self.heading_frame,text='Unknown Name',font=('times',25,'bold'),bg='chocolate2')
        self.heading_label.pack(anchor=tk.CENTER) #place(x=220,y=10)
        UserLogin.login_frame(self)

    def login_frame(self):
        #create login user password frame
        self.login_frame=tk.Frame(self.main_window,height=500,width=800,relief=tk.GROOVE,bg='light green',border=15)
        self.login_frame.place(x=0,y=100)

        #add widgets frame2-Login
        self.login_lb=tk.Label(self.login_frame,text='Login',font=('times',30,'bold'),bg='light green')
        self.login_lb.place(x=330,y=20)
        self.error_lb_log=tk.Label(self.login_frame,text='',font=('times',12,'bold'),bg='light green') 
        self.error_lb_log.place(x=270,y=80)
        self.login_user_name=tk.Label(self.login_frame,text='User Name ',font=('times',20,'bold'),bg='light green')
        self.login_user_name.place(x=130,y=120)
        self.login_user_name_text=tk.Entry(self.login_frame,font=('times',20,'bold'))
        self.login_user_name_text.place(x=270,y=120)
        self.login_password=tk.Label(self.login_frame,text='Password ',font=('times',20,'bold'),bg='light green')
        self.login_password.place(x=130,y=180)
        self.login_password_text=tk.Entry(self.login_frame,show='*',font=('times',20,'bold'))
        self.login_password_text.place(x=270,y=180)
        self.login_info1=tk.Label(self.login_frame,text='If you dont have account, click here',font=('times',20,'bold'),bg='light green')
        self.login_info1.place(x=130,y=320)

         #---login frame buttons---
        self.login_submit_bt=tk.Button(self.login_frame,text='Submit',font=('times',17,'bold'),bg='green',bd=10,command=self.name_password)
        self.login_submit_bt.place(x=480,y=250)
        self.login_cancel_bt=tk.Button(self.login_frame,text='Cancel',font=('times',17,'bold'),bg='green',bd=10)
        self.login_cancel_bt.place(x=270,y=250)
        self.login_register_bt=tk.Button(self.login_frame,text='Register',font=('times',17,'bold'),bg='green',bd=10,command=self.call_register)
        self.login_register_bt.place(x=300,y=370)

    def call_register(self):
        self.main_window.destroy()
        UserRegisteration()

    def name_password(self):
        name=self.login_user_name_text.get()
        password=self.login_password_text.get()

        if name.strip()!='' and password.strip()!='':
            result=um.Userdb.get_user_name_password(name,password)
            if result is False:
                self.error_lb_log.config(text='Please give correct user_name password',fg='red',bg='white')
                return False
            else:
                self.main_window.destroy()
                success=tk.Tk()
                success.title('Loged in Successfully!!!  Congratulations')
                success.geometry('600x400')
                success_label=tk.Label(success,text='Logged in Successfully!!!  Congratulations',font=('times',50,'bold'),bg='white',fg='Green4')
                success_label.place(x=50,y=100)
                suc_exit_bt=tk.Button(success,text='EXIT',font=('times',15,'bold'),bd=8,bg='khaki4',command=success.destroy)
                suc_exit_bt.place(x=200,y=300)
                

        else:
            self.error_lb_log.config(text='Please fill all details before give submit',fg='red',bg='white')
            return False    
    

        

    
class UserRegisteration():
    def __init__(self):
        self.reg_window=tk.Tk()
        self.reg_window.geometry('470x600')
        self.reg_frame=tk.Frame(self.reg_window,height=600,width=470,relief=tk.GROOVE,bg='light green',border=15)
        self.reg_frame.place(x=0,y=0)

        #Add widgets frame -Register

        self.error_lb=tk.Label(self.reg_frame,text='',font=('times',12,'bold'),bg='light green')
        self.error_lb.place(x=10,y=100)                                                           
        self.reg_lb_info2=tk.Label(self.reg_frame,text='Rigister here ',font=('times',20,'bold'),bg='light green')
        self.reg_lb_info2.place(x=150,y=50)
        self.reg_lb_first_name=tk.Label(self.reg_frame,text='First Name ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_first_name.place(x=25,y=150)
        self.reg_lb_first_name_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),width=22)
        self.reg_lb_first_name_text.place(x=140,y=150)
        self.reg_lb_last_name=tk.Label(self.reg_frame,text='Last Name ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_last_name.place(x=25,y=190)
        self.reg_lb_last_name_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),width=22)
        self.reg_lb_last_name_text.place(x=140,y=190)
        self.reg_lb_email_id=tk.Label(self.reg_frame,text='Email Id ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_email_id.place(x=25,y=230)
        self.reg_lb_email_id_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),width=22,validatecommand=self.is_valid_email,validate='focusout')
        self.reg_lb_email_id_text.place(x=140,y=230)
        self.reg_lb_mobile_number=tk.Label(self.reg_frame,text='Mobile NO ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_mobile_number.place(x=25,y=270)
        self.reg_lb_mobile_number_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),width=22,validatecommand=self.is_valid_mobile,validate='focusout')
        self.reg_lb_mobile_number_text.place(x=140,y=270)
        self.reg_lb_user_name=tk.Label(self.reg_frame,text='User Name ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_user_name.place(x=25,y=310)
        self.reg_lb_user_name_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),width=22,validatecommand=self.is_valid_user_name,validate='focusout')
        self.reg_lb_user_name_text.place(x=140,y=310)
        self.reg_lb_password=tk.Label(self.reg_frame,text='Password ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_password.place(x=25,y=350)
        self.reg_lb_password_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),show='*',width=22,validatecommand=self.is_valid_password,validate='focusout')
        self.reg_lb_password_text.place(x=140,y=350)
        self.reg_lb_repassword=tk.Label(self.reg_frame,text='Re-Password ',font=('times',15,'bold'),bg='light green')
        self.reg_lb_repassword.place(x=25,y=390)
        self.reg_lb_repassword_text=tk.Entry(self.reg_frame,font=('times',15,'bold'),show='*',width=22,validatecommand=self.is_valid_repassword,validate='focusout')
        self.reg_lb_repassword_text.place(x=140,y=390)
        #---Buttons for register frame---
        self.reg_submit_bt=tk.Button(self.reg_frame,text='Submit',font=('times',15,'bold'),bg='green',bd=10,command=self.submit_action)
        self.reg_submit_bt.place(x=290,y=430)
        self.reg_clear_bt=tk.Button(self.reg_frame,text='Clear All',font=('times',15,'bold'),bg='green',bd=10,command=self.clear)
        self.reg_clear_bt.place(x=130,y=430)
        self.reg_cancel_bt=tk.Button(self.reg_frame,text='Cancel',font=('times',15,'bold'),bg='green',bd=10,command=self.reg_window.quit)
        self.reg_cancel_bt.place(x=290,y=505)

    def call_main(self):
        self.reg_window.destroy()
        main()  

    def get_data_reg(self):
        pass
        

    def is_valid_email(self):
        email_id=self.reg_lb_email_id_text.get()
        if not '@' in email_id:  
            self.error_lb.config(text='email id must contain @',fg='red',bg='white')
            return False
        elif  not um.Userdb.is_unique_email_id(email_id):
            self.error_lb.config(text='This email id is already used',fg='red',bg='white')
            return False

        else:
            self.error_lb.config(text='',fg='light green',bg='light green')
            return True 
        
    def is_valid_mobile(self):
        mobile_id=int(self.reg_lb_mobile_number_text.get())
        if not self.reg_lb_mobile_number_text.get().isdigit():
            self.error_lb.config(text='Mobile number must contain only digits',fg='red',bg='white')
            return False 
        elif not len(self.reg_lb_mobile_number_text.get())==10:
            self.error_lb.config(text='Mobile number must contain 10 digits',fg='red',bg='white')
            return False 
        elif not um.Userdb.is_unique_mobile_id(mobile_id):
            self.error_lb.config(text='This mobile number is already used',fg='red',bg='white')
            return False
        else:
            self.error_lb.config(text='',fg='light green',bg='light green')
            return True 
    def is_valid_user_name(self):
        user_name=self.reg_lb_user_name_text.get()
        
        if not len(self.reg_lb_user_name_text.get())>=8:  
            self.error_lb.config(text='user name at least contain 8 letters',fg='red',bg='white')
            return False
        elif not um.Userdb.is_unique_user_name(user_name):
            self.error_lb.config(text='This user name is already used',fg='red',bg='white')
            return False
        else:
            self.error_lb.config(text='',fg='light green',bg='light green')
            return True  
    def is_valid_password(self):
        
        if (len(self.reg_lb_password_text.get())<=8 and  not (self.reg_lb_password_text.get().isalnum())):
                
            #and  ('@' or '!' or '$' or '#' or '&' or '*' or '%' or '^' in (self.reg_lb_password_text.get()))):  
            self.error_lb.config(text='Password at least contains 8 charaters \nwith digits,letters and special characters{!@#$%^&*}',fg='red',bg='white')
            
            return False
        else:
            self.error_lb.config(text='',fg='light green',bg='light green')
            return True 

    def is_valid_repassword(self):
        
        if not self.reg_lb_repassword_text.get()==self.reg_lb_password_text.get():
            self.error_lb.config(text='Please make sure give same password',fg='red',bg='white')
            return False
        else:
            self.error_lb.config(text='',fg='light green',bg='light green')
            return True  

    def submit_action(self):
        
        print('MMMMMM:::',self.error_lb.cget('text'))
        first_name= self.reg_lb_first_name_text.get() 
        last_name=self.reg_lb_last_name_text.get() 
        email_id=self.reg_lb_email_id_text.get()  
        mobile_id=self.reg_lb_mobile_number_text.get() 
        user_name=self.reg_lb_user_name_text.get() 
        user_password=self.reg_lb_password_text.get()

        encpassword=ed.encrypt(user_password)
        if not (first_name.strip()!='' and last_name != '' and email_id!= '' and mobile_id!='' and user_name!= '' and encpassword!=''):
            self.error_lb.config(text='Please fill all the details before submit',fg='red',bg='white')
        
            
        
        elif not self.error_lb.cget('text') =='':
            self.error_lb.config(text='Please correct all error before submit',fg='red',bg='white')
            return False
        else:
            db=um.Userdb(first_name,last_name,email_id,mobile_id,user_name,encpassword)
            try:
                db.get_insert()
            except Exception as e:
                 print('Exception while insert data::',e)
                 self.error_lb.config(text='Technical issue, Please try after sometime!!',fg='red',bg='white')
                 return False  
            self.error_lb.config(text='Registered Successfully!!',fg='red',bg='white')
            self.reg_window.destroy()
            main()
            return True
    def clear(self):
        self.reg_lb_first_name_text.delete(0,tk.END)
        self.reg_lb_last_name_text.delete(0,tk.END)
        self.reg_lb_email_id_text.delete(0,tk.END)
        self.reg_lb_mobile_number_text.delete(0,tk.END)
        self.reg_lb_user_name_text.delete(0,tk.END)
        self.reg_lb_repassword_text.delete(0,tk.END)
        self.reg_lb_repassword_text.delete(0,tk.END)

    







def main():
    root=tk.Tk()
    userlog=UserLogin(root)

    root.mainloop()
    

if __name__=='__main__':
     main()