#!/usr/bin/env python
# coding: utf-8

# In[41]:


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
        
# A utility function to search a given key in BST
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
        


class Tree:
    def __init__(self):
        self.root = None
        self.size = 1

#         добавление узлов
    def addNode(self, node, value):
        if node is None:
            self.root = TreeNode(value)
        else:
            if value<node.data:
                if node.left is None:
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)
    
    def insertroot(self, node, value):#вставка нового узла с ключом k в корень дерева p 
        def rotateright(node):#правый поворот вокруг узла p
            node2 = node.left
            if node2 is None:
                return node
            node.left = node2.right
            node2.right = node
#             node2.size = node.size 
#             fixsize(node)
            return node2

        def rotateleft(node):#левый поворот вокруг узла q
            node2 = node.right
            if node2 is None:
                return node
            node.right = node2.left
            node2.left = node
#             node2.size = node.size
#             fixsize(node)
            return node2
        if node is None:
            self.root = TreeNode(value)
        else:
            if value<node.data:
                self.addNode(node.left, value)
                return (rotateright(node))
            else:
                self.addNode(node.right, value)
                return rotateleft(node)
                    

#                     выводы
#     симметричный порядок(отсортированный)
    def printInorder(self, node):
        if node is not None:
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)
    
#     как есть порядок
    def printLevelOrder(self, root):
        h = self.height(self.root)
        i=1
        while(i<=h):
            self.printGivenLevel(self.root, i)
            i +=1
            
#   по заданному уровню       
    def printGivenLevel(self, root, level):
        if root == None:
            return
        if level == 1:
            print ("%d " % root.data)
        elif level > 1:
            self.printGivenLevel(root.left, level-1);
            self.printGivenLevel(root.right, level-1);
            
#     высота дерева      
    def height(self,node):
        if node==None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return(lheight+1)
            else:
                return(rheight+1)


if __name__ == '__main__':
    testTree = Tree()
    testTree.addNode(testTree.root, 200)
    testTree.addNode(testTree.root, 300)
    testTree.addNode(testTree.root, 400)
    testTree.addNode(testTree.root, 100)
    testTree.addNode(testTree.root, 30)
    testTree.insertroot(testTree.root, 10)
    testTree.printInorder(testTree.root)
#     testTree.printLevelOrder(testTree.root)
#     testTree.printGivenLevel(testTree.root, 2)


# In[ ]:




