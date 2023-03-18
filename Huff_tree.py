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
            probDic[i]+=1
        else:
            probDic[i]=1
    return sorted(probDic.items(), key=lambda x: x[1], reverse=True)

def tree(freqList):
    while len(freqList)> 1:
        (a,a1) = freqList[-1]
        (b,b1) = freqList[-2]
        freqList = freqList[:-2]
        nod = Huff_tree(a,b)
        freqList.append((nod, a1+b1)) 
        freqList = sorted(freqList, key=lambda x: x[1], reverse = True)
    return freqList[0][0]

def huffCode(node, memo=''):
    
    if type(node) is str:
        return {node: memo}
    (left, right) = node.infoNode()
    code = dict()
    code.update(huffCode(left, memo + '0'))
    code.update(huffCode(right, memo + '1'))
    return code

def compressString(s,out=""):
    
    freqList=item_prob(s)    
    codingTable=huffCode(tree(freqList))
    for i in s:
        out+=codingTable[i]
    return out,codingTable
    # in rteal life the compressor is converting the data in bits 
    # but we exemplified with a strin of 1 and 0
def decompressString(bitString,codingTable,ind=0,out=""):
    codingTable={v: k for k, v in codingTable.items()}
    print(codingTable)
    for i in range(len(bitString)+1):
        
        if bitString[ind:i] in codingTable: 
            
            out+=codingTable[bitString[ind:i]]
            ind=i
        
    return out
