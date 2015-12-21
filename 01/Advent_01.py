f = open('input_01.txt')
text =  f.readline()
print 'String Length' + str(len(text))

floor = 0
firstEnteredBasement = 0
for char in range(0,len(text)):
    if (text[char] == '('):
        floor += 1
    elif (text[char] == ')'):
        floor -= 1
    if (floor == -1 and firstEnteredBasement == 0):
        firstEnteredBasement = char + 1
        print 'First entered basement at position ' + str(firstEnteredBasement)

print "Santa's final floor " + str(floor)