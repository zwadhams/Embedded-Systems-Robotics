from tokenize import String
from rsonlite import loads, simpleparse

class Dialog_Engine:

    def createTree(self, node):
        if isinstance(node, str):
            return node
        elif isinstance(node, dict):
            for key in node:
                assert (key.endswith(':') or key.endswith('\n'), key)
            return dict((key[:-1], fixup(value)) for key, value in node.items())
        else:
            assert isinstance(node, (list, str))
            result = {}
            for item in node:
                if isinstance(item, str):
                    assert not (item.endswith(':') or key.endswith('\n'))
                    assert result.setdefault(item, None) is None
                else:
                    for key, value in fixup(item).items():
                        assert result.setdefault(key, value) is value
        return result

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

            mystring = '''
            node1:
                node1
                node2:
                    node1
            node2:
                node1
                node2
                node3:
                    node1:
                        node1
                    node2:
                        node1
                        node2
            '''

            tree = self.createTree(f)
            print(tree)

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

main()
