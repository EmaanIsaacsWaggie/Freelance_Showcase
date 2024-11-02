Freelance Showcase

Description
Freelance Showcase is a Django-based web application that allows freelancers to showcase their work, connect with potential clients, and manage project submissions. Users can upload projects, view their portfolios, and engage with the community.

Installation Instructions
Prerequisites
Python 3.11 or higher
pip (Python package installer)
Docker (for containerization)

Step 1: Clone the Repository
Open your terminal or command prompt and clone the repository using git:

git clone https://github.com/EmaanIsaacsWaggie/freelance_showcase.git

Step 2: Navigate to the Project Directory
Change into the project directory:
cd freelance_showcase

Step 3: Build the Docker Image
Make sure you have Docker installed and running. Then, build the Docker image by running:
docker build -t freelance_showcase .

Step 4: Run the Docker Container
Once the image is built, you can run the application in a Docker container:
docker run -d -p 8000:8000 freelance_showcase
This command will run the container in detached mode and map port 8000 on your host to port 8000 on the container.

Step 5: Access the Application
You can now access the Freelance Showcase application by navigating to http://localhost:8000 in your web browser.

Additional Commands
To stop the running container, you can use:
docker ps  # Get the container ID
docker stop <container_id>


To remove the container after stopping it:
docker rm <container_id>

Usage
Once the application is running, you can create an account, upload projects, and interact with other users in the community.
