boardX = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10}
boardY = [1,2,3,4,5,6,7,8,9,10]
board = ["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]

initialboard = """\
{A1}	{B1}	{C1}	{D1}	{E1}	{F1}	{G1}	{H1}	{I1}	{J1}
{A2}	{B2}	{C2}	{D2}	{E2}	{F2}	{G2}	{H2}	{I2}	{J2}
{A3}	{B3}	{C3}	{D3}	{E3}	{F3}	{G3}	{H3}	{I3}	{J3}
{A4}	{B4}	{C4}	{D4}	{E4}	{F4}	{G4}	{H4}	{I4}	{J4}
{A5}	{B5}	{C5}	{D5}	{E5}	{F5}	{G5}	{H5}	{I5}	{J5}
{A6}	{B6}	{C6}	{D6}	{E6}	{F6}	{G6}	{H6}	{I6}	{J6}
{A7}	{B7}	{C7}	{D7}	{E7}	{F7}	{G7}	{H7}	{I7}	{J7}
{A8}	{B8}	{C8}	{D8}	{E8}	{F8}	{G8}	{H8}	{I8}	{J8}
{A9}	{B9}	{C9}	{D9}	{E9}	{F9}	{G9}	{H9}	{I9}	{J9}
{A10}	{B10}	{C10}	{D10}	{E10}	{F10}	{G10}	{H10}	{I10}	{J10}
"""

board1 = """\
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
{}	{}	{}	{}	{}	{}	{}	{}	{}	{}
"""
board2 = """\
{A1}	{B1}	{C1}	{D1}	{E1}	{F1}	{G1}	{H1}	{I1}	{J1}
{A2}	{B2}	{C2}	{D2}	{E2}	{F2}	{G2}	{H2}	{I2}	{J2}
{A3}	{B3}	{C3}	{D3}	{E3}	{F3}	{G3}	{H3}	{I3}	{J3}
{A4}	{B4}	{C4}	{D4}	{E4}	{F4}	{G4}	{H4}	{I4}	{J4}
{A5}	{B5}	{C5}	{D5}	{E5}	{F5}	{G5}	{H5}	{I5}	{J5}
{A6}	{B6}	{C6}	{D6}	{E6}	{F6}	{G6}	{H6}	{I6}	{J6}
{A7}	{B7}	{C7}	{D7}	{E7}	{F7}	{G7}	{H7}	{I7}	{J7}
{A8}	{B8}	{C8}	{D8}	{E8}	{F8}	{G8}	{H8}	{I8}	{J8}
{A9}	{B9}	{C9}	{D9}	{E9}	{F9}	{G9}	{H9}	{I9}	{J9}
{A10}	{B10}	{C10}	{D10}	{E10}	{F10}	{G10}	{H10}	{I10}	{J10}
"""

############### CLASS
class Players:
    board_confirmed = True
    boardavailable = ["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
    destoryer_location = []
    destroyer_complete = False
    submarine_location = []
    cruiser_location = []
    battleship_location = []
    carrier_location = []
    def __init__(self, name):
        self.name = name

    def destoryer(self):
        complete = False
        self.complete = complete
        destoyer_temp_location = []
        print("Destoryer Size is 2")
        destroyer_start = input("START TILE: ").upper()
        destroyer_end = input("END TILE: ").upper()
        if destroyer_start in self.boardavailable:
            if destroyer_end in self.boardavailable:
                if destroyer_start[0].upper() == destroyer_end[0].upper():
                    if int(destroyer_end[1]) > int(destroyer_start[1]) and int(destroyer_end[1]) == int(destroyer_start[1]) + 2:
                        tnum = int(destroyer_end[1]) - 1
                        secondtile = destroyer_start[0] + str(tnum)
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(secondtile)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    elif int(destroyer_start[1]) > int(destroyer_end[1]) and int(destroyer_start[1]) == int(destroyer_end[1]) + 2:
                        tnum = int(destroyer_start[1]) - 1
                        secondtile = destroyer_start[0] + str(tnum)
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(secondtile)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    else:
                        print("invalid entry try again")
                    
                elif destroyer_start[1] == destroyer_end[1]:
                    if boardX[destroyer_end[0].upper()] > boardX[destroyer_start[0].upper()] and boardX[destroyer_end[0].upper()] == boardX[destroyer_start[0].upper()] +2:
                        tnum = boardX[destroyer_end[0]] - 1
                        secondtile = getletter(tnum) + str(destroyer_start[1])
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(secondtile)
                        destoyer_temp_location.append(destroyer_end)
                        complete = True
                    elif boardX.get(destroyer_start[0].upper()) > boardX.get(destroyer_end[0].upper()) and boardX.get(destroyer_start[0].upper()) == boardX.get(destroyer_end[0].upper()) +2:
                        tnum =boardX.get(destroyer_start[0].upper()) -1
                        secondtile = getletter(tnum) + str(destroyer_start[1]) 
                        destoyer_temp_location.append(destroyer_end)
                        destoyer_temp_location.append(secondtile)
                        destoyer_temp_location.append(destroyer_start)
                        complete = True
                    else:
                        print("invalid entry try again")
                        
                else:
                    print("invalid entry try again")
                    
            else:
                    print("invalid entry try again")
                    
        else:
                    print("invalid entry try again")
                         
        if complete == True:
            print("Tiles Destoyer Tiles:", destoyer_temp_location)
            tcomplete = False
            while tcomplete == False:
                confirm = input("Would you like to continue, yes or no? ")
                if confirm == "yes":
                    for i in destoyer_temp_location:
                        self.destoryer_location.append(i)
                    for i in destoyer_temp_location:
                        tindex = self.boardavailable.index(i) 
                        self.boardavailable[tindex] = "D"
                    tcomplete = True
                    self.destroyer_complete = True
                elif confirm == "no":
                    complete = False
                    break
                else:
                    print("not an option try again")

    
    def submarine(self):
        submarine_temp_location = []
        print("Submarine Size is 3")
        submarine_start = input("START TILE: ").upper()
        submarine_end = input("END TILE: ").upper()
        if submarine_start in self.boardavailable:
            if submarine_end in self.boardavailable:
                if submarine_start[0].upper() == submarine_end[0].upper():
                    if int(submarine_end[1]) > int(submarine_start[1]) and int(submarine_end[1]) == int(submarine_start[1]) + 2:
                        tnum = int(submarine_end[1]) - 1
                        secondtile = submarine_start[0] + str(tnum)
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                    elif int(submarine_start[1]) > int(submarine_end[1]) and int(submarine_start[1]) == int(submarine_end[1]) + 2:
                        tnum = int(submarine_start[1]) - 1
                        secondtile = submarine_start[0] + str(tnum)
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                    else:
                        print("invalid entry try again")
                        self.submarine()
                elif submarine_start[1] == submarine_end[1]:
                    if boardX[submarine_end[0].upper()] > boardX[submarine_start[0].upper()] and boardX[submarine_end[0].upper()] == boardX[submarine_start[0].upper()] +2:
                        tnum = boardX[submarine_end[0]] - 1
                        secondtile = getletter(tnum) + str(submarine_start[1])
                        submarine_temp_location.append(submarine_start)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_end)
                    elif boardX.get(submarine_start[0].upper()) > boardX.get(submarine_end[0].upper()) and boardX.get(submarine_start[0].upper()) == boardX.get(submarine_end[0].upper()) +2:
                        tnum =boardX.get(submarine_start[0].upper()) -1
                        secondtile = getletter(tnum) + str(submarine_start[1]) 
                        submarine_temp_location.append(submarine_end)
                        submarine_temp_location.append(secondtile)
                        submarine_temp_location.append(submarine_start)
                    else:
                        print("invalid entry try again")
                        self.submarine()
                else:
                    print("invalid entry try again")
                    self.submarine()
            else:
                    print("invalid entry try again")
                    self.submarine()
        else:
                    print("invalid entry try again")
                    self.submarine()                 
        print("Tiles Destoyer Tiles:", submarine_temp_location)
        complete = False
        while complete == False:
            confirm = input("Would you like to continue, yes or no? ")
            if confirm == "yes":
                for i in submarine_temp_location:
                    self.submarine_location.append(i)
                for i in submarine_temp_location:
                    tindex = self.boardavailable.index(i) 
                    self.boardavailable[tindex] = "X"
                complete = True
            elif confirm == "no":
                self.submarine()
            else:
                print("not an option try again")

        

################## CLASS END

############ functions
def getletter(number):
    for key, value in boardX.items():
        if value == number:
            return key 


def print_updated_board(board, board2):
    print(board.format(*board2))
    
def destroyer_setup(player):
    destoyer_temp_location = []
    print("Destoryer Size is 2")
    destroyer_start = input("START TILE: ").upper()
    destroyer_end = input("END TILE: ").upper()
    if destroyer_start in player.boardavailable:
        if destroyer_end in player.boardavailable:
            if destroyer_start[0].upper() == destroyer_end[0].upper():
                if int(destroyer_end[1]) > int(destroyer_start[1]) and int(destroyer_end[1]) == int(destroyer_start[1]) + 2:
                    tnum = int(destroyer_end[1]) - 1
                    secondtile = destroyer_start[0] + str(tnum)
                    destoyer_temp_location.append(destroyer_start)
                    destoyer_temp_location.append(secondtile)
                    destoyer_temp_location.append(destroyer_end)
                elif int(destroyer_start[1]) > int(destroyer_end[1]) and int(destroyer_start[1]) == int(destroyer_end[1]) + 2:
                    tnum = int(destroyer_start[1]) - 1
                    secondtile = destroyer_start[0] + str(tnum)
                    destoyer_temp_location.append(destroyer_start)
                    destoyer_temp_location.append(secondtile)
                    destoyer_temp_location.append(destroyer_end)
                else:
                    return False
                        
            elif destroyer_start[1] == destroyer_end[1]:
                if boardX[destroyer_end[0].upper()] > boardX[destroyer_start[0].upper()] and boardX[destroyer_end[0].upper()] == boardX[destroyer_start[0].upper()] +2:
                    tnum = boardX[destroyer_end[0]] - 1
                    secondtile = getletter(tnum) + str(destroyer_start[1])
                    destoyer_temp_location.append(destroyer_start)
                    destoyer_temp_location.append(secondtile)
                    destoyer_temp_location.append(destroyer_end)
                elif boardX.get(destroyer_start[0].upper()) > boardX.get(destroyer_end[0].upper()) and boardX.get(destroyer_start[0].upper()) == boardX.get(destroyer_end[0].upper()) +2:
                    tnum =boardX.get(destroyer_start[0].upper()) -1
                    secondtile = getletter(tnum) + str(destroyer_start[1]) 
                    destoyer_temp_location.append(destroyer_end)
                    destoyer_temp_location.append(secondtile)
                    destoyer_temp_location.append(destroyer_start)
                else:
                    print("invalid entry try again")
                    return False
            else:
                print("invalid entry try again")
                return False
        else:
            print("invalid entry try again")
            return False
    else:
        print("invalid entry try again")
        return False  
    return destoyer_temp_location
        

############ end of functions



player_1_name = input("Input Player 1 Name: ")
player_2_name = input("Input Player 2 Name: ")

player1 = Players(player_1_name)
player2 = Players(player_2_name)

print("Player 2 LOOK AWAY!")

ready = False
while ready == False:
    answer = input("Ready for Board Set-Up, yes or no? ")
    if answer == "yes":
        ready = True
    

######### BOARD SETUP Player 1
player1_board_list = player1.boardavailable
print(initialboard)
player1.destoryer()
while player1.destroyer_complete == False:
    player1.destoryer()


print(player1.destoryer_location)
print_updated_board(board1, player1_board_list)

player1.submarine()
print(player1.submarine_location)
print_updated_board(board1, player1_board_list)
#print("Submarine Size is 3")
#p1_submarine_start = input("START TILE: ")
#p1_submarine_end = input("END TILE: ")

#print("Cruiser Size is 3")
#p1_cruiser_start = input("START TILE: ")
#p1_cruiser_end = input("END TILE: ")
#
#print("Battleship Size is 4")
#p1_battleship_start = input("START TILE: ")
#p1_battleship_end = input("END TILE: ")

#print("Carrier Size is 5")
#p1_carrier_start = input("START TILE: ")
#p1_carrier_end = input("END TILE: ")
#player1 = Players(player_1_name)
#print(player1.name)
