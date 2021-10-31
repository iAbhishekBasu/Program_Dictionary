from collections import defaultdict

class Heap():

	def __init__(self):
		self.array = []
		self.size = 0
		self.pos = []

	def newMinHeapNode(self, v, dist):
		minHeapNode = [v, dist]
		return minHeapNode

	def swapMinHeapNode(self, a, b):
		t = self.array[a]
		self.array[a] = self.array[b]
		self.array[b] = t

	# A standard function to heapify at given idx
	def minHeapify(self, idx):
		smallest = idx
		left = 2*idx + 1
		right = 2*idx + 2

		if left < self.size and self.array[left][1] < self.array[smallest][1]:
			smallest = left

		if right < self.size and self.array[right][1] < self.array[smallest][1]:
			smallest = right

		if smallest != idx:

			# Swap positions
			self.pos[self.array[smallest][0]] = idx
			self.pos[self.array[idx][0]] = smallest

			# Swap nodes
			self.swapMinHeapNode(smallest, idx)

			self.minHeapify(smallest)

	# Standard function to extract minimum node from heap
	def extractMin(self):

		# Return NULL if heap is empty
		if self.isEmpty() == True:
			return

		root = self.array[0]

		lastNode = self.array[self.size - 1]
		self.array[0] = lastNode

		# Update position of last node
		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		# Reduce heap size and heapify root
		self.size -= 1
		self.minHeapify(0)

		return root

	def isEmpty(self):
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist):

		# Get the index of v in heap array

		i = self.pos[v]

		# Get the node and update its dist value
		self.array[i][1] = dist

		# Travel up while the complete tree is not hepified. This is a O(Logn) loop
		while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:

			# Swap this node with its parent
			self.pos[ self.array[i][0] ] = (i-1)/2
			self.pos[ self.array[(i-1)//2][0] ] = i
			self.swapMinHeapNode(i, (i - 1)//2 )

			# move to parent index
			i = (i - 1) // 2;

	# A utility function to check if a given vertex 'v' is in min heap or not
	def isInMinHeap(self, v):

		if self.pos[v] < self.size:
			return True
		return False


def printArr(dist, n):
	print ("Vertex\tDistance from source")
	for i in range(n):
		print ("%d\t\t%d" %(i, dist[i]))

def printPar(parent, n):
	print ("Vertex\t\tParent")
	for i in range(n):
		print ("%d\t\t%d" %(i, parent[i]))
		
class Graph():

	def __init__(self, V):
		self.V = V
		self.graph = defaultdict(list)

	def addEdge(self, src, dest, weight):
		newNode = [dest, weight]
		self.graph[src].insert(0, newNode)

		newNode = [src, weight]
		self.graph[dest].insert(0, newNode)

	# The main function that calculates distances of shortest paths from src to all vertices. It is a O(ELogV) function
	def dijkstra(self, src):

		V = self.V 
		dist = [] # dist values used to pick minimum weight edge in cut
		parent =[]

		minHeap = Heap()
    # Initially size of min heap is equal to V
		minHeap.size = V;

		# Initialize min heap with all vertices dist value of all vertices
		for v in range(V):
			dist.append(100000000)
			minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]))
			minHeap.pos.append(v)
			parent.append(-1)

		# Make dist value of src vertex as 0 so that it is extracted first
		minHeap.pos[src] = src
		dist[src] = 0
		minHeap.decreaseKey(src, dist[src])

		
		# In the following loop, min heap contains all nodes whose shortest distance is not yet finalized.
		while minHeap.isEmpty() == False:

			# Extract the vertex with minimum distance value
			newHeapNode = minHeap.extractMin()
			u = newHeapNode[0]

			# Traverse through all adjacent vertices of u and RELAX them
			for adj in self.graph[u]:

				v = adj[0]

				#  distance to v through u is less  than its previously calculated distance, upadte dist[v]
				if minHeap.isInMinHeap(v) and dist[u] != 100000000 and adj[1] + dist[u] < dist[v]:
						dist[v] = adj[1] + dist[u]
						parent[v]=u
						# update distance valuein min heap also
						minHeap.decreaseKey(v, dist[v])

		printArr(dist,V)
		printPar(parent,V)


# main
n=int(input(("Enter total number of vertex in the network.")))
graph = Graph(n)
e=int(input(("Enter total number of edges in the network.")))
for i in range(0,e,1):
  u,v,wt=[int(x) for x in input().split()]
  graph.addEdge(u, v, wt)
print("Distance from vertex 0")
graph.dijkstra(0)

#0, 1, 4
#0, 7, 8
#1, 2, 8
#1, 7, 11
#2, 3, 7)
#2, 8, 2)
#2, 5, 4)
#3, 4, 9)
#3, 5, 14)
#4, 5, 10)
#5, 6, 2)
#6, 7, 1)
#6, 8, 6)
#7, 8, 7)
