class MinHeap:                                               

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = self.maxsize-1
        self.Heap = []
        for i in range(0,self.maxsize):
          element=int(input("Enter element."))
          self.Heap.append(element)

    def parent(self, index):
        return index//2

    def leftChild(self, index):
        return (2*index)+1
    
    def rightChild(self, index):
        return (2*index)+2

    def empty(self):
        if self.size == -1:
            return True
        return False

    def min_heapify(self,index):
        left = self.leftChild(index)
        right = self.rightChild(index)

        # finding smallest among index, left child and right child
        smallest = index

        if ((left <= self.size) ):
            if (self.Heap[left] < self.Heap[smallest]):
                smallest = left

        if ((right <= self.size )):
            if (self.Heap[right] < self.Heap[smallest]):
                smallest = right

        # smallest is not the node, node is not a heap
        if (smallest != index):
            self.Heap[index], self.Heap[smallest] = self.Heap[smallest], self.Heap[index]
            self.min_heapify(smallest)
    
    def top(self):
        if self.size!= -1:
            return self.Heap[0]
        return -1
    
    def pop(self):
        if self.size == -1:
            print("Priority Queue is empty.")
            return -1
        minm = self.Heap[0]
        self.Heap[0]=self.Heap[self.size]
        self.size-=1
        self.min_heapify(0)
        return minm
    
    def decrease_key(self,index):
        while((self.Heap[self.parent(index)] > self.Heap[index])):
            self.Heap[index], self.Heap[self.parent(index)] = self.Heap[self.parent(index)], self.Heap[index]
            index = self.parent(index)
    
    def push(self, element):
      if self.size==self.maxsize-1:
        print("Overflow detected")
        return
      self.size=self.size + 1
      self.Heap[self.size] = element
      self.decrease_key(self.size)
  
    def size(self):
        return self.size+1
    
    def display(self):
      if self.size == -1: #displaying the heap
            print("Underflow detected.")                             
      print(self.Heap[0:self.size+1])
    
    def build_heap(self):
      for i in range((self.size//2)-1,-1,-1):
        self.min_heapify(i)
    
s=int(input("Enter maximum size of heap"))
PQ=MinHeap(s)
PQ.build_heap()
PQ.display()
PQ.push(6)
PQ.pop()
PQ.pop()
PQ.pop()
PQ.pop()
PQ.pop()
PQ.push(2)
PQ.push(1)
PQ.pop()
PQ.display()
