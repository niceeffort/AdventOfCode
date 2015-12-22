f = open('input_03.txt')
text =  f.readline()

#Create a two dimensional array
#track x and y positions
x=0
y=0
SantaX = 0
SantaY = 0
RoboSantaX = 0
RoboSantaY = 0

xValues = []
yValues = []

map = { '0,0' : 1 }

SantaTurn = 1

for char in range(0,len(text)):

    if(SantaTurn):
        #print 'SantaX, SantaY = ' + str(SantaX) + ',' + str(SantaY)
        x = SantaX
        y = SantaY
    else:
        #print 'RoboSantaX, RoboSantaY = ' + str(RoboSantaX) + ',' + str(RoboSantaY)
        x = RoboSantaX
        y = RoboSantaY

    if (text[char] == '^'):
        y += 1
    elif(text[char] == 'v'):
        y -= 1
    elif(text[char] == '>'):
        x += 1
    elif(text[char] == '<'):
        x -= 1

    pair = str(x) + ',' + str(y)
    if (pair in map):
        map[pair] += 1
    else:
        map[pair] = 1

    if(SantaTurn):
        SantaX = x
        SantaY = y
        SantaTurn = 0
    else:
        RoboSantaX = x
        RoboSantaY = y
        SantaTurn = 1

#Create a dictionary and count pairs
print 'Number of houses delivered = ' + str(len(map))