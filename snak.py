import random

end = 100

# Setting the snake and the ladders on the board
ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 74, 50: 67, 71: 92, 88: 99}
snake = {32: 10, 34: 6, 48: 26, 62: 18, 88: 89, 95: 56, 97: 78}

def check_ladder(point):
    if point in ladder:
        print("Climb up!!")
        return ladder[point]
    return point

def check_snake(point):
    if point in snake:
        print("Ouch! Snake bite!!")
        return snake[point]
    return point

def reached_end(point):
    return point >= end

def play():
    p1_name = input("Enter Player 1 name: ")
    p2_name = input("Enter Player 2 name: ")

    pp1, pp2, turn = 0, 0, 0

    while True:
        if turn % 2 == 0:
            print(f"{p1_name}, your turn")
            c = int(input("Press 1 to continue or 0 to exit: "))
            if c == 0:
                print(f"{p1_name} score: {pp1}")
                print(f"{p2_name} score: {pp2}")
                print("Quitting the game!")
                break
            dice = random.randint(1, 6)
            print(f"Dice showed {dice}")
            pp1 += dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            if pp1 > end:
                pp1 = end
            print(f"{p1_name} Your score: {pp1}")
            if reached_end(pp1):
                print(f"{p1_name} won!")
                break
        else:
            print(f"{p2_name}, your turn")
            c = int(input("Press 1 to continue or 0 to exit: "))
            if c == 0:
                print(f"{p1_name} score: {pp1}")
                print(f"{p2_name} score: {pp2}")
                print("Quitting the game!")
                break
            dice = random.randint(1, 6)
            print(f"Dice showed {dice}")
            pp2 += dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            if pp2 > end:
                pp2 = end
            print(f"{p2_name} Your score: {pp2}")
            if reached_end(pp2):
                print(f"{p2_name} won!")
                break
        turn += 1

play()
