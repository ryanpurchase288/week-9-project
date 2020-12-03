  #!/bin/bash
ssh manager << EOF
scp /home/ryanpurchase288_rp/week-9-project/docker-compose.yaml /home/jenkins/
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF