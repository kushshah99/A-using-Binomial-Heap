from binheap import BinomialHeap
from binheap import BinomialTree

class node:
	def __init__(self,coordinates,g,value):
		self.value=value
		self.coordinates=coordinates
		self.goal=g
		self.parent=None
		self.approx=(((self.coordinates[0]-self.goal[0])**2)+((self.coordinates[1]-self.goal[1])**2))**0.5
		self.weight=float('inf')
		self.Total=self.approx+self.weight
		self.bheap=None

	def __lt__(self,x):
		if self.Total<x.Total:
			return True
		return False

def generatemap():
	i=int(input("Enter the no. of rows : "))
	j=int(input("Enter the no. of columns : "))
	map=[[ 0 for y in range(j)] for x in range(i)]
	print("Enter the places where obstacles exist as r c and to stop enter n")
	obstacle=True
	while obstacle:
		inp=input()
		if inp=='n':
			obstacle=False
		else:
			s=inp.split(" ")
			map[int(s[0])][int(s[1])]='X'
		
	print("The entered map is : ")
	for x in range(i):
		for y in range(j):
			print(map[x][y],end=" ")
		print()
	return map

class A_star:
	def __init__(self,M,S,D):
		self.map=[[node((j,i),D,M[j][i]) for i in range(len(M[0]))] for j in range(len(M))]
		for i in range(len(M)):
			for j in range(len(M[0])):
				if M[i][j]=='X':
					self.map[i][j].value='X'
		self.source=self.map[S[0]][S[1]]
		self.destination=self.map[D[0]][D[1]]

	def issafe(self,x,y):
		if (x<len(self.map) and y<len(self.map[0])) and x>=0 and y>=0 and self.map[x][y].value!='X':
			return True
		return False

	def neighbours(self,x,y):
		l=[(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
		return l

	def astar(self):
		Q=BinomialHeap()
		self.source.weight=0
		self.source.Total=self.source.approx
		for i in range(len(self.map)):
			for j in range(len(self.map[0])):
				Q.insert(self.map[i][j])

		while (not Q.trees==[]) and Q.get_min() != self.destination:
			q=Q.extract_min()
			for Neighbours in self.neighbours(q.coordinates[0],q.coordinates[1]):
				if self.issafe(Neighbours[0],Neighbours[1]):
					neighbour=self.map[Neighbours[0]][Neighbours[1]]
					if neighbour.Total>(q.weight+1+neighbour.approx):	
						neighbour.parent=q
						neighbour.weight=q.weight+1
						neighbour.Total=neighbour.approx+neighbour.weight
						Q.update(neighbour)
						
	def printmap(self):
		print("MAP")
		d=self.destination
		while d!=None:
			d.value='*'
			d=d.parent
		for i in range(len(self.map)):
			for j in range(len(self.map[0])):
				print(self.map[i][j].value,end=" ")
			print()
		l=[]
		d=self.destination
		while(d!=None):
			l.append(d.coordinates)
			d=d.parent
		print(l)


m=generatemap()
print("Enter details of source")
s1=int(input("enter the row index "))
s2=int(input("enter the column index"))
print("Enter details of destination")
d1=int(input("enter the row index "))
d2=int(input("enter the column index"))
a=A_star(m,(s1,s2),(d1,d2))
a.astar()
a.printmap()