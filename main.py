from playsound import playsound
q=1
print ("Welcome to KBC!")
print(f"{q}\n")

def quiz_game(q):
    from qn import questions
    score = 0
    while True and q<=20:  
        dict= questions[q]
        print(dict["question"])
        o=dict["options"]
        i=0
        while i<4:
            print(f"{i+1}.{o[i]}")
            i+=1
        ans=int(input("Enter your answer: "))
        if dict["options"][ans-1]==dict["answer"]:
            print("Correct answer!")
            playsound('bc.mp3')
            score += 1
            q += 1
            print(f"Your current score is: {score}\n")         
        
        else:
            print(f"Wrong answer! The correct answer is: {dict['answer']}")
            print(f"Your total score is: {score}/20")
            break
        

quiz_game(q)