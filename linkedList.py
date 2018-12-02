class linkedListNode:
    def __init__(self,data):
        self.data = data#data
        self.next = None#next node
'''
linkedList:
1.Reverse linkedList with inserting each node
(1)time complexity:O(n)
'''
def Reverse(head):#How to reverse a linkedList with head node
    if head is None or head.next is None:return
    cur = None#current node
    next = None#next node
    cur = head.next.next#the first node to insert

    head.next.next = None#the next of original node is nail
    while(cur is not None):
        next = cur.next#store the next node
        # insert the current node
        cur.next = head.next
        head.next = cur
        #insert the next node
        cur = next
'''
linkedList:
2.Reverse linkedList with recursive
(1)time complexity:O(n)
'''
def RecursiveReverse(head):
    if head is None or head.next is None:#linkedList is none or has only one node return this node
        return head
    else:
        newhead = RecursiveReverse(head.next)#recursive process
        head.next.next = head#head.next is not change during this recursive
        head.next = None
    return newhead

def ReverseRec(head):
    if head is None:
        return
    firstNode = head.next
    newhead = RecursiveReverse(firstNode)
    head.next = newhead
    return newhead

if __name__ == "__main__":#Creat a linkedList
    i = 0
    head = linkedListNode(-1)
    head.next = None
    tmp = None
    cur = head
    while i < 10:
        tmp = linkedListNode(i)
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("Before the reverse:")
    cur = head.next
    while cur is not None:
        print(cur.data,end='->')
        cur = cur.next
        if cur is None:
            print("end")
            break
    print("After the reverse")
    ReverseRec(head)#test the reverse function
    cur = head.next
    while cur!=None:
        print(cur.data,end='->')
        cur = cur.next
        if cur is None:
            print("end")
            break
