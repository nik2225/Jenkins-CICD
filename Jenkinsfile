pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-ci-cd-demo'
        DOCKER_REGISTRY = 'your-docker-registry-url'  // Optional if pushing to a registry
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

        stage('Post Build Actions') {
            steps {
                script {
                    // Optionally, you can push the image to DockerHub or another registry
                    // dockerImage.push()
                    // For example: dockerImage.push("${env.BUILD_ID}")
                }
            }
        }
    }

    post {
        always {
            // Clean up by stopping the container
            sh 'docker stop $(docker ps -q --filter ancestor=flask-ci-cd-demo)'
        }
    }
}
