# --- Day 2: Bathroom Security ---
#
# You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to
# use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search
# the front desk for the code.
#
# "In order to improve security," the document you find says, "bathroom codes will no longer be written down.
# Instead, please memorize and follow the procedure below to access the bathrooms."
#
# The document goes on to explain that each button to be pressed can be found by starting on the previous button and
#  moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right.
# Each line of instructions corresponds to one button, starting at the previous button (or, for the first line,
# the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button,
# ignore it.
#
# You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom.
# You picture a keypad like this:
#
# 1 2 3
# 4 5 6
# 7 8 9
# Suppose your instructions are:
#
# ULL
# RRDDD
# LURDL
# UUUUD
# You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
# Starting from the previous button ("1"), you move right twice (to "3") and then down three times
# (stopping at "9" after two moves and ignoring the third), ending up with 9.
# Continuing from "9", you move left, up, right, down, and left, ending with 8.
# Finally, you move up four times (stopping at "2"), then down once, ending with 5.
# So, in this example, the bathroom code is 1985.
#
# Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?

#Read input file
input_file = open('AOC_2016_02_input.txt','r')

#Store each line as a string
input_commands = []
line = input_file.readline().rstrip()
while line != "":
    input_commands.append(line)
    line = input_file.readline().rstrip()
print input_commands
print len(input_commands)


#Store the code
code = []

#Build a 3x3 grid
keypad = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#Start on the 5 key [1,1]
location = [1,1]

for command_line in input_commands:

    position = 0
    print 'command line length = ' + str(len(command_line))

    while position < len(command_line):
        print 'position = ' + str(position)
        command = command_line[position]
        #Map directions to operations
        #Locations cannot exeed 0 or 2
        print command

        if command == 'D':
            location[0] = min((location[0] + 1),2)
        if command == 'U':
            location[0] = max((location[0] - 1),0)
        if command == 'R':
            location[1] = min((location[1] + 1),2)
        if command == 'L':
            location[1] = max((location[1] - 1),0)
        print location
        position += 1

    code.append(keypad[location[0]][location[1]])

print 'Code for Part 1: ' + str(code)

# #Part 2
# --- Part Two ---
#
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy
# conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay,
# the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours
# of bathroom-keypad-design meetings:
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
# You still start at "5" and stop when you're at an edge, but given the same instructions as above,
# the outcome is very different:
#
# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input, what is the correct bathroom code?
keypad2 = [['*','*','1','*','*'],
           ['*','2','3','4','*'],
           ['5','6','7','8','9'],
           ['*','A','B','C','*'],
           ['*','*','D','*','*']]

max_position = 4
location = [1,1]
del code[:]
for command_line in input_commands:

    position = 0
    print 'command line length = ' + str(len(command_line))

    while position < len(command_line):
        print 'position = ' + str(position)
        command = command_line[position]

        print command

        new_pos = 0
        if command == 'D':
            new_pos = min((location[0] + 1),max_position)
            if (keypad2[new_pos][location[1]]) != '*':
                location[0] = new_pos
        if command == 'U':
            new_pos = max((location[0] - 1),0)
            if (keypad2[new_pos][location[1]]) != '*':
                location[0] = new_pos
        if command == 'R':
            new_pos = min((location[1] + 1),max_position)
            if (keypad2[location[0]][new_pos]) != '*':
                location[1] = new_pos
        if command == 'L':
            new_pos = max((location[1] - 1),0)
            if (keypad2[location[0]][new_pos]) != '*':
                location[1] = new_pos
        print location
        position += 1

    code.append(keypad2[location[0]][location[1]])

print 'Code for Part 2: ' + str(code)
