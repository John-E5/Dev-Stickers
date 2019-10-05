# Dev Stickers

[![Build Status](https://travis-ci.org/John-E5/Dev-Stickers.svg?branch=master)](https://travis-ci.org/John-E5/Dev-Stickers)


Forth milestone project for code institute full stack developer course, Full Stack Frameworks section.
This is an E-commerce and Blog web app for Stories and sales of Developer Stickers.
The app consists of a Landing, Registration, Login, Blog, Sticker Shop, Cart and checkout pages
Which allows users to Read blog posts about developer stickers and buy stickers related to software development.




## UX
This app was developed to allow users to read blog posts about stickers and buy stickers in  a hex format.

### Style
For this app i decided to use bootstrap 4 framework for the front end and the bootswatch superhero theme adding custom css styles to override values where needed.

### User Stories
As a User, Developer I would like to:
* Read about stickers.
* Be able to see stickers available.
* Add products to cart.
* Checkout securely.


### Mock-Up

1. [Desktop/Tablet](https://github.com/John-E5/Dev-Stickers/blob/master/project_media/mockups/dev-stickers-mockup.png)


### Project Management

For this project [Git Kraken/GloBoards](https://www.gitkraken.com/) was used as a task/issue tracker board which is synced
to the project repo on github.
Sections included - issues, to Do, in Progress, completed, bugs.

#### Usage

* When starting the project:
    1. Create cards
    2. Add descriptions
    3. Add assignee
    4. Add labels
    5. Add tasks
    6. Add files and comments where needed

* During the Project:
    1. Move card from ToDo to in Progress
    2. Check card for required tasks
    3. Complete task and tick off list
    4. Once all tasks completed move card to be completed and close issue

##### Screenshots for reference:

1. ![GitKraken](https://github.com/John-E5/Dev-Stickers/blob/master/project_media/glo_boards/gitKraken-1-dev-stick.png)
2. ![GitKraken](https://github.com/John-E5/Dev-Stickers/blob/master/project_media/glo_boards/gitkraken-4.png)
3. ![Glo-Board-1](https://github.com/John-E5/Dev-Stickers/blob/master/project_media/glo_boards/dev_stickers_glo_1.png)
4. ![Glo-Board-2](https://github.com/John-E5/Dev-Stickers/blob/master/project_media/glo_boards/glo-board-2-dev-stick.png)
5. ![Glo-Board-3](https://github.com/John-E5/Dev-Stickers/blob/master/project_media/glo_boards/glo-board4.png)

## Database Schema
For this app i decided to use postgreSQL for this project,
The app only required 4 tables Post and Order, OrderLineItem, Sticker which hold a relationship via foreign key to user id.

![database](https://github.com/John-E5/Dev-Stickers/blob/master/my_project_db.png)  
 

## Features

### Desktop/Tablet View

#### Home/Landing Page
The home page consists of a main title of the app with registration and login buttons underneath.
Then there is a hero section with the main site title in a jumbotron.
There are then 3 sections showing the mewest stickers, latest blog posts and customer reviews.
The bottom of the page has a basic footer with social icons.

#### Registration Page
The registration page consists of a form with 4 fields and a submit button:
* Username
* Email - with validation
* Password
* Confirm Password

#### Login Page
The login page consists of a form with 2 fields and a submit button:

* Username or Email - with validation
* Password - with validation

#### Blog Posts Page
The Blog page shows a list of blog posts with intros and read more links , which link to individual posts details

#### Blog Post Page
The post detail page shows the full content of the selected blog post

#### Shop page
The shop page shows a list of stickers available for purchase with price and option to add quantity.

#### Cart page
The cart page shows the products added to the cart for the user to purchase or amend the quantity, It also has a checkout button and total order value

#### Checkout page
The checkout page requires the user to be registered and logged in to complete payment it shows order total with fields for shipping/billing and card details to be entered with submit payment button


##### Dropdown Navigation Links

* Blog
* Shop
* Register
* Login
* Cart


### Features Left to Implement
- Improve profile page
- Fix search results page to show error for wrong search
- Improve tests and coverage

## Technologies Used

For this project the following Technologies were used:
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - The project uses **HTML5** to structure the content in line with modern semantic html5.

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#CSS_3)
    - The project uses **CSS3** to style the html content.

- [Bootstrap 4](https://getbootstrap.com/)
    - The project uses **Bootstrap 4** as the frontend framework for this app
 
- [Bootswatch](https://bootswatch.com/)
    - The project uses **Bootswatch** as the bootstrap theme for this app

- [Python](https://www.python.org/)
    - The project uses **Python3**

- [Django](https://www.djangoproject.com/)
    - The project uses **DJANGO** as the Fullstack framework for this app

- [POSTGRESQL](https://www.postgresql.org/)
    - The project uses **PostgreSQL** as the database for this app

- [PYTEST](https://docs.pytest.org/en/latest/)
    - The project uses **Pytest** as the testing framework for this app

- [HEROKU](https://www.heroku.com/)
    - The project uses **Heroku** for the deployment of this app

- [Mockflow](https://mockflow.com/)
    - The project used **Mockflow** for creating the mock-ups.

- [Git Github](https://github.com/)
    - The project uses **Git Github** for source control management.

- [Git Kraken/Glo Boards](https://www.gitkraken.com/)
    - The project used **Git Kraken/Glo Boards** for project and task management.

- [Saljs](https://mciastek.github.io/sal/)
    - The project uses **SalJs** to control scrolling and animation features.

- [PYCHARM](https://www.jetbrains.com/pycharm/)
    - I used **PyCharm** as the IDE of choice for the development of this app

- [TravisCI](https://travis-ci.org/)
    - I used **TravisCI** for deployment testing
    
- [AWS S3](https://aws.amazon.com/)
    - I used **AWS S3** for static file hosting
## Testing

### Unit Tests
Pytest and Pytest-django was used for unit testing this app,
I tested the views for the correct 200 responses of each app with also then testing some form elements
i used pytest-cov for tracking test coverage.
Travis CI is used for testing before deployment

### Manual Testing

To manually test this app go to:
####
    Home page
    1. Go to home page
    2. scroll down to see the sections  and scroll animations

   
####
    Registration page
    1. Go to register page
    2. Fill in the form
    3. Leave out some elements to see validation checks

####
    Login page
    1. Go to login page
    2. Try to add incorrect data and see validation
    3. See messsages for incorrect actions and when successful

   
####
    Blog Posts page
    1. Click Blog link in Nav
    2. See List of Blog Posts
    3. Click read more link to go to Blog Post Page

####
    Blog Post page
    1. See blog post rendered with full content
    2. See views details
   
   
####
    Shop page
    1. Click Shop Nav link
    2. See list of stickers
    3. Add desired quantity
    4. Click add to add products to cart
   
   
####
    Cart page
    1. Click Cart Nav link
    2. See list of stickers added for purchase
    3. Add new quantity and click amend to see values updated
    4. Click Checkout

####
    Checkout page
    1. Click Checkout button on cart page
    2. Fill out form with personal details
    3. Use 4242424242424242 as the credit card number to do a test purchase
    4. Click Submit payment button and see completed payment

####
    Profile Page
    1. Click profile in nav
    2. See user email address

####
    Logout
    1. Click logout to be logged out  
Testing for this project was done with several browsers and devices.

#### Browsers

##### Mobile
- Firefox
- Chrome
- Safari
- Opera

##### Desktop
- Firefox
- Chrome
- Opera
- Edge

#### Devices
- Hp Laptop
- Lenovo Laptop
- Huawei Nexus 6P android phone
- Samsung Galaxy Tab 4
- Samsung Galaxy J3
- Iphone 6s
- Iphone 7
- Ipad AIR

Firefox developer edition and chrome dev-tools were used during development and for manual testing of the site responsiveness
The devices and browsers listed above were used to test the app on different screen sizes and devices.

## Deployment
This app is Deployed on Heroku:  https://devstickers.herokuapp.com/

### To run this app locally

####
    * Clone the repo
    * Set up your virtual environment
    * In the repo root run pip3 install -r requirements.txt to install all the projects dependencies
    * Open the terminal and run python3 manage.py runserver
    * Then open 127.0.0.1 in your browser to view the running app

### To deploy to heroku
####
    * Clone the repo
    * Set up your virtual environment
    * In the repo root run pip3 install -r requirements.txt to install all the projects dependencies
   
    * In the terminal run heroku login to log into your heroku account
    * Then in terminal:
        * Add app to heroku
            - heroku create app <dev-stickers>

        * Add postgres to heroku
            - heroku addons:add heroku-postgresql:dev

        * Go to heroku.com and Add config/env vars
            - DATABASE_URL
            - Secret_key
            - AWS_ACCESS_KEY_ID
            - AWS_SECRET_ACCESS_KEY
            - STRIPE_PUBLISHABLE
            - STRIPE_SECRET
             
        * Commit and the push the changes to heroku
            - git push heroku master
       
       
## Credits
* Code Institute
* Maranatha Ilesanmi mentor