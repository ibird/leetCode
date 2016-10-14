# Definition for singly-linked list.
class MyListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def addNode(self, x):
        currentNode = self
        while currentNode.next is not None:
            currentNode = currentNode.next
        lastNode = currentNode
        newNode = MyListNode(x)
        lastNode.next = newNode

    def showNode(self):
        currentNode = self
        while currentNode.next is not None:
            print str(currentNode.val) + "->",
            currentNode = currentNode.next
        print str(currentNode.val)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        while l1 is not None or l2 is not None:
            l1v = 0 if l1 is None else l1.val
            l2v = 0 if l2 is None else l2.val

            rNode = MyListNode(l1v + l2v)
            if flag == 0:
                beginNode = rNode
                beforeNode = rNode
            elif flag == 1:
                beforeNode.next = rNode
                beforeNode = rNode

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            flag = 1

        currentNode = beginNode
        flag = 0
        further = 0
        while currentNode is not None:
            if currentNode.val >= 10:
                further = int(currentNode.val / 10)
                currentNode.val = currentNode.val % 10
            lastNode = currentNode
            currentNode = currentNode.next
            if further != 0 and currentNode is not None:
                currentNode.val += further

        if further != 0:
            newNode = MyListNode(further)
            lastNode.next = newNode
        return beginNode


if __name__ == "__main__":
    a = MyListNode(2)
    a.addNode(4)
    a.addNode(3)
    b = MyListNode(5)
    b.addNode(6)
    b.addNode(6)
    a.showNode()
    b.showNode()
    c = Solution().addTwoNumbers(a, b)
    c.showNode()
