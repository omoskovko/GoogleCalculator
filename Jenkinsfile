pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'python run_test.py'
            }
        }
    }
    post {
       always {
         junit '**/test-reports/*.xml'
       }
    }
}