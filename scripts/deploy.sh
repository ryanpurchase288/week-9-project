  #!/bin/bash
ssh manager << EOF
<<<<<<< HEAD
scp /home/ryanpurchase288_rp/Week-9-project/docker-compose.yaml /home/jenkins/
docker stack deploy --compose-file docker-compose.yaml projectApp
=======
docker pull ryanpurchase288/app1:latest
docker pull ryanpurchase288/app2:latest
docker pull ryanpurchase288/app3:latest
docker pull ryanpurchase288/app4:latest
git clone https://github.com/ryanpurchase288/week-9-project.git
cd week-9-project
docker stack deploy --compose-file docker-compose.yaml sfia2
>>>>>>> dbd2ff64ecad9a127d3299952c0e4cd036bc3e59
EOF