# Sepsis Prediction Models

This documentation offers a comprehensive insight into the code for three distinct sepsis prediction models: SepsisLabel, SepsisSIRS, and SepsisSOFA. 
These models are implemented using the code found in the file "modelo_de_entrenamiento.py" located within the "Modelos/BorradoresModelos" directory.
These models aim to predict sepsis in patients based on various clinical parameters. The code demonstrates how to build, train, and evaluate logistic regression models for each of these prediction tasks.
SepsisLabel Model

The SepsisLabel model focuses on predicting sepsis using the "SepsisLabel" target variable.
Data Reduction and Validation

The following steps are performed:

    A reduced dataset is created, including only the relevant features: 'Bilirubin_total', 'Creatinine', 'HR', 'MAP', 'Platelets', 'Temp', 'WBC', and 'SepsisLabel'.

    Data information and summary statistics are displayed.

    The dataset is split into training and testing sets, with 80% for training and 20% for testing.

    The 'SepsisLabel' column is removed from the training and testing datasets to create the input features.

Model Training and Evaluation

    A logistic regression model is created and trained using the training data.

    Predictions are made on the test data.

    The mean squared error is calculated, representing the prediction error as a percentage, and displayed as "Error by percentage."

SepsisSIRS Model

The SepsisSIRS model focuses on predicting sepsis using the "Sepsis_SIRS" target variable.
Data Reduction and Validation

Similar to the SepsisLabel model, the dataset is reduced and validated, and data information and summary statistics are displayed.
Model Training and Evaluation

    A logistic regression model is created and trained using the training data.

    Predictions are made on the test data.

    The mean squared error is calculated and displayed as "Error by percentage."

SepsisSOFA Model

The SepsisSOFA model focuses on predicting sepsis using the "Sepsis_SOFA" target variable.
Data Reduction and Validation

Similar to the previous models, the dataset is reduced and validated, and data information and summary statistics are displayed.
Model Training and Evaluation

    A logistic regression model is created and trained using the training data.

    Predictions are made on the test data.

    The mean squared error is calculated and displayed as "Error by percentage."

Important Notes

    Ensure that the required Python libraries, such as pandas, numpy, and scikit-learn, are installed in your environment.

    The code for each model is separated by comments and labeled to make it easy to identify the specific components for each model.

    It is essential to have a properly formatted dataset named 'GSepsis' with the necessary columns for these models to work.

    The evaluation metric used in this code is mean squared error, represented as a percentage error.

Please adapt this code and documentation to your specific dataset and requirements. This document serves as an overview of the provided code for sepsis prediction models.
