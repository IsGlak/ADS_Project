# Define a class for node in Huffman tree
class Huff_tree(object):
    # Initialize a node with left/rigth child node 
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
    # Return the left and rigth child nodes of the current one 
    def infoNode(self):
        return(self.left,self.right)
# Take a list on items and return a list of tuples containing 
# each item and it's frequency sorted in descending order of freq. 
def item_prob(itemList):
    probDic={}
    for i in itemList:
        if i in probDic:
            probDic[i]+=1
        else:
            probDic[i]=1
    return sorted(probDic.items(), key=lambda x: x[1], reverse=True)
# The function takes a list of tuples containing (item, freq)
# and return the root node of Huffman tree after merging
# nodes with lowest frequency. 
def tree(freqList):
    while len(freqList)> 1:
        (a,a1) = freqList[-1]
        (b,b1) = freqList[-2]
        freqList = freqList[:-2]
        nod = Huff_tree(a,b)
        freqList.append((nod, a1+b1)) 
        freqList = sorted(freqList, key=lambda x: x[1], reverse = True)
    return freqList[0][0]
# Takes a node in the tree and a prefix code and return a dict
# containing prefixes for each character in tree. 
# It recursively traverses all the tree recording a 0 for every
# left branch and 1 for every right branch. 
def huffCode(node, memo=''):
    if type(node) is str:
        return {node: memo}
    (left, right) = node.infoNode()
    code = dict()
    code.update(huffCode(left, memo + '0'))
    code.update(huffCode(right, memo + '1'))
    return code
# This function takes a string as input and returns a compressed
# version of the string as a string of 0's and 1's.
def compressString(s,out=""):
    
    freqList=item_prob(s)    
    codingTable=huffCode(tree(freqList))
    for i in s:
        out+=codingTable[i]
    return out,codingTable
    # in rteal life the compressor is converting the data in bits 
    # but we exemplified with a string of 1 and 0.

# Takes as input a compressed bit string, a coding table 
# and optionall arguments and returns the decompressed version
# of the input string. 
def decompressString(bitString,codingTable,ind=0,out=""):
    codingTable={v: k for k, v in codingTable.items()}
    print(codingTable)
    for i in range(len(bitString)+1):
        
        if bitString[ind:i] in codingTable: 
            
            out+=codingTable[bitString[ind:i]]
            ind=i
        
    return out
