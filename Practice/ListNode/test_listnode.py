class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def create_linked_list(self, values) -> 'ListNode':
        # no values provided
        if not values:
            return None
        
        # Create the head of the linked list
        head = ListNode(values[0])
        current_node = head
        for value in values[1:]:
            current_node.next = ListNode(value)
            current_node = current_node.next

        return head
    
    def linked_list_to_list(self) -> list:
        values = []
        current_node = self
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next
        
        return values
    
    def __repr__(self):
        return "->".join(str(value) for value in self.linked_list_to_list())
    
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.linked_list_to_list() == other.linked_list_to_list()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.linked_list_to_list() < other.linked_list_to_list()
    
    def __le__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.linked_list_to_list() <= other.linked_list_to_list()
    
    def __gt__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.linked_list_to_list() > other.linked_list_to_list()
    
    def __ge__(self, other):
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.linked_list_to_list() >= other.linked_list_to_list()
    
    def __hash__(self):
        return hash(tuple(self.linked_list_to_list()))
    
def test_linked_list():
    # Create a linked list from a list of values
    values = [1, 2, 3, 4, 5]
    head = ListNode().create_linked_list(values)
    
    # Convert the linked list back to a list
    assert head.linked_list_to_list() == values
    
    # Test string representation
    assert repr(head) == "1->2->3->4->5"
    
    # Test equality
    another_head = ListNode().create_linked_list(values)
    assert head == another_head
    
    # Test inequality
    different_head = ListNode().create_linked_list([1, 2, 3])
    assert head != different_head
    
    # Test comparison
    smaller_head = ListNode().create_linked_list([1, 2])
    assert smaller_head < head
    assert head > smaller_head
    assert smaller_head <= head
    assert head >= smaller_head
    
    # Test hashing
    hash_set = {head, another_head}
    assert len(hash_set) == 1  # Both heads are equal, so only one unique hash
    hash_set.add(different_head)
    assert len(hash_set) == 2  # Now we have two unique hashes
if __name__ == "__main__":
    test_linked_list()  
    print("All tests passed.")