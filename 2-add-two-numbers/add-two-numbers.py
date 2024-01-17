# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2 
        
        list1 = self.node2list(node1)
        list2 = self.node2list(node2)
        
        list1.reverse()
        list2.reverse()
        
        num1 = int(''.join(str(a) for a in list1))
        num2 = int(''.join(str(a) for a in list2))
        result = list(str(num1+num2))
        result.reverse()
        
        return self.list2node(result) 
    
    def node2list(self, node1: ListNode) -> List: #linked list -> list
        list1 = []
        while node1 != None :
            list1.append(node1.val)
            node1 = node1.next
        return list1
    
    def list2node(self, list1: List) -> ListNode:
        result_node = ListNode()
        
        for i,num in enumerate(list1):
            if i == 0 :
                result_node.val = num
            else :
                node = result_node
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)
        return result_node
        