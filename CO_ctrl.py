from Plantdb import*
import random
import math
import pyfiglet 

class Head:
    def Display(self,quote): 
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("                                       WELCOME TO VEDANTABHI NURSERY                                                           ")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("                                                   QUOTE                                                                           ")
        print(quote)
        print("                             ----------------------------------------------------                                                     ")
        print("WE CARE")
        print("-------------")

class Controls(Head):
    def Con(self):
        user=input("Select User\nStaff/Customer:").capitalize()
        if user=="Staff":
            showdb=input("Show Plant database\nYes/No:").capitalize()
            if showdb=="Yes":
                show=conn.execute("SELECT * from PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")
    
            showudb=input("Show Customer database\nYes/No:").capitalize()
            if showudb=="Yes":
                show=conn.execute("SELECT * from USERINFO")
                for row in show:
                    PHONE_NUMBER,NAME=row
                    print(f"PHONE NUMBER={PHONE_NUMBER} ,NAME={NAME}\n")

            add=input("Do you want to add plant data in database\nYes/No:").capitalize()
            if add=="Yes":
                a=int(input("Enter Id:"))
                b=input("Enter plant name:").capitalize()
                c=int(input("Enter quantity:"))
                d=float(input("Enter price:"))
                conn.execute(f"INSERT INTO PLANTINFO (ID,PLANT_NAME,QUANTITY,PRICE) \
                VALUES ({a}, '{b}', {c}, {d})")
                conn.commit()
                show=conn.execute("SELECT * from PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")

            remove=input("Do you want to remove plant from database?\nYes/No:").capitalize()
            if remove=="Yes":
                EnterId=int(input("Enter Id of plant:"))
                removes=conn.execute(f"DELETE FROM PLANTINFO WHERE ID = {EnterId}")
                show=conn.execute("SELECT * from PLANTINFO")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")

            update=input("Do you want to update plant quantity?\nYes/No:").capitalize()
            if update=="Yes":
                uid=int(input("Enter Id of plant you want to update:"))
                uquantity=int(input("Enter the new quantity:"))
                conn.execute(f"UPDATE PLANTINFO set Quantity = {uquantity} WHERE ID = {uid}")
                conn.commit()
                show=conn.execute(f"SELECT ID, PLANT_NAME, Quantity, PRICE FROM PLANTINFO WHERE ID ={uid}")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")
           
            updatep=input("Do you want to update price of plant?\nYes/No:").capitalize()
            if updatep=="Yes":
                uid=int(input("Enter Id of plant you want to update:"))
                uprice=float(input("Enter the new price:"))
                conn.execute(f"UPDATE PLANTINFO set PRICE= {uprice} WHERE ID = {uid}")
                conn.commit()
                show=conn.execute(f"SELECT ID, PLANT_NAME, Quantity, PRICE FROM PLANTINFO WHERE ID ={uid}")
                for row in show:
                    ID,PLANT_NAME,QUANTITY,PRICE=row
                    print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY}, price= ₹{PRICE}\n")
           


        if user=="Customer":
                ephone=int(input("Enter Number:"))
                cur=conn.execute(f"SELECT PHONE_NUMBER FROM USERINFO WHERE PHONE_NUMBER= {ephone}")
                row=cur.fetchone()
                if row != None:
                    showdb=input("Show Plant database\nYes/No:").capitalize()
                    if showdb=="Yes":
                        show=conn.execute("SELECT * from PLANTINFO")
                        for row in show:
                            ID,PLANT_NAME,QUANTITY,PRICE=row
                            print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY},price= ₹{PRICE}\n")

                    purchase = input("Do you want to purchase\nYes/No:").capitalize()
                    if purchase == "Yes":
                        Total_bill=0
                        n=int(input("Enter the number of plant you want:"))
                        for val in range(0,n):
                            plant_id = int(input("Enter the Plant Id:"))
                            quantity = int(input("Enter the Quantity:"))
                            cursor = conn.execute(f"SELECT quantity from PLANTINFO where id={plant_id}")
                            price = conn.execute(f"SELECT PRICE FROM PLANTINFO WHERE ID = {plant_id}")
                            for row in price:
                                ip=row[0]
                                Total_bill+=ip*float(quantity)
                            for row in cursor:
                                a = row[0]
                                remaining_quant = a-quantity
                                conn.execute(f"UPDATE PLANTINFO set QUANTITY = {remaining_quant} where id = {plant_id}")
                                conn.commit()
                        print(f"Original bill is ₹{Total_bill}")
                        discount=Total_bill*0.05
                        Finalprice=Total_bill-discount
                        print("Congratulations You Recived 5% Discount On Your Bill")
                        print(f"Discounted bill Is ₹{math.ceil(Finalprice)}")
                        result = pyfiglet.figlet_format("Thankyou For Shopping", font = "digital" )
                        print(result)
                else:
                    cname=input("Enter Your Name:")
                    cphone=int(input("Enter Phone Number:"))
                    conn.execute(f"INSERT INTO USERINFO (PHONE_NUMBER,NAME) \
                    VALUES ({cphone}, '{cname}')")
                    conn.commit()
                    showdb=input("Show Plant database\nYes/No:").capitalize()
                    if showdb=="Yes":
                        show=conn.execute("SELECT * from PLANTINFO")
                        for row in show:
                            ID,PLANT_NAME,QUANTITY,PRICE=row
                            print(f"ID= {ID}, Plant= {PLANT_NAME}, Quantity= {QUANTITY},price= ₹{PRICE}\n")

                    purchase = input("Do you want to purchase\nYes/No:").capitalize()
                    if purchase == "Yes":
                        Total_bill=0
                        n=int(input("Enter the number of plant you want:"))
                        for val in range(0,n):
                            plant_id = int(input("Enter the Plant Id:"))
                            quantity = int(input("Enter the Quantity:"))
                            cursor = conn.execute(f"SELECT quantity from PLANTINFO where id={plant_id}")
                            price = conn.execute(f"SELECT PRICE FROM PLANTINFO WHERE ID = {plant_id}")
                            for row in price:
                                ip=row[0]
                                Total_bill+=ip*float(quantity)
                            for row in cursor:
                                a = row[0]
                                remaining_quant = a-quantity
                                conn.execute(f"UPDATE PLANTINFO set QUANTITY = {remaining_quant} where id = {plant_id}")
                                conn.commit()
                        print(f"Total bill is ₹{Total_bill}")
                        result = pyfiglet.figlet_format("Thankyou For Shopping", font = "digital" )
                        print(result)

class In:
    Quote=("A beautiful plant is like having a friend around the house.\n-Beth Ditto","Always do your best. What you plant now, you will harvest later.\n-Og Mandino","Don't judge each day by the harvest you reap but by the seeds that you plant.\n-Robert Louis Stevenson")
    quote=random.choice(Quote)
    a=Controls()
    a.Display(quote)
    a.Con()
    
c=In()