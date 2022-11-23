# IBM-Project-39899-1660562087
Plasma Donor Application
Team Members:
            Team Leader:MUTHULAKSHMI.S
            Team member:DEEPIKA.M                      
            Team member:KAVIPRIYA .R                
            Team member:SRILEKA.R     
Objectives:     
      ●	The main objective of this project is to provide the recipient with a donor who is in good form with no health ailments to donate blood of the corresponding blood group. This project provides quick access to donors for an immediate requirement of blood. In case of an emergency/surgery, blood procurement is always a major problem which consumes a lot of time. This helps serve the major time-lapse in which a life can be saved. Users will have the option to request the blood. Once the user requests, all the people with that blood group will be notified with an mail  
  
      ●	Blood Plasma Donations are used for slightly more specific purposes than a general blood donation. The most common uses of plasma donations include individuals who have experienced a severe trauma, burn or shock, adults or children with cancer, and people with liver or clotting factor disorders. Donated plasma can be frozen and stored for up to one year. Nearly 10,000 units of plasma are needed every day in the United States, and plasma transfusions are often lifesaving.  
  
      ●	The proposed method helps the users to check the availability of donors. A donor has to register to the website providing their details. The registered users can get the information about the donor count of each blood group. The database will have all the details such as name, email, phone number, infected status. Whenever a user requests for a particular blood group then the concerned blood group donors will receive the notification regarding the requirement. A Json code is written to store the information, to fetch the requested information in lambda.   
  
      ●	When a user request for a particular blood group an API will invoke the lambda function and the lambda function will trigger operation and fetches the information of a particular blood group donor from the dynamo-db and it will then fetch it back to the API and this API will display the information in the user interface. when a user requests for a particular blood group a request sms will be sent to the particular blood group   
     
Propesed system:
      ●	To build a web application that is capable of acting as a medium for recipients and donors of blood. The application must be deployed on Cloud Foundry.  
  
      ●	Create an API Endpoint for the model with the help of IBM Cloud Functions.  
  
      ●	An alert is to be sent using the send-grid mail  Service to all the registered users whenever a request for blood is posted.  
  
      ●	In recent days, it is noticed the increase in blood request posts on social media such as Facebook, Twitter, and Instagram. Interestingly there are many people across the world interested in donating blood when there is a need, but those donors don’t have access to know about the blood donation requests in their local area. This is because there is no platform to connect local blood donors with patients.  
  
      ●	BLOODY solves the problem and creates a communication channel through authorized clinics whenever a patient needs blood donation. It is a useful tool to find compatible blood donors who can receive blood request posts in their local area. Clinics can use this web application to maintain the blood donation activity. Collected data through this application can be used to analyze donations to requests rates in a local area to increase the awareness of people by conducting donation camps.  
  
      ●	BLOODY Application can be developed to further improve user accessibility via integrating this application with various social networks application program interfaces (APIs). Consequently, users can login and sign up using various social networks. This would increase the number of donors and enhances the process of blood donation.  

REQUIREMENT ANALYSIS  
  
     SYSTEM REQUIREMENTS  
  
           We’ll be able to work on IBM DB2, creating flask application, making an application into an docker image and deploying app in kubernetes space. Build a flask application which-will take the user inputs,update the IBMDB2 database and notify the user upon request.  
  
       HARDWAREREQUIREMENTS  
           APC with internet connective  
  
       SoftwareRequirements  
           OperatingSystem -Windows11 or 10  
           FrontEndTool - Python 3.10.5  
           IDE -VisualStudioCode  
           CodeRepository - GitHub  
           BackEndTool - IBM DB2 service on IBM  
           CloudAppDeployment Environment - kuberster with docer  
CONCLUSION  
  
       During the days of COVID-19, it is noticed the increase in blood request posts on social media such as Facebook, Twitter, and Instagram. Interestingly there are many people across the world interested in donating blood when there is a need, but those donors don’t have an access to know about the blood donation requests. This is because there is no platform to connect blood donors with the person in need. Plasma Donor App solves the problem and creates a communication channel whenever a patient needs blood. It is a useful tool to find compatible blood donors who can receive blood requests from different areas. Clinics can use this web application to maintain the blood donation activity.  
  
       Plasma Donor Application can further improve user accessibility via integrating this application with various social networks application program interfaces (APIs). Consequently, users can login and sign up using various social networks. This would increase the number of donors and enhance the process of blood donation.User interface (UI) can be improved in future to accommodate more audiences by supporting different languages across the country.  


   
  
