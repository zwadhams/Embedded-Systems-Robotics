from tokenize import String
from rsonlite import loads, simpleparse
from Rule import Rule
from Concept import Concept

class Dialog:

    def openFile(self):
        count = 0
        fin = open("demoConvo.txt", "r")

        for line in fin:
            count += 1
            self.parseInput(line, count)
        pass

    def parseInput(self, line, count):
        rule = line.split(':')
        if len(rule) != 3:
            if rule[0] == 'proposal':
                print("Found proposal")
            elif rule[0][:1] == '#':
                v = 'comment, ignore'
            elif rule[0][:1] == "~":
                x = Concept(rule)
                Dialog.concepts.append(x)
            else:
                print("You have an error on line ", count)
        else:
            if (rule[0] == 'u'):
                self.current = Rule(rule, 0, self)
                self.rules.append(self.current)

    concepts = []
    def __init__(self):
        self.rules = []
        self.lastTalk = None
        self.openFile()
        pass

   
 

class Dialog_Engine:

    

    def checULine(self, line):
        count = 0
        
        

    def responseParse(self, line):
        print('hit responseParse')
        if line[1] == ':':
            pass
            #we need some functionality to check the stuff
        #runs command if the

    def definitionParse(self, line):
        print('hit defParse')
        # this definies a greeting variable and is given three values in square brackets
        pass

    def __init__(self, file:String):
        # Open File
        with open(file, "r") as f:
            # Read line by line
            lines = f.readlines()


            for line in lines:
                line = line.strip()
            # Check U, u2, u3, ... un,(not case sensitive) Ignore lines with invalid syntax and comments
            # Comments are marked with # at the beginning of the line
                if line[0] == "#": # Comments
                    print('hit comment')
                    pass
                elif line[0] == "u":
                    self.responseParse(line) #will eventually parse through the
                elif line[0] == "~":
                    self.definitionParse(line)
                #does something, not sure what that symbol means

                else:
                    pass

        # Then parse character by character to find defined characters
        # "" ~ [] _ $  Check the 2022DialogAssignment Document
        # Ignore ? , . ! (Special characters)

        return

    pass

def main():
   Dialog_Engine('demoConvo.txt')
   Dialog()

main()

