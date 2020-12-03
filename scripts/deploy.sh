  #!/bin/bash
ssh manager << EOF
docker pull ryanpurchase288/app1:latest
docker pull ryanpurchase288/app2:latest
docker pull ryanpurchase288/app3:latest
docker pull ryanpurchase288/app4:latest
git clone https://github.com/ryanpurchase288/week-9-project.git
cd week-9-project
docker stack deploy --compose-file docker-compose.yaml sfia2
EOF