import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Sample data
data = [12, 15, 14, 10, 18, 20, 22, 15, 17, 19, 16, 14, 13, 15, 18]
# ----- Scatter Plot -----
plt.figure(figsize=(10, 4))
plt.scatter(range(len(data)), data, color=&#39;blue&#39;, marker=&#39;o&#39;)
plt.title(&#39;Scatter Plot of Data&#39;)
plt.xlabel(&#39;Index&#39;)
plt.ylabel(&#39;Value&#39;)
plt.grid(True)
plt.show()
# ----- Heat Map -----
# Convert data into 2D array for heatmap (5x3 example)
heat_data = np.array(data[:15]).reshape(5, 3)
plt.figure(figsize=(6, 5))
sns.heatmap(heat_data, annot=True, cmap=&#39;coolwarm&#39;)
plt.title(&#39;Heat Map of Data&#39;)
plt.show()
