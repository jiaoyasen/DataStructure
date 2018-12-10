import collections
class BiTNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None



def array2tree(arr,start,end):
    root = None
    if end >=start:
        root = BiTNode()
        mid = int((start + end +1 )/2)
        root.data = arr[mid]
        root.lchild = array2tree(arr,start,mid-1)
        root.rchild = array2tree(arr,mid+1,end)
    else:
        root = None
    return root


def printTreeMidOrder(root):
    if root is None:
        return
    if root.lchild is not None:
        printTreeMidOrder(root.lchild)
    print(root.data)
    if root.rchild is not None:
        printTreeMidOrder(root.rchild)


def printTreeLayer(root):
    if root is None:
        return

    queue = collections.deque()
    queue.append(root)
    while len(queue)>0:
        p = queue.popleft()
        print(p.data)
        if p.lchild is not None:
            queue.append(p.lchild)
        if p.rchild is not None:
            queue.append(p.rchild)





if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("数组：")
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1

    root = array2tree(arr,0,len(arr)-1)
    print("转换为树的中序遍历为：")
    printTreeMidOrder(root)
    printTreeLayer(root)



