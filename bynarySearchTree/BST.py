#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Класс для инициализации узлов
class Node():
    def __init__(self, key):
        self.key = key #ключ
#         левое и правое поддеревья, пока считаем, что дерево пустое(т.е. попросту отсутствует)
        self.left = None 
        self.right = None 
        
# Задание дерева
class AVLTree():
    def __init__(self):
        self.node = None 
    
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
            
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key:
            self.node.right.insert(key)
        
        else: 
            print("Key [" + str(key) + "] already in tree.")
            

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
            
        elif key < tree.key: 
            self.node.left=self.node.left.insertroot(key)
            return self.leftRotate()
            
        elif key > tree.key: 
            self.node.right=self.node.right.insertroot(key)
            return self.rightRotate()
        
        else: 
            print("Key [" + str(key) + "] already in tree.")
             
        
    def rightRotate(self):
        # Поворот вправо
        print ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        C = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = C 

    
    def leftRotate(self):
        # Поворот влево
        print ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        C = B.left.node 
            
        self.node = B 
        B.left.node = A 
        A.right.node = C 

        
    def find(self, key):
        if self.node != None:
            
            if self.node.key == key :
                return True

            elif key < self.node.key:
                return self.node.left.find(key)

            elif key > self.node.key:
                return self.node.right.find(key)

            else:
                return False
            
        else:
            return False 
            

    def show(self, level=0, pref=''):     
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key)
            if self.node.left != None: 
                self.node.left.show(level + 1, '>L')
            if self.node.left != None:
                self.node.right.show(level + 1, '>R')


# In[22]:


a = AVLTree()
k = 8
a.insertroot(k)
list = [9, 4, 11, 13, 3, 2, 15, 1, 21]
for i in list: 
    a.insert(i) 
a.show()
print('-' * 20)
a.rightRotate()
a.show()
print('-' * 20)
a.leftRotate()
a.show()


# In[23]:


# Find values
# for i in range(len(list)):
print(a.find(list[4]))
print(a.find(-3))


# In[ ]:




