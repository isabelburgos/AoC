class MyItem:
    def __init__(self,worry):
        self.worry = worry

class Monkey:
    def __init__(self,number,starting_items,operation,test,if_true,if_false):
        self.number = number
        self.starting_items = starting_items
        self.operation = self.parse_operation(operation)
        self.test = test
        self.items_list = []
        for item in self.starting_items:
            self.items_list.append(MyItem(item))
        self.if_true = if_true
        self.if_false = if_false
        self.inspection_count = 0
    def parse_operation(self,operation):
        ops = operation.split()
        n = ops[2] #get the number on the other side of the operation
        if n == "old":
            if ops[1] == "*":
                return "s","s" # old * old = old ^2
            elif ops[1] == "+":
                return "m",2 #old + old = 2 * old
        else:
            if ops[1] == "*":
                return "m",int(n) # old * n
            elif ops[1] == "+":
                return "a",int(n) #old + n
    def take_turn(self):
        print("==Monkey number",self.number,"takes its turn==")
        for item in self.items_list:
            print("monkey inspects an item with", item.worry, "worry")
            self.inspection_count += 1
            self.do_operation(item)
            item.worry = int(item.worry/3)
            print("dividing by 3, worry:", item.worry)
            next_monkey_num = self.do_test(item)
            next_monkey = monkeys[next_monkey_num]
            next_monkey.items_list.append(item)
            print("item with worry",item.worry,"thrown to monkey",next_monkey_num)
        self.items_list = []
            
    def do_operation(self,item):
        op, n = self.operation
        if op == "m":
            item.worry = int(item.worry) * n
            print("multiplying by", n,", worry",item.worry)
        elif op == "a":
            item.worry = int(item.worry) + n
            print("adding", n, ", worry:",item.worry)
        elif op == "s":
            item.worry = int(item.worry)*int(item.worry)
            print("squaring, worry:",item.worry)
    def do_test(self,item):
        # remainder of worry level / test
        mod = item.worry%self.test
        if mod == 0:
            print("current worry level divisble by",self.test)
            return self.if_true
        else:
            print("current worry level not divisble by",self.test)
            return self.if_false



monkeys = []

file = open("input11.txt","r")
for line in file:
    if line.startswith("Monkey"):
        ## get the number after "Monkey"
        number = int(line.removeprefix("Monkey ").replace(":",""))
        ## get the list of numbers after "Starting Items:"
        starting_items_list = list(next(file).split(":")[1].split(","))
        ## convert to list of ints, strip spaces and newlines
        starting_items = [int(x.strip()) for x in starting_items_list]
        ## get the characters after "Operation: new = "
        operation = next(file).split(":")[1].split("=")[1].strip()
        ## get the number after "Test: divisible by "
        test = int(next(file).split(": divisible by ")[1].strip())
        ## get the number after "If true: throw to monkey"
        if_true = int(next(file).split(": throw to monkey ")[1].strip())
        ## get the number after "If false: throw to monkey"
        if_false = int(next(file).split(": throw to monkey ")[1].strip())
        monkeys.append(Monkey(number,starting_items,operation,test,if_true,if_false))

def do_round():
    for monkey in monkeys:
        monkey.take_turn()

def print_status():
    print("here's the status")
    for monkey in monkeys:
        print("Monkey",monkey.number,": ",[item.worry for item in monkey.items_list])
        print("Monkey",monkey.number,"inspected items",monkey.inspection_count,"times")

def monkey_business(n):
    i = 0
    while i < n:
        i += 1
        print("=======ROUND",i,"=======")
        do_round()
        print("Status..")
        print_status()

    monkey_counts = []
    for monkey in monkeys:
        print("Monkey",monkey.number,"inspected items",monkey.inspection_count,"times")
        monkey_counts.append(monkey.inspection_count)
        
    monkey_counts.sort(reverse=True)
    monkey_business = monkey_counts[0]*monkey_counts[1]
    print("Total monkey business:", monkey_business)

monkey_business(20)
