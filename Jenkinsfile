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
            when {
                branch 'release/*'  // Only deploy from release branch
            }
            steps {
                sh '''
                .venv/bin/activate
                .venv/bin/python run.py
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