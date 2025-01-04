from tut_dsa.tut_tree.TreeClass import TreeNode
from tut_dsa.tut_tree.BinaryTree import printing_tree_recursive


class BST:
    def __init__(self):
        self.root = None
        self.numNode = 0

    def get_replace_ele(self, root):
        if root is None:
            return 10000
        if root.left is None:
            return root.data
        return self.get_replace_ele(root.left)

    def insertHelper(self, root, data):
        if root == None:
            node = TreeNode(data)
            return node
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):
        self.root = self.insertHelper(self.root, data)

    def deleteHelper(self, root, data):
        if root == None:
            return False, None
        if root.data > data:
            left_deleted, left_rew_node = self.deleteHelper(root.left, data)
            root.left = left_rew_node
            return left_deleted, root
        if root.data < data:
            right_deleted, right_new_node = self.deleteHelper(root.right, data)
            root.right = right_new_node
            return right_deleted, root
        if root.data == data and root.left is None and root.right is None:
            return True, None
        if root.data == data and root.left is None:
            return True, root.right
        if root.data == data and root.right is None:
            return True, root.left
        if root.data == data and root.left is not None and root.right is not None:
            replacement = self.get_replace_ele(root.right)
            root.data = replacement
            # print(f"replacement ele is : {replacement}")
            deleted, new_right_node = self.deleteHelper(root.right, replacement)
            root.right=new_right_node
            return True,root

    def delete(self, data):
        deleted, new_root = self.deleteHelper(self.root, data)
        if deleted == True:
            self.numNode -= 1
        self.root = new_root
        return deleted


if __name__ == '__main__':
    print("Hello, BinarySearchTree....")
    obj = BST()
    obj.insert(2)
    obj.insert(4)
    obj.insert(1)
    obj.insert(3)
    obj.insert(14)
    obj.insert(12)
    obj.insert(11)
    obj.insert(0)
    printing_tree_recursive(obj.root)
    obj.delete(4)
    print("_______________")
    printing_tree_recursive(obj.root)
    obj.delete(0)
    print("_______________")
    printing_tree_recursive(obj.root)
    obj.delete(2)
    print("_______________")
    printing_tree_recursive(obj.root)


