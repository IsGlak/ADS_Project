class Huff_tree(object):
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    def info_node(self):
        return(self.left,self.right)