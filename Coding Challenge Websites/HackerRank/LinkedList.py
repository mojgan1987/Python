# Delete a node
def deleteNode(head, position):
    
    if head.next == None:
        return None
    
    if position == 0:
        return head.next
    
    node = head
    for i in range(position-1):
        node = node.next
        
    node.next = node.next.next
    return head


# Reverse
def reverse(head):
    if head == None:
        return head        

    prev = None
    current = head
    
    while current != None:
        # print(current.data)
        # print(f'prev={prev.data}')
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

  
# Recursive reverse
def reverse(head):
#     print(head.data)
    if head == None:
        return head
    if head.next == None:
        return head
    
    curr_head = reverse(head.next)
    
    head.next.next = head
    head.next = None

    return curr_head

# Insert
def insertNodeAtPosition(head, data, position):
    node = head
    if position == 0:
        newNode = SinglyLinkedListNode(data)
        newNode.next = head
        return newNode
    count = 1
    while count < position and node:
        count += 1
        node = node.next
    newNode = SinglyLinkedListNode(data)
    newNode.next = node.next
    node.next = newNode
    return head
