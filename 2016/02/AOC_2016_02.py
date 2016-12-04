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

print code
