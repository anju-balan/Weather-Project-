# Weather-Project

#URL to the directory where Project source code resides
https://github.com/anju-balan/Weather_Project

# URL of the deployed app
http://ec2-3-14-146-73.us-east-2.compute.amazonaws.com:5000/

A.	Problem Statement: 
To create a website for an IT consultancy company called 'Company INC' located in downtown Toronto. We have to work as a team in an Agile way to deliver the product. The project should be implemented in a continuous integration pipeline with the automated unit test cases, GitHub and Travis CI. The unit-tested end product should be deployed on the server for everyone's access.

B.	Functional requirements:
The website should have the below features, 
•	Current date and time to present in the specific format and refresh every second.
•	By using weather API, the temperature of the Toronto location is displayed in Celcius.
•	Few hyperlinks such as About us, Services, and Customers should be present.

C.	Tools Used : 
Based on our learning from this course, we have used the below tools to implement this project. 
          
D.	Web development with Flask
We have used jQuery as a scripting language to make the current DateTime stamp and developed the time interval to change every second using jQuery (JavaScript Library). With the help of HTML version 5, CSS3, and Bootstrap version 4, we designed the DateTime feature. 
We developed Ontario temperature in Celsius degrees with the help of Open Weather API documentation to create an API key. 
 
We used jQuery to collect latitude and longitude for the API to retrieve weather reports based on the current location.

E.	Unit Test with PyTest and Selenium
As we are creating the web application, we chose to use selenium to generate the test script for the unit test. Few test cases were designed to unit test all the expected components present in the application.
We integrated these tests cases with pytest and created the unit test report. To make the unit test report in HTML format, we must follow the pytest naming conventions and integrate it with the selenium. The unit test report looks like the one below.
             

F.	Deployment in AWS
We were facing multiple issues in this part as it needs to be automated using Travis CI. Below is the approach we followed to achieve this part.
1.	Create AWS Account
2.	Create a Free tier EC2 instance
3.	Download putty to interact with our EC2 instance
4.	Download puttygen to generate the key for authentication
5.	Download WinSCP to transfer the file from the local machine to the EC2 machine.
6.	Setup the security groups in AWS with full access everywhere.
7.	Link our EC2 instance with the full access network interface.
To do EC2 with Travis, we can't manually move the files from the local machine to the EC2 machine. We have to create the python script with the help of BOTO library to communicate with the EC2 instance and execute the commands in EC2 through python. Shell script will perform operations in this order :
1.	Remove the previous run logs.
2.	cd to the working directory of this project.
3.	Pull the latest code from the git.
4.	Run the webapp.py using nohup to run 24/7 without any error.
Screenshot of the end product :
 

G.	Addition Enhancement
1.	Change the background image of the website according to the weather type. E.g., a Rain image as the background if it rains.
2.	Show the last five days' average weather.
3.	Predict the next five days' weather.
4.	Change more user-friendly UI

H.	Conclusion:
This project helps us to involve more practical work as a team on the different advanced software tools from scratch. We tried out of the box and implemented new tools and techniques to do innovative work. It motivates us to learn and read new concepts and work towards building more the software development process.
