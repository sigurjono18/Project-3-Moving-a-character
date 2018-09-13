position_int = int(input("Input a position between n and 10: "))
new_position = position_int

def get_input():
    print("l - for moving left")
    print("r - for moving right")
    print("any other letter for quitting")
    character = input("Input your choice: ")
    return(character)

def Move_Right(position):  #fall sem heldur utan um alla jákvæða útreikninga
    if new_position >= 10:
        return position+0
    else:   
        return position+1

def Move_Left(position):  #fall sem heldur utan um alla nekvæða útreikninga
    if new_position <= 1:
        return position+0
    else:
        return position-1
    
while True:
    character = get_input()
    
    if character not in 'rl':
        print("New position is: ", new_position)
        break
    elif character in 'r':
        new_position = Move_Right(new_position)
    elif character in 'l':
        new_position = Move_Left(new_position)
    
    print("New position is:",new_position)

