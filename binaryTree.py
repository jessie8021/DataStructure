'''
Tree (Tree)
 - Root Node 에서 간선(edge) 들이 마치 나무에서 뿌리로 부터 잔가지로 뻗어 나가듯이 가지치기 된 구조.
 - 도식화

                          [A]                               ⇢ root node, level 0,  degree of A -  2

                    ↙               ↘                       ⇢ edges

            [B]                         [C]                 ⇢ internal nodes, level1, degree of B - 1, degree of C - 2

             ↓                        ↙     ↘

            [D]                     [E]     [F]             ⇢ internal nodes, level2, degree of D - 3, degree of F - 1

      ↙      ↓      ↘                        ↓

    [G]     [H]     [J]                     [K]             ⇢ leaf nodes, level3

 - parent node 와 child node

            [D]                    parent node

      ↙      ↓      ↘

    [G]     [H]     [J]             child node

 - node degree : child tree 의 개수
 - 높이 (Height, depth) : 최대수준(level) + 1
 - subtree : B 를 root node 로 하는 5개의 노드로 이루어진 서브트리


             [B]

             ↓

            [D]

      ↙      ↓      ↘

    [G]     [H]     [J]


이진트리 (Binary Trees)
 - 트리에 포함되는 모든 노드의 차수가 2 이하인 트리.
  즉, 모든 노드의 자식이 없거나(리프노드의 경우), 하나만 있거나, 아니면 둘 있는 경우
 - 이진 트리의 추상적 자료구조 - 연산의 정의
     • size() - 현재 트리에 포함되어 있는 노드의 수를 구함
     • depth() - 현재 트리의 깊이(또는 높이:height) 를 구함
     • 깊이 우선 순회 (depth first traversal)
        1) 중위순회 (In-order Traversal)
          순회의 순서 - (1) Left subtree (2) 자기자신 (3) Right subtree

                        5 [A]

                    ↙               ↘

              3 [B]               8 [C]

              ↙     ↘             ↙     ↘

          2 [D]   4 [E]       6 [F]   9 [G]

           ↙                       ↘

      1 [H]                       7 [J]

        2) 후위순회 (Post-order Traversal)
          순회의 순서 - (1) Left subtree (2) Right subtree (3) 자기자신

                        9 [A]

                    ↙               ↘

              4 [B]               8 [C]

              ↙     ↘             ↙     ↘

          2 [D]   3 [E]      6  [F]   7 [G]

           ↙                       ↘

       1 [H]                       5 [J]

        3) 전위순회 (Pre-order Traversal)
           순회의 순서 - (1) 자기자신 (2) Left subtree (3) Right subtree

                        1 [A]

                    ↙               ↘

              2 [B]              6  [C]

              ↙     ↘             ↙     ↘

          3 [D]   5 [E]       7 [F]   9 [G]

           ↙                       ↘

      4 [H]                       8 [J]


     • 넓이 우선 순회(breadth first traversal)
        - 수준(level)이 낮은 노드를 우선으로 방문
        - 같은 수준의 노드들 사이에는,
            1) 부모노드의 방문 순서에 따라 방문
            2) 왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문

                          [A]                    ➤➤➤➤➤   level0

                    ↙               ↘

                [B]                 [C]           ➤➤➤➤➤ level1

              ↙     ↘             ↙     ↘

            [D]     [E]         [F]     [G]        ➤➤➤➤➤ level2

           ↙                       ↘

        [H]                         [J]              ➤➤➤➤➤ level3

        - 순회결과 : A - B - C - D - E - F - G - H - J
        - 넓이 우선 순회 알고리즘 구현
            1) (초기화) traversal <- 빈리스트, q <- 빈 큐
            2) 빈 트리가 아니면, root node를 q에 추가 (enqueue)
            3) q가 비어 있지 않은 동안
                3.1) node <- q에서 원소를 추출(dequeue)
                3.2) node를 방문
                3.3) node의 왼쪽, 오른쪽 자식(있으면) 들을 q에 추가
            4) q가 빈 큐가 되면 모든 노드 방문 완료


'''

'''
이미 주어진 코드 (class Node 와 class BinaryTree 에 의하여) 의 구조를 따르는 이진 트리 (binary tree) 에 대하여, 
트리의 깊이 (depth) 를 구하는 연산의 구현을 완성하세요.

초기 코드에 pass 로만 되어 있는 class Node 의 depth() 메서드와 class BinaryTree 의 depth() 메서드를 구현합니다. 
코드의 다른 부분은 수정할 필요가 없습니다.

참고로 할 수 있도록, 강의에서 소개한 size() 메서드들 (class Node 와 class BinaryTree 에 대해서) 을 그대로 두었습니다. 
문제로 주어진 depth() 연산도 매우 비슷한 식으로 구현할 수 있으니 참고로 삼으세요.

[참고] 실행 을 눌렀을 때 통과하는 것은 아무 의미 없습니다.
또한, solution() 함수는 테스트에 영향을 미치므로 수정하지 말고 그대로 두세요.
'''
'''
이미 주어진 코드 (class Node 와 class BinaryTree 에 의하여) 의 구조를 따르는 
이진 트리 (binary tree) 에 대하여, 트리를 전위 순회 (preorder traversal) 하는 연산의 구현을 완성하세요.
초기 코드에 pass 로만 되어 있는 class Node 의 preorder() 메서드와 class BinaryTree 의 preorder() 메서드를 구현합니다. 
코드의 다른 부분은 수정할 필요가 없습니다.
'''
class ArrayQueue:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]

class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        # print(self.data)
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0

        # print('l : ', l, ', r : ', r)
        return l + r + 1

    def depth(self):
        # print(self.data)
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0

        # print('l : ', l, ', r : ', r)
        return  l + 1 if l >= r else r + 1

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:
    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

    def bft(self):
        traversal = []
        q = ArrayQueue()

        if self.root:
            q.enqueue(self.root)

        while not q.isEmpty():
            node = q.dequeue()
            traversal.append(node.data)

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return traversal

def solution():
    node1 = Node('B')
    node2 = Node('D')
    node3 = Node('E')
    node4 = Node('H')

    node1.left = node2
    node1.right = node3
    node2.left = node4

    bt = BinaryTree(node1)

    print(bt.bft())

solution()

