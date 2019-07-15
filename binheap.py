'''
Problem Solution
1. Create a class BinomialTree with instance variables key, children and order. 
    children is set to an empty list and order is set to 0 when an object is 
    instantiated.
2. Define method add_at_end which takes a binomial tree of the same order as argument 
    and adds it to the current tree, increasing its order by 1.
3. Create a class BinomialHeap with an instance variable trees set to an empty list. 
    This list will contain the set of binomial trees.
4. Define methods get_min, extract_min, combine_roots, merge and insert.
5. The method get_min returns the minimum element in the heap by returning the key 
    of the smallest root in the list trees.
6. The method merge takes a heap as argument and merges it with the 
    current heap. It iterates through the sorted (by order of each tree) list of trees
    and merges any two trees with the same order. It also checks for the case for three 
    consecutive trees of the same order and merges the last two trees.
7. The method combine_roots takes a heap as argument and combines the current heap’s 
    list of trees with its list of trees and sorts them by order of each tree.
8. The method extract_min removes and returns the minimum element in the current heap.
     It does so by removing the tree with the smallest root from the current heap’s 
     list of trees and creating a heap with the children of the smallest root as its 
     list of trees. This new heap is then merged with the current heap.
9. The method insert takes a key as argument and adds a node with that key to the heap.
    It does so by creating an order 0 heap with that key and then merging it with the 
    current heap.

'''
class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.parent=None
        self.children = []
        self.order = 0
 
    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1
 
 
class BinomialHeap:
    def __init__(self):
        self.trees = []
 
    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:  
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        for i in h.trees:
            i.parent=None
        self.merge(h)
 
        return smallest_node.key
 
    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least
 
    def combine_roots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)
 
    def merge(self, h):
        self.combine_roots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1
                    and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        after_after.parent=after
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        after.parent=after_after
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        after.parent=current
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        current.parent=after
                        del self.trees[i]
            i = i + 1
 
    def insert(self, key):
        g = BinomialHeap()
        a=BinomialTree(key)
        g.trees.append(a)
        self.merge(g)
        key.bheap=a

    def update(self,key):
        tr=key.bheap
        p=tr.parent
        while p!=None and p.key>tr.key:
            c=tr.key
            tr.key.bheap=p
            tr.key=p.key
            p.key.bheap=tr
            p.key=c
            tr=p
            p=p.parent

 
def main():
 
    bheap = BinomialHeap()
     
    bheap.insert((1,0))
    bheap.insert((0,1))
    print(bheap.extract_min())

if __name__=='__main__':
    main()