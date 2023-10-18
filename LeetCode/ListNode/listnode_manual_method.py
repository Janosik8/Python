class ListNode():
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1
if currentNode.value != None:
    while True:
        print(currentNode.value, "->", end=" ")
        if currentNode.nextNode == None:
            print("None", end="")
            break
        currentNode = currentNode.nextNode


