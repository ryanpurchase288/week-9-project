pipeline{
    agent any

	stages{
		slackSend botUser: true, 
  				channel: 'project9', 
  				color: '#00ff00', 
  				message: 'Testing Jekins with Slack', 
				  tokenCredentialId: 'slack-token'
		stage('Install Docker using ansible'){
            steps{
				
  				
				slackSend channel: '#project9', message: 'Started pipeline'
                slackSend channel: '#project9', message: 'Install Ansible and Docker'
				sh " ./scripts/ansible.sh"
				slackSend channel: '#project9', message: 'Install complete'
                	}
            	}
		stage ('Test application'){
			steps{
				slackSend channel: '#project9', message: 'Test started'
				sh " ./scripts/testing.sh"
				slackSend channel: '#project9', message: 'Test Finished'
			} 
		}
		stage ('Push Docker'){
            steps{
				#slackSend channel: '#project9', message: 'Build started'
                sh " ./scripts/docker.sh"
				slackSend channel: '#project9', message: 'Build Completed'
                        }
                }
        stage('Deploy application'){
            steps{
				slackSend channel: '#project9', message: 'Deploy Started'
                sh " ./scripts/deploy.sh"
				slackSend channel: '#project9', message: 'Deploy Finished'

                        }

        	}
	}
}
