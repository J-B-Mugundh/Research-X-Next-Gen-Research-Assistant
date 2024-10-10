import streamlit as st
import subprocess
import shutil
import os

# Define a session state variable to store the selected file
if 'selected_file' not in st.session_state:
    st.session_state['selected_file'] = None

def list_repo_files(repo_url):
    """Clones a GitHub repository and lists its files.

    Args:
        repo_url (str): The URL of the GitHub repository.

    Returns:
        list: A list of filenames within the cloned repository.
    """
    try:
        # Attempt to import shutil to check its availability
        try:
            import shutil
            shutil_available = True
        except ImportError:
            shutil_available = False

        # Clone the repository using the appropriate command (Git or GitHub CLI)
        if shutil_available:  # Check if shutil is available
            shutil.rmtree("cloned_repo", ignore_errors=True)  # Clean up previous clones
            subprocess.run(["git", "clone", repo_url, "cloned_repo"], check=True)
        else:
            subprocess.run(["gh", "repo", "clone", repo_url, "cloned_repo"], check=True)

        # List files within the cloned repository
        files = []
        for root, _, filenames in os.walk("cloned_repo"):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files
    except subprocess.CalledProcessError as e:
        st.error(f"Error cloning repository: {e}")
        return []
    finally:
        pass

def display_file_content(file_path):
    """Attempts to read the content of a file and display it in the app.

    Args:
        file_path (str): The path to the file to be displayed.
    """
    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            content = file.read()
            st.write(content)
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
    except PermissionError:
        st.error(f"Insufficient permissions to access file: {file_path}")

# Main title and URL input
st.title("Code Explorer 💻")

repo_url = st.text_input("Enter the URL of a GitHub repository to list its files:")

if st.button("List Files"):
    if not repo_url:
        st.error("Please enter a valid GitHub repository URL.")
    else:
        files = list_repo_files(repo_url)
        if files:
            st.success("Successfully cloned and listed files:")

            # Create a dropdown menu with the file list
            selected_file = st.selectbox("Select a file to interact with:", options=[""] + files)
            if selected_file:
                st.session_state['selected_file'] = selected_file  # Update session state

                # Display the content of the selected file
                display_file_content(selected_file)

# Sidebar with dummy button
with st.sidebar:
    st.button("Interact with file")
