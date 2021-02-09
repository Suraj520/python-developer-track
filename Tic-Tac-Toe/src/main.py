# Helper functions
letter = "X"
#function to print an array
def print_array(string):
    array = []
    print("---------")
    for i in range(3):
            array.append(string[3*i:3+3*i])
            print(("|"+string[3*i:3+3*i].replace('',' ')+"|").replace('_', ' '))
    print("---------")
    return array

def string_to_array(string):
    array=[]
    for i in range(3):
            array.append(string[3*i:3+3*i])
    return array
#function to prompt for coordinates from STDIN
def prompt():
        coordinates = input("Enter the coordinates:").split(' ')
        return coordinates
#function to fill X, O to empty position else return value
def coordinates_check(array, prev_string, letter):
    #Base case:: Checking if elements of array are integers r not
    if len(array[0])> 1 or len(array[1])>1:
        print("You should enter numbers!")
        output_array = ''.join(prev_string)
    #check the lower and upper bounds for array
    elif (int(array[0])>3 or int(array[0])<1) or (int(array[1])>3 or int(array[1])<1):
        print("Coordinates should be from 1 to 3!")
        output_array = ''.join(prev_string)
    else:
        x_pos = int(array[0])-1
        y_pos = int(array[1])-1
        #print(type(prev_string))
        #prev_string = list(prev_string)
        print(prev_string)
        if prev_string[x_pos][y_pos]!="_":
            print("This cell is occupied! Choose another one!")
            output_array = ''.join(prev_string)
        else:
            #assignment to X
            out_string = [list(i) for i in prev_string]
            out_string[x_pos][y_pos]= letter
            #now joining twice
            out_string = [''.join(i) for i in out_string]
            output_array= ''.join(out_string)
    return output_array

#flip player positions
def flip_player(letter):
    if letter =="X":
        new_letter = "O"
    elif letter =="O":
        new_letter ="X"
    return new_letter

#checking if X == O in the matrix
def check_balanced_count(string1):
    x_count=0
    y_count=0
    for str1 in string1:
        if str1=="X":
            x_count+=1
        elif str1=="O":
            y_count+=1
    #print(x_count,y_count)
    if x_count > y_count:
        return ("X",False)
    elif x_count < y_count:
        return("O",False)
    else :
        return ("O",True)
#discrete winning tests functions
def horizontal_test(string1, keys):
    for key in keys:
        if len(set([string1[int(key)], string1[int(key)+1], string1[int(key)+2]]))==1 and string1[int(key)]!="_":
            return (string1[int(key)]+" wins")
def vertical_test(string1, keys):
    for key in keys:
        if len(set([string1[int(key)], string1[int(key)+3], string1[int(key)+6]]))==1:
            return (string1[int(key)]+" wins")
def diagonal_test(string1, keys):
    for key in keys:
        if key == 0 and len(set([string1[int(key)], string1[int(key)+4], string1[int(key)+8]]))==1 and string1[int(key)]!="_":
            return (string1[int(key)]+" wins")
        elif key == 2 and len(set([string1[int(key)], string1[int(key)+2], string1[int(key)+4]]))==1 and string1[int(key)]!="_":
            return (string1[int(key)]+" wins")
#unfinished rule function
def Unfinished_rule(Array):
    #if array contains an underscore then it is not valid
    if '_' in set(Array):
        return True
    else:
        return False
#win or draw prediction function
def predict_win_draw(string1):
    start_idx = {'Horizontal': {0,3,6}, 'Vertical': {0,1,2}, 'Diagonal':{0,2}}
    output=[]
    for key in start_idx.keys():
            if key == 'Horizontal':
                output.append(horizontal_test(string1, start_idx[key]))
                #print(start_idx[key])
            elif key == 'Vertical':
                #vertical_test_case evaluation
                output.append(vertical_test(string1, start_idx[key]))
            elif key == 'Diagonal':
                #Diagonal_test_case evaluation
                output.append(diagonal_test(string1, start_idx[key]))
    return output
#function to check the result
def check_result(string1):
    result= []
    #checking if the game is completed or draw
    if Unfinished_rule(string1)== True:
        #print(check_balanced_count(string1))
        if check_balanced_count(string1)[1]==False:
            #print(string1)
            if (len(set(predict_win_draw(string1)))) >1:
                if ("X wins" in set(predict_win_draw(string1)))==True:
                    result.append("X wins")
                elif ("O wins" in set(predict_win_draw(string1)))== True:
                    result.append("O wins")
                output_array = string1
            else:
                #print("Impossible!")
                output_array = string1

        elif check_balanced_count(string1)[1]==True:
            list1 = predict_win_draw(string1)
            if (set(list1))=={None}:
                output_array= string1
            elif len(set(list1))>1:
                result.append(list1)
                output_array = string1
    else:
    #    print("here")
        Result = predict_win_draw(string1)
        #print(Result)
        if "X wins" in Result or "Y wins" in Result:
            output_array = string1
            result.append(Result)
        else:
            output_array = string1
            result.append("Draw")
    return result, output_array


string = "_________"
#string = "XXOOOXXX_"
init_count =0
stop_flag =0
out_string = print_array(string)
while(stop_flag!=1):
    if init_count == 0:
        #asking for new coordinates
        coordinates = prompt()
        mod_string = coordinates_check(coordinates, out_string,"X")
        #print(check_result(mod_string)[0]
        if (mod_string != string):
            game_string = check_result(mod_string)[1]
            game_result = check_result(mod_string)[0]
            game_state = print_array(game_string)
            a_string = game_string
            init_count+=1
            if game_result:
                if game_result[0]=="Draw":
                    print(game_result[0])
                    stop_flag =1
                else:
                    desired_list = game_result[0]
                    #print(desired_list)
                    try:
                        if (desired_list[desired_list.index("X wins")]):
                            print(desired_list[desired_list.index("X wins")])
                        elif desired_list[desired_list.index("Y wins")]:
                            print(desired_list[desired_list.index("Y wins")])
                        stop_flag=1
                    except:
                        pass

        else:
            a_string = string
            init_count+=1
    elif init_count>0:
        if init_count == 1:
            new_string = a_string
        elif init_count>1 and Unfinished_rule(new_string)== True: # and len(new_string)!=3
            new_string = game_string
            print("Here")
        #find the previous state's letter
        last_letter = check_balanced_count(new_string)[0]
        new_letter  = flip_player(last_letter)
        coordinates = prompt()
        if len(new_string)>3:
            new_string = string_to_array(new_string)
        #print(new_string)
        mod_string_new =coordinates_check(coordinates,new_string, new_letter)
        #print(mod_string_new)
        if mod_string_new != new_string:
            game_string = check_result(mod_string_new)[1]
            game_result = check_result(mod_string_new)[0]
            game_state = print_array(game_string)
            init_count+=1
            if game_result:
                if game_result[0]=="Draw":
                    print(game_result[0])
                    stop_flag =1
                else:
                    desired_list = game_result[0]
                    #print(desired_list)
                    try:
                        if (desired_list[desired_list.index("X wins")]):
                            print(desired_list[desired_list.index("X wins")])
                        elif desired_list[desired_list.index("Y wins")]:
                            print(desired_list[desired_list.index("Y wins")])
                        stop_flag=1
                    except:
                        pass
        else:
            #suspect
            #new_string = game_string
            init_count+=1
