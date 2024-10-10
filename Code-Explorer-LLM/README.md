# **Code Explorer LLM**

### 🎯 **Goal**

The primary goal of **Code Explorer LLM** is to provide an interactive tool for developers and researchers to explore and analyze code within GitHub repositories. The application allows users to clone repositories, list files, and view their contents, facilitating a deeper understanding of code structures and implementations.

### 🧵 **Dataset**

**Code Explorer LLM** does not use a static dataset; instead, it interacts directly with live GitHub repositories. Users can input the URL of any public repository to clone and explore its contents in real-time.

### 🧾 **Description**

**Code Explorer LLM** enables users to enter a GitHub repository URL, clone the repository, and view its files directly within the app. The application is designed for seamless navigation and interaction, making it easier for users to examine code snippets, documentation, and other resources contained in the repository.

### 🧮 **What I had done!**

- Developed a **repository cloning system** that uses `git` or GitHub CLI to clone repositories from GitHub.
- Implemented file listing and content display functionality to allow users to interactively explore code files.
- Utilized **Streamlit** for building a user-friendly web interface for easy navigation and interaction.

### 🚀 **Models Implemented**

- **Streamlit**: Used for creating an interactive web interface, allowing users to engage with the application seamlessly.

### 📚 **Libraries Needed**

- `streamlit`
- `subprocess`
- `shutil`
- `os`

### 📊 **Exploratory Data Analysis Results**

This project does not involve traditional exploratory data analysis, as it focuses on code exploration. However, if any performance metrics or usage statistics are collected (e.g., number of repositories explored, file types accessed), they can be displayed here.

### 📈 **Performance of the System**

The performance of the system can be evaluated based on:
- **Cloning efficiency**: The time taken to clone repositories and list files.
- **File content accessibility**: The ability to display file contents accurately without errors.

### 💻 How to run

To get started with **Code Explorer LLM**, follow these steps:

1. Navigate to the project directory:

    ```bash
    cd Code-Explorer-LLM
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
    streamlit run app.py
    ```

    PS: Explore the functionality of the app by inputting a GitHub repository URL.

### 📢 **Conclusion**

**Code Explorer LLM** successfully integrates GitHub repository exploration with an intuitive user interface, providing a reliable tool for developers and researchers to analyze and interact with code effectively.

### ✒️ **Signature**

**[J B Mugundh]**  
GitHub: [Github](https://github.com/J-B-Mugundh)  
LinkedIn: [Linkedin](https://www.linkedin.com/in/mugundhjb/)
