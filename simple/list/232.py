# coding=utf-8
# 从现在开始使用Python3做题，题号小于232的都是Python2下做的，题号大于等于232的将使用Python3


'''
    使用栈实现队列的下列操作：
    
    push(x) -- 将一个元素放入队列的尾部。
    pop() -- 从队列首部移除元素。
    peek() -- 返回队列首部的元素。
    empty() -- 返回队列是否为空。
    示例:
    
    MyQueue queue = new MyQueue();
    
    queue.push(1);
    queue.push(2);  
    queue.peek();  // 返回 1
    queue.pop();   // 返回 1
    queue.empty(); // 返回 false
    说明:
    
    你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
    你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
    假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


#  使用数组实现， pop的时候要最数组进行移动操作，比较耗费时间，可以使用循环链表
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.length = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.stack.append(x)
        self.length += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.length > 0:
            self.length -= 1
            return self.stack.pop(0)
        return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.length > 0:
            return self.stack[0]
        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length == 0


class MyQueue1:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.instack = []
        self.outstack = []
        self.length = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.stack.append(x)
        self.length += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.length > 0:
            self.length -= 1
            return self.stack.pop(0)
        return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.length > 0:
            return self.stack[0]
        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.length == 0


# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    queue = MyQueue()

    obj = MyQueue()
    obj.push(3)
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)
