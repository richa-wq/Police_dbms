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
        print(query)
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

    #UPDATE user details
    def update_police(self,police_id,newName,newPost,newSNo,newSAddress ):
        query ="update police set name='{}',post='{}',sno={},saddress='{}' where police_id={}".format(newName,newPost,newSNo,newSAddress)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User details updated")

#main coding
helper = DBHelper()
# helper.insert_police(7091128,'Ram','inspector',11,'kumarswamy layout')
# helper.insert_police(7091129,'Surya','Ast. Superintendent',11,'Kumarswamy Layout')
# helper.insert_police(7091130,'Nikhil','deputy inspector',11,'Kumarswamy Layout')
# helper.insert_police(7091131,'Jaya','Superintendent',11,'Kumarswamy Layout')
# helper.insert_police(,'Ankit','Constable',11,'Kumarswamy Layout')

#helper.insert_fir(112,'20-May-2021','Akash','Naik','9954621542','Stole 3 lakh from my house','JP Nagar')
#helper.insert_fir(113,'21-Mar-2022','Rahul','Shrivastav','7865231475','Murdered my wife','Jaya Nagar')
# helper.insert_fir(114,'15-Apr-2021','Anjali','Shenoy','8574263145','Kidnapped my son after school hours','Banashankari')
# helper.insert_fir(115,'07-Oct-2021','Tina','Oberoi','9578154263','Caught him smuggling for drugs','RR Nagar')
# helper.insert_fir(116,'03-Nov-2021','Nakul','Mehta','3326457895','Stole jewellery and set house on fire','Yeshwanthpur')
# helper.insert_fir(117,'10-Sept-2021','Ishaan','Khattar','4567853597','Murdered my sons','Rajajinagar')

#helper.insert_prison(15,'Bangalore Central Jail','Bangalore')
#helper.insert_prison(16,'Bangalore Central Jail','Bangalore')
# helper.insert_prison(17,'Bangalore Central Jail','Bangalore')
# helper.insert_prison(18,'Bangalore Central Jail','Bangalore')
# helper.insert_prison(19,'Bangalore Central Jail','Bangalore')

#helper.insert_criminals(1,'Ashish Kulkarni','07-05-1990','Malad, Mumbai','7070950840','Mole on right cheek',15,7091128)
# helper.insert_criminals(2,'Rohit Shet','25-09-1989','Thane, Mumbai','8521496314','Bald head',16,7091129)
# helper.insert_criminals(3,'Rhea Panday','05-09-1999','Srinagar, Jammu','8642189623','Star tattoo on neck',17,7091130)
# helper.insert_criminals(4,'Ritvik Sinha','29-09-1991','Chickpete, Bangalore','9641258630','left hand 6 fingers',18,7091131)
# helper.insert_criminals(5,'Arjun Reddy','07-08-1995','Avennue Road, Bangalore','9563254180','Stitches on right leg',19,7091132)

#helper.insert_court(101,'City Civil Court','MG Road','1 lakh fine and 5 Years of imprisonment',1)
# helper.insert_court(102,'City Civil Court','Ambedkar Road','1 Crore and 8 yrs of jail',2)
# helper.insert_court(103,'City Civil Court','Indira Nagar','Life imprisonment or death',3)
# helper.insert_court(104,'High Court','Ambedkar Road','1 yr imprisonment',4)
# helper.insert_court(105,'City Civil Court','MG Road','7 yrs of imprisonment',5)
#helper.delete_police('Ram')
#helper.fetch_all()
#helper.delete_fir(112)
#helper.delete_prison(15)
#helper.delete_criminals(1)
#helper.delete_court(101)
helper.update_police(7091129,'Ram','Ast. Superintendent',11,'KS Layout')



