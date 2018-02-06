pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'pip install -r requirments.txt'
                sh 'python jenkinsApp/manage.py test jenkinsApp.tests '
            }
        }
    }
}