"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
[
["hit","hot","dot","dog","cog"],
["hit","hot","lot","log","cog"],
["hit","hot","dot","dog","log","cog"],
["hit","hot","dot","lot","log","cog"],
["hit","hot","lot","dot","dog","cog"],
["hit","hot","lot","log","dog","cog"],
["hit","hot","dot","lot","log","dog","cog"],
["hit","hot","lot","dot","dog","log","cog"]
]
[
['hit', 'hot', 'dot', 'dog', 'cog'],
['hit', 'hot', 'lot', 'log', 'cog'],
['hit', 'hot', 'lot', 'log', 'dog', 'cog'], 
['hit', 'hot', 'lot', 'dot', 'dog', 'cog'], 
['hit', 'hot', 'dot', 'dog', 'log', 'cog']
['hit', 'hot', 'dot', 'lot', 'dot', 'dog', 'cog'], 
['hit', 'hot', 'dot', 'lot', 'log', 'dog', 'cog'], 
]
"qa"
"sq"
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci",
"ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or",
"rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb",
"sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo",
"na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr",
"pa","he","lr","sq","ye"]

ans:
[["qa","ba","be","se","sq"],["qa","ba","bi","si","sq"],["qa","ba","br","sr","sq"],
["qa","ca","cm","sm","sq"],["qa","ca","co","so","sq"],["qa","la","ln","sn","sq"],
["qa","la","lt","st","sq"],["qa","ma","mb","sb","sq"],["qa","pa","ph","sh","sq"],
["qa","ta","tc","sc","sq"],["qa","fa","fe","se","sq"],["qa","ga","ge","se","sq"],
["qa","ha","he","se","sq"],["qa","la","le","se","sq"],["qa","ma","me","se","sq"],
["qa","na","ne","se","sq"],["qa","ra","re","se","sq"],["qa","ya","ye","se","sq"],
["qa","ca","ci","si","sq"],["qa","ha","hi","si","sq"],["qa","la","li","si","sq"],
["qa","ma","mi","si","sq"],["qa","na","ni","si","sq"],["qa","pa","pi","si","sq"],
["qa","ta","ti","si","sq"],["qa","ca","cr","sr","sq"],["qa","fa","fr","sr","sq"],
["qa","la","lr","sr","sq"],["qa","ma","mr","sr","sq"],["qa","fa","fm","sm","sq"],
["qa","pa","pm","sm","sq"],["qa","ta","tm","sm","sq"],["qa","ga","go","so","sq"],
["qa","ha","ho","so","sq"],["qa","la","lo","so","sq"],["qa","ma","mo","so","sq"],
["qa","na","no","so","sq"],...
"""
class Solution:
    def getVertex(self, word, wordList):
        ret = []
        for w in wordList:
            if w == word:
                continue
            j = 0
            for i in range(len(word)):
                if w[i] != word[i]:
                   j+= 1
            if j == 1:
                ret.append(w)
        return ret
    def mergePath(self, start_path, end_path, common_vertex):
        sIdx = start_path.index(common_vertex)
        eIdx = end_path.index(common_vertex)
        return start_path[0:sIdx] + [common_vertex] + end_path[eIdx+1:]


    def findLadders(self, beginWord: str, endWord: str, wordList: [str]) -> [[str]]:
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        import collections

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res
        # graph = {}
        # graph[beginWord] = self.getVertex(beginWord, wordList)
        # graph[endWord] = self.getVertex(endWord, wordList)
        # for word in wordList:
        #     if graph.get(word) is None:
        #         graph[word] = self.getVertex(word, wordList)
        # ret = []
        # queue = [(beginWord, [beginWord])]
        # queue_back = [(endWord, [endWord])]
        # path = []
        # path_b = []
        # while queue and queue_back:
        #     vertex, path = queue.pop(0)
        #     if vertex == endWord:
        #         if len(ret) == 0 or len(ret[0]) == len(path):
        #             ret.append(path)
        #     elif vertex in path_b:
        #         ret.append(self.mergePath(path, list(reversed(path_b)), vertex))
        #     else:
        #         for child in graph[vertex]:
        #             if child not in path:
        #                 queue.append((child, path + [child]))

        #     vertex_b, path_b = queue_back.pop(0)
        #     if vertex_b == beginWord:
        #         if len(ret) == 0 or len(ret[0]) == len(path_b):
        #             ret.append(path_b)
        #     elif vertex_b in path:
        #         ret.append(self.mergePath(path, list(reversed(path_b)), vertex_b))
        #     else:
        #         for child in graph[vertex_b]:
        #             if child not in path_b:
        #                 queue_back.append((child, path_b + [child]))
        # return ret

s = Solution()
# print(s.findLadders("lost", "cost", ["most","fist","lost","cost","fish"]))
print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","cog"]))
# s.findLadders("qa",
# "sq",
# ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci",
# "ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or",
# "rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb",
# "sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo",
# "na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr",
# "pa","he","lr","sq","ye"])