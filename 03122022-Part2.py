### Part 2
def day3part2(file,lowercase_offset,uppercase_offset):
    count = 0
    rucksacks = file.readlines()
    rucksacks = [i.rstrip('\n') for i in rucksacks]
    for i in range(len(rucksacks)//3):
        group = rucksacks[i*3:i*3+3] # iterate in sets of three
        duplicate = set.intersection(*map(set,group)).pop()
        if duplicate.islower():
            count += ord(duplicate)-lowercase_offset # convert unicode to position on alphabet
        elif duplicate.isupper():
            count += ord(duplicate)-uppercase_offset
    return count

filepath = open(r"C:\Users\Jake\Documents\03122022-AoC-Rucksack.txt", 'r')
lowercase_UNICODE = 96
uppercase_UNICODE = 38
print(day3part2(filepath,lowercase_UNICODE,uppercase_UNICODE))