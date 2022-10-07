pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python3 main.py ${sender} ${recipient} ${serverconfig} ${msg}'
      }
    }
  }
}