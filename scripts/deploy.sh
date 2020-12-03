  #!/bin/bash
ssh manager << EOF
docker pull ryanpurchase288/app1:latest
docker pull ryanpurchase288/app2:latest
docker pull ryanpurchase288/app3:latest
docker pull ryanpurchase288/app4:latest
git clone https://github.com/ryanpurchase288/week-9-project.git
cd week-9-project
docker stack deploy --compose-file docker-compose.yaml projectApp
<<<<<<< HEAD
nginxPath=pwd
docker run -d -p 80:80 --name nginx-swarm-ingress --mount type=bind,source=$(nginxPath)/week-9-project/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine
=======
$(pwd)=pwd
cd ~/week-9-project
docker run -d -p 80:80 --name nginx-swarm-ingress --mount type=bind,source=pwd/week-9-project/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine
>>>>>>> 3b0a1ce2ea37f4efd5a70fd550a416bf27bb0edb
EOF