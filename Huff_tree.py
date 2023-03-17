class Huff_tree(object):
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    def info_node(self):
        return(self.left,self.right)

def item_prob(itemList):
    probDic={}
    for i in itemList:
        if i in probDic:
            probDic[i]=1
        else:
            probDic[i]+=1
    return probDic


