import os 
import sys
from typing import * 


class Main:
    def __init__(self):
        filename = sys.argv[1]
        self.filename = filename
   
    def print_input(self):
        with open(self.filename) as f:
            for line in f:
                print(line[:-1])


    def parse_line(self) -> List[str]:
        """
        Parse input line by line into a list ignoring trailing newline characters.
        """
        lines = []
        with open(self.filename) as f:
            for line in f: 
                line = line[:-1]
                lines.append(line)
        return lines

if __name__ == '__main__':
    main = Main()
    main.print_input()



