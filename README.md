# week-9-project

## Contents
- [Brief](#brief)
- [Risk Assessment](#risk-assessment)
- [Tracking](#tracking)
- [VSC](#vsc)
- [Architechture](#architechture)
- [CI Pipeline](#ci-pipeline)
- [Pipeline Stages](#pipeline-stages)
- [Tests](#tests)



    

## Brief
### Requirements
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the Service-oriented architecture that has been asked for.
  - Service #1: The core service – this will render the Jinja2 templates you need to interact with your application, it will also be responsible for communicating with the other 3 services, and finally for persisting some data in an SQL database.
  - Service #2 + #3 - These will both generate a random “Object”, this object can be whatever you like as we encourage creativity in this project.
  - Service #4 - This service will also create an “Object” however this “Object” must be based upon the results of service #2 + #3 using some pre-defined rules.
- The project must be deployed using containerisation and an orchestration tool.
- As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

## My Approach
To meet the given requirments I decided to create an application which will make use of random to retrieve a random day of the month 1-31 for service 3 and a random month for service 2 and then in service 4 using what was created in service 2 and 3 put together see if it matches my birthday. which is then displayed all on service 1.
Here is the display of my application to show:
![app](https://github.com/ryanpurchase288/week-9-project/blob/main/images/app.PNG)

## Risk Assessment
I had created a risk assessment for the project here is the link: https://1drv.ms/x/s!Av4eZvsa3rmzl31C7s0lHjzUdzz7?e=H6NBUf
![Risk](https://github.com/ryanpurchase288/week-9-project/blob/main/images/risk.PNG)

## Tracking
For project planning I have used trello which the link is here: https://trello.com/b/VMyn0jkN/week-9-project
![Trello](https://github.com/ryanpurchase288/week-9-project/blob/main/images/trello.PNG)
I created user stories, a to do, a doing, a testing and done stages. I also included an issues list so I can list any of the issues I was not able to solve.

## VSC
As part of the projet was to implement a CI pipeline. I have used Git using its provider github to store my code and to act as the VSC of my CI pipeline.
With this I am able to control my version and revert any changes which may have broken my application for example my database which I will talk about later in a lot more detail.


## Architechture
### ERD
Here is the first version of the ERD I have created for my application:
![erd1](https://github.com/ryanpurchase288/week-9-project/blob/main/images/ERDV1.png)

Here is the updated version of my ERD:
![erd2](https://github.com/ryanpurchase288/week-9-project/blob/main/images/ERDV2.png)

### Services
Here is version 1 of my service design:
![Service](https://github.com/ryanpurchase288/week-9-project/blob/main/images/ServiceV1.png)

Here is the version 2 of my service design for once the database was successfully added to it:
![service2](https://github.com/ryanpurchase288/week-9-project/blob/main/images/ServiceV2.png)

### Swarm Architechture
I had a jenkins server to deploy the app on a swarm manager which then deployed it to its worker nodes. To set up the swarm nodes I had used ansible to ensure everything they would need to have deploy the app is automatically installed so if i used new machines I would not need to install everything manually on each of the machines. I also had included an NGINX load balancer/reverse proxy on a VM as well to allow me to close all ports except port 80 on the NGINX machine.

The swarm allows me to run the application on many machines meaning access to the machine is greater so there should be no down time for anyone using it.

Here is the first version of my swarm architechture:
![swarm](https://github.com/ryanpurchase288/week-9-project/blob/main/images/ArchitectureV1.png)

Here is the second version of my swarm architechture after adding all the neccessary features:
![swarm2](https://github.com/ryanpurchase288/week-9-project/blob/main/images/ArchitectureV2.png)

## CI Pipeline
![Pipeline](https://github.com/ryanpurchase288/week-9-project/blob/main/images/CI%20Pipeline.png)
This is the pipeline I have used for my deployment. I had written the Jenkinsfile and scripts to run the deployment as scripts made it easier to found out errors when setting up the pipeline.

For development I had to use python to develop a simple app for this deployment.
As mentioned before I used Git as the VSC and explained in detail before and same with the project planning.
For the CI Server I used Jenkins as this was new and easy to use plus it is one of the most popular and common CI servers that exist that is why I chose this to be the CI server.
For testing I used pytest using unittesting and mock testing as this allowed me to fully test my appplication code to work.
I did not include an email server as I could not get it working due to time constraints but I would have used slack to act as this.
For my artefact repositry I used Docker Hub which you can see here:
![docker](https://github.com/ryanpurchase288/week-9-project/blob/main/images/docker.PNG)

This allows me to store my images in a centralised location online which I can access anywhere which is why I chose it over nexus which would rely on my VM with it on running.
For my live enviroments I have used Google Cloud Platform using a flask framework as I deemed this to be most cost effective place to run it as I have a free credit and a 3 month free trial so this seemed the best solution for me.

Making my application deploy automatically in continous integration meaning when I make a change into my main branch then it will automatically deploy it and update the page for everyone using my application without me having to do any more configuration. This is one of the best benefits of the pipeline which is why I choose to use it for my application deployment.

Here are the console outputs and stage views to show my app in deployment:
![jenkins1](https://github.com/ryanpurchase288/week-9-project/blob/main/images/jenkins1.PNG)

![jenkins2](https://github.com/ryanpurchase288/week-9-project/blob/main/images/jenkins2.PNG)

![jenkins3](https://github.com/ryanpurchase288/week-9-project/blob/main/images/jenkinsStage.PNG)

## Tests
Here is my service 1 test coverage:
![test1](https://github.com/ryanpurchase288/week-9-project/blob/main/images/service1Test.PNG)

Here is my service 2 test coverage:
![test2](https://github.com/ryanpurchase288/week-9-project/blob/main/images/service2Test.PNG)

Here is my service 3 test coverage:
![test3](https://github.com/ryanpurchase288/week-9-project/blob/main/images/service3Test.PNG)

Here is my service 4 test coverage:
![test4](https://github.com/ryanpurchase288/week-9-project/blob/main/images/service4Test.PNG)


## Issues
I had attempted to add a database to my application as the reason why I have included erds. My database dwas running as a container but as I tried to deploy it in swarm in my deployment it would break the whole app and I would no longer be able to view my application at the IP address.

## Author
Ryan Purchase
