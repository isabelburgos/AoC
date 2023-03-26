## ansi color reference

class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    end = '\033[0m'

class bg:
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
    end = '\033[0m'

directions = {
    "U":[1,0],"D":[-1,0],"R":[0,1],"L":[0,-1]
}

## color coded output
tail_symbol = fg.red + "T" + fg.end
head_symbol = fg.green + "H" + fg.end
start_symbol = fg.orange + "s" + fg.end
hash_symbol = fg.purple + "#" + fg.end

## starting positions
head = [0,0]
tail = [0,0]
start = [0,0]

class Grid(object):
    def __init__(self,dimensions=[5,5]):
        self.dimension_y, self.dimension_x = dimensions
        self.origin = [0,0]
        self.contents = self.create_blank()
        
    def create_blank(self):
        rows = []
        for y in range(0,self.dimension_y):
            row = ["."]*self.dimension_x
            rows.append(row)
        return rows

    def place(self,symbol,location):
        location_y, location_x = location
        origin_y, origin_x = self.origin

        ### if position is out of range, add extra columns or rows
        ### if position is out of range and negative,
        # add extra columns or rows and shift the origin
        #print("location:",location_y,location_x)
        #print("dimension:",self.dimension_y,self.dimension_x)
        #print("origin",origin_y,origin_x)
        if location_y  > self.dimension_y - origin_y - 1:
            self.extend([location_y - self.dimension_y + origin_y + 1,0])
        if location_x  > self.dimension_x - origin_x - 1:
            self.extend([0,location_x - self.dimension_x + origin_x +1])

        if location_y < (-1)*origin_y:
            offset = origin_y + location_y
            origin_y = origin_y - offset
            self.extend([offset,0])
        if location_x < (-1)*origin_x:
            offset = origin_x + location_x
            origin_x = origin_x - offset
            self.extend([0,offset])
        
        ## save the new origin
        self.origin = [origin_y, origin_x]
        ## re-reference location to the origin
        location_x = location_x + origin_x
        location_y = location_y + origin_y

        self.contents[location_y][location_x] = symbol
    
    def display(self):
        origin_y, origin_x = self.origin
        self.contents[origin_y][origin_x] = start_symbol
        for row in self.contents[::-1]:
            print(" ".join(row))
        print("   ")

    def extend(self,direction):
        #print("Extending by", direction)
        #print("dimensions: ",self.dimension_y,self.dimension_x)
        direction_y, direction_x = direction
        ### add rows
        if direction_y < 0:
            self.contents = [self.dimension_x*["."]]*abs(direction_y) + self.contents
            self.dimension_y += abs(direction_y)
        if direction_y > 0:
            self.contents = self.contents + [self.dimension_x*["."]]*direction_y
            self.dimension_y += direction_y

        ### add columns
        if direction_x < 0:
            for y in range(0,self.dimension_y):
                self.contents[y] = ["."]*abs(direction_x) + self.contents[y]
            self.dimension_x += abs(direction_x) 
        if direction_x > 0:
            for y in range(0,self.dimension_y):
                self.contents[y] = self.contents[y] + ["."]*direction_x
            self.dimension_x += direction_x


class Rope(object):
    def __init__(self,head,tail):
        self.head_y, self.head_x = head
        self.tail_y, self.tail_x = tail
        self.gridDisplay = Grid()

    def move_head(self,direction,distance):
        move_y, move_x = directions[direction]
        for i in range(distance):
            self.head_y += move_y
            self.head_x += move_x
            self.move_tail()
            self.display()
    
    def display(self):
        self.gridDisplay.contents = self.gridDisplay.create_blank()

        self.gridDisplay.place(head_symbol,[self.head_y,self.head_x])
        #self.gridDisplay.display()

        self.gridDisplay.place(tail_symbol,[self.tail_y,self.tail_x])
        #self.gridDisplay.display()

        tail_visited.place(hash_symbol,[self.tail_y,self.tail_x])
        #tail_visited.display()
    
    def move_tail(self):
        offset = [self.head_y-self.tail_y, self.head_x - self.tail_x]
        #print(offset)
        if (offset == [0,0]) or (offset == [1,1]):
            pass
        ## horizontal and vertical movement
        if offset == [0,2]:
            self.tail_x += 1
        if offset == [0,-2]:
            self.tail_x -= 1
        if offset == [2,0]:
            self.tail_y += 1
        if offset == [-2,0]:
            self.tail_y -= 1
        ## diagonal movement
        if (offset == [2,1]) or (offset == [1,2]):
            self.tail_y += 1
            self.tail_x += 1
        if (offset == [-2,1]) or (offset == [-1,2]):
            self.tail_y -= 1
            self.tail_x += 1
        if (offset == [2,-1]) or (offset == [1,-2]):
            self.tail_y += 1
            self.tail_x -= 1
        if (offset == [-2,-1]) or (offset == [-1,-2]):
            self.tail_y -= 1
            self.tail_x -= 1
        


rope = Rope(head,tail)
#rope.display()

tail_visited = Grid()
tail_visited.place(start_symbol,start)


file = open("input9.txt","r")
instructions = []
for line in file:
    instructions.append(line.split())


for instruction in instructions:
   #print("== " + " ".join(instruction) + " ==")
   direction = instruction[0]
   distance = int(instruction[1])
   rope.move_head(direction,distance)


#tail_visited.display()
hashes = [num for elem in tail_visited.contents for num in elem]
print(hashes.count(hash_symbol) + 1)