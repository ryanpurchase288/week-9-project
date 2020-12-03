pipeline{
        agent any

	stages{
		
		stage ('Test application'){
			steps{
				sh " ./scripts/testing.sh"
			} 
		}
		stage ('Push Docker'){
            steps{
                sh " ./scripts/docker.sh"
                        }
                }
        stage('Deploy application'){
            steps{
                sh " ./scripts/deploy.sh"

                        }

        	}
	}
}
