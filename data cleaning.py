pip install pandas
pip install numpy
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
# Create DataFrame
df = pd.DataFrame({
&#39;Date&#39;: [&#39;2023-01-01&#39;, &#39;02-01-2023&#39;, &#39;Invalid&#39;],
&#39;Category&#39;: [&#39;Apple&#39;, &#39;apple&#39;, &#39;Banana&#39;],
&#39;Value&#39;: [10, 1500, 20],
&#39;Missing&#39;: [1, np.nan, 3]
})
print(&quot;Original Data:\n&quot;, df)
# Remove duplicate rows
df.drop_duplicates(inplace=True)
# Fill missing values with mean
df[&#39;Missing&#39;] = df[&#39;Missing&#39;].fillna(df[&#39;Missing&#39;].mean())
# Convert &#39;Date&#39; column to datetime, coerce errors to NaT
df[&#39;Date&#39;] = pd.to_datetime(df[&#39;Date&#39;], errors=&#39;coerce&#39;)
# Forward fill missing dates
df[&#39;Date&#39;] = df[&#39;Date&#39;].ffill()
# Standardize &#39;Category&#39; text to lowercase
df[&#39;Category&#39;] = df[&#39;Category&#39;].str.lower()
# Clip &#39;Value&#39; column to a maximum of 100
df[&#39;Value&#39;] = df[&#39;Value&#39;].clip(upper=100)
# Normalize &#39;Value&#39; column using MinMaxScaler
scaler = MinMaxScaler()

df[&#39;Value_norm&#39;] = scaler.fit_transform(df[[&#39;Value&#39;]])
print(&quot;\nCleaned Data:\n&quot;, df)
