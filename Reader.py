#reads in a file, parses out dialog
# kblack 4/3/2020

import re

class Reader:
    def __init__(self):
        self.wd = "./" #working directory where file is located
        return
    
    def read_in(self, filename):
        #function to read in input file
        path = self.wd + filename #path to FILE
        file = open(path, "r")
        return file

    def parse_lines(self, fname):
        if fname is "":
            fname = "test.txt"
        # breaks down file to lines
        try:
            file = self.read_in(fname)
            pass
        except :
            print("file not found.")
            return
        
        in_lines = file.readlines() #gets all lines in file as a list

        # now that we have the lines, we need to clean them
        # first, remove all commented lines

        lines = []
        for line in in_lines:
            if re.search("\#.*", line) is None and line is not "\n" and line is not "": #checks if it matches regex, if not, then add it to list of lines
                tmp = line.strip("\n")
                lines.append(tmp)

        
        #so now we can assume that lines list only has relevant (non-commented, non-blank) lines in it

        print(lines)
        return

read = Reader()
read.parse_lines("")


