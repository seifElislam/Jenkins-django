pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            sh 'pip install -r requirments.txt',
            sh 'python jenkinsApp/manage.py test tests'
        }
    }
}