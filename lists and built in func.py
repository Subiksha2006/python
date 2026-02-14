nums = [10, 20, 30, 40, 50]
print(&quot;Original:&quot;, nums)

nums.append(60)
nums.insert(1, 15)
nums.remove(30)

nums.pop()
print(&quot;Modified:&quot;, nums)

nums.sort()
print(&quot;Sorted:&quot;, nums)

nums.reverse()
print(&quot;Reversed:&quot;, nums)

print(&quot;Length:&quot;, len(nums))
print(&quot;Max:&quot;, max(nums))
print(&quot;Min:&quot;, min(nums))
print(&quot;Sum:&quot;, sum(nums))

new_list = nums.copy()

print(&quot;Copied List:&quot;, new_list)

nums.clear()
print(&quot;Cleared List:&quot;, nums)
