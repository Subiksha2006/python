stack = []
print(&quot;--- Stack ---&quot;)
stack.append(10)
stack.append(20)
stack.append(30)
print(&quot;Stack:&quot;, stack)
print(&quot;Peek:&quot;, stack[-1])
stack.pop()
print(&quot;After Pop:&quot;, stack)
queue = []

print(&quot;\n--- Queue ---&quot;)
queue.append(10)
queue.append(20)
queue.append(30)
print(&quot;Queue:&quot;, queue)
queue.pop(0)
print(&quot;After Dequeue:&quot;, queue)
