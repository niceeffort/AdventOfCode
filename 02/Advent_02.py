#open the input file
f = open('input_02.txt')
delimeter = 'x'

#read the first line
currentLine = f.readline()
totalArea = 0

while (currentLine != '' ):
    length = 0
    width = 0
    height = 0
    area = 0

    firstDelimeterPos = 0
    secondDelimeterPos = 0

    side1 = 0
    side2 = 0
    side3 = 0
    smallestSide = 0

    #parse the text for values

    #find the delimeter positions
    firstDelimeterPos = currentLine.find(delimeter)
    secondDelimeterPos = currentLine.find(delimeter,firstDelimeterPos + 1)

    length = int(currentLine[: firstDelimeterPos])
    width = int(currentLine[firstDelimeterPos + 1 : secondDelimeterPos])
    height = int(currentLine[secondDelimeterPos + 1 :])

    print 'length = ' + str(length)
    print 'width = ' + str(width)
    print 'height = ' + str(height)

    #find the area of each side and smallest side
    side1 = length * width
    print 'side1 = ' + str(side1)
    side2 = length * height
    print 'side2 = ' + str(side2)
    side3 = width * height
    print 'side3 = ' + str(side3)
    smallestSide = min(side1, side2, side3)
    print 'smallestSide = ' + str(smallestSide)

    #calculate the area for this present plus the extra
    area = 2*side1 + 2*side2 + 2*side3 + smallestSide
    print 'area = ' + str(area)

    #add to the total area
    totalArea += area

    #read the next line
    currentLine = f.readline()

print 'totalArea =' + str(totalArea)


#calculate square feet of each side and store the smallest

#double each side and add them together

#add the smallet side

#add to the total

#print total