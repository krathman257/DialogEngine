#reads in a file, parses out dialog
# kblack 4/3/2020

import re


class Reader:
    def __init__(self):
        self.wd = "./" #working directory where file is located
        self.cons = {} #dictionary for concepts
        return
    
    def read_in(self, filename):
        #function to read in input file
        path = self.wd + filename #path to FILE
        file = open(path, "r")
        return file
    
    
    def parse_options(self, opts):
        opt_list = []
        opts = opts.replace("[", "", 1)
        opts = opts.replace("]", "", 1)
        opts = opts.replace("(", "", 1)
        opts = opts.replace(")", "", 1)
        opt_prelist = opts.split()

        tmp = ""
        flag = False
        for chunk in opt_prelist:
            if chunk.startswith("\""): #starts with quote = multiword
                flag = True #raise flag if its a multiword
                tmp = chunk.strip("\"") #strip quote
                continue
            if flag: #still a multiword               
                tmp = tmp + " " + chunk.strip("\"") #add the sentence chunk
                if chunk.endswith("\""): 
                    #reached end of multiword
                    flag = False
                    chunk = tmp #chunk collects the assembled word 
                    tmp = "" #tmp is reset
                else: continue
            opt_list.append(chunk)



        return opt_list

    def tknize(self, line):
        #from krathman:
        #first character = u (rule) -> [[list of string inputs], [list of string outputs], level]
        #first character = & (proposal) -> "thing to say"
        #first character = ~ (concept declaration) -> [concept name, [list of string definitions]]

        dia = re.split(":", line, 1) #splits line at first colon
        dia = tuple(dia)
        corp = []
        cmd = dia[0]
        cmd = cmd.strip()
        flag = False
        
        if cmd.startswith("u"): #rules require user input
            rule = re.split(":", dia[1], 1)
            #rule0 = tirgger/input
            #rule1 = resp/output
            #ensure that lists are parsed as lists
            if rule[0].strip().startswith("(["):
                trig = self.parse_options(rule[0])
            else: 
                trig = rule[0].strip()
                trig = trig.replace(")", "")
                trig = trig.replace("(", "")
                if trig.startswith("~"):#check if ref to concept
                    terms = list(self.cons.keys())
                    if trig.strip("~") in terms:
                        trig = self.cons[trig.strip("~")] 
            if rule[1].strip().startswith("["):
                resp = self.parse_options(rule[1])
            else:
                resp = rule[1]
                if resp.startswith(" "):
                    resp = resp.lstrip()
                if resp.startswith("~"): #check if ref to concept
                    terms = list(self.cons.keys())
                    if resp.strip("~") in terms:
                        resp = self.cons[resp.strip("~")]
            uid = cmd.strip("u")
            if uid.isnumeric():
                return (trig, resp, int(uid))
            else:
                return (trig, resp, 0)
        elif cmd.startswith("&"): #proposal\
            if flag:
                print("No more than one proposal!")
                return (None)
            flag = True
            print("Proposal found")
            prop = self.parse_options(dia[1])

            
        elif cmd.startswith("~"): #concept
            concept = cmd.strip("~") #get the concept name
            defs = self.parse_options(dia[1])
            self.cons[concept] = defs
            return (concept, defs)
    


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
        log = []
        for line in lines:
            dia = self.tknize(line)
            #todo: something with the dialog
            log.append(dia)
        
        print(log)
        return log
        
read = Reader()
read.parse_lines("test.txt")
print (read.cons)