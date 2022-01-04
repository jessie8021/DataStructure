'''
*** Linked List ***

 - [data | next] 데이터와 링크에 대한 정보를 포함한 Node가 일렬로 연결되어 있는 리스트.
 - 장점 : 삭제, 삽입이 용이
 - 단점 : head에서 tail까지의 순회는 용의하나, 역방향이 어려움
 - 사용 예 : 스마트폰의 홈버튼은 누를 시, 일렬로 표현되는 사용중인 앱 리스트
 - 도식

  [[head]]                                                              [[tail]]
  [43 | next address] -> [85 | next address] -> [62 | next address] -> [18 | None]

 - 연산정의
   1. 길이 얻어내기
   2. 리스트 순회
   3. 특정원소 참조(k번째)
   4. 원소 삽입
   5. 원소 삭제
   6. 두 리스트 합치기
'''

class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getLength(self):
        return self.nodeCount

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    '''
    제 7 강에서 소개된 추상적 자료구조로 LinkedList 라는 이름의 클래스가 정의되어 있다고 가정하고,
    이 리스트를 처음부터 끝까지 순회하는 메서드 traverse() 를 완성하세요.

    메서드 traverse() 는 리스트를 리턴하되,
    이 리스트에는 연결 리스트의 노드들에 들어 있는 데이터 아이템들을 연결 리스트에서의 순서와 같도록 포함합니다.
    예를 들어, LinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [43, 85, 62] 입니다.

    이 규칙을 적용하면, 빈 연결 리스트에 대한 순회 결과로 traverse() 메서드가 리턴해야 할 올바른 결과는 [] 입니다.

    [참고] "실행" 을 눌렀을 때 통과하는 것은 아무 의미 없습니다.

    '''
    def traverse(self):
        node = self.head
        data = []
        if node == None: return data

        while node:
            data.append(node.data)
            node = node.next
        return data

    '''
    제 8 강에서 소개된 추상적 자료구조 LinkedList 클래스의 메서드로서 
    popAt() 메서드를 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.

    초기 코드로 들어 있는 것은 solution() 함수를 포함하여 다른 부분은 수정하지 말고, 
    def popAt(self, pos): 의 메서드 몸체만 구현하세요.

    만약, 인자로 주어진 pos 가 올바른 범위의 값을 가지지 않는 경우에는 IndexError exception 을 발생시키도록 합니다. 
    이렇게 하기 위한 코드는 raise IndexError 입니다.

    (1) 삭제하려는 node가 맨 앞의 것일때
     - prev 없음
     - Head 조정 필요

    (2) 리스트 맨 끝의 node를 삭제할 때
     - Tail조정 필요
     
    (3) 유일한 노드일때

    '''
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        prev = self.getAt(pos - 1)

        if prev is None:
            curr = self.head
            if self.nodeCount == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        else:
            curr = prev.next
            prev.next = curr.next

            if pos == self.nodeCount:
                self.tail = prev

        self.nodeCount -= 1
        return curr.data

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount


# 이 solution 함수는 그대로 두어야 합니다.
def solution():
    node1 = Node(43)
    node2 = Node(85)
    node3 = Node(62)
    node4 = Node(18)

    mylink = LinkedList()
    mylink.insertAt(1, node1)
    mylink.insertAt(2, node2)
    mylink.insertAt(3, node3)
    mylink.insertAt(4, node4)

    # print(mylink.popAt(4))
    print(mylink.traverse())
    print(mylink.head.data)
    print(mylink.tail.data)
    print(mylink.getLength())



solution()