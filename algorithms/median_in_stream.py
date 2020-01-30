"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
"""
class MaxHeap:
    heap = []
    
    def size(self):
        return len(self.heap)
    
    def put(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)

    def remove(self):
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self.bubble_down(0)        
    
    def peek(self):
        return self.heap[0]

    def getLeftChild(self, parentIdx):
        idx = int(parentIdx*2+1)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])

    def getRightChild(self, parentIdx):
        idx = int(parentIdx*2+2)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])
    def getParent(self, childIdx):
        idx = int((childIdx-1)/2)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])
    
    def bubble_down(self, nodeIdx):
        l_idx, l_child_val = self.getLeftChild(nodeIdx)
        r_idx, r_child_val = self.getRightChild(nodeIdx)
        if r_idx is None and l_idx is None: return
        if( l_idx is not None and r_idx is None):
            target_idx = l_idx     
        elif( r_idx is not None and l_idx is None): 
            target_idx = r_idx
        else: 
            target_idx = r_idx if l_child_val < r_child_val else l_idx
        if(self.heap[nodeIdx] < self.heap[target_idx]):
            self.swap(nodeIdx, target_idx)
            self.bubble_down(target_idx)
            
    def bubble_up(self, nodeIdx):
        p_idx, p_val = self.getParent(nodeIdx)
        if p_idx is None: return
        if(self.heap[nodeIdx] > p_val):
            self.swap(p_idx, nodeIdx)
            self.bubble_up(p_idx)


    def swap(self, idx1, idx2):
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp
        
class MinHeap:
    heap = []
    
    def size(self):
        return len(self.heap)
    
    def put(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap)-1)

    def remove(self):
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()
        self.bubble_down(0)        
    
    def peek(self):
        return self.heap[0]

    def getLeftChild(self, parentIdx):
        idx = int(parentIdx*2+1)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])

    def getRightChild(self, parentIdx):
        idx = int(parentIdx*2+2)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])
    def getParent(self, childIdx):
        idx = int((childIdx-1)/2)
        if idx < 0 or idx >= len(self.heap):
            return None, None
        return (idx, self.heap[idx])
    
    def bubble_down(self, nodeIdx):
        l_idx, l_child_val = self.getLeftChild(nodeIdx)
        r_idx, r_child_val = self.getRightChild(nodeIdx)
        if r_idx is None and l_idx is None: return
        if( l_idx is not None and r_idx is None):
            target_idx = l_idx     
        elif( r_idx is not None and l_idx is None): 
            target_idx = r_idx
        else: 
            target_idx = r_idx if l_child_val > r_child_val else l_idx
        if(self.heap[nodeIdx] > self.heap[target_idx]):
            self.swap(nodeIdx, target_idx)
            self.bubble_down(target_idx)
            
    def bubble_up(self, nodeIdx):
        p_idx, p_val = self.getParent(nodeIdx)
        if p_idx is None: return
        if(self.heap[nodeIdx] < p_val):
            self.swap(p_idx, nodeIdx)
            self.bubble_up(p_idx)


    def swap(self, idx1, idx2):
        tmp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = tmp
        
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = MaxHeap()
        self.hi = MinHeap()
        

    def addNum(self, num: int) -> None:        
        self.lo.put(num)
        
        self.hi.put(self.lo.peek())
        self.lo.remove()
        
        if self.lo.size() < self.hi.size():
            self.lo.put(self.hi.peek())
            self.hi.remove()
            
        

    def findMedian(self) -> float:
        if self.lo.size() > self.hi.size():
            return self.lo.peek()
        return (self.lo.peek()+self.hi.peek())*0.5
        
        


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print(obj.findMedian())