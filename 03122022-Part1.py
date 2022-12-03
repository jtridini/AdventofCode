### Part 1
def day3part1(file,lowercase_offset,uppercase_offset):
    count = 0

    for rucksack in file.readlines():
        halfway = len(rucksack)//2
        rucksack1 = rucksack[:halfway]
        rucksack2 = rucksack[halfway:]

        duplicate = set(rucksack1).intersection(rucksack2).pop()

        if duplicate.islower():
            count += ord(duplicate)-lowercase_offset # convert unicode to position on alphabet
        elif duplicate.isupper():
            count += ord(duplicate)-uppercase_offset
    return count

filepath = open(r"C:\Users\Jake\Documents\03122022-AoC-Rucksack.txt", 'r')
lowercase_UNICODE = 96
uppercase_UNICODE = 38
print(day3part1(filepath, lowercase_UNICODE, uppercase_UNICODE))