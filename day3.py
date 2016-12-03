# Author: Michael Hawes
# Date: 3 December 2016
# day3.py

class Triangles:

    def check_if_valid(self, data):
        """Checks to see if the sum of any two sides is larger than the remaining side"""
        count = 0
        for numbers in data:
            sum_one = int(numbers[0]) + int(numbers[1])  # remaining side = 3
            sum_two = int(numbers[0]) + int(numbers[2])  # remaining side = 2
            sum_three = int(numbers[1]) + int(numbers[2])  # remaining side = 1
            if sum_one > int(numbers[2]) and sum_two > int(numbers[1]) and sum_three > int(numbers[0]):
                count += 1
            else:
                pass
        return count


    def read_file(self):
        """Reads in the file and formats to appropriate form"""
        num_list = []
        infile = open('input.txt', 'r')
        infile = infile.readlines()
        for line in infile:
            line = line.rstrip('\n')
            line = line.split()
            num_list.append(line)
        return num_list


def main():
    T = Triangles()
    data = T.read_file()
    print(T.check_if_valid(data))

if __name__ == '__main__':
    main()
