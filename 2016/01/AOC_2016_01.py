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
direction_vec = [1,1]
direction_map = [['NORTH', [1,1]],
                 ['SOUTH', [1,-1]],
                 ['EAST',  [0,1]],
                 ['WEST',  [0,-1]]]

#distance traveled [x,y]
distance_traveled = [0,0]

last_direction = 'NORTH'
for next_move in movement:
    if last_direction == 'NORTH':
        if next_move[0] == 0:
            direction_vec = [0,-1]
            last_direction = 'WEST'
        else:
            direction_vec = [0,1]
            last_direction = 'EAST'
    elif last_direction == 'SOUTH':
        if next_move[0] == 0:
            direction_vec = [1,-1]
            last_direction = 'EAST'
        else:
            direction_vec = [0,-1]
            last_direction = 'WEST'
    elif last_direction == 'EAST':
        if next_move[0] == 0:
            direction_vec = [1,1]
            last_direction = 'NORTH'
        else:
            direction_vec = [1,-1]
            last_direction = 'SOUTH'
    elif last_direction == 'WEST':
        if next_move[0] == 0:
            direction_vec = [1,-1]
            last_direction = 'SOUTH'
        else:
            direction_vec = [1,1]
            last_direction = 'NORTH'

    #print distance_traveled[next_move[0]]
    #print last_direction
    #print direction_vec
    distance_traveled[direction_vec[0]] += next_move[1]*direction_vec[1]
    print distance_traveled


print distance_traveled
total_distance = abs(distance_traveled[0]) + abs(distance_traveled[1])
print 'total_distance = ' + str(total_distance)

#Store x,y values

#Add x,y blocks

