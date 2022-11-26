from typing import  *
import os
import sys 

# Add working directory to pythonpath
parentdir = os.path.split(os.getcwd())[0]
sys.path.append(parentdir)

import main

class Day1(main.Main):

    def part_one(self):
        values = self.parse_line()
        ans = self.total_increases(values, 1)
        print(ans)

    def part_two(self):
        values = self.parse_line()
        ans = self.total_increases(values, 3)
        print(ans)

    def total_increases(self, input: List[str], window_size: int):
        count = 0
        for i in range(window_size, len(input)):
            if int(input[i]) > int(input[i - window_size]):
                count = count + 1
        return count


if __name__ == '__main__':
    ans = Day1()
    ans.part_one()
    ans.part_two()




