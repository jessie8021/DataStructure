'''
*** 변형된 연결 리스트 ***
 - head에 dummy node를 추가한 형태
 - 도식

  [[head]]                                                                                      [[tail]]
  [None | next address] -> [43 | next address] -> [85 | next address] -> [62 | next address] -> [18 | None]

'''

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    '''
    제 9 강에서 소개된 추상적 자료구조 LinkedList 는 dummy head node 를 가지는 연결 리스트입니다. 
    이 클래스의 아래와 같은 메서드들을, 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.

    popAfter()
    popAt()
    이 때, popAt() 메서드의 구현에서는 popAfter() 를 호출하여 이용하도록 합니다. 
    (그렇게 하지 않을 수도 있지만, 여기에서는 popAfter() 의 이용에 의해서 코드 구현이 보다 쉬워지는 것을 확인하기 위함입니다.)

    초기 코드로 들어 있는 것은 solution() 함수를 포함하여 다른 부분은 수정하지 말고, def popAfter(self, prev): 와 def popAt(self, pos): 의 메서드 몸체만 구현하세요.

    만약, popAt() 메서드에 인자로 주어진 pos 가 올바른 범위의 값을 가지지 않는 경우에는 IndexError exception 을 발생시키도록 합니다. 
    이렇게 하기 위한 코드는 raise IndexError 입니다.
    '''

    def popAfter(self, prev):
        if prev.next is None:
            raise IndexError

        curr = prev.next
        prev.next = curr.next

        if curr.next is None:
            self.tail = prev

        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        return self.popAfter(self.getAt(pos - 1))


def solution(x):
    node1 = Node(43)
    node2 = Node(85)
    node3 = Node(62)
    node4 = Node(18)

    L = LinkedList()
    L.insertAfter(L.head, node1)
    L.insertAfter(node1, node2)
    L.insertAfter(node2, node3)
    L.insertAfter(node3, node4)

    print(L.traverse())
    L.popAt(4)
    print(L.traverse())
    print(L.head.data)
    print(L.tail.data)
solution(1)