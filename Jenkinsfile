pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat '''pip install -U selenium
                       pip install -U xmlrunner
                    '''
            }
        }
        stage('Test') {
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