#!/usr/bin/env python
# coding: utf-8

# In[13]:


# печать
outputdebug = False 

def debug(msg):
    if outputdebug:
        print(msg)
        
# Класс для инициализации узлов
class Node():
    def __init__(self, key):
        self.key = key #ключ
#         левое и правое поддеревья, пока считаем, что дерево пустое(т.е. попросту отсутствует)
        self.left = None 
        self.right = None 
        self.height = 1
        
# Задание дерева
class AVLTree():
    def __init__(self):
        self.node = None #узлы
        self.height = -1  #высота дерева/размер
        self.balance = 0; #баланс/равновесие
        
        
#   Лист
    def is_leaf(self):
        return (self.height == 0) 
    
#     Вставка обычная
# рекурсивно вставляем новый ключ в корень левого или правого поддеревьев 
# (в зависимости от результата сравнения с корневым ключом)
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 

        #     Вставка в корень
#     Сначала рекурсивно вставляем новый ключ в корень левого или правого поддеревьев 
# (в зависимости от результата сравнения с корневым ключом)
# выполняем правый (левый) поворот, который поднимает нужный нам узел в корень дерева. 
    def insertroot(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left=self.node.left.insertroot(key)
            return self.lrotate()
            
        elif key > tree.key: 
            self.node.right=self.node.right.insertroot(key)
            return self.rrotate()
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 
        
    def rrotate(self):
        # Поворот вправо
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 
#         изменение высоты
        A.height = max(A.left.height, A.right.height)+1
        B.height = max(B.left.height, B.right.height)+1

    
    def lrotate(self):
        # Поворот влево
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
            
        self.node = B 
        B.left.node = A 
        A.right.node = T 
#         изменение высоты
        A.height = max(A.left.height, A.right.height)+1
        B.height = max(B.left.height, B.right.height)+1
        
#     Ребалансировка дерева   
    def rebalance(self):
        
        # Ключ вставлен. Надо проверить баланс
        self.update_heights(False)
        self.update_balances(False)
#         Пока дерево не сбалансировано
        while self.balance < -1 or self.balance > 1: 
#         Левое поддерево> Правое поддерево
            if self.balance > 1:
                # Left-Right Case
                #      o
                #     / \
                #   o    o
                #  / \      => left rotation
                # o   o
                #    / \
                #   o   o
                if self.node.left.balance < 0:  
#                   Левое поддерево> Правого -> поворот влево
                    self.node.left.lrotate() # in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
            # Левое поддерево> Правое поддерево    
            if self.balance < -1:
                #      o
                #     / \
                #   o    o
                #       / \      => right rotation
                #      o   o
                #    / \
                #   o   o
                if self.node.right.balance > 0: 
#                     Левое поддерево <правого -> поворот вправо
                    self.node.right.rrotate() # in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

        
#     Изменение высоты         
    def update_heights(self, recurse=True):
#         если дерево не пустое
# Высота дерева - это максимальная высота либо левого, либо правого поддерева +1
        if self.node: 
            if self.node.left != None: 
                self.node.left.update_heights()
            if self.node.right != None:
                self.node.right.update_heights()
            
            self.height = max(self.node.left.height,self.node.right.height) + 1 
        else: 
            # корень
            self.height = -1 
            
#      Изменение баланса       
    def update_balances(self, recurse=True):
# # Баланс = Высота слева - Высота правого узла
        if self.node:  
            if self.node.left != None: 
                self.node.left.update_balances()
            if self.node.right != None:
                self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            # корень
            self.balance = 0 
    
#     перемещение по порядку
    def inorder_traverse(self):
#       если дерево пустое
        if self.node == None: 
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):     
        self.update_heights()  # Изменение высоты до измения баланса 
        self.update_balances()
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" +                    str(self.balance) + "]", 'L' if self.is_leaf() else 'R')
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

if __name__ == "__main__": 
    a = AVLTree()
    print( "Inserting")
    k=9
    a.insertroot(k)
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 10, 0]
    for i in inlist: 
        a.insert(i)
         
    a.display()
    
    print("Input for insert in root:", k)
    print ("Input:", inlist )
    print ("Inorder traversal:", a.inorder_traverse() )


# In[ ]:





# In[ ]:





# In[ ]:




