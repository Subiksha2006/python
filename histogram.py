import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Sample data
data = [12, 15, 14, 10, 18, 20, 22, 15, 17, 19, 16, 14, 13, 15, 18]
# ----- Line Plot -----
plt.figure(figsize=(10, 4))
plt.plot(data, marker=&#39;o&#39;, linestyle=&#39;-&#39;, color=&#39;b&#39;)
plt.title(&#39;Line Plot of Data&#39;)
plt.xlabel(&#39;Index&#39;)
plt.ylabel(&#39;Value&#39;)
plt.grid(True)
plt.show()
# ----- Box Plot -----
plt.figure(figsize=(6, 4))
sns.boxplot(data=data, color=&#39;lightgreen&#39;)
plt.title(&#39;Box Plot of Data&#39;)
plt.show()
# ----- Histogram -----
plt.figure(figsize=(8, 4))
plt.hist(data, bins=5, color=&#39;orange&#39;, edgecolor=&#39;black&#39;)
plt.title(&#39;Histogram of Data&#39;)
plt.xlabel(&#39;Value Range&#39;)
plt.ylabel(&#39;Frequency&#39;)
plt.show()
