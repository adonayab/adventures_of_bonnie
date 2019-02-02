import re
import math

with open('bonnie.txt', 'r') as f:
    b_data = f.read()

# extracting the flipped pattern <x, y, z>:[time]
flipped_pattern = re.compile(r'(<\d+.,\d+.,\d+.>)(:)(\[\d*\])')

# positioning time to the correct place [time]:<x, y, z>
fliped_time = flipped_pattern.sub(r'\3\2\1', b_data)

# extracting wrong positioned negative signs
flip_neg_sign = re.compile(r'(\d*)(\b-)')

# flipping negative to the right position
flipped_data = flip_neg_sign.sub(r'\2\1', fliped_time)

# grouping and extracting only the data (of type int no [ or ]) of the time
time_pattern = re.compile(r'\[(\d*)\]')
matches_time = re.findall(time_pattern, flipped_data)

total_time = 0
for match in matches_time:  # calculating the total time
    total_time += int(match)

total_time = total_time / 3600

# extracting x coordinate the number and the sign
data_x = re.compile(r'<(.\d*),.\d*,.\d*>')
# extracting y coordinate the number and the sign
data_y = re.compile(r'<.\d*,(.\d*),.\d*>')
# extracting z coordinate the number and the sign
data_z = re.compile(r'<.\d*,.\d*,(.\d*)>')

matches_x = re.findall(data_x, flipped_data)
matches_y = re.findall(data_y, flipped_data)
matches_z = re.findall(data_z, flipped_data)

dir_x = []
dir_y = []
dir_z = []

for match in matches_x:  # collecting the x coordinates to a list dir_x
    dir_x.append(int(match))
for match in matches_y:  # collecting the y coordinates to a list dir_y
    dir_y.append(int(match))
for match in matches_z:  # collecting the z coordinates to a list dir_z
    dir_z.append(int(match))

# inserting the 0 coordinate to the start of list of x coordinates
dir_x.insert(0, 0)
# inserting the 0 coordinate to the start of list of y coordinates
dir_y.insert(0, 0)
# inserting the 0 coordinate to the start of list of z coordinates
dir_z.insert(0, 0)

# for storing list of distances traveled from point a(x,y,z) to b(x,y,z)
dist_list = []
# because the length of dir_x dir_y dir_z is the same i took any of them
for i in range(len(dir_x) - 1):
    # distance formula in the x,y,z plane from a(x1, y1, z1) to b(x2, y2, z2)
    # is sqrt of (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2
    a_to_b = math.sqrt(math.pow((dir_x[i + 1] - dir_x[i]), 2) + math.pow((dir_y[i + 1] - dir_y[i]), 2) + math.pow(
        (dir_z[i + 1] - dir_z[i]), 2))
    # collecting the distances to dist_list
    dist_list.append(a_to_b)

total_dist = sum(dist_list)

speed_of_boonie = total_dist / total_time

print('The total distance boonie traveled is: ', total_dist)
print('The average speed of boonie was: ', speed_of_boonie)
