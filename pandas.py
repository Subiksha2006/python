import pandas as pd
from functools import reduce
data = {
&quot;Name&quot;: [&quot;Ravi&quot;, &quot;Anu&quot;, &quot;Kiran&quot;, &quot;Meena&quot;],
&quot;Age&quot;: [30, 22, 45, 19],
&quot;Income&quot;: [40000, 28000, 50000, 30000],
&quot;CreditScore&quot;: [720, 680, 750, 600],
&quot;LoanAmount&quot;: [300000, 200000, 400000, 150000]
}
df = pd.DataFrame(data)
eligible = df[
(df[&quot;Age&quot;] &gt;= 21) &amp;
(df[&quot;Income&quot;] &gt;= 25000) &amp;
(df[&quot;CreditScore&quot;] &gt;= 650) &amp;
(df[&quot;LoanAmount&quot;] &lt;= df[&quot;Income&quot;] * 10)
]
eligible[&quot;ProcessingFee&quot;] = list(
map(lambda x: x * 0.02, eligible[&quot;LoanAmount&quot;])
)
eligible[&quot;LoanStatus&quot;] = eligible.apply(
lambda row: &quot;Approved&quot;,
axis=1
)
total_loan = reduce(
lambda x, y: x + y,
eligible[&quot;LoanAmount&quot;]
)
print(&quot;Eligible Customers:\n&quot;)
print(eligible)
print(&quot;\nTotal Approved Loan Amount:&quot;, total_loan)
