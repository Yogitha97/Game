#Rock, Paper, Scissors Game for 2 Players!!!
#First one to Score 3, Wins the game 

print("Let's play Rock, Paper, Scissors game!! ")
print("First one to Three wins!\n")
print("*****************************************")

player1 = input("Enter Player1 name: ")
player2 = input("Enter Player2 name: ")

score1=0
score2=0

while True:
    print("*************************************\n")
    u1 = input("%s, What do you choose rock, paper or scissors?: " %player1)
    u2 = input("%s, What do you choose rock, paper or scissors?: " %player2)
        
    #if statement for player1 to win
    if(u1=="rock" and u2=="scissors") or (u1=="scissors" and u2=="paper") or (u1=="paper" and u2=="rock"):
        print(player1,"Wins!")
        score1+=1
        print("Scoreboard \n Player1: " +str(score1)+ " , " +"Player2: " +str(score2))

    #statement for player2 to win
    elif(u2=="rock" and u1=="scissors") or (u2=="scissors" and u1=="paper") or (u2=="paper" and u1=="rock"):
        print(player2,"Wins!")
        score2+=1
        print("Scoreboard \n Player1: " +str(score1)+ " , " +"Player2: " +str(score2))

    #statement for tie between the players
    elif(u1==u2):
        print("It's a tie!")
        print("Scoreboard \n Player1: " +str(score1)+ " , " +"Player2: " +str(score2))

    #statment for invalid input
    else:
        print("Invalid input, You haven't entered rock, paper os scissors, try again. ")
        break

    #if statement for winner
    if score1 == 3:
        print(player1, "won the game!")
        break
    
    if score2 == 3:
        print(player2, "won the game!")
        break
    
print("Game Over")


#compare_game(player1_answer,player2_answer)