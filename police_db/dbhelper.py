import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                  port='3306',
                  user='root',
                  password='System#1',
                  database='police_records')
        query = 'create table if not exists police(police_id int primary key,name varchar(200),post varchar(100),sno int, saddress varchar(200))'
        query = 'create table if not exists fir(fir_id int primary key, fdate varchar(50),v_fname varchar(200), v_lname varchar(200), vcontact varchar(12), statement varchar(200), vaddress varchar(200))'
        query = 'create table if not exists prison(prison_id int primary key,prison_name varchar(200), location varchar(200))'
        query = 'create table if not exists criminals(criminal_no int primary key, criminal_name varchar(100),dob varchar(100), address varchar(200), phone_num varchar(12), iden_mark varchar(200), prison_id int, police_id int, foreign key(prison_id) references prison(prison_id), foreign key(police_id) references police(police_id))'
        query = 'create table if not exists court(court_id int primary key, court_name varchar(100), court_address varchar(200),punishment varchar(200),criminal_no int, foreign key(criminal_no) references criminals(criminal_no))'
        cur = self.con.cursor()
        cur.execute(query)
        #print("Created")

    #insert query for police
    def insert_police(self,police_id ,name ,post ,sno, saddress):
        query = "insert into police(police_id ,name ,post ,sno, saddress) values({},'{}','{}',{},'{}')".format(police_id ,name ,post ,sno, saddress)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")
    
    #insert query for fir
    def insert_fir(self,fir_id,fdate,v_fname,v_lname,vcontact,statement,vaddress):
        query = "insert into fir (fir_id ,fdate ,v_fname ,v_lname ,vcontact ,statement ,vaddress) values({},'{}','{}','{}','{}','{}','{}')".format(fir_id,fdate,v_fname,v_lname,vcontact,statement,vaddress)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")
    
    #insert query for prison
    def insert_prison(self, prison_id ,prison_name , location):
        query = "insert into prison(prison_id ,prison_name , location) values ({},'{}','{}')".format(prison_id ,prison_name , location)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")

    #insert query for criminals
    def insert_criminals(self,criminal_no , criminal_name ,dob ,address ,phone_num ,iden_mark ,prison_id , police_id):
        query = "insert into criminals(criminal_no , criminal_name ,dob ,address ,phone_num ,iden_mark ,prison_id , police_id) values ({},'{}','{}','{}','{}','{}',{},{})".format(criminal_no , criminal_name ,dob ,address ,phone_num ,iden_mark ,prison_id , police_id)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")

    #insert query for court
    def insert_court(self, court_id , court_name , court_address ,punishment ,criminal_no):
        query = "insert into court(court_id , court_name , court_address ,punishment ,criminal_no) values ({},'{}','{}','{}',{})".format (court_id , court_name , court_address ,punishment ,criminal_no)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User saved to DB")

    #Fetch all
    def fetch_all(self):
        query = "select * from police"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Police Id : ",row[0])
            print("Name : ",row[1])
            print("Post : ",row[2])
            print("Station No. : ",row[3])
            print("Station Address : ",row[4])
            print()
            print()

    def fetch_all(self):
        query = "select * from fir"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("FIR Id : ",row[0])
            print("FIR date : ",row[1])
            print("Victim Name : ",row[2])
            print("Last Name : ",row[3])
            print("Victim's Contact : ",row[4])
            print("Statement : ",row[5])
            print("Victim's Address : ",row[6])
            print()
            print()

    def fetch_all(self):
        query = "select * from prison"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Prison Id : ",row[0])
            print("Prison Name : ",row[1])
            print("Location : ",row[2])
            print()
            print()

    def fetch_all(self):
        query = "select * from criminals"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Criminal Number : ",row[0])
            print("Criminal Name : ",row[1])
            print("DOB : ",row[2])
            print("Address : ",row[3])
            print("Phone Numer : ",row[4])
            print("Identification Mark : ",row[5])
            print("Prison Id : ",row[6])
            print("Police Id : ",row[7])
            print()
            print()

    def fetch_all(self):
        query = "select * from court"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Court Id : ",row[0])
            print("Court Name : ",row[1])
            print("Court Addresss  : ",row[2])
            print("Punishment : ",row[3])
            print("Criminal No. : ",row[4])
            print()
            print()

    #delete police tuples
    def delete_police(self, name):
        query = "delete from police where name = '{}'".format(name)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        print("User Deleted")
    
    #DELETE FIR tuples
    def delete_fir(self, fir_id):
        query = "delete from fir where fir_id = {}".format(fir_id)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("User Deleted")

    #DELETE prison tuples
    def delete_prison(self, prison_id):
        query = "delete from prison where prison_id = {}".format(prison_id)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("User Deleted")

    #DELETE criminals tuples
    def delete_criminals(self, criminal_no):
        query = "delete from criminals where criminal_no = {}".format(criminal_no)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("User Deleted")

     #DELETE court tuples
    def delete_court(self, court_id):
        query = "delete from court where court_id = {}".format(court_id)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("User Deleted")


    #UPDATE police details
    def update_police(self,police_id,newName,newPost,newSNo,newSAddress ):
        query ="update police set name='{}',post='{}',sno={},saddress='{}' where police_id={}".format(newName,newPost,newSNo,newSAddress,police_id)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User details updated")

    #update fir details
    def update_fir(self,newDate,newFname,newLname,newContact,newStatement,newAddress,fir_id):
        query = "update fir set fdate ='{}',v_fname='{}',v_lname='{}',vcontact='{}',statement='{}',vaddress='{}' where fir_id = '{}'".format(newDate,newFname,newLname,newContact,newStatement,newAddress,fir_id)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User details updated")
    
    #update prison details
    def update_prison(self,newprison_name , newlocation,prison_id):
        query = "update prison set prison_name='{}',location = '{}' where prison_id={}".format(newprison_name,newlocation,prison_id)
        print(query)
        cur = self.con.cursor()
        cur.execute.commit()
        print("User details updated")
    
    #update criminal details
    def update_criminals(self,newCname ,newDob ,newAddress ,newPhone_num ,newIden_mark,criminal_num):
        query = "update criminals set criminal_name='{}',dob='{}',address='{}',phone_num='{}',iden_mark='{}' where criminal_num ={}".format(newCname ,newDob ,newAddress ,newPhone_num ,newIden_mark,criminal_num)
        print(query)
        cur = self.con.cursor()
        cur.execute.commit()
        print("User details updated")

    #update court details
    def update_court(self,newCourtName , newCourtAdd ,newPunishment,court_id ):
        query = "update court set court_name = '{}',court_address='{}',punishment='{}' where court_id={}".format(newCourtName , newCourtAdd ,newPunishment,court_id )
        print(query)
        cur = self.con.cursor()
        cur.execute.commit()
        print("User details updated")

