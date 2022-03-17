''''
Heap
 - 이진 트리의 한 종류(이진 힙 - binary heap)
    1. Root Node가 언제나 최댓값 또는 최솟값을 가짐.
        - 최대 힙(max heap), 최소 힙(min heap)
    2. 완전 이진 트리여야 함.
        - 높이 k 인 완전 이진 트리
        - 레벨 k-2 까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리
        - 레벨 k-1 에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리

                       [A]
                 ↙             ↘
            [B]                 [C]
          ↙     ↘             ↙     ↘
       [D]      [E]          [F]    [G]
      ↙   ↘    ↙
   [H]    [I][J]
 - 최대 힙의 예 : 재귀적으로도 정의됨.(어느 노드를 루트로 하는 서브트리도 모두 최대 힙)

                        [30]
                 ↙             ↘

            [24]                [12]

          ↙     ↘             ↙     ↘

       [18]     [21]       [8]      [6]

      ↙   ↘    ↙

   [4]    [2][19]
 - 최대 힙(Max Heap) 의 추상적 자료 구조
    연산의 정의
    ∙ __init__() - 빈 최대 힙을 생성
    ∙ insert(item) - 새로운 원소를 삽입
    ∙ remove() - 최대 원소 (root node) 를 반환
                (그리고 동시에 이 노드를 삭제)
 - 데이터 표현의 설계
    배열을 이용한 이진 트리의 표현

                        [30] 1                          노드번호 m을 기준으로
                 ↙              ↘                       ∙ 왼쪽 자식의 번호 : 2 * m
                                                        ∙ 오른쪽 자식의 번호 : 2 * m + 1
           2 [24]              3 [12]                   ∙ 부모 노드의 번호 : m // 2

          ↙      ↘              ↙      ↘                완전 이진 트리이므로
                                                        ∙ 노드의 추가 / 삭제는 마지막 노드 에서만
    4 [18]     5 [21]      6 [8]      7 [6]

     ↙   ↘     ↙                                        [-, 30, 24, 12, 18, 21, 8, 6, 4, 2, 19]

  [4]    [2] [19]
  8       9   10

 - 최대 힙에 원소 삽입
    1. 트리의 마지막 자리에 새로운 원소를 임시로 저장
    2. 부모 노드와 키 값을 비교하여 위로 .., 이동

 - 최대 힙에서 원소의 삭제
    1. 루트 노드의 제거 - 이것이 원소들 중 최댓값
    2. 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치
    3. 자식 노드들과의 값 비교와 아래로, 아래로 이동
        - 자식이 둘인 경우, 더 큰 수 쪽으로 이동
 - 최대/최소 힙의 응용
    1. 우선 순위 큐(priority queue)
        ∙ Enqueue할 때 "느슨한 정렬"을 이루고 있도록 함: O(logn)
        ∙ Dequeue할 때 최댓값을 순서대로 호출: O(logn)
    2. 힙 정렬(heap sort)
        ∙ 정렬되지 않은 원소들을 아무 순서로나 최대 힙에 삽입: O(logn)
        ∙ 삽입이 끝나면, 힙이 비게 될 때까지 하나씩 삭제: O(logn)
        ∙ 원소들이 삭제된 순서가 원소들의 정렬 순서
        ∙ 정렬 알고림즘의 복잡도: O(nlogn)
'''
class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)

        itemIndex = self.data.index(item)
        parentIndex = itemIndex // 2

        if parentIndex == 0:
            return

        while parentIndex > 0 and self.data[parentIndex] < item :
            self.data[itemIndex], self.data[parentIndex] = self.data[parentIndex], item
            itemIndex = parentIndex
            parentIndex = itemIndex // 2

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        smallest = i

        if len(self.data) > left and self.data[left] > self.data[i]:
            smallest = left
        if len(self.data) > right and self.data[right] > self.data[left]:
            smallest = right
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxHeapify(smallest)


### 힙 정렬(heap sort)의 코드 구현
def heapsort(unsorted):
    H = MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted = []
    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted


def solution():
    print('--solution--')

    # print(heapsort([30, 24, 12, 18, 21, 8, 6, 4, 2, 19]))


    myheap = MaxHeap()
    myheap.insert(24)
    myheap.insert(30)
    myheap.insert(12)
    myheap.insert(18)
    myheap.insert(21)
    myheap.insert(8)
    myheap.insert(6)
    myheap.insert(4)
    myheap.insert(2)
    myheap.insert(19)
    # myheap.data = [None, 30, 24, 12, 18, 21, 8, 6, 4, 2, 19]
    # myheap.insert(35)
    # myheap.insert(22)

    # print(myheap.data)

    myheap.remove()
    print(myheap.data)

solution()