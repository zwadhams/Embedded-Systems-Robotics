from tokenize import String
import regex as re
   
class Dialog_Engine:

    storeList = []
    
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
                comment = 0
                line = line.strip()
                line = re.sub(' {2,}', ' ', line)
                # Remove Whitespaces in the first few characters in the line
                for charac in line:
                    if (charac == ":"):
                        colonCount += 1
                    if (charac == "~"):
                        tildeCount += 1
                    
                if (line[0] == "#"):
                        comment += 1      
                # Recondition the line to be easy to be read
                validLine = False
                if((tildeCount == 1 and colonCount >= 1) or (tildeCount == 0 and colonCount == 2)):
                    recondLine = self.recondition_line(line)
                    validLine = True
                if comment == 1:
                    print("Comment detected")
                elif validLine:
                    print(recondLine)
                    self.storeList.append(self.createList(recondLine))
                else:
                    print("Error detected")
                    

        print(self.storeList)

        self.checkLines(self.storeList, 0, 1)
        
                    
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

    def createList(self, line):
        myList = []

        strip_lines = line.strip()
        listli = strip_lines.split()
        #print(listli)
        m = myList.append(listli)

        return listli

    pass

    def checkLines(self, l, i, count):
        
        #for i in range(len(l)):
        if (l[i][0][0] == '~'):
            print("tilde hit")
            
        elif (l[i][0][0]) == 'u':
            if ('~' in l[i][0]):
                string = " tilde found"
            else:
                string = ""
            if(l[i][0][1]) == chr(count + 48):
                string = ""
                print("hit u" + chr(count + 48), string)
               
                if (l[i + 1][0][1]) == chr(count + 48):
                    if ('~' in l[i][0]):
                        string = " tilde found"
                    else:
                        string = ""
                    print("hit u" + chr(count + 48), string)
                    i += 1
                    string = ""
                count += 1
                
               
            else:
                if ('~' in l[i][0]):
                    string = " tilde found"
                else:
                    string = ""
                print("hit u" + string)
                count = 1

            
        if (len(l)-1 > i):
            i += 1
            self.checkLines(l, i, count)

    print(len(storeList))
        

def main():
   Dialog_Engine('demoConvo.txt')

main()
