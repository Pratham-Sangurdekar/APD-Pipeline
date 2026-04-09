pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker compose up --abort-on-container-exit'
            }
        }

    }

    post {

        success {
            emailext(
                subject: "Jenkins SUCCESS: ${env.JOB_NAME}",
                body: "Build successful.\n\nCheck Jenkins for output.",
                to: "wannabegmpratham@gmail.com"
            )
        }

        failure {
            emailext(
                subject: "Jenkins FAILED: ${env.JOB_NAME}",
                body: "Build failed.\n\nCheck Jenkins logs.",
                to: "wannabegmpratham@gmail.com"
            )
        }
    }
}