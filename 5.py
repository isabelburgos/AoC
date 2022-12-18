file = open("input5.txt","r")

instructions = []
crates = []
readingCrates = True
for line in file:
    if readingCrates:
        if line == '\n':
            readingCrates = False
            continue
        else: 
            crates.append(line)
    else:
        instructions.append(line)

stacks_list = []
for i in range(0,len(crates[0]),4):
    stack = []
    for row in crates:
        letter = row[i+1:i+2]
        if not (letter == " "):
            stack += letter
    stacks_list.append(stack)


def rearrange(stacks,model = 9000):
    def pick_up_crates(n_to_move,n_from):
        stack_from = stacks[int(n_from)-1]
        crates_picked_up = stack_from[0:n_to_move]
        new_stack = stack_from[n_to_move:]
        stacks[int(n_from)-1] = new_stack
        return crates_picked_up

    def put_down_crates(crates_picked_up,n_to):
        stack_to = stacks[int(n_to)-1]
        if model == 9000:
            new_stack = crates_picked_up[::-1] + stack_to
        if model == 9001:
            new_stack = crates_picked_up + stack_to
        stacks[int(n_to)-1] = new_stack

    def move_crate(n_to_move,n_from,n_to):
        crates_picked_up = pick_up_crates(n_to_move,n_from)
        put_down_crates(crates_picked_up,n_to)

    for instruction in instructions:
        line = instruction.split()
        n_to_move = int(line[1])
        n_from = int(line[3])
        n_to = int(line[5])
        move_crate(n_to_move,n_from,n_to)

    top = []
    for stack in stacks:
        top += stack[0]

    print("".join(top))


one = stacks_list[:]
rearrange(one)
two = stacks_list[:]
rearrange(two, 9001)




