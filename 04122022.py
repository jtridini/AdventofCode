def day4(file):
    overlap = 0
    partial = 0
    for line in [i.rstrip('\n') for i in file.readlines()]:
        s1, e1, s2, e2 = map(int, line.replace('-', ',').split(','))
        if (s1 >= s2 and e1 <= e2) or (s1 <= s2 and e1 >= e2):
            overlap += 1
        elif e1 < s2 or s1 > e2:
            None
        else:
            partial += 1
    return overlap, partial

f = open(r"C:\Users\Jake\Documents\04122022-AoC-Sections.txt", 'r')
print(day4(f))