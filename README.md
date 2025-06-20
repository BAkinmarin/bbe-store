# bbe-store

Hello and welcome to B's Beauty Emporium (BBE) eCommerce Website!

At BBE, we harness the power of God's Earth to produce luxurious, indulgent, and intensely moisturising hand-whipped body butters.

This eCommerce web application allows buyers to register an account, login, shop, and finally rate and review previous purchases.

This website was created using Django and has full CRUD functionality with an intuitive User Interface to make purchasing products simple and straightforward!

<!--![Am I Responsive Screenshot]()-->

[Live Site](https://bbe-ecommerce-store-92b8a29d8b51.herokuapp.com/)

## Table of Contents

1. [UX](#ux)
2. [Features](#features)
3. [Future Features](#future-features)
4. [Responsiveness](#responsiveness)
5. [Technologies](#technologies)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)


## UX

This e-Commerce website was created using the Five Planes of Website Design:

- [Strategy](#strategy)
### Shopper

As a shopper, I want to view available products so I can select something to purchase.

As a shopper, I want to search the website so I can quickly locate specific products.

As a shopper, I want to read reviews so I know what other shoppers think about the products.

As a shopper, I want to review items in my cart so I can make adjustments prior to checking out.

As a shopper, I want to checkout so I can have my products shipped to my desired delivery address.

As a shopper, I want to view past purchases so I can keep track of items I have purchased previously.

### Super User
 
As a super user, I want to be able to add a product to my database so it is displayed on my store.

As a super user, I want to be able to modify the list of products so I can adjsut our offerings over time.

As a super user, I want to be able to print and keep track of orders so I can prepare products for shipping.

- [Scope](scope)
- [Structure](structure)
- [Skeleton](skeleton)
- [Surface](surface)

[Back to Top](#ux)

## Features

[Back to Top](#ux)

## Responsiveness

[Back to Top](#ux)

## Technologies

<table>
  <tr>
    <td valign="top">
      <table>
        <tr>
          <td><strong>Back End</strong></td>
          <td style="text-align:right;">Django 5.1.1 <code>Django==5.1.1</code></td>
        </tr>
        <tr>
          <td><strong>Database</strong></td>
          <td style="text-align:right;">PostgreSQL <code>psycopg2==2.9.10</code></td>
        </tr>
        <tr>
          <td><strong>Authentication</strong></td>
          <td style="text-align:right;">Django Allauth <code>django-allauth==65.5.0</code></td>
        </tr>
        <tr>
          <td><strong>Frontend</strong></td>
          <td style="text-align:right;">JavaScript, JSON, HTML5, CSS3</td>
        </tr>
        <tr>
          <td><strong>Styling</strong></td>
          <td style="text-align:right;">Crispy Forms | Bootstrap4 <code>crispy-bootstrap4==2025.6</code></td>
        </tr>
        <tr>
          <td><strong>Media Storage</strong></td>
          <td style="text-align:right;">Cloudinary <code>cloudinary==1.43.0</code></td>
        </tr>
        <tr>
          <td><strong>Static Files</strong></td>
          <td style="text-align:right;">Whitenoise <code>whitenoise==6.9.0</code></td>
        </tr>
        <tr>
          <td><strong>Server</strong></td>
          <td style="text-align:right;">Gunicorn <code>gunicorn==23.0.0</code></td>
        </tr>
        <tr>
          <td><strong>Image Handling</strong></td>
          <td style="text-align:right;">Pillow <code>pillow==11.2.1</code></td>
        </tr>
        <tr>
          <td><strong>Payment Handling</strong></td>
          <td style="text-align:right;">Stripe <code>stripe==12.2.0</code></td>
        </tr>
      </table>
    </td>
    <td valign="top" style="padding-left: 20px;">
      <h3>Other Dependencies</h3>
      <ul style="list-style-type: none; padding-left: 0;">
        <li><code>sqlparse==0.5.3</code></li>
        <li><code>asgiref==3.8.1</code></li>
        <li><code>packaging==24.2</code></li>
        <li><code>setuptools==76.0.0</code></li>
        <li><code>oauthlib==3.2.2</code></li>
        <li><code>typing_extensions==4.12.2</code></li>
        <li><code>tzdata==2025.1</code></li>
        <li><code>django-summernote==0.8.20.0</code></li>
      </ul>
    </td>
  </tr>
</table>

[Back to Top](#ux)

### Tools

- [Github](https://github.com/): Used to host source code and version control.
- [VSCode](https://code.visualstudio.com/): Used as Integrated Development Environment (IDE).
- [Font Awesome](https://fontawesome.com/): Source of all the icons used in this project.
- [Coolors](https://coolors.co/): Used to generate color palette.
- [Favicon](https://favicon.io/): Used to generate the favicon used in this project.
- [Convertio](https://convertio.co/): Used to compress images used in the project for optimal load times.
- [Microsoft Copilot](https://copilot.microsoft.com/chats/RcVt8VMZjqsoZP8a7Tq5V): Used to generate images.
- [AssignmentGPT](https://assignmentgpt.ai/): Used to create the Entity Relationship Diagram (ERD).

## Packages
- [Django](https://www.djangoproject.com/) was used as the framework for the blog.
- [Allauth](https://django-allauth.readthedocs.io/) for the login authentication.
- [Pillow](https://pypi.org/project/pillow/) for rendering images.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/) for collecting and posting comments.
- [Cloudinary](https://cloudinary.com/) for hosting shopper images.
- [Gunicorn](https://gunicorn.org/) for handling the HTTP requests in production.
- [Psycopg2](https://www.psycopg.org/) for aiding communication between Django and PostgresSQL.
- [Formtools](https://django-formtools.readthedocs.io/) for additional form utilities.
- [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) for serving static files.

[Back to Top](#ux)

## Testing

### User Testing

<!--<details>
    <summary>User Navigation</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>User can view product and details without signing in</td>
                    <td>Pass</td>
                    <th>Pass</th>
                </tr>
                <tr>
                    <td>Navigation links lead to their intended pages</td>
                    <td>User is made aware via navigation links where they are on the website</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User can signup for an account to keep track of purchases</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User can navigate to home page at any time by clicking Logo or Home </td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>User Registration</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>User can create an account on the blogsite</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User can login to existing account</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User is informed once account has successfully been created</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>User Experience</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>User can click a post to view full content</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>User can comment on post</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>User can edit previous post</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>User can delete previous post</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>User receives message to confirm status of all activities on site</td>
                    <td>Pass</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>User Authentication</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Test</th>
                    <th>Expectation</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>User can create an account on the website</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User can login to existing account</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User is informed once account has successfully been created</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
                <tr>
                    <td>User is unable to leave review on unauthorised purchase</td>
                    <td>Pass</td>
                    <th>...</th>
                </tr>
            </table>
        </div>
    </div>
</details>-->

[Back to Top](#ux)

## Bugs

<details>
    <summary>Development Phase</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Bug</th>
                    <th>Action</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Favicon not rendering to Browser</td>
                    <td>Moved Favicon images from 'Root' to 'Static' folder of main project</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Virtual Environment Pushed to GitHub</td>
                    <td>Deleted using git rm command in terminal</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Duplicate base.css file causing styling issues</td>
                    <td>Deleted duplicate file</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Images not rendering as expected</td>
                    <td>Reviewed naming conventions and used relative path</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Unable to migrate to secure database</td>
                    <td>Installed correct version of psycopg</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Fatal error creating processes due to change in project name</td>
                    <td>Reset VS Code terminal settings.json</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Unable to display individual product details</td>
                    <td>Updated return url in views.py</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Sort selector on products page fixed to bottom of screen</td>
                    <td>Added missing div close tag</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Sort selector logic not working on sorting by highest and lowest rated</td>
                    <td>Renamed database field to 'rating' to avoid formatting issues</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Update functionality in shopping basket view not working</td>
                    <td>Removed href from anchor tag</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Toast not working for 'remove' functionality in basket view</td>
                    <td>Updated server return response</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Django returns 'TemplateDoesNotExist' when using Crispy Forms</td>
                    <td>Installed Django Crispy Forms template packs as separate packages</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Failed to redirect to checkout success page</td>
                    <td>Corrected indentation issue in checkout views.py</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Images not rendering on Heroku</td>
                    <td>Set DEBUG environment variable in Heroku to False</td>
                    <td>Fixed</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Deployment Phase</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Bug</th>
                    <th>Action</th>
                    <th>Outcome</th>
                </tr>
                <tr>
                    <td>Error loading Application in Heroku</td>
                    <td>Amended project name in Procfile</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Static files not served on Heroku</td>
                    <td>Wire up WhiteNoise to Django Middleware</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Error loading images on Heroku</td>
                    <td>Amended media urls</td>
                    <td>Fixed</td>
                </tr>
                <tr>
                    <td>Error loading Cloudinary files on Heroku</td>
                    <td>...</td>
                    <td>Not Fixed</td>
                </tr>
            </table>
        </div>
    </div>
</details>

[Back to Top](#ux)

## Deployment

[Back to Top](#ux)

## Credits

### [Content](#content)
- [Spencer's README](https://github.com/5pence/djangohelp/blob/main/readme.MD) was useful for setting up Django on my Windows machine.

- [Dimitris' README](https://github.com/Dimitris112/rum-away-testp4/blob/main/README.md) inspired the use of toggle view for tables.

- [Dan's README](https://github.com/DanMorriss/nialls-barbershop/blob/main/README.md) inspired some of the descriptions used in my write up.

- [Maria Pavlenko's Blog](https://www.altexsoft.com/blog/user-stories/) inspired User Stories format.

- [Dave Todaro's Article](https://ascendle.com/ideas/writing-user-stories-its-not-as-difficult-as-you-think/) inspired User Stories format.

-[Trey Hunner's Contribution](https://stackoverflow.com/questions/75495403/django-returns-templatedoesnotexist-when-using-crispy-forms) helped fix the DjangoTemplateDoesNotExist bug with Crispy Forms.

### [Media](#media)
- [A. Raouf Stack Overflow Contribution](https://stackoverflow.com/questions/21938028/how-to-get-a-favicon-to-show-up-in-my-django-app) inspired method used to fix favicon bug.

- [Blackbull256's Reddit Contribution](https://www.reddit.com/r/django/comments/kiphpl/django_deployment_heroku_server_status_500_when/) inspired method used to fix Heroku DEBUG issue.

- [vlogize Tutorial on Django / Heroku Debug = False Issues](https://www.youtube.com/watch?v=1BEgCw0acUg) further clarified resolution of deployment issues on Heroku when working with static and media files.

### [Code](#code)
- [Code Institute's Boutique Ado Walkthrough](https://github.com/Code-Institute-Solutions/Boutique-Ado) Project created in line with course content and within scope of e-Commerce Specialisation Project.

[Back to Top](#ux)

## Acknowledgements

### Family
Thankful to God for my sister, Boluwatife Akinmarin and friend, Rebecca Wilson-Kane - who both contributed immensely towards the content, reviews and ratings used in this project, as well as supporting with user testing and feedback on flow, navigation and checkout experiences.

### Spencer Barriball
My mentor who provided me with loads of tips and tricks to speed up the development of this project.

### Code Institute's Boutique-Ado Walkthrough Project
Special thanks to Code Institute's Learning Team who delivered the learning material applied in the development of this project.

[Back to Top](#ux)