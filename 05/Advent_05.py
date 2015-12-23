import re

f = open('input_05.txt')

def part_1():

    currentLine =  f.readline().rstrip()
    count = 0

    while (currentLine != '' ):

        #find at least 3 vowels
        pattern = re.compile(r'(.*[a|e|i|o|u]){3,}')
        if( pattern.match(currentLine) ):

            #find a letter repeated twice
            pattern = re.compile(r'.*([a-z])\1')
            if( pattern.match(currentLine)):

                #it does not contain these patterns
                pattern = re.compile(r'.*(ab|cd|pq|xy)')
                if(pattern.match(currentLine) ==  None):
                    #print currentLine
                    count += 1

        currentLine = f.readline().rstrip()

    return count

def part_2():

    f.seek(0)
    currentLine =  f.readline().rstrip()
    count = 0

    while (currentLine != '' ):

        #find at least 3 vowels
        pattern = re.compile(r'.*([a-z][a-z]).*\1')
        if( pattern.match(currentLine) ):
            #print 'First Match: ' + currentLine

            #find a letter repeated twice
            pattern = re.compile(r'.*([a-z]).\1')
            if( pattern.match(currentLine)):
                    #print 'Second Match: ' + currentLine
                    count += 1

        currentLine = f.readline().rstrip()

    return count

#solve part 1
f.seek(0)
answer = part_1()
print 'Part 1 Answer: ' + str(answer)

#solve part 2
f.seek(0)
answer = part_2()
print 'Part 2 Answer: ' + str(answer)
