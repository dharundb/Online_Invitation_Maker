
# ONLINE INVITATION MAKER

Online invitation maker provides a group of works with interface environments to create an invitation for numerous occasions. 
This web application is intended to be used by anyone that wants to create an invitation for any kind of occasion one might have.
Online invitation preparation system will allow users to design and prepare their own invitation.
Users can change font style, colour, template and can prepare their own custom invitation by using one of many template options we have  provided or with a picture of their own choice as template.
We have made the web application to look visually appealing to the user by using techniques like glassmorphism.
Parts of the web application are designed to be dynamic considering the nature of our project.
It has the necessary functions to further share the invitation through mail or download it and we also provide options to the user like applying image filers to the template.
We hope you would like our work!

## Code Description
### HTML, CSS & JS

- **Welcome** - Start page.
- **Login and Signup** - Gets the user Credentials in forms.
- **Get Credentials** - Gets the occasion details from the user and stores it in the backend tables depending on the occasion.
- **Template choices** - Gets the template choice from user.
- **Stylings** - Formatting options
- **Download** - Creates a new Canvas object, writes the user's necessities in the image and lets you download the invitation.
- **Share through mail** - Gets the receiver mail ID and sends the invitation.
- **Filter options** - Editing the invitation and lets you download it.


###  Django Apps used 

- **Enter** - This app takes care of the welcome, login and signup page.
- **Details** - This app takes care of all other pages. 

        1. Occasion selection.
        2. Get Credentials
        3. Template choices
        4. Formatting
        5. Filter options for template
        6. Download & Share through mail
## Demo

🔗[Online Invitation Maker Demo](https://drive.google.com/file/d/1DFipqJCbqRNUxxm66FmZSKTwHKB3uTgv/view?usp=sharing)

## Tools Used
#### IDEs Used

![Logo](https://surveymonkey-assets.s3.amazonaws.com/survey/290106376/1176d9f5-b9e8-4e70-9c53-e7373809ba8b.png)

#### Front-End
![Logo](https://miro.medium.com/max/2560/1*l4xICbIIYlz1OTymWCoUTw.jpeg)

#### Back-End

![Logo](https://static.djangoproject.com/img/logos/django-logo-negative.png)


## Deployment

#### Django installation
```bash
    pipenv install django
```

#### Project and App creation
```bash
    django-admin startproject {project-name}
    python manage.py startapp {app-name}
```

#### Admin registration
```bash
    python manage.py createsuperuser
```

#### Run the Project (you can add a port number if you want)
```bash
    python manage.py runserver {port number}
```

#### Install SMTP
```bash
    pip install secure-smtplib
```

## Authors

- [DHARUN BHARATHI S](https://github.com/dharundb)
- [BHARATH S](https://github.com/Bharath1811)
- [MAHESH BOOPATHY M](https://github.com/Mahesh-021101)
- [SURTIK S](https://github.com/surtik48)
- [GOWTHAM S](https://github.com/jgowtham193)
- [SHASHAANK R](https://github.com/shashaank13)
