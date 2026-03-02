
pipeline {
  agent any
  options { timestamps() }
  stages {
    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM', branches: [[name: '*/dev']], userRemoteConfigs: [[url: 'https://github.com/vince-cbaov/azure-crud-demo.git']]])
      }
    }
    stage('Python') {
      steps {
        sh 'python3 --version || true'
        sh 'python3 -m pip install --upgrade pip'
        sh 'python3 -m pip install -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        sh 'pytest -v'
      }
      post {
        always { junit allowEmptyResults: true, testResults: '**/test-results.xml' }
      }
    }
  }
}
