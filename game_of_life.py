#%%
from functools import reduce


#%%
grid = (
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (1, 1, 0, 0)    
)
print(grid[1][2])

def count(grid:tuple, i:int, j:int) -> bool:
    return reduce(lambda a,b: a+b, (grid[x+i][y+j] for x in [-1,0,1] for y in [-1,0,1] if (x!= 0 or y!=0)),0) 
   
    #lambda a,b: a+b, for grid[x][y] + x,y in offset
    #sum of [x-1 -> x+1, y-1 -> y+1 except x,y=0,0 ] =2 | 3 -> 1 else 0
    #comprehensions: python but not in hask -> sonst if -> filter, for -> map, () iterator keine list comprehension!

print(count(grid, 2,2))

# %%
