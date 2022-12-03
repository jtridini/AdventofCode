### Part 2
def day3part1(file):
    line = []

    # Convert file into list of list of ints for each line
    for content in file.readlines():
        priority = []
        for item in content:
            if item.islower():
                priority.append(ord(item)-96) # convert unicode to position on alphabet
            elif item.isupper():
                priority.append(ord(item)-38)
        line.append(priority)

    count = 0

    for i in range(len(line)//3):
        group = line[i*3:i*3+3] # iterate in sets of three
        count += list(set.intersection(*map(set,group)))[0]
    return count

filepath = open(r"C:\Users\Jake\Documents\03122022-AoC-Rucksack.txt", 'r')
print(day2part1(filepath))