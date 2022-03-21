'''
[피보나치 수열]
인자로 0 또는 양의 정수인 x 가 주어질 때,
Fibonacci 순열의 해당 값을 구하여 반환하는 함수 solution() 을 완성하세요.

Fibonacci 순열은 아래와 같이 정의됩니다.
F0 = 0
F1 = 1
Fn = Fn - 1 + Fn - 2, n >= 2

재귀함수 작성 연습을 의도한 것이므로,
재귀적 방법으로도 프로그래밍해 보고,
반복적 방법으로도 프로그래밍해 보시기 바랍니다.
'''
def solution(x):
    f0 = 0
    f1 = 1
    s = 0
    cnt = 1

    if x <= cnt: return x
    while cnt < x:
        s = f0 + f1
        f0 = f1
        f1 = s
        x -= 1
    return s

'''
[풀이]                                1️⃣
                            fibo(4) → def fibo(4):  3
                                        if 4 < 2: return 4                   ← #1       8️⃣
                                        return fibo(4-1) + fibo(4-2)         →          def fibo(2):
                                                                                            if 2 < 2: return 2
                                                ↓ ↑ #2                                      return fibo(2-1) + fibo(2-2)
                                    2️⃣                                 
                                      def fibo(3):                                             ↓ ↑ #1             ↓ ↑ #0      
                                        if 3 < 2: return 3                          9️⃣                              🔟
                                        return fibo(3-1) + fibo(3-2)                def fibo(1):                    def fibo(0):
                                                                                        if 1 < 2: return 1              if 0 < 2: return 0
                                            ↓ ↑ #1              ↓ ↑ #1
                 3️⃣                                             6️⃣
                 def fibo(2):                                   def fibo(1):
                    if 2 < 2: return 2                              if 1 < 2: return 1
                    return fibo(2-1) + fibo(2-2) 
                    
                                         
                            ↓ ↑ #1      ↓ ↑ #0
          4️⃣                         5️⃣
          def fibo(1):              def fibo(0):
            if 1 < 2: return 1          if 0 < 2: return 0
          

'''
def fibo(x):
    if (x < 2): return x
    return solution(x - 1) + solution(x - 2)

'''
[순열]
n(5) 개의 서로 다른 원소에서 m(2) 개를 택하는 경우,

도식화 하면...
    1   2   3   4   5

    2   3   4   5
    3   4   5
    4   5
    5
    ↓   ↓   ↓   ↓      
    4   3   2   1

    ⌦ 4 + 3 + 2 + 1 = 10

수학식으로 나타내면
⎛n⎞          n!          ⎛ n - 1 ⎞      ⎛ n - 1 ⎞ 
     =  ------------- =             + 
⎝m⎠      m! (n - m)!     ⎝   m   ⎠      ⎝ m - 1 ⎠


[풀이]
    comb(5,2)
        
    return comb(4,2) + comb(4,1)
                            ↓
            ⎥           return comb(3,1) + comb(3,0)
            ⎥                           ↓
            ⎥                   return comb(2,1) + comb(2,0)
            ⎥                                  ↓
            ↓                          return comb(1,1) + comb(1,0)
    
    return comb(3,2) + comb(3,1)
                            ↓
            ⎥           return comb(2,1) + comb(2,0)
            ⎥                           ↓
            ↓                  return comb(1,1) + (1,0)
    
    return comb(2,2) + comb(2,1)
                            ↓
                        return comb(1,1) + comb(1,0)
    
'''
def comb(n, m):
    # print('[' + str(n) + ', ' + str(m) + ']')
    if n == m : return 1
    if m == 0 : return 1
    return comb(n - 1, m) + comb(n - 1, m - 1)

# print(comb(5, 2))
''' 
[하노이의 탑]
1. 크기가 다른 원반 n개를 출발점 기둥에서 도착점 기둥로 전부 옮겨야 한다.
2. 원반은 한 번에 한 개씩만 옮길 수 있다.
2. 원반을 옮길 때는 한 기둥의 맨 위 원반을 빼내어, 다른 기중의 맨 위로만 옮길 수 있다.
4. 원반을 옮기는 과정에서 큰 원반을 작은 원반 위로 올릴 수 없다.

 

- 하노이의 탑 알고리즘 풀이

1. 원반이 n개 일때, 1번 기둥에 있는 n-1개의 원반을 2번 기둥에 옮긴다.
2. 1번 기둥에 남아 있는 원반 중 가장 큰 원반을 3번으로 옮긴다.
3. 2번 기둥에 있는 n-1원반을 3번 기둥으로 옮긴다.

1 : a - b - c - a - b - c - a - b - c
2 : a - c - b - a - c
3 : a - b - c
4 : a - c

'''
def hanoi(n, from_pos, to_pos, aux_pos):
    # print(n, ' - ', from_pos, to_pos, aux_pos)
    if n == 1:
        print(from_pos, '->>', to_pos)
        return

    hanoi(n-1, from_pos, aux_pos, to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

# hanoi(3, 'a', 'b', 'c')
'''

[재귀적 이진탐색]
리스트 L 과, 그 안에서 찾으려 하는 원소 x 가 인자로 주어지고, 
또한 탐색의 대상이 되는 리스트 내에서의 범위 인덱스가 l 부터 u 까지로 (인자로) 정해질 때, 
x 와 같은 값을 가지는 원소의 인덱스를 리턴하는 함수 solution() 을 완성하세요. 
만약 리스트 L 안에 x 와 같은 값을 가지는 원소가 존재하지 않는 경우에는 -1 을 리턴합니다. 
리스트 L 은 자연수 원소들로 이루어져 있으며, 크기 순으로 정렬되어 있다고 가정합니다. 
또한, 동일한 원소는 두 번 이상 나타나지 않습니다.

인덱스 범위를 나타내는 l 과 u 가 인자로 주어지는 이유는, 
이 함수를 재귀적인 방법으로 구현하기 위함입니다. 
빈 칸에 알맞은 내용을 채워서 재귀 함수인 solution() 을 완성하세요.

예를 들어,
L = [2, 3, 5, 6, 9, 11, 15]
x = 6
l = 0
u = 6
의 인자들이 주어지면, L[3] == 6 이므로 3 을 리턴해야 합니다.

또 다른 예로,
L = [2, 5, 7, 9, 11]
x = 4
l = 0
u = 4
로 주어지면, 리스트 L 내에 4 의 원소가 존재하지 않으므로 -1 을 리턴해야 합니다.


'''
def solution(L, x, l, u):
    if x < L[l] or x > L[u]:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)
# print(solution([2, 5, 7, 9, 11], 7, 0, 4))

