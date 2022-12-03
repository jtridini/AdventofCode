### Part 1
def day2part1(file):
    line = file.readlines()
    line = [i.rstrip('\n') for i in line]
    score = 0
    for string in line:
        their_choice = string[0]
        your_choice = string[2]
        if your_choice == 'X': #you choose rock
            score += 1
            if their_choice == 'A': #they also choose rock, draw!
                score += 3
            elif their_choice == 'C': #they choose scissors, win!
                score += 6
            else:# they choose paper, lose!
                None
        elif your_choice == 'Y': #you choose paper
            score += 2
            if their_choice == 'B':  #they also choose paper, draw!
                score += 3
            elif their_choice == 'A':  #they choose rock, win!
                score += 6
            else:  #they choose scissors, lose!
                None
        elif your_choice == 'Z': #you choose scissors
            score += 3
            if their_choice == 'C':  #they also choose scissors, draw!
                score += 3
            elif their_choice == 'B': #they choose paper rock, win!
                score += 6
            else:  # they choose rock, lose!
                None
    return score

### Part 2
def day2part2(file):
    line = file.readlines()
    line = [i.rstrip('\n') for i in line]
    score = 0
    for string in line:
        their_choice = string[0]
        your_choice = string[2]
        if your_choice == 'X': #you must lose
            if their_choice == 'A': #they choose rock
                score += 3 #you must choose scissors
            elif their_choice == 'B': #they choose paper
                score += 1 #you must choose rock
            elif their_choice == 'C': #they choose scissors
                score += 2 #you must choose paper
        elif your_choice == 'Y': #you must draw
            score += 3
            if their_choice == 'A': #they choose rock
                score += 1 #you must choose rock
            elif their_choice == 'B': #they choose paper
                score += 2 #you must choose paper
            elif their_choice == 'C': #they choose scissors
                score += 3 #you must choose scissors
        elif your_choice == 'Z': #you must win
            score += 6
            if their_choice == 'A': #they choose rock
                score += 2 #you must choose paper
            elif their_choice == 'B': #they choose paper
                score += 3 #you must choose scissors
            elif their_choice == 'C': #they choose scissors
                score += 1 #you must choose rock
    return score

filepath = open(r"C:\Users\Jake\Documents\02122022-AoC-RockPaperScissors.txt", 'r')
print(day2part1(filepath))
print(day2part2(filepath))
