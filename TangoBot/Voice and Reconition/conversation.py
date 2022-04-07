from tokenize import String
from rsonlite import loads, simpleparse
#import rules
#from Concept import Concept

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
    def __init__(self, file:str):
        # Open File
        self.root = {}
        self.customVariable = {}
        with open(file, "r") as f:
            # Read line by line
            lines = f.readlines()
            for line in lines:
                colonCount = 0
                tildeCount = 0
                line = line.strip()
                line = re.sub(' {2,}', ' ', line)
                # Remove Whitespaces in the first few characters in the line
                for charac in line:
                    if (charac == ":"):
                        colonCount += 1
                    if (charac == "~"):
                        tildeCount += 1
                # Recondition the line to be easy to be read
                validLine = False
                if((tildeCount == 1 and colonCount >= 1) or (tildeCount == 0 and colonCount == 2)):
                    recondLine = self.recondition_line(line)
                    validLine = True
                if validLine:
                    print(recondLine)
                    
        return
    def recondition_line(self, line):
        # Expected to be u:(...):[... ... ...] or u:(...):...
        allowWhitespace = False
        openSqrBrackets = False
        openParenthesis = False
        openDoubleQuote = False
        newLine = ""
        colonCnt = 0
        for index in range(len(line)):
            charac = line[index]
            if index == 0 and line[0] == 'U':
                charac = 'u'
            if charac == '[':
                openSqrBrackets = True
            if charac == ']' and openSqrBrackets:
                openSqrBrackets = False
            if charac == '(':
                openParenthesis = True
            if charac == ')' and openParenthesis:
                openParenthesis = False
            if charac == '\"':
                openDoubleQuote = True
            if charac == '\"' and openDoubleQuote:
                openDoubleQuote = False
            if colonCnt == 2:
                # Check if a non-whitespace
                if charac == ' ':
                    pass
                else:
                    allowWhitespace = True
            if charac == ":":
                colonCnt += 1
            
            
            if (not (openSqrBrackets or openParenthesis or openDoubleQuote or allowWhitespace) and charac == ' ') :
                pass
            else:
                newLine += charac
        return newLine

    pass

def main():
   Dialog_Engine('demoConvo.txt')
   #Dialog()

main()
