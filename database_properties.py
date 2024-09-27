import cx_Oracle
from jproperties import Properties

class Util():
    
    def common():
        
        configs = Properties()                                              #return a b c
        with open('database.properties', 'rb') as read_prop:                #A,B,C=common()
            configs.load(read_prop) 
            
        prop_view = configs.items() 
        #print(type(prop_view)) 
        
        for item in prop_view: 
            #print(item)
            #print(item[0], '=', item[1].data)
            
            db_url= configs.get ('DB_URL').data #DB_User,DB_PWD
            db_user=configs.get ('DB_User').data
            db_pwd=configs.get ('DB_PWD').data
            return db_url,db_user,db_pwd
                                            # print({configs.get ('DB_URL').data})
                                                #print({configs.get ('DB_User').data})
                                                #print({configs.get ('DB_PWD').data})    
        
            
    def test_a(self):
        url,user,pwd=Util.common()
        
        data=''
        
        data=f"{user}/{pwd}{url}"
        
        #print(data)
        #print('ok')
        con=cx_Oracle.connect(data)
        #print(con.version)
        cursor_data=con.cursor()
        #cursor_data.execute('select*from expense_tracker')
        #a=cursor_data.fetchall()
        #print(a)
        return cursor_data,con

obj=Util() 
obj.test_a() 

