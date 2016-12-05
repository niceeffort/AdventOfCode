# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes
# up this part of Easter Bunny HQ. This must be a graphic design department;
# the walls are covered in specifications for triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these
# aren't triangles. You can't help but mark the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the remaining side.
# For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?

#def countTriangles(the_codes):


#open the file
f = open('AOC_2016_03_input.txt', 'r')

#store the data in a list
code_strings = f.readlines()

code_list = []

#parse lines into an array of groups
for code in code_strings:
    #split the stings and use map to convert to int
    code_list.append(map(int, code.split()))

number_of_triangles = 0
#count the valid triangles
for code in code_list:
    a,b,c = code
    if( a + b > c and a + c > b and b + c > a ):
        number_of_triangles += 1

print 'Part 1: Number of triangles = ' + str(number_of_triangles)

# --- Part Two ---
#
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
