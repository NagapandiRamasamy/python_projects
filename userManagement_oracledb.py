import cx_Oracle
from database_properties import Util
import tkinter.messagebox as messagebox
import EncryptDecrypt as ed

class Userdb():
    def __init__(self,user_first_name,user_last_name,user_email_id,user_mobile_id,user_name,user_password):
        self.user_first_name=user_first_name
        self.user_last_name=user_last_name
        self.user_email_id=user_email_id
        self.user_mobile_id=user_mobile_id
        self.user_name=user_name
        self.user_password=user_password
   
    
    def get_insert(self):
            uf=self.user_first_name
            ul=self.user_last_name
            ue=self.user_email_id
            um=self.user_mobile_id
            un=self.user_name
            up=self.user_password
            print('THIS MY PRINT::',uf,ul,ue,um,un,up,)

            try:
                obj=Util()
                cursor_data,con=obj.test_a() 
                sql_query="insert into user_management (user_id,user_first_name,user_last_name,user_email_id,user_mobile_id,user_name,user_password) values(umseq.nextval,:uf,:ul,:ue,:um,:un,:up)"
                                      
                print('sql_query::Insert::',sql_query)
                #print(user_id,user_first_name,user_last_name,user-email_id,user_mobile_id,user_name,user_password)
                cursor_data.execute(sql_query,{'uf':uf,'ul':ul,'ue':ue,'um':int(um),'un':un,'up':up})
                print('Error')
                con.commit()

                #Add()
                #show_manu_1()

            except cx_Oracle.Error as e:
                print("There is a problem with Oracle",e)
                raise e
            except:
                print("There is a problem with Oracle")
                raise Exception


            finally:
                if cursor_data:
                    cursor_data.close()
                if con:
                    con.close()
    
    def is_unique_email_id(user_email_id):
        try:
            obj=Util()
            cursor_data,con=obj.test_a()
            #email=user_email_id
            sql_q=('select user_email_id from user_management where user_email_id=:n')
            a=cursor_data.execute(sql_q,{'n':user_email_id})
            a=cursor_data.fetchone()
            if a is not None:
                return False
            else:
                return True

            
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)  

        finally:
            if cursor_data:
                cursor_data.close()
            if con:
                con.close() 
    def is_unique_mobile_id(mobile_id):
        try:
            obj=Util()
            cursor_data,con=obj.test_a()
            print("mobile",type(mobile_id))
            sql_q=("select user_mobile_id from user_management where user_mobile_id=:n1")
            print("Mobile_unique",sql_q,mobile_id)
            b=cursor_data.execute(sql_q,{'n1':mobile_id})
            b=cursor_data.fetchone()
            if b is not None:
                return False
            else:
                return True

            
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)  

        finally:
            if cursor_data:
                cursor_data.close()
            if con:
                con.close() 

    def is_unique_user_name(user_name):
        try:
            obj=Util()
            cursor_data,con=obj.test_a()
            
            sql_q=("select user_name from user_management where user_name=:n3")
            c=cursor_data.execute(sql_q,{'n3':user_name})
            c=cursor_data.fetchone()
            print('THIS MY OUT ::',c)
            if c is not None:
                return False
            else:
                return True
                            
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)  

        finally:
            if cursor_data:
                cursor_data.close()
            if con:
                con.close()

   


    def get_user_name_password(name,password):
        try:
            obj=Util()
            cursor_data,con=obj.test_a()
            
            sql_q=("select user_password from user_management where user_name=:n3")
            e=cursor_data.execute(sql_q,{'n3':name})
            e=cursor_data.fetchone()
            print('This my decode:::--',e[0])           
            decpassword=ed.decrypt(e[0])
            if password!=decpassword:
                return False
            else:
                return True

            
        except cx_Oracle.DatabaseError as e:
            print("There is a problem with Oracle", e)  

        finally:
            if cursor_data:
                cursor_data.close()
            if con:
                con.close()   

    
                                                          

    
