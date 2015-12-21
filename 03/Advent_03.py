f = open('input_03.txt')
text =  f.readline()

#Create a two dimensional array
#track x and y positions
x=0
y=0

xValues = []
yValues = []

map = {'count' : 7};

for char in range(0,len(text)):
    if (text[char] == '^'):
        y += 1
    elif(text[char] == 'v'):
        y -= 1
    elif(text[char] == '>'):
        x += 1
    elif(text[char] == '<'):
        x -= 1
    xValues.append(x)
    yValues.append(y)

print xValues
print yValues

    #Create a dictionary and count pairs
    dict[ x,y ] += 1
    print dict