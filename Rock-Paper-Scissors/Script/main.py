# Write your code here
import random
class Game:
    def __init__(self,user_name, file_name):
        self.user_name = user_name
        self.file_name = file_name

    def predict_outcome(self,choice,score):
        self.score = score
        self.choice = choice
        computer_choices = ["rock","paper","scissors"]
        computer_option = random.randint(0,2)
        computer_choice = computer_choices[computer_option]
        win_pair = {"rock": "scissors","scissors":"paper","paper":"rock"}
        #print(choice,computer_choice)
        #print("Well done. The computer chose {0} and failed".format(str(computer_choice)))
        if self.choice == computer_choice:
            print("There is a draw ({0})".format(str(choice)))
            self.score+=50
        elif win_pair[computer_choice] != self.choice:
            print("Well done. The computer chose {} and failed".format(str(computer_choice)))
            self.score+=50
        elif win_pair[computer_choice] == self.choice:
            print("Sorry, but the computer chose {0}".format(str(computer_choice)))
            self.score+=50
        return self.score

    def file_operation(self, *args):
        #first argument of the args need to be operation
        operation = args[0]
        user = args[1]
        if operation =="read":
            score =0
            score_file = open(self.file_name,'r')
            entry_list = score_file.readlines()
            for i in range(len(entry_list)):
                if user in entry_list[i]:
                    score = int(list(entry_list[i].split())[1])
            return score
        elif operation =="append":
            pass


#set of valid inputs for the game
valid_inputs = ["rock","paper","scissors"]
#file name
file_name = "rating.txt"
#prompt for user __name__
username = input("Enter your name:")
print("Hello. {0}".format(username))
#initialising the class
RCP = Game(username,file_name)
#now fetch the score
score = RCP.file_operation("read",username)
while(True):
    choice = input()
    if choice == "!exit":
        print("Bye!")
        break
    elif choice not in valid_inputs:
        print("Invalid input")
    elif choice == "!rating":
        #print score
        print("Your rating: {0}".format(score))
    else:
        score = RCP.predict_outcome(choice,score)


