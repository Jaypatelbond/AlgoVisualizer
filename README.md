# Algorithm Executor with Docker

The Algorithm Executor is a web application that allows you to execute various algorithms. It provides a user-friendly interface where you can select an algorithm type and an algorithm file to execute.

## Features

- Selection of algorithm types:
  - Recursion
  - Dynamic Programming
  - Greedy Algorithm
  - Backtracking

- Code Execution:
  - Upload and execute algorithm files.
  - View algorithm code with syntax highlighting.

## Prerequisites

- Docker: Ensure that Docker is installed on your device. You can download and install Docker from the official Docker website (https://www.docker.com/get-started).
- Python installed on your system.


## Getting Started on Local Machine

1. To get started with the AlgoVisualizer application, you can clone the repository using the following command:

		git clone https://github.com/Himanshutomar31/AlgoVisualizer.git

2. After cloning the repository, navigate to the project directory and install the necessary dependencies by running the following command:

		pip install -r requirements.txt

3. You can skip to 6th step if you have virtual env dependencies installed and activated. If not then run the following command to install the virtual enviroment:

		pip install virtualenv

4. Next, run the following command to install the virtual enviroment:

		python -m virtualenv env

5. Next, run the following command to activate:

		source env/bin/activate

6. Finally, to run the project, run the following command to start the web application:

		bash scripts/startup.sh

This will start the application on port 8000. Once the application is running, open a web browser and navigate to `http://localhost:8000` to access the application.

## Getting Started with Docker. By following these steps, you can run the Streamlit app as a Docker container on any device with Docker installed and access it through a web browser. The app will be available at the specified port, allowing you to interact with it regardless of the device's operating system or environment.

1. Clone the repository to your local machine:

		git clone https://github.com/Himanshutomar31/AlgoVisualizer.git

2. Navigate to the project directory:

		cd algorithm-executor-docker

3. Prepare the code and Dockerfile:

- Put your Streamlit app code and any necessary files (such as requirements.txt) in the project directory.
  Ensure that you have a Dockerfile in the project directory. If not, create one using the provided instructions.


4. Ensure that Docker is installed:

- Make sure Docker is installed on the device where you want to run the app. You can download and install Docker from the official Docker website (https://www.docker.com/get-started).

5. Build the Docker image:

		docker build -t algorithm-executor .

6. Run the Docker container:

		docker run -p 8501:8501 algorithm-executor

- This command runs a container based on the algorithm-executor image and maps port 8501 from the container to port 8501 on your local machine.

7. Access the Streamlit app:

- Open a web browser on your device and navigate to http://localhost:8501 or http://<machine-ip-address>:8501.
  Replace <machine-ip-address> with the IP address of the machine running the Docker container. If you're running Docker locally, you can use localhost as the IP address.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.





