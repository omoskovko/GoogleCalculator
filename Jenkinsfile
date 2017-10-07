pipeline {
    agent { docker 'python:3.4' }
    stages {
        stage('build') {
            steps {
                sh 'python run_test.py'
            }
        }
    }
}
