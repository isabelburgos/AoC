file = open("input10.txt","r")
instruction_list = []
for line in file:
    instruction_list.append(line.split())

instructions = iter(instruction_list)

x_reg = 1
v = 0
signal_strengths = []
i = 0
cur_inst = None
cur_inst_cycles = 0
crt_display_row = ""
crt_rows = []

while i < 240:

    if (cur_inst == "noop" and cur_inst_cycles == 1):
        cur_inst = None
        cur_inst_cycles = 0
    if (cur_inst == "addx" and cur_inst_cycles == 2):
        x_reg += v
        v = 0
        cur_inst = None
        cur_inst_cycles = 0
    i += 1
    print("start cycle",i)
    #print("x:",x_reg)
    if not cur_inst:
        next_inst = next(instructions)
        print(next_inst)
        cur_inst = next_inst[0]
        if next_inst[0] == "noop":
            pass
        if next_inst[0] == "addx":
            v = int(next_inst[1])
    cur_inst_cycles += 1
    signal_strengths.append(x_reg*i)

    chars = len(crt_display_row)
    print(x_reg-1,chars,x_reg+1)
    if x_reg - 1 <= chars <= x_reg +1:
        crt_display_row += "#"
    else:
        crt_display_row += "."
    print(crt_display_row)
    if len(crt_display_row) > 39:
        crt_rows.append(crt_display_row)
        crt_display_row = ""
    



def add_signals(signals):
    total = 0
    for n in signals:
        total += signal_strengths[n-1]
    return total

signals_to_add = [20,60,100,140,180,220]

print(add_signals(signals_to_add))

for row in crt_rows:
    print(row)

    
    