# ML-Projects "Practice Makes Perfect 📈✨"

Welcome to my collection of Machine Learning Projects! Here, I practice and showcase various ML models and techniques. Let's dive in! 🚀

# Index:
- **1. Diabetes Classification**
- **2. Titanic Classification**
- **3. Mall Customer Segmentation**
- **4. Iris Species Multi-Classifier**

## 📊 1. Diabetes Classification

### Project Overview

This beginner-friendly project involves classifying diabetes status using the **Pima Indians Diabetes Database** with a simple neural network.

---

## 🚢 2. Titanic Classification | A Data Leakage-Free Approach ✅

### Project Overview

In this project, we perform data preprocessing and complex imputation methods based on other non-null variables to prepare the dataset for analysis. We conduct extensive exploratory data analysis (EDA) to extract new features, including:

| Feature                    | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| **Title from Names**       | Extracting titles (Mr, Mrs, Miss, etc.) from names.   |
| **IsAlone Feature**        | Binary feature indicating if a passenger is alone.    |
| **Categorization of Age**  | Transforming continuous age into categorical ranges.  |
| **Categorization of Fare** | Transforming continuous fare into categorical ranges. |

**Imputation and Feature Engineering**: We apply these techniques only on the training data, using the same transformations on the validation/test data without accessing target information.

### Model Evaluation

After feature extraction, we select the most appropriate features and create a validation split to evaluate various models, including:

- **Logistic Regression**: `LogisticRegression()`
- **XGBoost**: `XGBClassifier()`
- **Support Vector Machine (SVM)**: `SVC()`
- **Decision Tree**: `DecisionTreeClassifier()`
- **Random Forest**: `RandomForestClassifier()`
- **Naive Bayes**: `GaussianNB()`
- **K-Nearest Neighbors (KNN)**: `KNeighborsClassifier()`
- Using the **F1-score** for evaluation, we cannot rely on accuracy as a metric due to the **data imbalance problem** in the dataset. The F1-score provides a better measure of a model's performance, particularly in imbalanced situations, as it considers both precision and recall—the harmonic mean of these two metrics. We identify the best **4** models and perform **hyperparameter tuning** on `XGBoost`, `Random Forest`, and `Decision Tree` using Grid Search. We also visualize feature importances to gain insights and save predictions for submission to the **Kaggle competition**. 🏆

---

## 🎯 3. Mall Customer Segmentation

### Overview
This project focuses on performing **customer segmentation** using unsupervised learning techniques to group customers based on their spending patterns and annual income. The goal is to identify distinct groups to better understand customer behavior.

![image](https://github.com/user-attachments/assets/8aaaf57c-1464-4812-aa1f-b9634533b32c)


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

## 🌷 4. Iris Species Multi-Classifier

### Overview
Classifying **Iris species** using the **Iris dataset** with features: sepal length, sepal width, petal length, and petal width.

### Techniques

- **Data Exploration**
- **Models**: Logistic Regression, Random Forest, Xgboost Classifier, Decision Tree, SVM
- **Evaluation**: Accuracy metrics as the dataset is balanced as well as classification report.

### Visualizations
- Pair plot and confusion matrix.

---

Thank you for checking out my ML projects! Feel free to explore and provide feedback! 😊
