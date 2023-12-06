#--- Day 6: Wait For It ---

with open('2023/06/input.txt') as f:
    times,distances = f.read().splitlines()
times = list(map(int,times.split()[1:]))
distances = list(map(int,distances.split()[1:]))

def get_number_of_winning(time,to_beat):
    for held_time in range(1,time):
        if held_time * (time-held_time) > to_beat:
            low_win = held_time
            return time-(2*low_win)+1

margin_of_error = 1
for i in range(len(times)):
    margin_of_error *= get_number_of_winning(times[i],distances[i])
print('part 1:',margin_of_error)

time = int(''.join(map(str,times)))
distance = int(''.join(map(str, distances)))
print('part 2:',get_number_of_winning(time,distance))
