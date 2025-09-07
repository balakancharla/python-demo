pipeline {
  agent {
    kubernetes {
      label 'ec2-builder'
      defaultContainer 'python'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: ec2-builder
spec:
  containers:
  - name: python
    image: python:3.10
    command:
    - cat
    tty: true
"""
    }
  }

  // 👇 Declare pipeline parameter
  parameters {
    string(name: 'INSTANCE_TYPE', defaultValue: 't2.micro', description: 'Enter EC2 instance type (e.g., t2.micro, t3.small)')
  }

  environment {
    AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
  }

  stages {
    stage('Checkout Code') {
      steps {
        git 'https://github.com/balakancharla/python-demo.git'
      }
    }

    stage('Install Dependencies') {
      steps {
        container('python') {
          sh 'pip install boto3'
        }
      }
    }

    stage('Launch EC2 Instance') {
      steps {
        container('python') {
          sh "python launch_ec2.py ${params.INSTANCE_TYPE}"
        }
      }
    }
  }
}
