emp_details = (
(&quot;EmpID&quot;, input(&quot;Enter Employee ID: &quot;)),
(&quot;EmpName&quot;, input(&quot;Enter Employee Name: &quot;)),
(&quot;EmpAge&quot;, int(input(&quot;Enter Employee Age: &quot;))),
(&quot;EmpCity&quot;, input(&quot;Enter Employee City: &quot;))
)

dict1 = dict(emp_details)

print(&quot;\nDictionary is :&quot;, dict1)

print(&quot;\nEmployee Name is :&quot;, dict1[&quot;EmpName&quot;])
print(&quot;\nEmployee City is :&quot;, dict1[&quot;EmpCity&quot;])

print(&quot;\nAll Keys in Dictionary&quot;)
for x in dict1:
print(x)

print(&quot;\nAll Values in Dictionary&quot;)
for x in dict1:
print(dict1[x])

dict1[&quot;Phno&quot;] = int(input(&quot;\nEnter Phone Number: &quot;))
print(&quot;\nUpdated Dictionary is :&quot;, dict1)

dict1[&quot;EmpName&quot;] = input(&quot;\nEnter New Employee Name: &quot;)
print(&quot;\nUpdated Dictionary is :&quot;, dict1)

dict1.pop(&quot;EmpAge&quot;)
print(&quot;\nUpdated Dictionary is :&quot;, dict1)
print(&quot;Length of Dictionary is :&quot;, len(dict1))

dict2 = dict1.copy()
print(&quot;\nNew Dictionary is :&quot;, dict2)

dict1.clear()
print(&quot;\nUpdated Dictionary is :&quot;, dict1)
