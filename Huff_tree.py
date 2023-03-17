class Huff_tree(object):
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    def infoNode(self):
        return(self.left,self.right)

def item_prob(itemList):
    probDic={}
    for i in itemList:
        if i in probDic:
            probDic[i]=1
        else:
            probDic[i]+=1
    return probDic

def tree(nod):
    while len(nod)> 1:
        (a,a1) = nod[-1]
        (b,b1) = nod[-2]
        nod = nod[:-2]
        nod = Huff_tree(a,b)
        nod.append(X, a1+b1) ##### missing variable 
        nod = sorted(nod, key=lambda x: x[1], reverse = True)
    return nod[0][0]

def huffCode(node, memo=''):
    
    if type(node) is str:
        return {node: memo}
    (left, right) = node.infoNode()
    code = dict()
    code.update(huffCode(left, memo + '0'))
    code.update(huffCode(right, memo + '1'))
    return code