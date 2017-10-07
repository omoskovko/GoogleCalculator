pipeline {
    agent { docker 'python:3.4' }
    stages {
        stage('build') {
            steps {
                bat 'python run_test.py'
            }
        }
    }
}
