pipeline {
    agent any
    tools{
        jdk 'jdk11'
        maven 'maven3'
    }
    environment {
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', changelog: false, credentialsId: 'f7451ce6-b62a-4d2c-b3d4-b464bee02780', poll: false, url: 'https://github.com/yying1207/desktop-tutorial.git'
            }
        }
        stage('Compile') {
            steps {
                sh "mvn clean compile -DskipTests=true"
            }
        }
        stage('OWASPScan') {
            steps{
                dependencyCheck additionalArguments: '--scan ./ ', odcInstallation: 'DP'
                dependencyCheck publisher pattern: '**/dependency check report.xml'
            }
        }
        stage('Sonar Analysis') {
            steps{
                WithSonarQubeEnv('sonar-server'){
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=desktop-tutorial \
                    -Dsonar.java.binaries=. \
                    -Dsonar.projectkey=desktop-tutorial '''
                }
            }
        }
        stage('Build') {
            steps{
                sh "mvn clean package -DskipTests=true"
            }
        }
        stage('Docker Build & Push') {
            steps{
                script{
                    withDockerRegistry(credentialsId: 'f7451ce6-b62a-4d2c-b3d4-b464bee02780', toolName: 'docker') {
                    
                        sh "docker build -t desktop-tutorial -f docker/Dockerfile ."
                        sh "docker tag desktop-tutorial yying1207/desktop-tutorial:latest"
                        sh "docker push desktop-tutorial yying1207/desktop-tutorial:latest"
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                script{
                    withDockerRegistry(credentialsId: 'f7451ce6-b62a-4d2c-b3d4-b464bee02780', toolName: 'docker') {
                        sh "docker run -d --name shop-shop -p 8070:8070 desktop-tutorial yying1207/desktop-tutorial:latest"
                }
            }
        }
    }
}
