pipeline {
    agent any
    options {
        timeout(time: 5, unit: 'MINUTES') 
        disableConcurrentBuilds()
    }
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'ls'
                    sh 'python3 -m venv .venv'
                    sh '.venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                sh '.venv/bin/python -m unittest discover -s tests'
            }

        }
        stage('Deploy') {

            steps {
                sh '''
                nohup .venv/bin/python run.py > run.log 2>&1 &
                '''
            }
        }
    }
    post {
        failure {
            emailext (
                subject: 'FAILED: Job ${JOB_NAME} - Build #${BUILD_NUMBER}',
                body: """Check console output: ${BUILD_URL}console""",
                to: 'kevin.koreth@gmail.com'
            )
        }
    }
}