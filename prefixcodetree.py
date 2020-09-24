class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        
class PrefixCodeTree:
    dic = []
    root = Node(0)
    def __init__(self):
        pass
    def insert(self, codeword, symbol):
        self.dic.append(symbol)
        nod = self.root
        for bit in codeword:
            if bit == 1:
                if(nod.right == None):
                    nod.right = Node(0)
                nod = nod.right
            elif bit == 0:
                if(nod.left == None):
                    nod.left = Node(0)
                nod = nod.left

        nod.val = len(self.dic) -1

    def decode(self, encodedData, datalen):
        endata = []
        for byte in encodedData:
            endata.append(f'{byte:0>8b}')
        enbitstr = ''.join(endata)

        result = []
        nod = self.root
        i = datalen
        for bot in enbitstr:
            bit = int(bot)
            if i == 0:
                break
            if bit == 1:
                nod = nod.right
                if(nod.right == None and nod.left == None):
                    result.append(self.dic[nod.val])
                    nod = self.root
            elif bit == 0:
                nod = nod.left
                if(nod.right == None and nod.left == None):
                    result.append(self.dic[nod.val])
                    nod = self.root
            i -= 1

        return ''.join(result)

codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}

codeTree = PrefixCodeTree()
for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

message = codeTree.decode(b'\xd2\x9f\x20', 21)

print(message)