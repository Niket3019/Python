print("Welcome to the word game!\nyou were going to think of a word and you have to guess it!\n")
print("Guess which letters are correct,\nthen you will get score value,for each correct you will get +1 else -1 for incorrect\nGood luck!")
puzzle1 = ["RAEHTF","KABRE","YCR","RENEG","OAERELANP"]
puzzle2 = ["FATHER","BARKE","CRY","GREEN","AEROPLANE"]
tries = 0
i=0
InCorrect_Correct_total = 0
while tries<5:
    ab = puzzle1[i]
    print("The puzzle are:",ab)
    puzzle1[i] = input("Guess the puzzle value :")
    if puzzle1[i] == puzzle2[i]:
        print("Good job! Guess another!")
        InCorrect_Correct_total+=1
        print("Good! Your score is:",InCorrect_Correct_total)
    else:
        print("Sorry, try again.")
        InCorrect_Correct_total-=1
        print("Oops! The decrement score value is:",InCorrect_Correct_total)
    i+=1
    tries+=1

print("The total score is:",InCorrect_Correct_total)
if InCorrect_Correct_total == 5:
    print("Bravo! Your All Answer War Right....")
elif InCorrect_Correct_total>=1 and InCorrect_Correct_total<5:
    print("Oops! Try Next Time...Make More Score")
else:
    print("Your Score Is In Negative...Do Practice!")