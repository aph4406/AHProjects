"""
Stack interface.
file: cs_stack.py
author: CS @ rit.edu
This is the Stack data structure implemented by linked node sequences.

The Stack datatype constructor makes a growable stack of nodes.

"""

from node_types import FrozenNode as Node
from typing import Any, Union

class CSStack:
    size: int
    top: Union[None, Node]
    
    def __init__(self):
        """
        Initializes size to 0 and the top to None
        """
        self.size = 0
        self.top = None


    def push(self, element:Any):
        """
        Add an element to the top of the stack. The stack state changes.
        """
        self.top = Node(element, self.top)
        self.size = self.size + 1

        
    def peek(self)->Any:
        """
        Return top element on stack.  Does not change stack.
        precondition: stack is not empty
        """
        if self.is_empty():
            raise IndexError("top of empty stack") 
        return self.top.value

    def pop(self)->Any:
        """
        Remove the top element in the stack and returns the removed value. 
        The stack state changes.
        precondition: stack is not empty
        """
        if self.is_empty():
            raise IndexError("pop on empty stack") 
        popped = self.top.value
        self.top = self.top.next
        self.size = self.size - 1
        return popped
    
    def is_empty(self)->bool:
        """
        Is the stack empty?
        """
        return self.top is None

    def __str__(self)->str:
        result = "CSStack: [  "
        next = self.top
        while next != None:
            result += str(next.value) + ", "
            next = next.next
        result = result[:-2] + " ]"
        return result
    


