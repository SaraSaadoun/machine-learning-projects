## 🎯 3. Mall Customer Segmentation

### Overview
This project focuses on performing **customer segmentation** using unsupervised learning techniques to group customers based on their spending patterns and annual income. The goal is to identify distinct groups to better understand customer behavior.

![image](https://github.com/user-attachments/assets/6815784c-dade-43b6-a2aa-9db99d59d4c6)

### Deployed Using Streamlit
This project is deployed using a **Streamlit app**, providing an interactive interface to visualize customer segmentation results.

### Techniques Used
- **K-Means Clustering**: Applied to segment customers into distinct groups based on features like annual income and spending score.
- **Elbow Method & Silhouette Score**: Used to determine the optimal number of clusters for segmentation.
- **Principal Component Analysis (PCA)**: Implemented for dimensionality reduction and to visualize the clusters in two dimensions.
- **Hierarchical Clustering**: Used as an alternative clustering method to group customers into hierarchical structures.

### Visualizations
- **Pair Plot**: Visualized relationships between different features to explore potential clusters.
- **PCA Scatter Plot**: Visualized clusters after applying PCA for dimensionality reduction.
- **Cluster Visualizations**: Displayed clustered data points using seaborn and matplotlib to understand customer grouping.

### Interpretation of Customer Segmentation
You can find a notebook from which we gain insights in a separate directory. Here are the key results:

After clustering the customers, we can interpret the segmentation as follows. From the 'Age' column and the scatter plot above, we observe:

1. **Cluster 1**: Young adults, budget-conscious with high spending tendencies.
2. **Cluster 2**: Middle-aged customers with stable income and moderate spending.
3. **Cluster 3**: Older professionals with high income but low spending.
4. **Cluster 4**: Individuals enjoying luxury and high spending.
5. **Cluster 5**: Older individuals or lower-income customers focused on value.

---
