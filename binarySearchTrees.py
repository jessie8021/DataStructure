'''
이진 탐색 트리
 - 모든 노드에 대해서,
    • 왼쪽 서브 트리에 있는 데이터는 모두 현재 노드의 값보다 작고
    • 오른쪽 서브 트리에 있는 데이터는 모두 현재 노드의 값보다 큰
   성질을 만족하는 이진 트리
 - 중복되는 데이터 원소는 없는 것으로 가정
 - (정렬된) 배열을 이용한 이진 탐색과 비교

            [2, 3, 5, 6, 9, 11, 15]         (장점) 데이터 원소의 추가, 삭제가 용이
                    ↑     ↑      ↑          (단점) 공간 소요가 큼큼
                lower  middle  upper


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
            raise KeyError('Key %s already exists.' % key)

    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()

        return traversal

    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)

    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None

    def remove(self, key):
        node, parent = self.lookup(key)

        if node:
            nChildren = node.countChildren()

            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None으로 하여
                # leaf node였던자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if node == parent.left:
                        parent.left = None
                    if node == parent.right:
                        parent.right = None
                # 만약 parent가 없으면 (node는 root인 경우)
                # self.root를 None으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    children = node.left
                else:
                    children = node.right
                # 만약 parent가 있으면
                # node가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node의 자리에 넣습니다.
                if parent:
                    if node == parent.left:
                        parent.left = children
                    if node == parent.right:
                        parent.right = children
                # 만약 parent가 없으면(node는 root인 경우)
                # self.root에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = children
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node를 가리키고 있고,
                # successor는 node의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽자식의 링크를 반복하여 따라감으로써,
                # 순환문이 종료할 때 successor는 바로 다음 키를 가진 노드를,
                # parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left

                # 삭제하려는 노드인 node에 successor의 key 와 data를 대입합니다.
                node.key = successor.key
                node.data = successor.data

                # successor가 parent의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에땨라 parent.left 또는 parent.right를
                # successor가 가지고 있던(없을 수도 있지만) 자식을 가리키도록 합니다.

                if parent.left == successor:
                    if successor.right:
                        parent.left = successor.right
                    if successor.right is None:
                        parent.left = None

                elif parent.right == successor:
                    if successor.right:
                        parent.right = successor.right
                    if successor.right is None:
                        parent.right = None

            return True
        else:
            return False


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
    bt.insert(6, 'Anne')
    bt.insert(10, 'clara')
    bt.insert(7, 'ted')
    bt.insert(9, 'A')
    bt.insert(11, 'B')



    for i in bt.inorder():
        print(i.key, ' : ', i.data)

    # node, parent = bt.lookup(7)
    # print(node.key, ', ', parent.key)


    bt.remove(8)

    for i in bt.inorder():
        print(i.key, ' : ', i.data)
    # print(bt.root.key)

solution()