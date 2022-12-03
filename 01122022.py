def day1part1and2(file):
    line = [i.rstrip('\n') for i in file.readlines()]
    i = 0
    #[print(len(i)) for i in line] # check length of emtpy string
    list = []
    val = 0

    while i < len(line):
        if len(line[i]) < 1:
            list.append(val)
            val = 0
        else:
            val += int(line[i])
        i+=1

    top_total = max(list) # part 1
    top_three_total = sum(sorted(list, key=int, reverse=True)[0:3]) # part 2
    return top_total, top_three_total

filepath = open(r"C:\Users\Jake\Documents\01122022-AoC-Calories-CSV.txt", 'r')
print(day1part1and2(filepath))