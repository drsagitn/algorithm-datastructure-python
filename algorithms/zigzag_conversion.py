class Solution(object):
    def put(self, c, storage, i, j, o, numRows):
        if o == 1:
            if len(storage[i]) == j + 1:
                storage[i][j] = c
            else:
                storage[i].insert(j, c)
        if o == 0:
            for k in range(numRows):
                storage[k].append(' ')
            storage[i][j] = c
        # calculate next orientation
        if o == 1 and i == numRows - 1:
            o = 0
        elif o == 0 and i == 0:
            o = 1
        # calcualte next potition
        if o == 1:
            i += 1
        if o == 0:
            i -= 1
            j += 1
        return i, j,o
        
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        storage = []
        for i in range(numRows):
            storage.append([])
        # put string in array
        i = 0
        j = 0
        o = 1
        for c in s:
            i, j, o = self.put(c, storage, i, j, o, numRows)
        ret = ""
        for arr in storage:
            for c in arr:
                if c != " ":
                    ret += c
        return ret

a = Solution()
r = a.convert("PAYPALISHIRING", 1)
print(r)
