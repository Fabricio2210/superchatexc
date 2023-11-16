pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/Fabricio2210/superchatexc.git']]])
            }
        }
        stage('Set Permissions') {
            steps {
                script {
                    // Add your sudo command here
                    sh 'sudo /bin/chmod -R a+rwx /var/lib/jenkins/workspace'
                }
            }
        }
        stage('Build') {
            steps {
                sh 'pip install openpyxl'
            }
        }

        stage('Print Workspace') {
            steps {
                echo "Workspace directory: ${WORKSPACE}"
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application.......'
                script {
                    sh 'sudo systemctl restart superchatexc'
                }
            }
        }
    }
}