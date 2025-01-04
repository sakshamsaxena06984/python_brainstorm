from tut_dsa.tut_tree.TreeClass import TreeNode
import queue


def printing_tree_recursive(root):
    if root is None:
        return
    print(root.data, end=' : ')
    if root.left is not None:
        print(f"L-> {root.left.data} ", end=',')
    if root.right is not None:
        print(f"R-> {root.right.data}", end=' ')
    print()
    printing_tree_recursive(root.left)
    printing_tree_recursive(root.right)


def input_level_wise():
    root_data = int(input("Enter the root node value"))
    if root_data == -1:
        return None
    q = queue.Queue()
    root = TreeNode(root_data)
    q.put(root)
    while not (q.empty()):
        curr = q.get()
        print(f"Enter the left child value of {curr.data}")
        curr_left_data = int(input())
        if curr_left_data != -1:
            curr_left_root = TreeNode(curr_left_data)
            curr.left = curr_left_root
            q.put(curr_left_root)
        print(f"Enter the right child value of {curr.data}")
        curr_right_data = int(input())
        if curr_right_data != -1:
            curr_right_root = TreeNode(curr_right_data)
            curr.right = curr_right_root
            q.put(curr_right_root)
    return root


def maxVal(root):
    if root == None:
        return -100000
    left_max = maxVal(root.left)
    right_max = maxVal(root.right)
    return max(root.data, left_max, right_max)


def minVal(root):
    if root == None:
        return 1000000
    left_min = minVal(root.left)
    right_min = minVal(root.right)
    return min(root.data, left_min, right_min)


def isBST(root):
    if root is None:
        return True
    left_max = maxVal(root.left)
    right_min = minVal(root.right)
    if left_max > root.data or right_min < root.data:
        return False
    isLeftBST = isBST(root.left)
    isRightBST = isBST(root.right)
    return isLeftBST and isRightBST


def isBST1(root):
    if root is None:
        return 1000, -1000, True
    leftmin, leftmax, leftbst = isBST1(root.left)
    rightmin, rightmax, rightbst = isBST1(root.right)
    isbstans = True
    if leftmax >= root.data or rightmin < root.data:
        isbstans = False
    if leftbst == False or rightbst == False:
        isbstans = False
    minimum = min(leftmin, rightmin, root.data)
    maximum = max(rightmax, leftmax, root.data)
    return minimum, maximum, isbstans


def isBST2(root, min_r, max_r):
    if root == None:
        return True
    if root.data < min_r or root.data > max_r:
        return False
    is_left_bst = isBST2(root.left, min_r, root.data - 1)
    is_right_bst = isBST2(root.right, root.data, max_r)
    return is_left_bst and is_right_bst


if __name__ == '__main__':
    root = TreeNode(1)
    root_left = TreeNode(2)
    root_right = TreeNode(3)
    root.left = root_left
    root.right = root_right

    print("printing the tree structure.....")
    printing_tree_recursive(root)
    root = input_level_wise()
    print("printing the tree structure.....")
    printing_tree_recursive(root)

    # 1 2 3 6 7 9 -1 -1 -1 -1 -1 -1 -1
    print(f"is my tree BST : {isBST(root)}")
    print(f"is my tree BST : {isBST1(root)}")
    print(f"is my tree BST : {isBST2(root,-1000,1000)}")
