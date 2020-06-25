# Django project submission for final Full Stack Framework for Diploma in Software-Engineering with Code Institute(CI).

# Introduction & Project Purpose

For my final project I decided to create a live website for an actual business idea that I decided to start. Born from a natural like for candles, I decided to start a candle making business and thought this would be an ideal project idea as it evidently meant e-commerce functionality using the Django Framework. My business is actually called 0&X Candles (Naught and cross) and this project will be used to launch the business and 'go live' after the assessment process has been completed.

The site offers prospective customers everything listed within the requirements of this final project for the course. As a brief hight level overview the project incorporates some of the following features:

- Django 3.0
- HTML5, CSS3, JS and Python
- CSS Grid and Bootstrap 4
- Postrgres 
- Stripe for payments (https://stripe.com/docs/payments/checkout)
- Integration of Snipcart - A third party 'shopping cart' (https://snipcart.com/)
- Integration of SendInBlue - A third-party email/marketing platform (https://www.sendinblue.com/)
- Use of Cloudinary for marketing imagery (https://cloudinary.com/)
- User authenticated membership section & option reliant on Django User Authentication
- Deployment on PythonAnywhere(https://peggy535.pythonanywhere.com/) (The domain of the site will be changed subsequently after review and assessment)

A brief personal note: I spoke with Neil McEwan in March 2020. I believe I was meant to complete my course by the end of April 2020. As I explained to Neil, I have been suffering from the effects of several mental health illnesses since the end of last year and was kindly granted an extension to access and complete my course up until August 2020. Although I'm not asking for any special treatment and hope my project is marked and assessed in line with everyone else's I have found it challenging over the past few months to complete this project as my mental health has been significantly poor during this time.

I would also like to thank both Neil McEwan and Code Institute for their support and understanding during what has been a very turbulent and challenging period of life.

## Django 3.0 and the projects reuseable apps.

For this project Django 3.0 was used. I commenced this before the CI change of learning materials and changed to this version of the course/project towards the end of May. Thanks to CI for informing me of this, the new material is brilliant and was most welcomed!

The following table provides a breakdown of the apps and details about the specific and individual apps created.
#### Table 1 - A brief overview of the apps created in this Django project. named Candles

|App Name|Details|
|--------|--------|
|account|This app covers the various logic, views and urls needed for the member account creation and user-authentication|
|contact|This app was created to provide any user the ability to send an emails to the business owner|
|home|This app is the main landing page for the website which presents the user a brief summary of the business and navigation options|
|media|This directory is where uploaded views from the sites Django admin panel are uploaded to for the individual products|
|payment|This app integrates the use of Stripe Checkout and provides the user a 'Quick Buy' option rather than using using a cart|
|products|This app probvides the site owner the ability to store and update the businesses products|
|review|If a user decides to join 0&X Candles one of the added benefits is that they can leave member reviews. This app provides that functionality.|
|shop|This app uses the products and review apps to display a brief overview of the current 4 products available. The user can also read and view a more detailed product page for the specific item they're interested in.|

# Usability and Visual Impact

### UX Design/Suitability/Navigation and Defensive Design

Adobe XD was used to design the user-experience aspect of this project. The wireframes for desktop and tablet devices can be viewed [here](https://xd.adobe.com/view/72e5a7ad-59a4-42fd-9101-ad286d3cffe7-27b6/), the mobile design can be seen [here](https://xd.adobe.com/view/be4883b7-230c-410b-ba1e-25b0cd5dab32-eb1b/).

You will notice some differences from the initial wireframes I designed to the current site. Throughout the project it became apparent that certain sections weren't neccesary and didn't neccesarily add value to the user's experience.

Having taken inspiration from the likes of Dribble and Behance, I decided to take a slightly un-orthadox apporoach to the design of the site following a principle of 'deconstructing' the normal way of presenting certain aspects of the site. For example, the navigation menu is still available on the landing page of each section of the site yet instead of hiding this from view I've attempted to integrate it into the design and make it an actual feature. Using design research and ideas from a book called, "Making and breaking the Grid" by Timothy Samara, each landing page has 3 distinct points that attempts to draw the user's attention, in effect requesting the user to gaze and follow a shape of a right-angled triangle, allowing virtually half a page of negative space. The theory that less is more is also applied here.

To integrate the menu even further, and to make it part of the design, different colours have been used to signify and prompt the user to notice the change of section. Yellow, Blue and Black have been used as background colours.

Another aspect I wanted to achieve was to offer the user an almost guided route through the website. For example, if the user scrolls all the way to the bottom of the home landing page, it would have been negative ux experience for the user to then have to scroll back up to the fixed space menu that is included in the landing view-port of whatever device it is they are using. As such, a prompting tab is included at the bottom of the home and shop app views that allows the user to easily go forwards or backwards withoiut having to scroll back to the fixed menu for that section of the site.

I would hope the user would agree that the site is relatively easy to use. I have tested this with 3 people and they have all managed to use the features of the site with ease and stated that it was easy to navigate as well as being prompted correctly with meaningful messages that ascertain and inform the user when certain actions have been completed. Reinforcing my desire to make the user feel as though their respective journey within and throughout the site has been thought about.

For example, when an email has been sent a confirmation page with a short message is displayed, when a user registers for the first-time their name is used within a confirmatory message that their account has been created as well as confirmatory emails sent to the users registered email address further provides the user with the clear message that the design of the site has taken into account the users needs as well as affirming the promised actions of the various features.

# Layout and Visual Impact

As previously detailed, both CSS Grid and Bootstrap were employed when coding the site. Due to the design of the landing page, CSS Grid felt a natural choice. This has been made to be responsive for all device types as well as using the added benefits that Bootstrap provides. Further, the site has been tested within Google Chrome and Firefox Developer Edition on various device screens for responsive design ensuring the correct design and layout features are presented.

A specific type font was purchased for this product from called Grotesk from a typefont foundry. I felt this provided and emanated the correct feel for the product I wish to sell on the site. It's easily readable and accesible and am very happy with the style aspect of it. This is hosted within the projects static folder using ```.woff``` and ```.woff2``` file formats.

I purposefully made some additional images using Adobe Illustrator, these are some of the actual design images that will be used for the live final site and for marketing eventually. I decided to employ the use of Cloudinary for certain images. I've found the service incredible sophisticated and extremely easy to use. Particularly, when looking to resize images it reduces the need to use Adobe Photoshop. For those images that are present within the project's static file, 'image shrinker' was used to minify the file. Photographic images were sourced from www.unsplash.com.

# Code verification

Having completed the project and deployed it using [PythonAnywhere](www.pythonanywhere.com) I ran the sites code through the [W3 Markup Validation Service](https://validator.w3.org/) and unsured the css code was checked through [PurifyCSS](https://purifycss.online/) for any unused css code and [Autoprefixer CSS online](http://autoprefixer.github.io/) to add vendor prefixes to the code.

Throughout the project I used the most relevant and up to date documentation for the third-party services I employed as well as that documentation for Django 3.0, Bootstrap 4.4.

# Application Features

As detailed earlier in table 1, I created several app's in this project. Each of them having a specific and focused design.

```home app``` - This has primarily one focus, to present a landing page to the user, navigation and display information about the Candle business and it's products.

```shop, payment, review & products app's``` - The ```shop app``` uses the ```payment, review and products app's``` to populate specific areas of the different ```shop``` views.

The products app was created to seperate the concerns of the specific details of each product from the shop app which ultimately is designed to present and display those products of the e-commerce website to users. The ```products app``` is registered with the admin section of the Django project and provides the superuser with the ability to create a product and update specific feild entries for each candle from the model that is created for each product. Images for the individual product are uploaded to the ```/media/``` folder of the Candles project.

The shop app has a general overview of each candle, highlighting 40 words of the candle description. The user is able to click on a button titled, "Discover more" which allows the user to then progress to a specific page devoted to the individual candle and read the full description. It also provides the user a carousel of images for marketing purposes and the option to either add the item to the shopping cart of the project powered by snipcart, or offer the user the ability to 'Quick Buy' the product. 

Whilst researching this project I came across much research from the likes of Snipcart and Stripe indicating the growing importance of a fast, user-friendly, reliable checkout process where the user doesn't have to neccesarily 'HAVE TO become a member' or 'HAVE TO subscribe' to a companies website so that they may be able to purchase an item. Indeed, this actually holds true for myself in my own experience as a consumer. It also makes a lot of sense to have less 'potential-barriers' in the way of a potential consumer and surely it makes sense to ensure that the process of parting with ones money is as frictionless as possible.

For this 'Quick Buy' functionality, I decided to use Stripe Checkout. This seemed the most obvious choice for this type of product. It also allowed me to ensure requirement 6 (6. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe.). This allowed a lightweight footprint of code on the project and at the same time, allowed me to use what is an incredibly powerful and functional api that is perfect for the type of products being sold. As requested, the test api keys are currently being used. 

The ```review app``` provides registered members the ability to leave product reviews. As will be described later, this is one of the 'good' reasons for joining. This app is only accesible for logged-in members and is accessed through the user's dashboard. Once clicked, the user can choose the product and then leave a review. Once saved through the models.py file, this is then displayed on the individual product page after the products description.

The ```contact app``` provides any user the ability to send a message to 0&X. A simple form is created and allows the user to enter their name, email and message. A confirmation display is presented upon successfully sending the message. This employs the use of sendinblue and anymail in the Django project. Once an email is sent, an automated email template is sent to the users email to confirm that their message has been sent and to confirm that someone will be in touch with them. The actual message, is then sent to the 0&X email account with the appropriate information.

The ```account app``` was inspired from Django's User Authentication as well as the immensely helpful book, "Django 3 By Example" by Antonio Mele. I found this aspect of the project very challenging and made use of the example given in this book for user creation and authentication. I made my own modifications to the code that provided the functionality that I was aiming for as some of those provided did not seem neccesary.

The app provides the functionality needed to authenticate as well as register and update respective parts of their own profile. The individual has their own dashboard from which they can update their profile, write a review and have access to 'Member Only' candles. 

The following apps have all been used in cross-app logic with this project:

```shop/products/payment/review```
```account/review/products```
```review/products```

The site was developed to be an e-commerce website. Although the user has the ability to 'Quick Buy' a candle, they also have the option to use a shopping cart. I felt it best to use Snipcart for this. It's a brilliant service, lightweight and incredibly resilient and reliable.

The project as a whole relies on the the in-built security of Django 3.0. ```csrf-tokens``` have been used where required and design consideration's from django considered throughout.

# Software Development

Throughout the project I have structured the directories and used file names as per Django's recommendations. With this I used a Git repository to host the code and updated this accordingly when significant changes were made with commit messages that were meaningful and useful to me as the projects developer but also to others who may not have worked on the project.

### Testing 

I was able to use in part ```unittest's``` and ```coverage``` for most of the apps logic. I decided to user test the user account creation and authentication myself and went through the checklist below. I also requested two family members (Non-Developers) to go through and test all the possible scenarios and features on the site. This provded very fruitful receiving 3 sets of positive live-trials.

The unitests for the ```home, shop, products, review and contact``` apps tested the apps specific models, forms and views where applicable.

The following was a checklist I used and two family-members for live user testing:

#### User tests for live site - 'Candles' by Wayne Pegg

###### Login/Logout
- User with account can login 
- Correct forms errors displayed if either Username and/or password not included
- User is not logged in if invalid login information is given, errors provided to user
- User with account who is logged in can logout and receives a message to confirm this
- After 5 mins of user inactivity user is logged out

###### User Registration
- A new user can register with required user information given
- Correct errors are highlight when required information is invalid and/or missing for all required fields 
- A new user cannot register if invalid information is given or required information not provided
- Once a new user has registered and their account has successfully created they are presented a view that confirms this with their detailed First name.
- The new user can login and the login/logout tests still apply
-Once a new user has been registered with valid information, a template email is sent to their registered email address. This template being sent from SendInBlue with business branding and the correct welcoming message.

###### Forgotten password

- A registered user can access the forgotten password functionality on the member Login page
- Correct error message displayed to user if invalid email format provided
- With correct email entry ensure email is received in specific email inbox
- User receives notification that if their email exists, an email will be sent to them from which they can reset their email
- User is able to click on link that has been emailed to users email account which directs the user to the websites reset password page
- User is able to provide two identical passwords and reset their password to this
- If user does not provide valid passwords or inputs invalid data, the correct error messages are displayed to the user.
- Once the user has reset their password, they receive a confirmatory message detailing this and the user then must login with the new password.
- Ensure that the correct error messages are displayed if the user enters an incorrect password

###### Profile 

- The 'Edit my profile' menu tab or the Profile Admin 'Update' button directs the user to their account profile page
- The user is promoted with the correct form errors if required information is missing and/or invalid
- The user cannot update their profile with missing required information
- Once the user has updated and submitted their profile information this saves correctly and a message confirming this is displayed to the user

### Data store integration

Throughout the development phase of the project I initially used the associated default sqlite3 database supplied. When I was ready to deploy this I removed the previous associated data and then migrated this to PostgreSQL. Initially, I performed a migration with the original data stored and came accross some errors. After researching this topic on 'Stack Overflow' I realised the best option was to remove this data and then migrate. This actually worked out well as I had re-written and re-designed some of the products images and descriptions. Initially I used PG Admin 4 to checked the successful migration and correct schema was in place as it should be. Once this was in place still using a localhost server I then progressed onto the deployment phase for the project.

### Deployment - PythonAnywhere

Having previously used PythonAnywhere for my third project, I was that immpressed with the ease and reliability of it that I decided to use it again. One of the added benefits for this is that there is an option to integrate and have the platform also host a PostgreSQL server for the Django project. 

The process for deployment is well documented and was relatively easy. I was able to clone my Git repository, create a virtual environment with all the required dependencies and then integrate the PostgreSQL database having configured the projects settings file and the wsgi configuration file on PythonAnywhere.

I then re-configured the ```.env``` file for the api keys used to ensure dotenv was able to load them when needed. Finally, I configured the paths for the projects static and media folders. Once this was done the project was ready to go live at the following address (https://peggy535.pythonanywhere.com/).


