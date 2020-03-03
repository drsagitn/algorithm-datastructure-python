"""
loop through the grid and only check for item that has building in it (value = 1)
save the cordinate of the checked item into hashmap by add_to_hash() function.
The add_to_has
"""
def numberOfStores(rows, column, grid):
    # WRITE YOUR CODE HERE
    def add_to_hash(i, j):
        hashmap[str(i)+":"+str(j)] = 1
        if i < rows-1 and grid[i+1][j] == 1 and hashmap.get(str(i+1)+":"+str(j)) is None:
            add_to_hash(i+1, j)
        if j < column-1 and grid[i][j+1] == 1 and hashmap.get(str(i)+":"+str(j+1) is None:
            add_to_hash(i, j+1)
        if i > 0 and grid[i-1][j] == 1 and hashmap.get(str(i-1)+":"+ str(j) is None:
            add_to_hash(i-1, j)
        if j > 0 and grid[i][j-1] == 1 and hashmap.get(str(i)+":"+str(j-1) is None:
            add_to_hash(i, j-1)
            
            
    hashmap = {}
    ret_count = 0
    for i in range(rows):
        for j in range(column):
            if grid[i][j] == 1 and hashmap.get(str(i) + ":" + str(j)) is None:
                add_to_hash(i, j)
                ret_count += 1
    return ret_count

print(numberOfStores(4, 4, 
[
[1,1,0,0],
[0,0,0,0],
[0,0,1,1],
[0,0,0,0]
]))