pipeline {
  agent any
  parameters {
        string(defaultValue: 'vaibhavk0011@outlook.com', description: 'Add sender\'s email address', name: 'sender')
        string(defaultValue: 'khandekarv0@gmail.com', description: 'Add recipient\'s email address', name: 'recipient')
        string(defaultValue: 'Server Configurations', description: 'Add server configurations', name: 'serverconfig')
        string(defaultValue: 'Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET', description: 'Add message to send', name: 'msg')
    }
  stages {
    stage('build') {
      steps {
        sh 'python3 main.py ${sender} ${recipient} ${serverconfig} ${msg}'
      }
    }
  }
}