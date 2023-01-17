pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/hamzayawa/alx-system_engineering-devops', branch: 'master')
      }
    }

    stage('Logs') {
      steps {
        sh 'ls -la'
      }
    }

  }
}