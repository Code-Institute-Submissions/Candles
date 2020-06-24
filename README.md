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

Adobe XD was used to design the user-experience aspect of this project. They can be viewed here: (https://xd.adobe.com/view/72e5a7ad-59a4-42fd-9101-ad286d3cffe7-27b6/).

Having taken inspiration from the. likes of Dribble and Behance, I decided to take a slightly un-orthadox apporoach to the design of the site following a principle of 'deconstructing' the normal way of presenting certain aspects of the site. For example, the navigation menu is still available on the landing page of each section of the site yet instead of hiding this from view I've attempted to integrate it into the design and make it an actual feature. Using design research and ideas from a book called, "Making and breaking the Grid" by Timothy Samara, each landing page has 3 distinct points that attempts to draw the user's attention, in effect requesting the user to gaze and follow a shape of a right-angled triangle, allowing virtually half a page of negative space. The theory that less is more is also applied here.

To integrate the menu even further, and to make it part of the design, different colours have been used to signify and prompt the user to notice the change of section. Yellow, Blue and Black have been used as background colours.

Another aspect I wanted to achieve was to offer the user an almost guided route through the website. For example, if the user scrolls all the way to the bottom of the home landing page, it would have been negative ux experience for the user to then have to scroll back up to the fixed space menu that is included in the landing view-port of whatever device it is they are using. As such, a prompting tab is included at the bottom of the home and shop app views that allows the user to easily go forwards or backwards withoiut having to scroll back to the fixed menu for that section of the site.


