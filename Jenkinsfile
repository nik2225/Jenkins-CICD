pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-ci-cd-demo'
        DOCKER_REGISTRY = 'your-docker-registry-url'  // Replace with your registry URL if pushing to a registry
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clones your repository from GitHub
                git 'https://github.com/nik2225/Jenkins-CICD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image from the Dockerfile
                    dockerImage = docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container in the background
                    sh "docker run -d -p 5000:5000 ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Push Docker Image to Registry') {
            when {
                expression { return env.DOCKER_REGISTRY != '' } // Ensure registry URL is set
            }
            steps {
                script {
                    // Log in to Docker registry (use DockerHub as an example)
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-hub-credentials') {
                        // Push the Docker image to the registry
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up by stopping and removing the container
            sh """
                CONTAINER_ID=\$(docker ps -q --filter ancestor=${DOCKER_IMAGE})
                if [ -n "\$CONTAINER_ID" ]; then
                    docker stop \$CONTAINER_ID
                    docker rm \$CONTAINER_ID
                fi
            """
        }
    }
}
