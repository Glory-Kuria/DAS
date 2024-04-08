
# create a simple binary tree



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
 

if __name__ == '__main__':
 
 
    r = Node(50)
    r = insert(r, 60)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 60)
    r = insert(r, 70)
 
    inorder(r)
    
    
    
    
    # Write a function to determine the largest  element in a binary tree

class Node:  
    def __init__(self,data):  
         
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class LargestNode:  
    def __init__(self):  
         
        self.root = None;  
          
     
    def largestElement(self, temp):  
        
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
              
        else:      
             
            maximum = temp.data;  
              
            
            if(temp.left != None):  
                leftMax = self.largestElement(temp.left);  
                
                maximum = max(maximum, leftMax);  
              
             
            if(temp.right != None):  
                rightMax = self.largestElement(temp.right);  
                  
                maximum = max(maximum, rightMax);  
              
            return maximum;  
   
bt = LargestNode();  

bt.root = Node(15);  
bt.root.left = Node(30);  
bt.root.right = Node(55);  
bt.root.left.left = Node(70);  
bt.root.right.left = Node(60);  
bt.root.right.right = Node(6);  
   

print("Largest element in the binary tree: " + str(bt.largestElement(bt.root)));  
