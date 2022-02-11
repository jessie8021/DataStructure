'''
이진 탐색 트리
 - 모드 노드에 대해서,
    • 왼쪽 서브 트리에 있는 데이터는 모두 현재 노드의 값보다 작고
    • 오른쪽 서브 트리에 있는 데이터는 모두 현재 노드의 값보다 큰
   성질을 만족하는 이진 트리
 - 중복되는 데이터 원소는 없는 것으로 가정
 - (정렬된) 배열을 이용한 이진 탐색과 비교

            [2, 3, 5, 6, 9, 11, 15]         (장점) 데이터 원소의 추가, 삭제가 용이
                    ↑     ↑      ↑          (단점) 공간 소요가 큼큼                  lower   ⎮     upper
                        middle


                          [5]

                    ↙               ↘

               [2]                 [8]

              ↙     ↘             ↙     ↘

            [1]     [4]         [6]     [9]

                                   ↘

                                    7 [7]

 - 이진 탐색 트리의 추상적 자료구조
    • 데이터 표현 - 각 노드는 (key, value) 의 쌍으로
    • 키를 이용해서 검색가능. 보다 복작한 데이터 레코드로 확장가능

                          [5] john

                    ↙               ↘

            David [2]               [8] Mary

              ↙     ↘             ↙     ↘

    Patrick [1]  Sue [4]   Anne [6]      [9] Clara

                                   ↘

                                 Ted [7]

 - 연산의 정의
    • insert(key, data) - 트리에 주어진 데이터 원소를 추가
    • remove(key) - 특정 원소를 트리로부터 삭제
    • lookup(key) - 특정 원소를 검색
    • inorder() - 키읭 순서대로 데이터 원소를 나열
    • min(), max() - 최소 키, 최대 키를 가지는 원소를 각각 탐색

'''

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key Error')


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()

        return traversal

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

def solution():
    bt = BinarySearchTree()
    bt.insert(5, 'john')
    bt.insert(2, 'David')
    bt.insert(8, 'Mary')
    bt.insert(1, 'Patric')
    bt.insert(4, 'Sue')


solution()