n = int(input())
for i in range(n):
    def xo():
        game = []
        val = ""
        for i in range(3):
            game.append(input())
        # check vertical
        if game[0][0] == game[1][0] == game[2][0] != ".":
            return(game[0][0])
        elif game[0][1] == game[1][1] == game[2][1]!= ".":
            return(game[0][1])
        elif game[0][2] == game[1][2] == game[2][2]!= ".":
            return(game[0][2])
        
        #check horizontal
        if game[0][0] == game[0][1] == game[0][2]!= ".":
            return(game[0][0])
        elif game[1][0] == game[1][1] == game[1][2]!= ".":
            return(game[1][0])
        elif game[2][0] == game[2][1] == game[2][2]!= ".":
            return(game[2][0])
        
        # check diagonal
        if game[0][0] == game[1][1] == game[2][2]!= ".":
            return(game[0][0])
        elif game[0][2] == game[1][1] == game[2][0]!= ".":
            return(game[0][2])
        return "DRAW"
    print(xo())