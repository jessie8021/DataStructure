'''
스택 (Stacks)
 - 추가된 데이터 원소들을 입력된 역순으로 마지막 원소부터 꺼내는 자료구조
 - 후입선출 (LIFO : last-in first-out)
 - 스택 언더플로우 (stack underflow) : 비어있는 스택에서 데이터 원소를 꺼내려 할 때 발생하는 오류.
 - 스택 오버플로우 (stack overflow) : 꽉 찬 스택에 데이터 원소를 넣으려 할 떄 발생하는 오류.
 - 도식화

    | [D] |  S = stack()
    | [C] |  S.push(A)
    | [B] |  S.push(B)
    | [A] |  S.push(C)
    ------   S.push(D)

'''

from doublyLinkedList import Node
from doublyLinkedList import DoublyLinkedList

class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

class LinkedListStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data


def test() :
    aryStack = ArrayStack()
    aryStack.push(11)
    aryStack.push(12)
    aryStack.push(13)

    print(aryStack.data)
    print(aryStack.peek())

    linkedStack = LinkedListStack()
    linkedStack.push(111)
    linkedStack.push(222)
    linkedStack.push(333)

    print(linkedStack.peek())


'''
소괄호: ( )
중괄호: { }
대괄호: [ ]
를 포함할 수 있는 수식을 표현한 문자열 expr 이 인자로 주어질 때, 
이 수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수 solution() 을 완성하세요. 
이 함수는 수식의 괄호가 유효하면 True 를, 그렇지 않으면 False 를 리턴합니다.

스택을 활용하여 수식 내의 괄호 여닫음의 유효성을 검사하는 알고리즘에 대해서는 동영상 강의 내용을 참고하세요.

*** 수식의 괄호 유효설 검사 ***
 - 알고리즘 설계 - 수식을 왼쪽부터 한 글자씩 읽어서:
    • 여는 괄호 - ( 또는 { 또는 { 를 만나면 스택에 푸쉬
    • 닫는 괄호 - ) 또는 } 또는 ] 를 만나면 :
        • 스택이 비어 있으면 올바르지 않은 수식
        • 스택에서 pop, 쌍을 이루는 여는 괄호인지 검사
            • 맞지 않으면 올바르지 않은 수식
            
    끌까지 검사한 후, 스택이 비어 있어야 올바른 수식
    


'''
def solution(expr):
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    S = ArrayStack()

    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            if S.isEmpty():
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()

print(solution('{(A + B) * C}'))