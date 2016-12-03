# Author: Michael Hawes
# Date: 2 December 2016
# Day 2

#======KEY=================
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
#=========================
num_pad_two = [['x', 'x', '1', 'x', 'x'],
               ['x', '2', '3', '4', 'x'],
               ['5', '6', '7', '8', '9'],
               ['x', 'A', 'B', 'C', 'x'],
               ['x', 'x', 'D', 'x', 'x']]

class Helpers:

    def algorithm(self, data):
        """determines a 5 digit number based off movements within num_pad"""
        number = []
        x = 1
        y = 1
        for line in data:
            for j in line:
                if j == 'U':
                    y = max(0, y - 1)
                elif j == 'R':
                    x = min(2, x + 1)
                elif j == 'L':
                    x = max(0, x - 1)
                elif j == 'D':
                    y = min(2, y + 1)
            number.append(num_pad[y][x])
        return number

    def import_data(self):
        """Reads in text file and formats accordingly"""
        data = []
        infile = open("input.txt", "r")
        lines = infile.readlines()
        #lines = ['ULL','RRDDD','LURDL', 'UUUUD']  # test file
        for i in lines:
            new = i.rstrip('\n')
            data.append(new)
        return data


def main():
    H = Helpers()
    data = H.import_data()
    print('Part One:',H.algorithm(data))

if __name__ == '__main__':
    main()
