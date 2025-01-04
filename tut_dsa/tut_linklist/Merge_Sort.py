from tut_dsa.tut_linklist.SinglyLinklist import create_link_list, print_link_list


def merge_lin(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    real_head = None
    if head1.data < head2.data:
        real_head = head1
        real_head.next = merge_lin(head1.next, head2)
    else:
        real_head = head2
        real_head.next = merge_lin(head1, head2.next)

    return real_head


def get_mid(head):
    slow = head
    speed = head
    while speed.next is not None and speed.next.next is not None:
        slow = slow.next
        speed = speed.next.next
    return slow


def merge_sort(head):
    if head is None or head.next is None:
        return head
    mid = get_mid(head)
    head2 = mid.next
    mid.next = None
    left_part = merge_sort(head)
    right_part = merge_sort(head2)
    return merge_lin(left_part, right_part)


if __name__ == '__main__':
    print("Hello, MergeSort of linkList")
    head = create_link_list()
    print_link_list(head)
    print("applying merge sort")
    head = merge_sort(head)
    print(head)
    print_link_list(head)
