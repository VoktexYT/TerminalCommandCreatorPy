"""

The 'Split' class is using for separate each element in Script

Example:
    > commit -m "fist commit"
    > [[commit, -m, "fist commit"]]

    > cd ../ && mkdir project1
    > [[cd, ../], [mkdir, project1]]

"""


class Split:

    # separate element with space and if this is string keep space
    def splits(self, line):
        elements = []
        strings = ""
        inString = False

        for char in line:
            if char == " " and not inString:
                elements.append(strings)
                strings = ""
            elif char == '"':
                strings += '"'
                if inString:
                    inString = False
                else:
                    inString = True
            else:
                strings += char
        else:
            elements.append(strings)

        return self.separate_command(elements)

    # separate each Script if there are keyword '&&', 'and', '/+/'
    def separate_command(self, line):
        allCommand = []
        eachElement = []

        for el in line:
            if el in ['&&', 'and', '/+/']:
                allCommand.append(eachElement)
                eachElement = []
            else:
                eachElement.append(el)
        else:
            allCommand.append(eachElement)

        return allCommand
