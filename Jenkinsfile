pipeline {
  agent any
  options { timestamps() }
  environment {
    PYTHONUNBUFFERED = '1'
  }
  stages {

    stage('Checkout') {
      steps {
        checkout([$class: 'GitSCM',
          branches: [[name: '*/dev']],
          userRemoteConfigs: [[url: 'https://github.com/vince-cbaov/azure-crud-demo.git']]
        ])
      }
    }

    stage('Path diagnostics') {
      steps {
        sh '''
          set -eux
          echo "HOME=$HOME"
          echo "PATH=$PATH"
          which python3 || true
          which pytest  || true
          python3 -c "import sys,site; print('exe=', sys.executable); print('user_site=', site.getusersitepackages())"
          ls -la "$HOME/.local/bin" || true
        '''
      }
    }

    stage('Python') {
      steps {
        sh '''
          set -eux
          python3 --version || true
          python3 -m pip install --upgrade pip
          # user install may put scripts in ~/.local/bin
          python3 -m pip install --user -r requirements.txt
        '''
      }
    }

    stage('Tests') {
      steps {
        sh '''
          set -eux
          mkdir -p reports
          # call pytest as a module so we don't depend on PATH to find the script
          python3 -m pytest -v --maxfail=1 --disable-warnings --junitxml=reports/junit.xml
        '''
      }
      post {
        always {
          junit allowEmptyResults: true, testResults: 'reports/junit.xml'
        }
      }
    }
  }
}
