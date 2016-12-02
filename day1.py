# Author: Michael Hawes
# Date: 1 December 2016
# Day 1
import math

def main():

    #===START=============
    direction = 'N'

    #===BASIS===========
    num_list = []
    X = 0
    Y = 0
    count = 0

    #===INPUT============
    numbers = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"

    #===CODE============
    numbers = numbers.split()
    for i in numbers:
        new = i.rstrip(',')
        num_list.append(new)
    while count < len(num_list):

        next_num = num_list[count]
        new_num = next_num[1:len(next_num)]

        #=====NORTH CASE=========================
        if direction == 'N' and next_num[0] == "L":
            X -= int(new_num)
            direction = 'W'
        elif direction == 'N' and next_num[0] == 'R':
            X += int(new_num)
            direction = 'E'

        #======WEST CASE=========================
        elif direction == 'W' and next_num[0] == 'L':
            Y -= int(new_num)
            direction = 'S'
        elif direction == 'W' and next_num[0] == 'R':
            Y += int(new_num)
            direction = 'N'

        #=====SOUTH CASE=========================
        elif direction == 'S' and  next_num[0] == 'L':
            X += int(new_num)
            direction = 'E'
        elif direction == 'S' and next_num[0] == 'R':
            X -= int(new_num)
            direction = 'W'

        #====EAST CASE==========================
        elif direction == 'E' and next_num[0] == 'L':
            Y += int(new_num)
            direction = 'N'
        elif direction == 'E' and next_num[0] == 'R':
            Y -= int(new_num)
            direction = 'S'

        count += 1

    print('Part One:',abs(X) + abs(Y))

if __name__ == '__main__':
    main()
