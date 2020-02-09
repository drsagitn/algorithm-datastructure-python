def minimumDays(rows, columns, grid):
    # WRITE YOUR CODE HERE
    def has_positive_ajacent(i, j):
        if i > 0 and grid[i-1][j] == 1:
            return True
        if j > 0 and grid[i][j-1] == 1:
            return True
        if i < rows-1 and grid[i+1][j] == 1:
            return True
        if j < columns-1 and grid[i][j+1] == 1:
            return True
        return False
        
    ret_count = 0
    if sum(sum(grid,[])) == 0:
        grid[0][0] = 1
        ret_count = 1
    update_buffer = []
    while True:
        for (i_, j_) in update_buffer:
            grid[i_][j_] = 1
        update_buffer.clear()
        if rows*columns == sum(sum(grid,[])):
            break
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0 and has_positive_ajacent(i, j) == True:
                    update_buffer.append((i, j))
        ret_count += 1
    return ret_count

print(minimumDays(5, 4, 

[
[0,0,1,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,1,1,0]
]))