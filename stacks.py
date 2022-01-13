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

# print(solution('{(A + B) * C}'))

'''
스택의 응용 - 수식의 후위 표기법(postfix Notation)
 -  중위 표기법 (infix notaion)
    • 연산자가 피연산자들의 사이에 위치
    • (A + B) * (C + D)
    
 - 후위 표기법 (postfix notation)
    • 연산자가 피연산자들의 뒤에 위치
    • AB + CD +*
    • 괄호의 처리 : 여는 괄호는 스택에 push. 닫는 괄호는 여는 괄호를 만날때까지 pop
       
 - 알고리즘의 설계
    • 중위 표현식을 왼쪽부터 한글씩 읽어서
        피연산자이면 그냥 출력
        ')' 이면 '(' 이 나올 때까지 스택에서 pop, 출력
        연산자이면 스택에서 이보다 높거나 (같은) 우선순위의 것들을 pop 출력
            그리고 이 연산자는 스택에 push
    • 스택에 남아 있는 연산자는 모두 pop, 출력
'''

'''
중위 표기법을 따르는 수식 S 가 인자로 주어질 때, 
이 수식을 후위 표기법을 따르는 수식으로 변환하여 반환하는 함수 solution() 을 완성하세요.

인자로 주어지는 수식 문자열 S 는 영문 대문자 알파벳 한 글자로 이루어지는 변수 A - Z 까지와 4칙연산을 나타내는 
연산자 기호 +, -, *, /, 그리고 여는 괄호와 닫는 괄호 (, ) 로 이루어져 있으며 공백 문자는 포함하지 않는 것으로 가정합니다. 
또한, 올바르게 구성되지 않은 수식은 인자로 주어지지 않는다고 가정합니다. (수식의 유효성은 검증할 필요가 없습니다.)

문제에서 미리 주어진, 연산자의 우선순위를 표현한 python dict 인 prec 을 활용할 수 있습니다.
또한, 스택의 기초 강의에서 이미 구현한, 배열을 이용한 스택의 추상적 자료 구조 코드가 이미 포함되어 있으므로 그대로 이용할 수 있습니다.
'''

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''

    for c in S:
        if c in prec:
            if opStack.isEmpty() or prec[opStack.peek()] < prec[c] or c == '(':
                opStack.push(c)
            else:
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[c]:
                    answer += opStack.pop()
                opStack.push(c)
        elif c == ')':
            while not opStack.isEmpty():
                op = opStack.pop()
                if op == '(':
                    break
                answer += op
        else:
            answer += c

    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer
'''
print(solution('(A+(B-C))*D'))  #ABC-+D*
print(solution('A*(B-(C+D))'))  #ABCD+-*
print(solution('((A+B)*(C+D))'))    # AB+CD+*
print(solution('A*B+C'))  #AB*C+
print(solution('A+B*C'))  #ABC*+
print(solution('A+B+C'))    #AB+C+
print(solution('A+B+C*D'))    #
print(solution('(A+B)*C'))  #AB+C*
print(solution('A*(B+C)')) #ABC+*
'''

'''
인자로 주어진 문자열 expr 은 소괄호와 사칙연산 기호, 그리고 정수들로만 이루어진 중위 표현 수식입니다. 
함수 solution() 은 이 수식의 값을 계산하여 그 결과를 리턴하도록 작성되어 있습니다. 
이 함수는 차례로 splitTokens(), infixToPostfix(), 그리고 postfixEval() 함수를 호출하여 
이 수식의 값을 계산하는데,

splitTokens() - 강의 내용에서와 같은 코드로 이미 구현되어 있습니다.
infixToPostfix() - 지난 강의의 연습문제에서 작성했던 코드를 수정하여, 문자열이 아닌 리스트를 리턴하도록 작성합니다.
postfixEval() - 이번 강의의 연습문제입니다. 함수의 내용을 완성하세요.
즉, 두 개의 함수 infixToPostfix() 와 postfixEval() 을 구현하는 연습입니다. 
스택을 이용하기 위하여 class ArrayStack 이 정의되어 있으므로 그것을 활용하세요.
'''

def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False

    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens

def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    opStack = ArrayStack()
    postfixList = []

    for t in tokenList:
        if t in prec:
            if opStack.isEmpty() or  prec[opStack.peek()] < prec[t] or t == '(':
                opStack.push(t)
            else:
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[t]:
                    postfixList.append(opStack.pop())
                opStack.push(t)
        elif t == ')':
            while not opStack.isEmpty():
                op = opStack.pop()
                if op == '(':
                    break
                postfixList.append(op)
        else:
            postfixList.append(t)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList

def postfixEval(postfix):
    # [12, 10, 3, '-', '+', 2, '*']

    opStack = ArrayStack()
    for p in postfix:
        t = type(p)
        if t == int:
            opStack.push(p)
        elif t == str:
            op1 = opStack.pop()
            op2 = opStack.pop()

            if p == '+':
                opStack.push(op2 + op1)
            elif p == '-':
                opStack.push(op2 - op1)
            elif p == '*':
                opStack.push(op2 * op1)
            elif p == '/':
                opStack.push(op2 / op1)
    return opStack.data[-1]


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)

    print(val)

    # return val


solution('(12+(10-3))*2')   #ABC-+D* 38
solution('2*(3-(3+6))')     #ABCD+-* -12
solution('((2+3)*(5+6))')   #AB+CD+* 55
solution('12*3+2')          #AB*C+ 38
solution('7+8*9')           #ABC*+ 79
solution('5+6+7')           #AB+C+ 18
solution('34+5+6*4')        #AB+CD*+ 63
solution('(4+5)*4')         #AB+C* 36
solution('5*(4+1)')         #ABC+* 25