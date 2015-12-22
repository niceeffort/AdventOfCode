import hashlib

f = open('input_04.txt')
text =  f.readline().rstrip()

m = hashlib.md5()
m.update('abcdef609043')
print m.hexdigest()

answerNotFound = 1
counter = 0
#text = 'abcdef'
while( answerNotFound ):
    counter += 1
    m = hashlib.md5()
    tempText = text
    tempText += str(counter)
    print 'tempText = ' + tempText
    m.update( tempText )
    print m.hexdigest()[:6]
    if( str(m.hexdigest())[:6] == '000000'):
        answerNotFound = 0
        print 'Final Answer Hex = ' + str(m.hexdigest())
        print 'Final Answer = ' + str(counter)

