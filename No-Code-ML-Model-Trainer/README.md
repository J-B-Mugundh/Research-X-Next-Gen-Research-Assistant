# **No Code ML Model Trainer**

### 🎯 **Goal**

The primary goal of **No Code ML Model Trainer** is to provide a no-code interface for users to train machine learning models effortlessly. The application allows users to upload datasets, preprocess the data, select machine learning models, and evaluate their performance without requiring extensive programming knowledge.

### 🧵 **Dataset**

**No Code ML Model Trainer** allows users to work with their datasets by either selecting from pre-existing datasets or uploading new ones. The application is designed to support various data formats, enabling users to train models on a wide range of datasets.

### 🧾 **Description**

**No Code ML Model Trainer** offers a user-friendly interface that guides users through the machine learning workflow. Users can select datasets, specify target columns, choose preprocessing methods, and select from a variety of machine learning algorithms to train models. The application also displays the accuracy of the trained models, making machine learning accessible to everyone.

### 🧮 **What I had done!**

- Implemented a **dataset management system** that allows users to select from existing datasets or upload new ones.
- Developed preprocessing options, including various scaling methods to prepare data for training.
- Integrated multiple machine learning algorithms such as Logistic Regression, Support Vector Classifier, Random Forest, and XGBoost for model training.
- Created a streamlined interface using **Streamlit** for easy navigation and interaction.

### 🚀 **Models Implemented**

- **Logistic Regression**: A linear model for binary classification.
- **Support Vector Classifier**: A model that finds the hyperplane that best separates the data points.
- **Random Forest Classifier**: An ensemble method that uses multiple decision trees to improve accuracy.
- **XGBoost Classifier**: An optimized gradient boosting algorithm known for its performance and speed.

### 📚 **Libraries Needed**

- `streamlit`
- `scikit-learn`
- `xgboost`
- `ml_utility` (custom module for data reading, preprocessing, model training, and evaluation)

### 📊 **Exploratory Data Analysis Results**

This project focuses primarily on the training of models rather than traditional exploratory data analysis. However, users can visualize the dataset and its basic statistics upon uploading or selecting a dataset.

### 📈 **Performance of the Models based on the Accuracy Scores**

The performance of the models can be evaluated based on:
- **Test Accuracy**: The accuracy achieved by the model on the test dataset after training.

### 💻 How to run

To get started with **No Code ML Model Trainer**, follow these steps:

1. Navigate to the project directory:

    ```bash
    cd No-Code-ML-Model-Trainer
    ```

2. (Optional) Activate a virtual environment:

    ```bash
    conda create -n venv python=3.10+
    conda activate venv
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    streamlit run main.py
    ```

    PS: Explore the functionality of the app by uploading or selecting a dataset and training a model.

### 📢 **Conclusion**

**No Code ML Model Trainer** democratizes machine learning by providing a no-code solution for users to train and evaluate models easily. The integration of various machine learning algorithms and preprocessing techniques allows for a comprehensive approach to model training, making it accessible for users of all skill levels.

### ✒️ **Signature**

**[J B Mugundh]**  
GitHub: [Github](https://github.com/J-B-Mugundh)  
LinkedIn: [Linkedin](https://www.linkedin.com/in/mugundhjb/)
