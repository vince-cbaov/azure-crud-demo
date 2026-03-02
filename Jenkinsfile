
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

stage('Path diagnostics') {
  steps {
    sh '''
      set -eux
      echo "HOME        =" "$HOME"
      echo "USER        =" "$(whoami)"
      echo "SHELL       =" "$SHELL"
      echo "Current PWD =" "$PWD"
      echo "PATH        =" "$PATH"
      which python3 || true
      which python  || true
      python3 -c "import sys; print('sys.executable =', sys.executable)"
      python3 -m site
      python3 -c "import site; print('USER_BASE =', site.getusersitepackages().rsplit('/',1)[0]); print('USER_SITE =', site.getusersitepackages())"
      # Common location for user-installed scripts:
      ls -la "$HOME/.local/bin" || true
      # If using a venv later:
      ls -la .venv/bin || true
    '''
  }
}
