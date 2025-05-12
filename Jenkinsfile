pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run App') {
            steps {
                bat 'python app.py'
            }
        }
    }
}
