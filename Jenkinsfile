pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                bat 'npm install'
            }
        }
        stage('Run App') {
            steps {
                bat 'npm start'
            }
        }
    }
}
