from io import StringIO # We use String-io to get low the time complexity 
                        # because to do the string tratment is faster with their methods

def createEncoder(): # Create the table to change char to code
    return {chr(i): i for i in range(256)}


def LZWCompress(encoder,str,out=[],memo="",size=256):

    for char in str:
        memChar = memo + char
        if memChar in encoder:
            memo = memChar
        else:
            out.append(encoder[memo])
            
            encoder[memChar] = size
            size += 1
            memo = char

    
    if memo:
        out.append(encoder[memo])
    return out

def LZWDecompress(encoder,compressed):
    pass



