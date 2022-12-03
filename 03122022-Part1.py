# checking int to convert alphabet from unicode for lower- and uppercase
#alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#alphabet_cap = [i.capitalize() for i in alphabet]
#alphabet_to_int = [ord(letter)-96 for letter in alphabet] # convert unicode id to position in alphabet
#alphabet_cap_to_int = [ord(letter)-38 for letter in alphabet_cap]

### Part 1
def day3part1(file):
    count = 0
    for content in file.readlines():
        priority = []
        for item in content:
            if item.islower():
                priority.append(ord(item)-96) # convert unicode to position on alphabet
            elif item.isupper():
                priority.append(ord(item)-38)
        firstpart, secondpart = priority[:len(priority)//2], priority[len(priority)//2:] # split list in half
        #count += np.intersect1d(firstpart,secondpart) # count priority when appearing in both compartments
        count += list(set(firstpart).intersection(secondpart))[0]
    return count
filepath = open(r"C:\Users\Jake\Documents\03122022-AoC-Rucksack.txt", 'r')
print(day3part1(filepath))
