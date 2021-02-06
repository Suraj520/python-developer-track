#Defining the coffee machine class
class CoffeeMachine:
    def __init__(self,water,milk,coffee,disposable_cups,money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.disposable_cups = disposable_cups
        self.money = money
    #Method for printing acknowledgement of processing/!processing coffee
    def acknowledgment(self,flag, *args):
        self.flag = flag
        if self.flag=="ok":
            print("I have enough resources, making you a coffee!")
            print()
        elif self.flag=="error":
            finished_ingredient = args[0]
            print("Sorry, not enough {0}!".format(finished_ingredient))
            print()

#function for displaying contents
#displaying method
def print_qty(water,milk,coffee,disposable_cups,money):
    print("The coffee machine has:")
    print("{0} of water".format(water))
    print("{0} of milk".format(milk))
    print("{0} of coffee beans".format(coffee))
    print("{0} of disposable cups".format(disposable_cups))
    if money!=0:
        print("{0} of money".format(money))
    else:
        print("{0} of money".format(money))
    print()

#**********************************************************************
# Init amount
water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550
#**************************************************************************
#Actions begins
#Instantiate the class
CoffeeMaker = CoffeeMachine(water,milk,coffee,disposable_cups,money)
while(True):
    input_action = input("Write action (buy, fill, take, remaining, exit):")
    print()
    if input_action == "remaining":
        print_qty(water,milk,coffee,disposable_cups,money)
    elif input_action=="take":
        print("I gave you ${0}".format(money))
        print()
        money = 0
    elif input_action=="buy":
        buy_choice = (input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
        if buy_choice =="1":
            if water-250>0 and coffee-16>0:
                CoffeeMaker.acknowledgment(flag ="ok")
                disposable_cups = disposable_cups-1
                water,coffee,money =  (water-250, coffee-16, money+4)
            else:
                #print the exhausted resource
                qty1= water-250
                qty2 = coffee- 16
                finished_qty = min(qty1,qty2)
                if finished_qty==qty1:
                    finished_ingredient ="water"
                else:
                    finished_ingredient = "coffee"
                CoffeeMaker.acknowledgment("error", finished_ingredient)

        elif buy_choice =="2":
            if water-350>0 and milk-75>0 and coffee-20>0 :
                CoffeeMaker.acknowledgment(flag="ok")
                water,milk, coffee,money = water-350,milk-75, coffee-20, money+7
                disposable_cups = disposable_cups-1
            else:
                #print the exhausted resource
                qty1= water-350
                qty2 = milk-75
                qty3 = coffee- 20
                finished_qty = min(qty1,qty2,qty3)
                if finished_qty==qty1:
                    finished_ingredient ="water"
                elif finished_qty == qty2:
                    finished_ingredient = "milk"
                else:
                    finished_ingredient="coffee"
                CoffeeMaker.acknowledgment("error", finished_ingredient)
            #water,milk,coffee,money = latte(water,milk,coffee,money)
            #disposable_cups = disposable_cups-1
        elif buy_choice=="3":
            if water-200>0 and milk-100>0 and coffee-12>0 :
                CoffeeMaker.acknowledgment(flag="ok")
                water,milk,coffee,money = (water-200,milk-100,coffee-12, money+6)
                disposable_cups = disposable_cups-1
            else:
                #print the exhausted resource
                qty1= water-200
                qty2 = milk-100
                qty3 = coffee- 12
                finished_qty = min(qty1,qty2,qty3)
                if finished_qty==qty1:
                    finished_ingredient ="water"
                elif finished_qty == qty2:
                    finished_ingredient = "milk"
                else:
                    finished_ingredient="coffee"
                CoffeeMaker.acknowledgment("error", finished_ingredient)
    elif input_action=="fill":
        water+= int(input("Write how many ml of water do you want to add:"))
        milk+= int(input("Write how many ml of milk do you want to add:"))
        coffee+= int(input("Write how many grams of coffee beans do you want to add:"))
        disposable_cups+= int(input("Write how many disposable cups of coffee do you want to add:"))
    elif input_action =="remaining":
        pass

    elif input_action == "exit":
        break

