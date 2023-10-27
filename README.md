# Sepsis Prediction Models

This documentation offers a comprehensive insight into the code for three distinct sepsis prediction models: SepsisLabel, SepsisSIRS, and SepsisSOFA. 
These models are implemented using the code found in the file "modelo_de_entrenamiento.py" located within the "Modelos/BorradoresModelos" directory.
These models aim to predict sepsis in patients based on various clinical parameters. The code demonstrates how to build, train, and evaluate logistic regression models for each of these prediction tasks.
SepsisLabel Model

**Prerequisites**

Before running this code, ensure that you have the following set up:
```
Verify that essential Python libraries, including pandas, numpy, and scikit-learn, are installed in your environment.
The code for each individual model is thoughtfully organized, accompanied by clear comments, and appropriately labeled to facilitate easy identification of specific components related to each model.
Ensure the presence of a well-structured dataset named 'GSepsis,' which should contain the necessary columns for these models to function effectively. Proper formatting of this dataset is crucial for the models to operate as intended.
```

### The following steps are performed:
1. A reduced dataset is created, including only the relevant features: 'Bilirubin_total', 'Creatinine', 'HR', 'MAP', 'Platelets', 'Temp', 'WBC', and 'SepsisLabel'.
2. Data information and summary statistics are displayed.
3. The dataset is split into training and testing sets, with 80% for training and 20% for testing.
4. The 'SepsisLabel' column is removed from the training and testing datasets to create the input features.

### Model Training and Evaluation
+ A logistic regression model is created and trained using the training data.
+ Predictions are made on the test data.
+ The mean squared error is calculated, representing the prediction error as a percentage, and displayed as "Error by percentage."

### SepsisSIRS Model
The SepsisSIRS model focuses on predicting sepsis using the "Sepsis_SIRS" target variable.
Data Reduction and Validation

Similar to the SepsisLabel model, the dataset is reduced and validated, and data information and summary statistics are displayed.

### Model Training and Evaluation:
+ A logistic regression model is created and trained using the training data.
+ Predictions are made on the test data.
+ The mean squared error is calculated and displayed as "Error by percentage."
