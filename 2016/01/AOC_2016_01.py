f = open('AOC_2016_01_input.txt')
directions = f.readline()
#Remove whitespace
directions = directions.replace(" ","")
directions = directions.split(',')

#Build direction and distance
movement = []
for dir in directions:
    #Store L to 0, and R to 1
    movement.append([0 if dir[0] == 'L' else 1, int(dir[1:])])
print directions
print movement

#Store movement direction axis and direction [axis, direction]
direction_map = {'NORTH':[1,1],
                 'SOUTH':[1,-1],
                 'EAST': [0,1],
                 'WEST':[0,-1]}

#distance traveled [x,y]
distance_traveled = [0,0]

direction = 'NORTH'
for next_move in movement:
    if direction == 'NORTH':
        if next_move[0] == 0:
            direction = 'WEST'
        else:
            direction = 'EAST'
    elif direction == 'SOUTH':
        if next_move[0] == 0:
            direction = 'EAST'
        else:
            direction = 'WEST'
    elif direction == 'EAST':
        if next_move[0] == 0:
            direction = 'NORTH'
        else:
            direction = 'SOUTH'
    elif direction == 'WEST':
        if next_move[0] == 0:
            direction = 'SOUTH'
        else:
            direction = 'NORTH'

    distance_traveled[direction_map[direction][0]] += next_move[1] * direction_map[direction][1]
    #print distance_traveled


#print distance_traveled
total_distance = abs(distance_traveled[0]) + abs(distance_traveled[1])
print 'total_distance = ' + str(total_distance)
