name = input(&quot;Enter Student Name: &quot;)
regno = input(&quot;Enter Register Number: &quot;)

n = int(input(&quot;Enter number of subjects: &quot;))

total = 0
result = &quot;Pass&quot;

for i in range(1, n + 1):
mark = int(input(f&quot;Enter mark for subject {i}: &quot;))

if mark &lt; 35:
result = &quot;Fail&quot;

total += mark
average = total / n

if result == &quot;Fail&quot;:
grade = &quot;No Grade&quot;
elif average &gt;= 90:
grade = &quot;A&quot;
elif average &gt;= 75:
grade = &quot;B&quot;
elif average &gt;= 60:
grade = &quot;C&quot;
else:
grade = &quot;D&quot;
print(&quot;\n------ STUDENT MARK STATEMENT ------&quot;)
print(&quot;Name :&quot;, name)
print(&quot;Register No :&quot;, regno)
print(&quot;Total Marks :&quot;, total)
print(&quot;Average :&quot;, average)
print(&quot;Result :&quot;, result)
print(&quot;Grade :&quot;, grade)
