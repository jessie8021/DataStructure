'''
우선순위 큐 (Priority Queues)
 - 큐가 FIFO (First-In First_Out) 방식을 따르지 않고 원소들의 우선순위에 따리 큐에서 빠져 나오는 방식
 - 도식화

        Enqueue             Dequeue
            6                   2
            7                   3
            3                   6
            2                   7

 - 우선순위 큐의 구현: 서로 다른 방식이 가능하지만 (1) 번 방식이 탐색에 약간 유리함.
    (1) Enqueue 할 때 우선순위 순서를 유지하도록
    (2) Dequeue 할 때 우선순위 높은 것을 선택
'''

'''
앞선 강의에서 소개된 양방향 연결 리스트의 추상적 자료구조 구현인 클래스 DoublyLinkedList 를 이용하여 
우선순위 큐의 추상적 자료구조인 클래스 PriorityQueue 의 구현을 완성하세요.

코드의 윗부분은 양방향 연결 리스트를 이용하기 위한 클래스 Node 와 DoublyLinikedList 의 구현입니다. 
그대로 둔 채, 아래에 있는 class PriorityQueue 의 메서드들 중 
enqueue() 메서드의 구현을 위한 빈 칸 채우기만 완성하면 됩니다.
'''
from doublyLinkedList import *

class PriorityQueue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def size(self):
        return self.queue.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, x):
        # 4
        newNode = Node(x)

        # None 8 5 3 1 None
        curr = self.queue.head

        while curr.next.data is not None and newNode.data < curr.next.data:
            curr = curr.next

        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data

def solution():
    que = PriorityQueue()
    que.queue.insertAt(1, Node(8))
    que.queue.insertAt(2, Node(5))
    que.queue.insertAt(3, Node(3))
    que.queue.insertAt(4, Node(2))
    que.enqueue(7)

    print(que.queue.traverse())

solution()



