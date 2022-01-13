'''
양방향 연결 리스트(Doubly Linked Lists)
 - 노드들이 앞/뒤로 연결되어 있음.
 - head 와 tail 에 dummy node 추
 - 단점 : 링크를 나타내기 위한 메모리 사용량이 을어남.
 - 장점 : 데이터 원소들을 앞/뒤 양방향에서 차례로 방문가능.
 - 도식화

 [head]                                                                                                   [tail]
 [prev(None) | dummy | next] <--> [prev | 43 | next] <--> [prev | 85 | next] <--> [prev | 62 | next] <--> [prev | dummy | next(None)]

'''


class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    '''
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여, 또한 강의 내용에서 언급한 reverse() 메서드를 구현하세요.
    이 reverse() 메서드는 양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지 (tail 방향에서 head 방향으로) 순회하면서, 
    방문하게 되는 node 에 들어 있는 data item 을 순회 순서에 따라 리스트에 담아 리턴합니다.
    예를 들어, DoublyLinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [62, 85, 43] 입니다.
    이 규칙을 적용하면, 빈 연결 리스트에 대한 역방향 순회 결과로 reverse() 메서드라 리턴해야 할 올바른 결과는 [] 입니다.
    '''
    def reverse(self):
        result = []

        curr = self.tail

        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)

        return result

    def traverse(self):
        result = []
        curr = self.head

        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getLength(self):
        return self.nodeCount

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr

    def insertAfter(self, prev, newNode):
        next = prev.next

        newNode.prev = prev
        newNode.next = next

        prev.next = newNode
        next.prev = newNode

        self.nodeCount += 1

        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)

        return self.insertAfter(prev, newNode)

    '''
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 의 메서드로 insertBefore() 를 구현하세요.
    이 insertBefore() 메서드에는 두 개의 인자가 주어지는데, 
    next 는 어느 node 의 앞에 새로운 node 를 삽입할지를 지정하고, 
    newNode 는 삽입할 새로운 node 입니다.
    강의 내용에서 소개된 insertAfter() 메서드의 구현과 매우 유사하게 할 수 있습니다.
    '''
    def insertBefore(self, next, newNode):
        prev = next.prev

        newNode.prev = prev
        newNode.next = next

        prev.next = newNode
        next.prev = newNode

        self.nodeCount += 1

        return True

    '''
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여 node 의 삭제 연산에 관련한 아래와 같은 메서드들을 구현하세요.
    popAfter()
    popBefore()
    popAt()
    popAfter(prev) 는 인자 prev 에 의하여 주어진 node 의 다음에 있던 node 를 삭제하고, 
    popBefore(next) 는 인자 next 에 의하여 주어진 node 의 이전에 있던 node 를 삭제합니다.
    그리고 삭제되는 node 에 담겨 있던 data item 을 리턴합니다.

    popAt(pos) 는 인자 pos 에 의하여 지정되는 node 를 삭제하고 그 node 에 담겨 있던 data item 을 리턴하는데, 
    위 popAfter() 또는 popBefore() 를 호출하여 이용하는 방식으로 구현하세요. 
    또한, 만약 인자 pos 가 올바른 범위 내에 있지 않은 경우에는 raise IndexError 를 이용하여 IndexError exception 을 일으키도록 구현하세요.

    테스트 케이스 1-3 은 각각 (1) popAfter(), (2) popBefore(), (3) popAt() 메서드의 올바른 동작을 검증하는 케이스입니다.
    '''
    def popAfter(self, prev):
        curr = prev.next
        next = curr.next

        prev.next = curr.next
        next.prev = curr.prev

        self.nodeCount -= 1

        return curr.data


    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev

        prev.next = curr.next
        next.prev = curr.prev

        self.nodeCount -= 1

        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        return self.popAfter(self.getAt(pos - 1))

    '''
    제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여 두 개의 양방향 연결 리스트를 앞뒤로 이어 붙이는 메서드 concat() 을 구현하세요.
    예를 들어, 양방향 연결 리스트 L1 에는 1 -> 2 -> 3 의 원소가 순서대로 들어 있고, 
    또다른 양방향 연결 리스트 L2 에는 4 -> 5 의 순서로 원소가 들어 있을 때, 
    메서드 호출 L1.concat(L2) 의 결과로 L1 은 1 -> 2 -> 3 -> 4 -> 5 의 양방향 연결 리스트가 됩니다. 
    물론, L1 또는 L2 또는 둘 다가 비어 있는 양방향 연결 리스트인 경우도 고려되도록 코드를 작성해야 합니다.
    '''
    def concat(self, L):
        prev = self.tail.prev
        next = L.head.next

        prev.next = next
        next.prev = prev

        self.tail = L.tail
        self.nodeCount += L.nodeCount


def solution(x):
    node1 = Node(43)
    node2 = Node(85)
    node3 = Node(62)

    node4 = Node(11)
    node5 = Node(12)
    node6 = Node(13)

    mylink = DoublyLinkedList()
    # mylink.insertAfter(mylink.head, node1)
    # mylink.insertAfter(node1, node2)
    # mylink.insertAfter(node2, node3)

    mylink2 = DoublyLinkedList()
    # mylink2.insertAfter(mylink2.head, node4)
    # mylink2.insertAfter(node4, node5)
    # mylink2.insertAfter(node5, node6)

    print(mylink.traverse())

    # print(mylink.popAfter(node2))
    # print(mylink.popBefore(node2))
    # print(mylink.popAt(2))
    mylink.concat(mylink2)

    print(mylink.traverse())


    return 0

# solution(1)

