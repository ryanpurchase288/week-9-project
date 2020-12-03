  #!/bin/bash
ssh manager << EOF
scp /home/ryanpurchase288_rp/Week-9-project/docker-compose.yaml /home/jenkins/
docker stack deploy --compose-file docker-compose.yaml projectApp
EOF