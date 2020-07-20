class Node:
    def __init__(self, val, prev = None, next = None, child = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def flatten(node: 'Node') -> 'Node':
    if not head:
        return None

    tmp1 = tmp2 = None

    if head.child:
        tmp1 = flatten(head.child)
        head.child = None
    if head.next:
        tmp2 = flatten(head.next)

    if tmp1:
        head.next = tmp1
        head.next.prev = head

        cur = tmp1
        while cur.next:
            cur = cur.next

        if tmp2:
            cur.next = tmp2
            tmp2.prev = cur

    elif tmp2:
        head.next = tmp2
        head.next.prev = head

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.child = Node(7)
    head.next.next.child.next = Node(8)
    head.next.next.child.next.prev = head.next.next.child
    head.next.next.child.next.next = Node(9)
    head.next.next.child.next.next.prev = head.next.next.child.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next.next

    flatten(head)
