'''
        1
    2       3
4       5


inorder ( left , Root, right ) : 4,2,5,1,3
preorder ( root, left, right) :1,2,4,5,3
postorder (left, right, root) : 4,5,2,3,1

'''

class node:
    def __init__(self, data):
        self.data = data 
        self.r= None
        self.l=None

def bt_pre(a):
    if a:
        print(a.data)
        bt_pre(a.l)
        bt_pre(a.r)

def bt_post(a):
    if a:
        bt_post(a.l)
        bt_post(a.r)
        print(a.data)
    
root = node(1)
root.l = node(2)
root.r= node(3)
root.l.l=node(4)
root.l.r=node(5)

bt_post(root)