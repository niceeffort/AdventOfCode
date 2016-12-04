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
location_map = []

direction = 'NORTH'
duplicate_found = 0
first_duplicate = []
positions = []
count = 0
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


    step = 1

    while step <= next_move[1]:
        distance_traveled[direction_map[direction][0]] += 1 * direction_map[direction][1]

        #print 'positions = ' + str(positions)

        print 'count = ' + str(count)
        if duplicate_found == 0:
            print 'dist_traveled =' + str(distance_traveled)
            print 'positions = ' + str(positions)
            if distance_traveled in positions:
                print 'Dupilcate Found!'
                first_duplicate = [distance_traveled[0],distance_traveled[1]]
                print 'first_duplicate' + str(first_duplicate)
                duplicate_found = 1
            else:
                positions.append([distance_traveled[0], distance_traveled[1]])

        step +=1
        count +=1
    #print distance_traveled

    #store a grid of every location you have visited. Once you find the match calculate the distance from 0


    #look for existing position
    # if duplicate_found == 0:
    #     if distance_traveled in location_map:
    #         print 'location_found'
    #         print distance_traveled
    #         first_duplicate = [distance_traveled[0],distance_traveled[1]]
    #         print 'first_duplicate' + str(first_duplicate)
    #         duplicate_found = 1

    location_map.append([distance_traveled[0],distance_traveled[1]])
    #print 'loc_map' + str(location_map)


print distance_traveled
total_distance = abs(distance_traveled[0]) + abs(distance_traveled[1])
print 'total_distance = ' + str(total_distance)
print location_map

print 'first_duplicate' + str(first_duplicate)
duplicate_distance = abs(first_duplicate[0]) + abs(first_duplicate[1])
print 'position_set' + str(positions)
print 'duplicate_distance = ' + str(duplicate_distance)


