from tut_dsa.tut_linklist.Node import Node


def create_link_list():
    li = input("Enter the element of link-list")
    dataSet = [int(ele) for ele in li.split(' ')]
    head = None
    tail = None
    for ele in dataSet:
        NewNode = Node(ele)
        if head == None:
            head = NewNode
            tail = NewNode
        else:
            tail.next = NewNode
            tail = tail.next

    return head


# calculating the length of the linkList
def length_link_list(head):
    ct = 0
    while head is not None:
        head = head.next
        ct = ct + 1
    return ct


# insertion of element the linklist
def insert_ele(head, p, ele):
    # base case
    if p > length_link_list(head):
        return head
    if p == 1:
        NewNode = Node(ele)
        NewNode.next = head
        return NewNode
    prev = None
    cur = head
    count = 1
    while count < p:
        prev = cur
        cur = cur.next
        count = count + 1
    NewNode = Node(ele)
    print(f"current element value is : {prev.data}")
    if cur.next is None:
        cur.next = NewNode
        return head

    prev.next = NewNode
    NewNode.next = cur
    return head


# printing the link list
def print_link_list(head):
    print("Printing the linkList")
    cur = head
    while cur is not None:
        print(cur.data)
        cur = cur.next


# deletion of element in the link-list
def deletion_link_list(head, p):
    if p > length_link_list(head):
        return head
    if p == 1:
        return head.next

    # p=p-1
    prev = None
    cur = head
    count = 1
    while count < p:
        prev = cur
        cur = cur.next
        count = count + 1
    if cur is None:
        prev.next = None
        return head
    prev.next = cur.next
    return head


if __name__ == '__main__':
    print("Hello Link-List")
    head = create_link_list()
    print_link_list(head)
    print(head)
    print(f"length of the linklist : " + str(length_link_list(head)))
    print("Insert the element in the link-list")
    # nhead = insert_ele(head, 1, 111)
    # print_link_list(nhead)
    dhead = deletion_link_list(head, 5)
    print_link_list(dhead)
