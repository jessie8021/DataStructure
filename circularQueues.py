'''
환형 큐 (Circular Queues)
 - 이용 예
    • 컴퓨터시스템에서 서로 다른 응용 프로그램들이 프린터에 인쇄할 경우 - 운영체제에서
        프린팅 큐라는 자료 구조를 유지하여 프린터에 보내진 문서를 유지
    • 네트워크 인터페이스를 통하여 도착하는 패킷(packet) 들도 큐에 쌍아서 도착한 순서대로
        해당 응용 프로그램에게 데이터 송신하는 기능
 - 큐의 데이터 원소 개수가 유한하므로, 원소의 상한을 정하고 선형 배열의 한쪽 끝과 다른 쪽 끝이
   맞닿는 환형 큐를 이용해 데이터 저장소를 재활용 하면서 데이터를 관리.
    • front : 큐의 맨 앞
    • rear : 큐의 맨 뒤
 - 활용
    • 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비 동기적으로 일어나는 경우 활용
    • 자료를 생성하는 작업이 여러 곳에서 일어나는 경우
    • 자료를 이용하는 작업이 여러 곳에서 일어나는 경우
    • 자료를 생성하는 작업과 그 자료를 이용하는 작업이 여러 곳에서 일어나는 경우

        [Consumer1] ---------------------------- [Producer1]
                     ↖     ⎡  ⎤     ⎡  ⎤      ↙
                           ⎜  ⎪     ⎜  ⎪
                     ↙     ⎣  ⎦     ⎣  ⎦      ↖
        [Consumer2] ---------------------------- [Producer2]

    • 자료를 처리하여 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야 하는 작업의 경우

 - 환형 큐 : 정해진 개수의 저장 공간을 빙 돌려가며 이용
 - 연산의 정의
    • size() - 현재 큐에 들어 있는 데이터 원소의 수를 구함
    • isEmpty() - 현재 큐가 비어 있는 지를 판단
    • isFull() - 데이터 원소가 꽉 차 있는지를 판
    • enqueue(x) - 데이터 원소 x 를 큐에 추가
    • dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거 (또한, 반환)
    • peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)
'''
'''
Python 의 내장 데이터형인 리스트 (list) 를 이용하여 
환형 큐의 추상적 자료 구조를 구현한 클래스 CircularQueue 를 완성하세요.
'''
class CircularQueue:
    def __init__(self, n):
        self.maxCount = n   # 6
        self.data = [None] * n  # 6
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = self.rear + 1 if self.rear < (self.maxCount - 1) else 0
        self.data[self.rear] = x
        self.count += 1


    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = self.front + 1 if self.front < (self.maxCount - 1) else 0
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[self.front + 1 if self.front < (self.maxCount - 1) else 0]

def solution():
    que = CircularQueue(6)

    que.enqueue(11)
    que.enqueue(22)
    que.enqueue(33)
    que.enqueue(44)
    que.enqueue(55)
    que.enqueue(66)


    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()


    que.enqueue(111)
    # que.enqueue(222)
    # que.enqueue(333)
    # que.enqueue(444)
    # que.enqueue(555)
    # que.enqueue(666)


    print('front: ', str(que.front), ', rear: ', str(que.rear), ', count: ', str(que.count))
    print(que.data)
    print(que.peek())

solution()

