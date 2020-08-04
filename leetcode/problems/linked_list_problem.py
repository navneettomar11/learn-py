from typing import List

class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'Val '+str(self.val)+' Next --> '+str(self.next)


def create_linked_list(nums: List[int]) -> ListNode:
    node: ListNode = None
    head: ListNode = None
    for num in nums:
        if head is None:
            head = ListNode(num)
            node = head
        else:
            node.next = ListNode(num)
            node = node.next

    return  head


"""
 Reverse List - Leetcode 206
"""
def reverse_list(head: ListNode) -> ListNode:

    def helper(node: ListNode, prev: ListNode) -> ListNode:
        #print(node,'----------------', prev)
        if node is None:
            return prev

        next = node.next
        node.next = prev
        prev = node
        node = next
        return helper(node, prev)

    return helper(head, None)

"""
 Plaindrome Linked List - Leetcode 234
 
"""
def is_plaindrome(head: ListNode) -> bool:
    if head is None:
        return  False

    values = [ ]
    node = head
    while node is not None:
        values.append(node.val)
        node = node.next

    return values == values[::-1]

def remove_elements(head: ListNode, val: int) -> ListNode:
    if head is None:
        return  None

    prev = None
    curr = head
    while curr is not None:
        if curr.val == val and curr == head:
            head = curr.next
            prev = head
        elif curr.val == val:
            prev.next = curr.next
        else: prev = curr
        curr = curr.next
    return head

"""
Leetcode 1290. Convert Binary Number in a Linked List to Integer
"""
def get_decimal_value(head: ListNode) -> int:
    temp = head
    res = 0
    size = 0
    while temp is not None: 
        size+=1
        temp = temp.next
    
    n = size-1
    temp = head
    while temp is not None:
        res = res | temp.val << n
        n-=1
        temp = temp.next

    return res


if __name__ == "__main__":

    #head = create_linked_list([1,2,3,4,5])
    #print(reverse_list(head))
    #head = create_linked_list([1,2,2,1])
    #print(is_plaindrome(head))
    """
    head = create_linked_list([1,2,6,3,4,5,6])
    head = remove_elements(head, 6)
    print(head)
    head = create_linked_list([1])
    head = remove_elements(head, 1)
    print(head)
    head = create_linked_list([1,2,2,1])
    head = remove_elements(head, 2)
    print(head)
    """
    head = create_linked_list([1,0,1])
    print(get_decimal_value(head))
    head = create_linked_list([1,1,1,1,1])
    print(get_decimal_value(head))
