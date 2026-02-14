import pandas as pd
# Create Product DataFrame
products = {
&quot;ProductID&quot;: [1, 2, 3, 4, 5],
&quot;ProductName&quot;: [&quot;Rice&quot;, &quot;Milk&quot;, &quot;Bread&quot;, &quot;Oil&quot;, &quot;Sugar&quot;],
&quot;Category&quot;: [&quot;Grocery&quot;, &quot;Dairy&quot;, &quot;Bakery&quot;, &quot;Grocery&quot;, &quot;Grocery&quot;],
&quot;CostPrice&quot;: [40, 20, 25, 120, 35]
}
df_products = pd.DataFrame(products)
# Create Sales DataFrame
sales = {
&quot;ProductID&quot;: [1, 2, 3, 4, 5],
&quot;QuantitySold&quot;: [50, 120, 80, 40, 60],
&quot;SellingPrice&quot;: [55, 30, 40, 150, 50]
}
df_sales = pd.DataFrame(sales)
# Merge DataFrames
df = pd.merge(df_products, df_sales, on=&quot;ProductID&quot;)
# Inspection
print(&quot;\nDATA INFORMATION&quot;)
print(df.info())
print(&quot;\nSTATISTICAL SUMMARY&quot;)
print(df.describe())
# Revenue and Profit Calculation - merging example
df_sales_subset = pd.DataFrame({
&quot;ProductID&quot;: [1, 2, 3, 5],

&quot;QuantitySold&quot;: [50, 120, 80, 60],
&quot;SellingPrice&quot;: [55, 30, 40, 50]
})
df_merged = pd.merge(df_products, df_sales_subset, on=&quot;ProductID&quot;, how=&quot;inner&quot;)
print(&quot;\nMERGED DATAFRAME EXAMPLE&quot;)
print(df_merged)
# Profit and Revenue Calculations
df[&quot;Profit&quot;] = (df[&quot;SellingPrice&quot;] - df[&quot;CostPrice&quot;]) * df[&quot;QuantitySold&quot;]
df[&quot;Revenue&quot;] = df[&quot;SellingPrice&quot;] * df[&quot;QuantitySold&quot;]
# Sorting
print(&quot;\nSORTED BY PROFIT (DESCENDING)&quot;)
print(df.sort_values(by=&quot;Profit&quot;, ascending=False))
# Filtering
print(&quot;\nPRODUCTS WITH REVENUE GREATER THAN 4000&quot;)
print(df[df[&quot;Revenue&quot;] &gt; 4000])
print(&quot;\nGROCERY CATEGORY PRODUCTS&quot;)
print(df[df[&quot;Category&quot;] == &quot;Grocery&quot;])
# Grouping
print(&quot;\nCATEGORY WISE TOTAL REVENUE&quot;)
print(df.groupby(&quot;Category&quot;)[&quot;Revenue&quot;].sum())
print(&quot;\nCATEGORY WISE TOTAL PROFIT&quot;)
print(df.groupby(&quot;Category&quot;)[&quot;Profit&quot;].sum())
# Best and Worst Products
print(&quot;\nBEST SELLING PRODUCT&quot;)
print(df.loc[df[&quot;Revenue&quot;].idxmax()])
print(&quot;\nLEAST PROFIT PRODUCT&quot;)
print(df.loc[df[&quot;Profit&quot;].idxmin()])
# Final Output
print(&quot;\nFINAL SUPERMARKET SALES REPORT&quot;)
print(df)
