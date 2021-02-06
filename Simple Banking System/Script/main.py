#Import statements
import random
import _sqlite3
#Helper functions for calculating checksum via Luhn check and checking validity of a card
#Luhn_check method to find check sum
def checksum_calculator(card_number):
    #Removing last digit from the card
    card_number = card_number[0:len(card_number)-1]
    #Luhn check algorithm starts here
    #multiply odd digits by 2 and subtract 9 from all numbers >9 and then add
    #converting to int
    out_num = [int(i) for i in card_number]
    #multiply all odd places by 2 and subtract 9 from them
    for idx in range(len(out_num)):
        if (idx+1)%2!=0:
            out_num[idx] = out_num[idx]*2
            if out_num[idx]>9:
                out_num[idx]= out_num[idx]-9
    out_sum = sum(out_num)
    out = out_sum%10
    if out >0:
        check_sum = 10 - out
    else:
        check_sum = 0
    #converting to string for validity checker and appending
    check_sum = str(check_sum)
    return check_sum
#checking the validity of a method using luhn_check
def card_validity_checker(card_number):
    #checking if last digit of the card is equal to the check sum calculated by Luhn check or not
    if checksum_calculator(card_number) == card_number[-1]:
        return True
    else:
        return False
#Helper function ends here >>>>>>

#Credit Card class starts here >>>>>>>>>>>>>>>>>>>>>>>>>>>>
#core class of credit card with various operational methods
class CreditCard:
    #init method
    def __init__(self):
        #creating or dropping the database during constructor init.
        self.card_number = None
        self.atm_pin = None
        self.conn = _sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
    # create account method
    def create_account(self,id):
        self.id = id
        print()
        print("Your card has been created")
        print("Your card number:")
        random_number = random.randint(1000000000, 9999999999)
        self.atm_pin = random.randint(1000,9999)
        card_number = "400000"+str(random_number)#4000004938320895
        #calculating checksum
        check_sum = checksum_calculator(card_number)
        card_number = (card_number[:len(card_number)-1]+check_sum)
        #card number generated from Luhn's algorithm
        self.card_number = card_number
        print(self.card_number)
        print("Your card PIN:")
        print(self.atm_pin)
        print()
        #appending the data into the card table database
        self.cur.execute("INSERT INTO card (number,pin) VALUES ({0},{1})".format(self.card_number,self.atm_pin))
        self.conn.commit()
        return self.card_number, self.atm_pin,self.id
    #login check method
    def login_check(self,desired_id,card,pin):
        self.desired_id = desired_id
        self.card = card
        self.pin = pin
        self.cur.execute("SELECT * FROM card WHERE number={0} AND pin={1}".format(self.card,self.pin))
        rows = self.cur.fetchall()
        if len(rows)>0:
            print()
            self.desired_id = rows[0][0]
            print("You have successfully logged in!")
            print()
        else:
            print()
            print("Wrong card number or PIN!")
            print()
        flag = self.prompt(self.desired_id)
        return flag

    #Continuos prompt method once user is logged in
    def prompt(self,desired_id):
            flag = 0
            #continue prompt till flag is set to 0 i.e 0 is not pressed.
            while(flag==0):
                print('''
        1. Balance
        2. Add income
        3. Do transfer
        4. Close account
        5. Log out
        0. Exit''')
                self.desired_id = desired_id
                input_choice = input()
                if input_choice == "1":
                    print(self.check_balance(self.desired_id))
                elif input_choice == "2":
                    new_sum = int(input("Enter income:"))
                    self.add_income(self.desired_id, new_sum)
                elif input_choice == "3":
                    self.transfer_method()
                elif input_choice =="4":
                    self.close_account()
                elif input_choice == "5":
                    print("You have successfully logged out!")
                elif input_choice == "0":
                    print("Bye")
                    flag = 1
                    return flag

    #Helper methods post login check
    #check balance method
    def check_balance(self,id):
        self.cur.execute("SELECT balance FROM card WHERE id={0}".format(self.desired_id))
        rows = self.cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        return 0

    #add income method
    def add_income(self,desiredid,new_sum):
        self.new_sum = new_sum
        #fetch balance from db for that ID::
        balance1 = self.check_balance(self.desired_id)
        balance1+=self.new_sum
        #update the value in the database
        self.cur.execute("UPDATE card SET balance={0} WHERE id ={1}".format(balance1,self.desired_id))
        self.conn.commit()
        print("Income was added!")
        #self.print()
        #displaying tables
    #optional print method to check the contents of the database; Useful while debugging.
    def print(self):
        self.cur.execute('SELECT * FROM card')
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    #do transfer method
    def transfer_method(self):
        print("Transfer")
        #prompt the user to enter card number
        receiver_account = input("Enter card number:")
        #fetch sender account, It is the card number of logged in user
        sender_account = self.card
        #sender account fetched till this point
        #fetch sender balance by sender account
        self.cur.execute("SELECT balance FROM card WHERE number={0}".format(sender_account))
        rows = self.cur.fetchone()
        sender_balance= rows[0]
        #sender balance fetched
        if sender_account == receiver_account:
             print("You can't transfer money to the same account!")
             print("You can't transfer money to the same account!")
        #checking if account passes the Luhn check or not
        if card_validity_checker(receiver_account)!=True:
            print("Probably you made a mistake in the card number. Please try again!")
        #checking if reciever account exists in DB
        elif not self.cur.execute("SELECT pin FROM card WHERE number={0}".format(receiver_account)).fetchall():
            print("Such a card does not exist.")
        #else asking user for input
        else:
             print("Enter how much money you want to transfer: ")
             amount = int(input())
             #if amount is greater than sender balance then return not enough money
             if amount > sender_balance:
                 print("Not enough money!")
             else:
                 #let the transfer begin ;)
                 #step1 : fetch the id of reciever's account number and reciever's balance
                 self.cur.execute("SELECT * FROM card WHERE number={0}".format(receiver_account))
                 rows = self.cur.fetchall()
                 reciever_id = rows[0][0]
                 reciever_balance = rows[0][3]
                 #step 2: add amount to existing reciever balance, decrease it from sender's balance and update the attribute
                 send_amount = amount + reciever_balance
                 left_amount = sender_balance - amount
                 self.cur.execute("UPDATE card SET balance={0} WHERE id ={1}".format(amount,reciever_id))
                 self.cur.execute("UPDATE card SET balance={0} WHERE id ={1}".format(amount,self.desired_id))
                 self.conn.commit()
                 #self.print() #optional debugging by printing the contents of the database.
                 print("Success!")
    #close account method
    def close_account(self):
        self.cur.execute(("DELETE FROM card WHERE id = {0}").format(self.desired_id))
        self.conn.commit()
        print("The account has been closed!")
#Credit Card class ends here >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#main loop starts here
conn = _sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS card")
cur.execute('''CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, 
                        pin TEXT, balance INTEGER DEFAULT 0);''')
conn.commit()
#if database is freshly created point ID to 0
id =0
while(True):
    print('''
    1. Create an account
    2. Log into account
    0. Exit''')
    choice = input()
    Card = CreditCard()
    if choice =="1":
        _,_,id1 = Card.create_account(id)
        #after the account is created, increment the id with the id of insertion
        id = id1+1
    elif choice == "2":
        card_number =input("Enter your card number:")
        pin = input("Enter your PIN:")
        flag = Card.login_check(id,card_number,pin)
        #if 0 is pressed, exit
        if flag:
            break
    elif choice =="0":
        print("Bye")
        break

