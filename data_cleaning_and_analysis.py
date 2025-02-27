import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('healthcare_dataset.csv')


print("Initial Data Preview:")
print(df.head())  # Display the first few rows of the dataset


print("\nMissing Values per Column:")
print(df.isnull().sum())


df['Age'].fillna(df['Age'].mean(), inplace=True)  # Replace missing 'Age' with mean value
df['Gender'].fillna(df['Gender'].mode()[0], inplace=True)  # Replace missing 'Gender' with mode value
df.dropna(subset=['Billing Amount'], inplace=True)  # Drop rows where 'Billing Amount' is missing


df.drop_duplicates(inplace=True)


print("\nBasic Statistics:")
print(df.describe())


age_avg = df['Age'].mean()
print(f"\nAverage Age: {age_avg:.2f}")


gender_mode = df['Gender'].mode()[0]
print(f"Most Common Gender: {gender_mode}")


# Plot: Distribution of 'Age'
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plot: Countplot of the 'Gender' column (or another relevant categorical column)
sns.countplot(x='Gender', data=df)
plt.title('Count of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


df.to_csv(r'D:\JOBS\Healthcare-Data-Cleaning-and-EDA\cleaned_healthcare_dataset.csv', index=False)


# Additional Analysis: Distribution of 'Billing Amount'
sns.histplot(df['Billing Amount'], kde=True)
plt.title('Billing Amount Distribution')
plt.xlabel('Billing Amount')
plt.ylabel('Frequency')
plt.show()

# Additional Analysis: Boxplot of 'Age' by 'Gender'
sns.boxplot(x='Gender', y='Age', data=df)
plt.title('Age Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()

# Additional Analysis: Countplot of 'Admission Type'
sns.countplot(x='Admission Type', data=df)
plt.title('Count of Admission Type')
plt.xlabel('Admission Type')
plt.ylabel('Count')
plt.show()
