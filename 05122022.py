#instructions = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']
#column1 = ['N','Z']
#column2 = ['D','C','M']
#column3 = ['P']

#column1 = column1[::-1]
#column2 = column2[::-1]
#column3 = column3[::-1]

column1 = ['Q','F','M','R','L','W','C','V']
column2 = ['D','Q','L']
column3 = ['P','S','R','G','W','C','N','B']
column4 = ['L','C','D','H','B','Q','G']
column5 = ['V','G','L','F','Z','S']
column6 = ['D','G','N','P']
column7 = ['D','Z','P','V','F','C','W']
column8 = ['C','P','D','M','S']
column9 = ['Z','N','W','T','V','M','M','P','C']

filePath = r"C:\Users\Jake\Documents\05122022-AoC-Crates.txt"
with open(filePath) as f:
    instructions = [i.rstrip('\n') for i in f.readlines()[10:]]

stack = [column1,column2,column3,column4,column5,column6,column7,column8,column9]

cratesOnTop = []
for instruction in instructions:
    _, numberOfCrates, _, moveFrom, _, moveTo = instruction.split(' ')
    numberOfCrates = int(numberOfCrates)
    moveFrom = int(moveFrom)
    moveTo = int(moveTo)

    moveFrom -= 1
    moveTo -= 1

    stack[moveTo] += stack[moveFrom][-numberOfCrates:]#[::-1]
    stack[moveFrom] = stack[moveFrom][:-numberOfCrates]

for i in range(len(stack)):
    cratesOnTop += stack[i][-1]
print(cratesOnTop)

# print(stack[moveFrom])
# print(stack[moveTo])
# print('\n')
# print(stack[moveFrom][-numberOfCrates:])#[::-1])
# print('\n')
# print(stack[moveTo] += stack[moveFrom][-numberOfCrates:][::-1])
# print(stack[moveFrom][:-numberOfCrates])