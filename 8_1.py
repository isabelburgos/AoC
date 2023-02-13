### Contains the code that correctly solved the first problem
### and code that did not solve the second problem
### so I ended up starting fresh


import numpy as np
from matplotlib import pyplot as plt

file = open("input8_real.txt","r")

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
visibility = np.ones((gridsize,gridsize))


def search(search_array):
    for n in range(gridsize):
        #print("n:",n)
        max_left = -1
        max_right = -1
        max_top = -1
        max_bottom = -1
        for i in range(gridsize):
            #print("i:",i)
            val_left = search_array[n,i]
            #print("left:",val_left)
            val_right = search_array[n,-i-1]
            #print("right:",val_right)
            val_top = search_array[i,n]
            #print("top:",val_top)
            val_bottom = search_array[-i-1,n]
            #print("bottom:",val_bottom)
            
            if val_left > max_left:
                #print(val_left,"L is >",max_left)
                max_left = val_left
                visibility[n,i] = 0
            if val_right > max_right:
                #print(val_right,"R is >",max_right)
                max_right = val_right
                visibility[n,-i-1] = 0
                #print(visibility)
            if val_top > max_top:
                #print(val_top,"T is >",max_top)
                max_top = val_top
                visibility[i,n] = 0
                #print(visibility)
            if val_bottom > max_bottom:
                #print(val_bottom,"B is >",max_bottom)
                max_bottom= val_bottom
                visibility[-i-1,n] = 0
                #print(visibility)


search(heights)
total_visible = gridsize*gridsize - np.sum(visibility)
## prints the answer for part 1
print(total_visible)

# get a visual just for fun
plt.matshow(heights)


def search_scenic(search_array,visibility_array,debug = False):
    #for each row in the grid of heights
    for n in range(1,gridsize):
        if n == 37:
            print("n = 37!")
            debug = True
        else:
            debug = False
        if debug:
            print("Searching the following row:",search_array[n])
        #array to hold all trees with views
        unblocked_trees = np.array([[0,-1,-1]])
        # starting values:
        #   index in the row: 0
        #   tree height: -1
        #   visibility distance: -1

        

        # for each tree in the row
        for i in range(gridsize):
            if debug:
                print("*New iteration, i = ",i)
                        # iterate through the tallest_trees list again
            # this time without breaking
            #print("scoring")
            
            for t in range(len(unblocked_trees)):
                unblocked_trees[-t-1,2] += 1
                #if debug:
                    #print("**Updated visibility for unblocked trees",unblocked_trees)
                # for all trees in the list of tallest trees
                position = unblocked_trees[-t-1,0]
                visibility_array[n,position] = unblocked_trees[-t-1,2]
                #if debug:
                    #print("**Updated stored visibility at position",position,": ", visibility_array[n])
                #store the visibility score for each tree 
                # at the matching position in the visibility scores array
                
                # increment the visibility score by 1

            if debug:
                print("*Unblocked trees up to position",i,": ",unblocked_trees)
            # get the height of the tree
            current_tree_height = search_array[n,i]
            if debug:
                print("*Current tree height:", current_tree_height)
            #print("Current tree is",current_tree_height,"tall, located at",i)




            # for all stored unblocked trees (where view distance is still counting up)
            t = 0
            while t < len(unblocked_trees):
                stored_tree_index = -t-1 #-t-1
                if debug:
                    print("**Checking stored tree at index",stored_tree_index)
                
                #starting from the right end of the list (the shortest tree) at position -t-1
                # get that tree's height at position 1
                stored_tree_visibility = unblocked_trees[stored_tree_index,2]
                stored_tree_height = unblocked_trees[stored_tree_index,1]
                stored_tree_position = unblocked_trees[stored_tree_index,0]
                

                if debug:
                    print("**Compare to tree of height",stored_tree_height,"located at",stored_tree_position,"with visibility",stored_tree_visibility)
                if current_tree_height >= stored_tree_height:
                    #print("The current tree is blocking the stored tree")
                    #visibility_array[n,stored_tree_position] += 1
                    if debug:
                        print("***Updated visibility array at position",stored_tree_position,": ",visibility_array[n])
                    # if the current tree is taller than one of the stored tallest trees

                    taller_unblocked_trees = unblocked_trees[stored_tree_index:]
                    if debug:
                        print("***These trees are still unblocked:",taller_unblocked_trees)
                    # slice the tallest trees array
                    #   from the beginning
                    #   to the tree before the tree that's shorter than the current tree
                    
                    current_tree = np.array([i,current_tree_height,0])
                    unblocked_trees = np.r_[taller_unblocked_trees,[current_tree]]
                    if debug:
                        print("***Updated unblocked trees:",unblocked_trees)
                    
                    # add the current tree to the tallest trees list
                    
                  #  if current_tree_height == stored_tree_height:
                       # if debug:
                           # print("****BREAK")
                        #break
                    #else:
                        
                        
                  
                     #   print("Checking the next tallest stored tree")
                     #  
                        #print("incremented t",t)
                      #  continue
                    #else:
                      #  print("The current tree is equal to the stored tree")
                       # 
                       # break
                
                t += 1
                if debug:
                    print("***Increment t",t)

                if current_tree_height > stored_tree_height:
                   # print("The current tree doesn't block the stored tree")
                    #print("current",current_tree_height,"<",tree_height)
                    unblocked_trees = np.r_[unblocked_trees[:t],[np.array([i,current_tree_height,0])]]
                    if debug:
                        print("***Added to unblocked trees.",unblocked_trees)
                    # add the current tree to the tallest trees list
                    #print("new tallest added",tallest_trees)
                    break
                
def score():
    score_array = visibility_l_to_r*visibility_r_to_l*visibility_t_to_b*visibility_b_to_t
    print(score_array)
    plt.matshow(score_array)
    print(np.amax(score_array))

    
               
visibility_l_to_r = np.zeros((gridsize,gridsize))
visibility_r_to_l = np.zeros((gridsize,gridsize))   
visibility_t_to_b = np.zeros((gridsize,gridsize))  
visibility_b_to_t = np.zeros((gridsize,gridsize)) 

search_scenic(heights,visibility_l_to_r)




heights_r_to_l = np.fliplr(heights)         
search_scenic(heights_r_to_l,visibility_r_to_l)
visibility_r_to_l = np.fliplr(visibility_r_to_l)




heights_t_to_b = np.fliplr(np.rot90(heights,3))
search_scenic(heights_t_to_b,visibility_t_to_b)
visibility_t_to_b = np.fliplr(np.rot90(visibility_t_to_b,3))




heights_b_to_t = np.rot90(heights,3)
search_scenic(heights_b_to_t,visibility_b_to_t)
visibility_b_to_t = np.rot90(visibility_b_to_t,1)




def showAll():
    print("directional arrays:")
    plt.matshow(visibility_b_to_t)
    #print(visibility_b_to_t)

    plt.matshow(visibility_r_to_l)
    plt.matshow(visibility_l_to_r)
    #print(visibility_r_to_l)
    #print(visibility_l_to_r)
    plt.matshow(visibility_t_to_b)
    #print(visibility_t_to_b)


showAll()
score()

plt.show()






