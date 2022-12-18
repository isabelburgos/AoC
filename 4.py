

def countCompleteOverlap():
    file = open("input4.txt","r")
    total = 0
    for row in file:
        r = row.split()[0].split(",")
        elf1 = r[0].split("-")
        elf2 = r[1].split("-")
        elf1_1 = int(elf1[0])
        elf1_2 = int(elf1[1])
        elf2_1 = int(elf2[0])
        elf2_2 = int(elf2[1])
        if elf1_1 <= elf2_1:
            if elf1_2 >= elf2_2:
                total += 1
                continue
        if elf1_1 >= elf2_1:
            if elf1_2 <= elf2_2:
                total += 1
                continue
    print(total)


def countOverlaps():
    file = open("input4.txt","r")
    totalB = 0
    for row in file:
        r = row.split()[0].split(",")
        elf1 = r[0].split("-")
        elf2 = r[1].split("-")
        elf1_1 = int(elf1[0])
        elf1_2 = int(elf1[1])
        elf2_1 = int(elf2[0])
        elf2_2 = int(elf2[1])
        if elf2_1 <= elf1_1 <= elf2_2:
            totalB += 1
        elif elf1_1 <= elf2_1 <= elf1_2:
            totalB += 1
    print(totalB)


countCompleteOverlap()
countOverlaps()
