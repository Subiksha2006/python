def strlen(str):
counter = 0

while str[counter:]:
counter += 1
return counter
def strrev(str):
rstr = &quot; &quot;
l = strlen(str)
while l&gt;0:
rstr = rstr + str[l-1]
l=l-1
return rstr
def strcat(st1,st2):
return(st1 + st2)
def strcmp(st1,st2):
if(st1 == st2):
print(st1+&quot;and&quot;+st2+&quot;are same&quot;)
elif(st1&gt;st2):
print (st1 + &quot; comes after&quot; + st2 + &quot; in the Dictionary&quot;)
else:
print(st1 + &quot; comes before&quot; + st2 + &quot; in the Dictionary&quot;)
print(&quot;String Functions:\n 1.String Length \n 2.String Reverse \n 3.String Concatenation
\n 4.Sring Comparison \n 5.Exit \n&quot;)
while(1):
n=int(input(&quot;Enter your choice:&quot;))
if (n==1):
str=input(&quot;Enter a string:&quot;)
print(&quot;Length of the string is:&quot;,strlen(str))
elif (n==2):
str=input(&quot;Enter a string:&quot;)
print(&quot;Reversed string is:&quot;,strrev(str))
elif (n==3):
st1=input(&quot;Enter the first string:&quot;)
st2=input(&quot;Enter the second string:&quot;)
print(&quot;Concatenated string is:&quot;,strcat(st1,st2))
elif (n==4):
str1=input(&quot;Enter the first string:&quot;)
str2=input(&quot;Enter the second string:&quot;)
strcmp(str1,str2)
elif (n==5):

print(&quot;Exited&quot;)
break
else:
print(&quot;Invalid choice&quot;)
