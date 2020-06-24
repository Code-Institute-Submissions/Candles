#Django Candle e-Commerce site for UK company 0&X.
#Django project submission for final Full Stack Framework for Diploma in Software-Engineering with Code Institute(CI).

#Introduction

For my final project I decided to create a live website for an actual business idea that I decided to start. Born from a natural like for candles, I decided to start a candle making business and thought this would be an ideal project idea as it evidently meant e-commerce functionality using the Django Framework. My business is actually called 0&X Candles (Naught and cross) and this project will be used to launch the business and 'go live' after the assessment process has been completed.

The site offers prospective customers everything listed within the requirements of this final project for the course. As a brief hight level overview the project incorporates some of the following features:

- Django 3.0
- HTML5, CSS3, JS and Python
- CSS Grid and Bootstrap 4
- Postrgres 
- Stripe for payments
- Integration of Snipcart - a third party 'shopping cart'
- Integration of SendInBlue - A third-party email/marketing platform
- User authenticated membership section & option reliant on Django User Authentication
- Deployment on PythonAnywhere(https://peggy535.pythonanywhere.com/) (The domain of the site will be changed subsequently after review and assessment)

##Django 3.0 and the projects reuseable apps.

For this project Django 3.0 was used. I commenced this before the CI change of learning materials and changed to this version of the course/project towards the end of May. Thanks to CI for informing me of this, the new material is brilliant and was most welcomed!

The following table provides a breakdown of the apps and details about the specific and individual apps created

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

Adobe XD was used to design the user-experience aspect of this project. They can be viewed here: (https://xd.adobe.com/view/72e5a7ad-59a4-42fd-9101-ad286d3cffe7-27b6/).

Having taken inspiration from the likes of Dribble and Behance, I decided to take a slightly un-orthadox apporoach to the design of the site following a principle of 'deconstructing' the normal way of presenting certain aspects of the site. For example, the navigation menu is still available on the landing page of each section of the site yet instead of hiding this from view I've attempted to integrate it into the design and make it an actual feature. Using design research and ideas from a book called, "Making and breaking the Grid" by Timothy Samara, each landing page has 3 distinct points that attempts to draw the user's attention, in effect requesting the user to gaze and follow a shape of a right-angled triangle, allowing virtually half a page of negative space. The theory that less is more is also applied here.

To integrate the menu even further, and to make it part of the design, different colours have been used to signify and prompt the user to notice the change of section. Yellow, Blue and Black have been used as background colours.

Another aspect I wanted to achieve was to offer the user an almost guided route through the website. For example, if the user scrolls all the way to the bottom of the home landing page, it would have been negative ux experience for the user to then have to scroll back up to the fixed space menu that is included in the landing view-port of whatever device it is they are using. As such, a prompting tab is included at the bottom of the home and shop app views that allows the user to easily go forwards or backwards withoiut having to scroll back to the fixed menu for that section of the site.

I would hope the user would agree that the site is relatively easy to use. I have tested this with 3 people and they have all managed to use the features of the site with ease and stated that it was easy to navigate as well as being prompted correctly with meaningful messages that ascertain and inform the user when certain actions have been completed. Reinforcing my desire to make the user feel as though their respective journey within and throughout the site has been thought about.

For example, when an email has been sent a confirmation page with a short message is displayed, when a user registers for the first-time their name is used within a confirmatory message that their account has been created as well as confirmatory emails sent to the users registered email address further provides the user with the clear message that the design of the site has taken into account the users needs as well as affirming the promised actions of the various features.

# Layout and Visual Impact

As previously detailed, both CSS Grid and Bootstrap were employed when coding the site. Due to the design of the landing page, CSS Grid felt a natural choice. This has been made to be responsive for all device types as well as using the added benefits that Bootstrap provides.

A specific type font was purchased for this product from called Grotesk. I felt this provided and emanated the correct feel for the product I wish to sell on the site. It's easily readable and accesible and am very happy with the style aspect of it.

I purposefully made some additional images using Adobe Illustrator, these are some of the actual design images that will be used for the live final site and for marketing eventually. I decided to employ the use of Cloudinary for certain images. I've found the service incredible sophisticated and extremely easy to use. Particularly, when looking to resize images it reduces the need to rezie images using Adobe Photoshop. For those images that are present within the project's static file, 'image shrinker' was used to minify the file.
