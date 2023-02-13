### After struggling with this one for a while
### I decided to make an animation to help debug visually
### The animation worked for small grids of test data
### but when it came to the actual data it slowed WAY down
### The new code I wrote got the correct answer
### so I stopped trying to make the animation work


import numpy as np
from matplotlib import pyplot as plt

file = open("input8.txt","r")

data = []
gridsize = 0

for row in file:
    #turn each line into a list of numbers
    r = [int(x) for x in list(row.strip())]
    data.append(list(r))
    #count up each row to get the size of the array
    #   it's already known to be a square 
    #   so this is also the length of each row
    gridsize += 1

#put raw data into np.array format
heights = np.array(data)
#create an array of the same shape, full of ones
visibility = np.zeros((gridsize,gridsize))

visibility_l_to_r = np.zeros((gridsize,gridsize))
visibility_t_to_b = np.zeros((gridsize,gridsize))
visibility_b_to_t = np.zeros((gridsize,gridsize))
visibility_r_to_l = np.zeros((gridsize,gridsize))



from matplotlib.animation import FuncAnimation

fig = plt.figure(num=1)
ax = fig.add_subplot(231)

fig2 = plt.figure(num=1)
ax2 = fig.add_subplot(232)

fig3 = plt.figure(num=1)
ax3 = fig.add_subplot(233)

fig4 = plt.figure(num=1)
ax4 = fig.add_subplot(235)

fig5 = plt.figure(num=1)
ax5 = fig.add_subplot(236)

fig6 = plt.figure(num=1)
ax6 = fig.add_subplot(234)


label = ax.text(0, 0, "hello", fontsize=20, color="black")


def search_scenic(row,col):
    current_tree_height = heights[row,col]
    current_tree_visibility_l_r = 0
    current_tree_visibility_t_b = 0
    current_tree_visibility_b_t = 0
    current_tree_visibility_r_l = 0
    #print("current tree height", current_tree_height)
    for tree_height in heights[row][col+1:]:
        #print("tree height", tree_height)
        current_tree_visibility_l_r += 1
        #print("visibility l r", current_tree_visibility_l_r)
        visibility_l_to_r[row,col] = current_tree_visibility_l_r
        if tree_height >= current_tree_height:
            break
    
    if col > 0:
        for tree_height in heights[row][col-1::-1]:
            #print("tree height", tree_height)
            current_tree_visibility_r_l += 1
            #print("visibility r l", current_tree_visibility_r_l)
            visibility_r_to_l[row,col] = current_tree_visibility_r_l
            if tree_height >= current_tree_height:
                break

    for n in range(row+1,gridsize):
       # print("n",n)
        tree_height = heights[n][col]
        #print("tree height", tree_height)
        current_tree_visibility_t_b += 1
       # print("visibility t b", current_tree_visibility_t_b)
        visibility_t_to_b[row,col] = current_tree_visibility_t_b
        if tree_height >= current_tree_height:
            break
    
    if row > 0:
        for n in range(row-1,-1,-1):
            #print("n",n)
            tree_height = heights[n][col]
            #print("tree height", tree_height)
            current_tree_visibility_b_t += 1
            #print("visibility b t", current_tree_visibility_b_t)
            visibility_b_to_t[row,col] = current_tree_visibility_b_t
            if tree_height >= current_tree_height:
                break
            
def update(i):
    #print("i",i)
    row = int(i/gridsize)
    #print("row",row)
    col = int(i%gridsize)
    #print("col",col)
    search_scenic(row,col)
    newarray = np.concatenate((heights[:row],[visibility[row]],heights[row+1:]))
    ax.imshow(newarray)
    ax.set_axis_off()

def update2(i):
    ax2.imshow(visibility_l_to_r)
    label.set_text("%.2f" % i)
    ax2.set_axis_off()

def update3(i):
    ax3.imshow(visibility_t_to_b)
    ax3.set_axis_off()

def update4(i):
    ax4.imshow(visibility_b_to_t)
    ax4.set_axis_off()

def update5(i):
    ax5.imshow(visibility_r_to_l)
    ax5.set_axis_off()


def update6(i):
    score_array = visibility_l_to_r*visibility_r_to_l*visibility_t_to_b*visibility_b_to_t
    ax6.imshow(score_array)

#anim = FuncAnimation(fig, update, frames=gridsize*gridsize, interval=1, repeat = False)
#anim2 = FuncAnimation(fig2, update2, frames=gridsize*gridsize, interval=10,repeat = False)
#anim3 = FuncAnimation(fig3, update3, frames=gridsize*gridsize, interval=10,repeat = False)
#anim4 = FuncAnimation(fig4, update4, frames=gridsize*gridsize, interval=10,repeat = False)
#anim5 = FuncAnimation(fig5, update5, frames=gridsize*gridsize, interval=10,repeat = False)
#anim6 = FuncAnimation(fig6, update6, frames=gridsize*gridsize, interval=10,repeat = False)

#plt.show()

for i in range(gridsize*gridsize):
    row = int(i/gridsize)
    col = int(i%gridsize)
    search_scenic(row,col)


score_array = visibility_l_to_r*visibility_r_to_l*visibility_t_to_b*visibility_b_to_t
print(np.amax(score_array))

