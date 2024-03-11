pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Ammar123890/mlops_class_task_i202417'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Execute test.py') {
            steps {
                sh 'python test.py'
            }
        }

        stage('Deploying') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo 'Deploying to production'
                    } else {
                        echo 'Deploying to UAT'
                    }
                }
            }
        }
    }
}
