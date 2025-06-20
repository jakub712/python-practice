#ask 10: Rock Paper Scissors

#Ask for two inputs: player1 and player2 choices. Print the winner or "Draw".
Player_1 = input("Pick rock, paper or scissors. ")
Player_2 = input("Pick rock, paper or scissors. ")

if Player_1 == ("rock") and Player_2 == ("rock"):
    print("It's a Draw!")
elif Player_1 == ("rock") and Player_2 ==("paper"):
    print("Player two Wins!")
elif Player_1 == ("rock") and Player_2 == ("scissors"):
    print("Player one Wins!")
elif Player_1 == ("paper") and Player_2 == ("scissors"):
    print("Player two Wins!")
elif Player_1 == ("paper") and Player_2 == ("paper"):
    print("It's a Draw!")
else:
    print("It's a Draw!")

