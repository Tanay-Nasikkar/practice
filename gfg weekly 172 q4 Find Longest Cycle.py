'''
https://practice.geeksforgeeks.org/contest/gfg-weekly-172-rated-contest
q4: Find Longest Cycle
'''

from typing import List

class Node:
    def __init__(self, num):
        self.num = num
        self.roads = []
        self.parent = None
        
        #self.depth = 0
        #self.x = 0
        
    def __eq__(self,other):
        return False if other is None else self.num == other.num

class Solution:
    def find_lca(self,a,b):
        if a.depth > b.depth:
            a,b = b,a
            
        if a == b:
            return a
            
        while b.depth != a.depth:
            b = b.parent
        
        while b != a:
            b = b.parent
            a = a.parent
        
        return a
        
        
    def solve(self,queries):
        for a,b in queries:
            lca = self.find_lca(self.nodes[a],self.nodes[b])
            maxi = 0
            child = None
            i = -1
            while lca:
                i+=1
                
                if lca.maxi[0] == child:
                    a = lca.second_max[1] + i
                else:
                    a = lca.maxi[1] + i
                    
                if a > maxi:
                    maxi = a
            
                child = lca
                lca = lca.parent
                
            yield max(maxi,i) + 1
            
    def resolveTree(self,node):
        maxi = [0,0]
        second_max = [0,0]
        for i in node.roads:
            i.roads.remove(node)
            i.parent = node
            i.depth = node.depth + 1
            a = self.resolveTree(i) + 1
            if a > second_max[1]:
                if a >= maxi[1]:
                    second_max[0] = maxi[0]
                    second_max[1] = maxi[1]
                    maxi[0] = i
                    maxi[1] = a
                else:
                    second_max[0] = i
                    second_max[1] = a
                    
        node.maxi = maxi
        node.second_max = second_max
        
        return maxi[1]
        
    def findLongest(self, n : int, q : int, edges : List[List[int]], queries : List[List[int]]) -> List[int]:
        # code here
        '''
        Assumed BT and solved... therefore errors first time
        Assuming no loop now (since tree-like is mentioned)
        '''
        
        self.nodes = [Node(i+1) for i in range(n)]
        self.nodes.insert(0, None)
        root = self.nodes[1]
        root.depth = 0
        
        for i,v in edges:
            i = self.nodes[i]
            v = self.nodes[v]
            i.roads.append(v)
            v.roads.append(i)
            
        self.resolveTree(root)
        
        return self.solve(queries)
            

#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        q = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.findLongest(n, q, edges, queries)

        IntArray().Print(res)

# } Driver Code Ends