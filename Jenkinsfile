pipeline {
agent any
    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/yoavsharon80/day8.git'
            }
        }
        stage('build') {
            steps {
                sh 'python Git_test.py'
            }
        }
    }
}