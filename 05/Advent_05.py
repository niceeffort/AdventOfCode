import re

f = open('input_05.txt')
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
                print currentLine
                count += 1

    currentLine = f.readline().rstrip()

print count