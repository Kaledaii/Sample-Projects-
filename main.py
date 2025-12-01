import random 

TRIES=10
colors=['R','B','G','Y','W','O']
CODE_LENGTH=4

def geneate_code():
    code=[]
    for _ in range(CODE_LENGTH):
        color=random.choice(colors)
        code.append(color)
    return code    


def guess_code():
    while True:
        guess=input("Guess: ").upper().split(' ')
        if len(guess) != CODE_LENGTH:
            print(f"Invalid Guess.You need to guess {CODE_LENGTH} colors")
            continue
    
        for color in guess:
            if color not in colors:
                print(f'Invalid color {color}')
                break
        else:
            return guess

def check(real_code,guess):
    color_count={}
    correct_pos=0
    incorrect_pos=0 

    for color in real_code:
        if color not in color_count:
            color_count[color]=0
        color_count[color]+=1
    for guess_color,real_color in zip(guess,real_code):
        if guess_color==real_color:
            correct_pos+=1
            color_count[guess_color]-=1

    for guess_color,real_color in zip(guess,real_code):
        if guess_color in color_count and color_count[guess_color]>0:
            incorrect_pos+=1
            color_count[guess_color]-=1
    return correct_pos,incorrect_pos

def main():
    print("Welcome to Mastermind!")
    print(f"The colors are {colors}")
    code=geneate_code()
    
    attempt=0
    for attempt in range(TRIES+1):
        guess=guess_code()
        correct_pos,incorrect_pos=check(code,guess)

        if correct_pos==CODE_LENGTH:
            print(f"Congratulations! You've guessed the code in {attempt} tries!")
            print(code)
            break

        print(f'Correct Position: {correct_pos}\tIncorrect Position: {incorrect_pos}')
    else:
        print("Sorry, you've used all your tries.The code was:")
        print(code)
main()