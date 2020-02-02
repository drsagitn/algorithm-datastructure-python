


class Solution:
    def breakToSubsequence(self, labels):
        hash = {}
        for i, label in enumerate(labels):
            hash[label] = i
        left = right = 0
        ret = []
        while right < len(labels):
            if hash.get(labels[right]) > right:
                right = hash.get(labels[right])
            i = left + 1
            while i < right:
                if hash.get(labels[i]) > right:
                    right = hash.get(labels[i])
                i += 1
            ret.append(right-left+1)
            right += 1
            left = right
        return ret


s = Solution()
print(s.breakToSubsequence(['a','b','c']))
print(s.breakToSubsequence(['a','b','c', 'a']))
print(s.breakToSubsequence(['a','b','a','b','c','b','a','c','a','d','e','f','e','g','d','e','h','i','j','h','k','l','i','j']))




# [a,b,a,b,c,b,a,c,a,
# d,e,f,e,g,d,e,
# h,i,j,h,k,l,i,j]
