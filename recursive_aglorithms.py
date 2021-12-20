'''
[피보나치 순열]
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



def solution(x):
    # print('[' + str(x) + ']')
    if (x < 2): return x
    return solution(x - 1) + solution(x - 2)


'''
n 개의 서로 다른 원소에서 m 개를 택하는 경우,

도식화 하면...
1   2   3   4   5
2   3   4   5
3   4   5
4   5
5

수학식으로 나타내면
⎛n⎞          n!          ⎛ n - 1 ⎞      ⎛ n - 1 ⎞ 
     =  ------------- =             + 
⎝m⎠      m! (n - m)!     ⎝   m   ⎠      ⎝ m - 1 ⎠

'''
def comb(n, m):
    # print('[' + str(n) + ', ' + str(m) + ']')
    if n == m : return 1
    if m == 0 : return 1
    return comb(n - 1, m) + comb(n - 1, m - 1)

'''
하노이의 탑
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
    print(from_pos, '->>', to_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

hanoi(3, 1, 3, 2)








