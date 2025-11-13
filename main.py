import random
import time



def gen_qn():
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 12)
    operator = random.choice(operators)
    qn=str(num1)+' '+operator+' '+str(num2)
    return qn
def ans_qn(q):
    ans=round(eval(q))
    return (ans)
if __name__ == "__main__":
    print("\033[1m\nYou have 60 seconds. Answer as many as you can!\033[0m")
    print("Generating random math questions...\n")
    score=0
    start_time = time.time()

    while time.time() - start_time < 60:
        '''time_left = int(60 - (time.time() - start_time))    to show time left
            print(f"\n⏳ Time left: {time_left} seconds")'''
        qn = gen_qn()
        answer = ans_qn(qn)
        print(f"Question: {qn}")

        try:
            user=input("Enter your answer:")
            if int(user)==answer:
                print("Correct!")
                score+=1
            else:
                print("Incorrect!The correct answer was:", answer)
                print(f"\033[1mYour final score is: {score}\n\033[0m")  
                exit()
        except ValueError:
            print("Invalid number.")
            print(f"\033[1mYour final score is: {score}\n\033[0m")
            exit()

    print(f"\033[1mYour final score is: {score}\n\033[0m")     