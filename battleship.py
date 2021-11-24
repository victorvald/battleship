boardX = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J"}
boardY = [1,2,3,4,5,6,7,8,9,10]


class Players:
    board_confirmed = True
    boardavailable = ["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","A2","B2","C2","D2","E2","F2","G2","H2","I2","J2","A3","B3","C3","D3","E3","F3","G3","H3","I3","J3","A4","B4","C4","D4","E4","F4","G4","H4","I4","J4","A5","B5","C5","D5","E5","F5","G5","H5","I5","J5","A6","B6","C6","D6","E6","F6","G6","H6","I6","J6","A7","B7","C7","D7","E7","F7","G7","H7","I7","J7","A8","B8","C8","D8","E8","F8","G8","H8","I8","J8","A9","B9","C9","D9","E9","F9","G9","H9","I9","J9","A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
    destoryer_location = []
    submarine_location = []
    cruiser_location = []
    battleship_location = []
    carrier_location = []
    def __init__(self, name):
        self.name = name
    def destoryer(self):
        destoyer_temp_location = []
        print("Destoryer Size is 2")
        destroyer_start = input("START TILE: ")
        destroyer_end = input("END TILE: ")
        if destroyer_start.upper in self.boardavailable:
            if destroyer_end.upper in self.boardavailable:
                if destroyer_start[0].upper == destroyer_end[0].upper:
                    if int(destroyer_end[1]) > int(destroyer_start[1]) and int(destroyer_end[1]) == int(destroyer_start[1]) + 2:
                        tnum = int(destroyer_end[1]) - 1
                        secondtile = destroyer_start[0] + str(tnum)
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(secondtile)
                        destoyer_temp_location.append(destroyer_end)
                    elif int(destroyer_start) > int(destroyer_end) and int(destroyer_start[1]) == int(destroyer_end[1]) + 2:
                        tnum = int(destroyer_start[1]) - 1
                        secondtile = destroyer_start[0] + str(tnum)
                        destoyer_temp_location.append(destroyer_start)
                        destoyer_temp_location.append(secondtile)
                        destoyer_temp_location.append(destroyer_end)
        print("Tiles Destoyer Tiles:", destoyer_temp_location)
        complete = False
        while complete == False:
            confirm = input("Would you like to continue, yes or no? ")
            if confirm == "yes":
                self.destoryer_location.append(destoyer_temp_location)
                complete = True
            elif confirm == "no":
                self.destoryer()
            else:
                print("not an option try again")
        
        for i in destoyer_temp_location:
            self.boardavailable.remove(i)



    
    def submarine(self, lsubmarine):
        self.lsubmarine = lsubmarine
        
    def cruiser(self, lcruiser):
        self.lcruiser = lcruiser
    
    def battleship(self, lbattleship):
        self.lbattleship = lbattleship
    
    def carrier(self, lcarrier):
        self.carrier = carrier


def destoryerstart():
    print("Destoryer Size is 2")
    p1_destroyer_start = input("START TILE: ")
    p1_destoryer_end = input("END TILE: ")


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
    
board = """\
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
player1.destoryer()

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
print(player1.destoryer_location)