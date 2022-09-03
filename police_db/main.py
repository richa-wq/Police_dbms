
import datetime
import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                  port='3306',
                  user='root',
                  password='System#1',
                  database='police_records')
        query = 'create table if not exists police(police_id int primary key,name varchar(200),post varchar(100),sno int, saddress varchar(200))'
        query = 'create table if not exists fir(fir_id int primary key, fdate date,v_fname varchar(200), v_lname varchar(200), vcontact varchar(12), statement varchar(200), vaddress varchar(200))'
        query = 'create table if not exists prison(prison_id int primary key,prison_name varchar(200), location varchar(200))'
        query = 'create table if not exists criminals(criminal_no int primary key, criminal_name varchar(100),dob date, address varchar(200), phone_num varchar(12), iden_mark varchar(200), prison_id int, police_id int, foreign key(prison_id) references prison(prison_id), foreign key(police_id) references police(police_id))'
        query = 'create table if not exists court(court_id int primary key, court_name varchar(100), court_address varchar(200),punishment varchar(200),criminal_no int, foreign key(criminal_no) references criminals(criminal_no))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    #insert query for police
    #def insert_police(self,police_id ,name ,post ,sno, saddress):
        #query = "insert into police(police_id ,name ,post ,sno, saddress) values({},'{}','{}',{},'{}')".format(police_id ,name ,post ,sno, saddress)
        #print(query)
        # cur = self.con.cursor()
        # cur.execute(query)
        # self.con.commit()
        # print("User saved to DB")
    
    #insert query for fir
    def insert_fir(self,fir_id,fdate,v_fname,v_lname,vcontact,statement,vaddress):
        query = "insert into fir (fir_id ,fdate ,v_fname ,v_lname ,vcontact ,statement ,vaddress) values({},{},'{}','{}','{}','{}','{}')".format(fir_id,fdate,v_fname,v_lname,vcontact,statement,vaddress)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        fdate = datetime.date(%Y,%m,%d) 
        print("User saved to DB")

#main coding
helper = DBHelper()
#helper.insert_police(7091129,'Surya','Ast. Superintendent',11,'Kumarswamy Layout')
#helper.insert_police(7091130,'Nikhil','deputy inspector',11,'Kumarswamy Layout')
#helper.insert_police(7091131,'Jaya','Superintendent',11,'Kumarswamy Layout')
#helper.insert_police(7091132,'Ankit','Constable',11,'Kumarswamy Layout')

#insert into fir database 
helper.insert_fir(112,'May','Akash','Rao','9954621542','Stole 3 lakh from my house at 9 pm','JP Nagar')