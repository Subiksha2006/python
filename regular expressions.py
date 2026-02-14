import re
phone = input(&quot;Enter your phone number (format XXX-XXX-XXXX): &quot;)
phone_pattern = r&quot;^\d{3}-\d{3}-\d{4}$&quot;
if re.match(phone_pattern, phone):
print(&quot;Phone number is valid!&quot;)
else:
print(&quot;Invalid phone number format!&quot;)
password = input(&quot;Enter your password: &quot;)
password_pattern = r&quot;^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$&quot;
if re.match(password_pattern, password):
print(&quot;Strong password!&quot;)
else:
print(&quot;Weak password! Make sure it has at least 8 characters, including:&quot;)
print(&quot; - 1 uppercase letter&quot;)
print(&quot; - 1 lowercase letter&quot;)
print(&quot; - 1 digit&quot;)
