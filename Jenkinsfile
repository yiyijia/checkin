pipeline {
    agent any
    parameters {
        string(name: 'ID', defaultValue: '0')
    }
    stages {
          stage('Build') {
              steps {
                  echo "Building..."
              }
          }
          stage('Test') {
              steps {
                  echo "Testing..."
              }
          }
          stage('Deploy') {
              steps {
                  echo "Deploying..."
              }
          }
      }
}
