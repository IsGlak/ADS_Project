class Huff_tree(object):
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    def info_node(self):
        return(self.left,self.right)

def item_freq(itemList):
    probDic={}
    for i in itemList:
        if i in probDic:
            probDic[i]=1
        else:
            probDic[i]+=1
    return probDic

def tree(freqList):
    while len(freqList)> 1:
        (a,a1) = freqList[-1]
        (b,b1) = freqList[-2]
        freqList = freqList[:-2]
        node = Huff_tree(a,b)
        freqList.append(node, a1+b1) 
        freqList = sorted(node, key=lambda x: x[1], reverse = True)
    return freqList[0][0]

