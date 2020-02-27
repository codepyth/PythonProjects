import random
win = random.randint(1,50)
guessN = 1
num = int(input("Enter Number between 0 and 50: "))
done = False
while not done:
    if num==win:
        print(f"You WON!! \nGuessed in {guessN} times")
        done = True
    else:
        if num<win:
            print("its Low")
            guessN += 1
            num = int(input("Enter guess number again: "))
        else:
            print("its High!!")
            guessN += 1
            num = int(input("Enter guess number again: "))