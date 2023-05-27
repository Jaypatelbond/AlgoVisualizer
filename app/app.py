import os
import streamlit as st
import importlib.util


def execute_main(file_path):
    # Get the file name and module name
    file_name = os.path.basename(file_path)
    module_name = file_name[:-3]

    try:
        # Load the module
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Check if the main function exists in the module
        if hasattr(module, 'main') and callable(module.main):
            # Call the main function
            output = module.main()
            return output
        else:
            return 'Error: The main function does not exist in the module.'
    except Exception as e:
        return f'Error: {str(e)}'

# Function to read the content of a file


def read_file(filename):
    with open(filename) as f:
        code = f.read()
    return code


# Set the path to the algos directory
curr_dir = os.path.dirname(__file__)
algo_path = os.path.join(curr_dir, "algos")

# Define the list of algorithms and their file extensions
algos = {
    "Recursion": "recursion",
    "Dynamic Programming": "dynamic_programming",
    "Greedy Algorithm": "greedy_algorithm",
    "Backtracking": "backtracking"
}

# Set the app title
st.set_page_config(page_title="Algorithm Executor")

# Create the sidebar menu with algorithm selection
algo_type = st.sidebar.radio("Select algorithm type", list(algos.keys()))

# Get the list of files for the selected algorithm type
algo_dir = os.path.join(algo_path, algos[algo_type])
algo_files = os.listdir(algo_dir)

# Create the dropdown menu with algorithm file selection
selected_file = st.selectbox("Select algorithm file", algo_files)

# Create the code section with the selected algorithm code
if selected_file.endswith(".py"):
    algo_file_path = os.path.join(algo_dir, selected_file)
    with open(algo_file_path) as f:
        code = f.read()
    st.code(code, language="python")
else:
    st.write("Please select a valid Python file.")

# Execute the main function on button click
if st.button('Execute'):
    try:
        output = execute_main(algo_file_path)
        st.write('Output:')
        st.write(output)
    except Exception as e:
        st.write('Error:')
        st.write(e)
