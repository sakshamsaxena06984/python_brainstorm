class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def print_generic_tree(root):
    if root is None:
        return
    print(f"root -> {root.data} : ", end=' ')
    for ele in root.children:
        print(ele.data, end=' , ')
    print()
    for ele in root.children:
        print_generic_tree(ele)


def takeInput():
    root_data = int(input("Enter the root value"))
    if root_data == -1:
        return
    root = GenericTreeNode(root_data)
    child_num = int(input(f"Enter the number of children {root.data}"))
    for ele in range(child_num):
        print(f"enter the {ele+1}'th value of {root.data}")
        child_data = takeInput()
        root.children.append(child_data)
    return root

if __name__=='__main__':
    root=takeInput()
    print_generic_tree(root)
