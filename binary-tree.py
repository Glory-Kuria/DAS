
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
    
    
    
    
    # Write a function to determine the last element in a binary tree
    #Represent a node of binary tree  
class Node:  
    def __init__(self,data):  
        #Assign data to the new node, set left and right children to None  
        self.data = data;  
        self.left = None;  
        self.right = None;  
   
class LargestNode:  
    def __init__(self):  
        #Represent the root of binary tree  
        self.root = None;  
          
    #largestElement() will find out the largest node in the binary tree  
    def largestElement(self, temp):  
        #Check whether tree is empty  
        if(self.root == None):  
            print("Tree is empty");  
            return 0;  
              
        else:      
            #Variable maximum will store temp's data  
            maximum = temp.data;  
              
            #It will find largest element in left subtree  
            if(temp.left != None):  
                leftMax = self.largestElement(temp.left);  
                #Compare variable maximum with leftMax and store greater value into maximum  
                maximum = max(maximum, leftMax);  
              
            #It will find largest element in right subtree  
            if(temp.right != None):  
                rightMax = self.largestElement(temp.right);  
                #Compare variable maximum with rightMax and store greater value into maximum  
                maximum = max(maximum, rightMax);  
              
            return maximum;  
   
bt = LargestNode();  
#Add nodes to the binary tree  
bt.root = Node(15);  
bt.root.left = Node(30);  
bt.root.right = Node(55);  
bt.root.left.left = Node(70);  
bt.root.right.left = Node(60);  
bt.root.right.right = Node(6);  
   
#Display largest node in the binary tree  
print("Largest element in the binary tree: " + str(bt.largestElement(bt.root)));  
