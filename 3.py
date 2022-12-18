file = open("input3.txt","r")

priorities = {"":0}

def generate_priorities(starting_char, starting_priority):
    alphabets=[]
    # starting from the ASCII value of 'a' and keep increasing the value by i.
    alphabets=[(chr(ord(starting_char)+i)) for i in range(26)]
    for i in range(26):
        priorities.update({alphabets[i]:i+starting_priority})

generate_priorities('a',1)
generate_priorities('A',27)


def compare(A,B):
    priority = 0
    match = ""
    intersection = [value for value in A if value in B]
    match = intersection[0]
    priority = priorities[match]    
    return priority


def comparesides():
    total = 0
    for row in file:
        midpt = int((len(row)+1)/2 - 1)
        sectionA = row[0:midpt]
        sectionB = row[midpt:]
        total += compare(sectionA,sectionB)
    print(total)


def comparetriplets(list):
    A = list[0]
    B = list[1]
    C = list[2]
    intersectionAB = [value for value in A if value in B]
    intersectionABC = [value for value in intersectionAB if value in C]
    match = intersectionABC[0]
    priority = priorities[match]    
    return priority


def comparebadges():
    total = 0
    i = 0
    strings = []
    for row in file:
        i += 1
        strings.append(row.strip())
        if i == 3:
            i = 0
            total += comparetriplets(strings)
            strings = []
    print(total)


comparebadges()


    

