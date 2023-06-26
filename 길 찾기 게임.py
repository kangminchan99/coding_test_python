# 트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다
# main 쪽에서 solution불러주는 곳에서 재귀호출이 1000을 넘어갈 수 밖에없다.
# 그 이유는 파이썬의 재귀 호출 재약이 1000이기 때문이다.

# 재귀 호출제약 늘리기
import sys

# 노드의 정보를 담기위한 클래스 정의
class Node:
    def __init__(self, id, x, y):
        # 받은 파라미터 초기화
        self.id = id
        self.x = x
        self.y = y
        # 루트의 왼쪽과 오른쪽을 비어있는 상태로 초기화
        self.left = None
        self.right = None
    
    # __lt__ - "<" 연산자의 동작을 정의 (작은건 앞에 큰건 뒤에)
    def __lt__(self, other):
        if (self.y == other.y):
            # y값이 같을 때는 x값이 작은게 앞으로 와야한다.
            return self.x < other.x
        # y값이 제일 큰게 루트 이므로 아래와 같이 정의
        return self.y > other.y
    

def addNode(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            addNode(parent.left, child)
    
    else:
        if parent.right is None:
            parent.right = child
        else:
            addNode(parent.right, child)
# preorder - root, left, right 순
def preorder(ans, node):
    # 노드가 none이면 재귀 호출을 끝냄
    if node is None:
        return
    ans.append(node.id)
    preorder(ans, node.left)
    preorder(ans, node.right)
# postorder - left, right, root 순
def postorder(ans, node):

    if node is None:
        return
    postorder(ans, node.left)
    postorder(ans, node.right)
    ans.append(node.id)
    
def solution(nodeinfo):
    # 재귀 호출 제약 늘리기
    sys.setrecursionlimit(1500)
    size = len(nodeinfo)
    nodelist = []
    for i in range(size):
        # nodeinfo[i] 는 i + 1번(id), [x축 좌표, y축 좌표] 순.
        nodelist.append(Node(i+1, nodeinfo[i][0], nodeinfo[i][1]))
        
    # 위의 클래스에서 정렬해 놓은 데로 정렬이 되어있음. 
    nodelist.sort()
    # nodelist[0]이 y값이 가장 큰 것이므로 루트 노드임.
    root = nodelist[0]
    # root를 제외한 1번 부터 끝까지 진행을 하면서 root에 더해준다.
    for i in range(1, size):
        addNode(root, nodelist[i])
        

    # 0 - 전위순회, 1 - 후위 순회
    answer = [[], []]
    preorder(answer[0], root)
    postorder(answer[1], root)
    return answer