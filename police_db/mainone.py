from dbhelper import DBHelper

def main():
    db = DBHelper()
    while True:
        print("*********WELCOME**********")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display users")
        print("Press 3 to delete user")
        print("Press 4 to update user details")
        print("Press 5 to exit")
        print()
        try:
            choice = int(input())
            if(choice==1):
                #insert user
                police_id = int(input("Enter police I'd: "))
                name = input("Enter name: ")
                post = input("Enter post of the police: ")
                sno = input("Enter police station address: ")
                saddress = input("Enter police station address: ")
                db.insert_police(police_id,name,post,sno,saddress)
            elif choice==2:
            #displayuser
                db.fetch_all()
                pass
            elif choice==3:
                #delete user
                police_id = int(input("Enter police id which you want to delete: "))
                db.delete_police(police_id)
            elif choice==4:
                #update user
                police_id = int(input("Enter police I'd which you want to update: "))
                name = input("Enter new name: ")
                post = input("Enter new post of the police: ")
                sno = input("Enter new police station number: ")
                saddress = input("Enter new police station address: ")
                db.update_police(police_id,name,post,sno,saddress)
            elif choice==5:
                break
            else:
                print("invalid Input.... Try again")
        except Exception as e:
            print(e)
            print("Invalid Details!! Try Again!!")

if __name__ == "__mainone__":
    main()

#main coding
# helper = DBHelper()
# helper.insert_police(7091128,'Ram','inspector',11,'kumarswamy layout')
# helper.insert_police(7091129,'Surya','Ast. Superintendent',11,'Kumarswamy Layout')
# helper.insert_police(7091130,'Nikhil','deputy inspector',11,'Kumarswamy Layout')
# helper.insert_police(7091131,'Jaya','Superintendent',11,'Kumarswamy Layout')
# helper.insert_police(7091132,'Ankit','Constable',11,'Kumarswamy Layout')

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
#helper.update_police(7091130,'Ram','Ast. Superintendent',11,'KS Layout')



