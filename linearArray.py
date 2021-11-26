'''
리스트 원소의 합

입력으로 주어지는 리스트 x 의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution() 을 완성하세요.
'''
def solution(x):

    return x[0] + x[len(x) - 1]

def solution(x):

    return x[0] + x[-1]

# print(solution([2,3,5,6,7,8,9]))

'''
정렬된 리스트에 원소 삽입
리스트 L 과 정수 x 가 인자로 주어질 때, 리스트 내의 올바른 위치에 x 를 삽입하여 그 결과 리스트를 반환하는 함수 solution 을 완성하세요.

인자로 주어지는 리스트 L 은 정수 원소들로 이루어져 있으며 크기에 따라 (오름차순으로) 정렬되어 있다고 가정합니다.

예를 들어, L = [20, 37, 58, 72, 91] 이고 x = 65 인 경우, 올바른 리턴 값은 [20, 37, 58, 65, 72, 91] 입니다.

힌트: 순환문을 이용하여 올바른 위치를 결정하고 insert() 메서드를 이용하여 삽입하는 것이 한 가지 방법입니다.

주의: 리스트 내에 존재하는 모든 원소들보다 작거나 모든 원소들보다 큰 정수가 주어지는 경우에 대해서도 올바르게 처리해야 합니다.
'''

def solution(L, x):
    max = len(L)
    min = 0
    p = int(max / 2)

    while True:
        if L[p] == x:
            break
        elif L[p] < x:
            p += 1
            
            if max <= p:
                p = max
                break
            if L[p] > x: break

        elif L[p] > x:
            p -= 1

            if min >= p:
                p = min
                if L[p] < x: p += 1
                break
            if L[p] < x: break

    L.insert(p, x)
    return L

def solution(L, x):

    if L[-1] <= x:
        L.append(x)
        return L

    for i, j in enumerate(L):
        if j > x:
            L.insert(i, x)
            break

    return L
# print(solution([20, 37, 58, 72, 91, 98], 97))

'''
인자로 주어지는 리스트 L 내에서, 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 이 인덱스들로 이루어진 리스트를 반환하는 함수 solution 을 완성하세요.

리스트 L 은 정수들로 이루어져 있고 그 순서는 임의로 부여되어 있다고 가정하며, 동일한 원소가 반복하여 들어 있을 수 있습니다. 
이 안에 정수 x 가 존재하면 그것들을 모두 발견하여 해당 인덱스들을 리스트로 만들어 반환하고, 만약 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1] 를 반환하는 함수를 완성하세요.

예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 72 인 경우의 올바른 리턴 값은 [1, 3] 입니다.
또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 83 인 경우의 올바른 리턴 값은 [2] 입니다.
마지막으로 또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 49 인 경우의 올바른 리턴 값은 [-1] 입니다.

힌트 1: 리스트의 index() 메서드와 리스트 슬라이싱을 활용하는 것이 한 가지 방법이 됩니다. 리스트 슬라이싱은 아래와 같이 동작합니다.

L = [6, 2, 8, 7, 3] 인 경우
L[1:3] = [2, 8]
L[2:] = [8, 7, 3]
L[:3] = [6, 2, 8]

힌트 2: 리스트의 index() 메서드는, 인자로 주어지는 원소가 리스트 내에 존재하지 않을 때 ValueError 를 일으킵니다. 
이것을 try ... except 로 처리해도 되고, "if x in L" 과 같은 조건문으로 특정 원소가 리스트 내에 존재하는지를 판단해도 됩니다.
'''

def solution(L, x):
    anwser = [i for i, j in enumerate(L) if j == x]
    return [-1] if len(anwser) == 0 else anwser

def solution(L, x):
    anwser = []
    maxIndex = len(L)
    index = 0
    checkIndex = 0
    try :
        while maxIndex != checkIndex:
            index = L[checkIndex:].index(x)
            checkIndex += index
            anwser.append(checkIndex)
            checkIndex += 1
        return anwser

    except ValueError:
        return [-1] if len(anwser) == 0 else anwser

# print(solution([64, 72, 83, 72, 54], 54))