#%%
from functools import reduce
from pickle import FALSE

#%%
grid = (
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 1, 0, 1),
    (1, 1, 0, 0)    
)
print(grid[1][2])

def is_alive(grid:tuple, x:int, y:int) -> bool:
    if reduce(lambda a,b: a+b, [grid[x][y] for x in [-1,0,1] for y in [-1,0,1] if (x!= 0 and y!=0)],0) in [2,3]:
        return True 
    else:
        return False
    #lambda a,b: a+b, for grid[x][y] + x,y in offset
    #sum of [x-1 -> x+1, y-1 -> y+1 except x,y=0,0 ] =2 | 3 -> 1 else 0

print(is_alive(grid, 2,2))

# %%
