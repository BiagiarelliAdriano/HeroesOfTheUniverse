# Heroes Of The Universe
Live version: [Heroes Of The Universe](https://heroes-of-the-universe-d056e159be1f.herokuapp.com/)

Repository: [GitHub Repo](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse)

The app is developed by Biagiarelli Adriano.
![Landing Page](https://i.ibb.co/5rwtzkM/landingpage.png)

## About
Heroes Of The Universe is a social platform where fans of Tabletop Roleplaying Games like Dungeons & Dragons are able to create their own characters within the page and share them with other users. The main goal for this app is to offer a page to share the heroes played during the user's adventures and view what other heroes may be present in a different universe, each unique and special for all people.

## User Experience Design
### Strategy
The app is designed to be easy to use and intuitive for anyone that would like to use the platform, not only people that play Dungeons & Dragons. The main goal of the app is to offer a place to share your characters and heroes with other people and comment about their adventures. This has been achieved by the use of a simple and intuitive interface. As a final goal, the app is aimed at increasing the interaction in the Dungeons & Dragons community.
### Target Audience
The app was developed for all people that would like to share and view characters created by the users for their own adventures playing Dungeons & Dragons. The main target audience is, of course, people that play Tabletop Roleplaying games on a regular basis, but anyone can freely create their own characters and share their ideas and adventures.
### User stories
I started out by creating a Google Document as a draft for my user stories. Some of these do not reflect the final user stories, as their are part of the draft. If interested, you can find the Google Document [here](https://docs.google.com/document/d/14HGU-_M8eFG6tbEmyOQRU3fcUhpdaqVkLYOh1duqaIM/edit?usp=sharing).


|Issue ID        |User story                          |Acceptance Criterias    | Label |
|----------------|-------------------------------|-----------------------------|-----|
|[#1](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/1)|As a **site visitor** I can **interact with the title "Heroes Of The Universe"** so that **I can access the Home button and the Register / Log In button**.| - The landing page shows only the title "Heroes Of The Universe", enticing the visitor to click on it. - Clicking on it reveals two buttons: "Home" and "Register / Log In". -   If the visitor is already logged in, instead of rendering the landing page, the home page will be rendered.           | Must-Have |
|[#2](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/2)          |As a **site visitor** I can **register an account** so that **I can interact with other user's posts and create my characters**.|-   The Register page contains fields for name, password and favorite TTRPG. -   Submitting the form creates the account and logs the user in automatically. -   After login, the user is redirected to the Home page.| Must-Have |
|[#3](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/3)          |As a **site user** I can **log in** so that **I can access my account and its features**.|-   The Log In page has fields for the username and password. -   Submitting the correct credentials logs the user into their account. -   After logging in, the user is redirected to the Home page. -   Incorrect credentials show an error message.|Must-Have |
| [#4](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/4) | As a **site user** I can **log out** so that **I can end my session securely**. | -   Clicking the "Log Out" button logs the user out of their account. -   After logging out, the user is redirected to the Home page as a site visitor. |Must-Have |
| [#5](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/5) | As a **site visitor** I can **browse character posts without needing to register** so that **I can explore what the platform offers**. | -   The Home page displays a list of characters shared by users, each represented by an image. -   The user can scroll to see more posts.|Must-Have |
| [#6](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/6) | As a **site user** I can **click on the image for a character** so that **I can view that character's full informations**. | -   The user can click on the image of a character posted. -   Clicking on the image redirects the user to that character's sheet. -   If the user is not the owner of the post, they will not be able to edit the character sheet.|Must-Have |
| [#7](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/7) | As a **site user** I can **like character posts** so that **I can show appreciation for them**. | -   Clicking the Like button increases the like count of the post. -   Liking a post is stored in the user data to prevent multiple likes from the same user to the same post.| Won't-Have|
| [#8](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/8) | As a **site user** I can **comment on character posts** so that **I can share my thoughts about them**. | -   Clicking the Comment button reveals a comment section to the right of the character image. -   The comment section includes a text field for adding comments and a list of existing comments. -   Submitting a comment updates the list in real-time.| Could-Have |
| [#9](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/9) | As a **visitor/site user** I can **search for profiles or filter posts** so that **I can quickly find what I'm looking for**. | -   The Home page includes a search bar. -   Typing a username and submitting it navigates to that user's profile. -   Filters allow narrowing down posts by tags or keywords. -   Failing to find a user or post shows a message saying "No User/Character found".| Won't-Have |
| [#10](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/10) | As a **site user** I can **update my profile informations** so that **I can personalize my account**. | -   The user can change their profile name, favorite TTRPG and description through text input fields. -   Submitting the changes updates the user profile immediately.| Must-Have |
| [#11](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/11) | As a **site user** I can **view the characters I've created in my Profile page** so that **I can easily access them**. | -   The Profile page lists created characters by that user in order of recency, each with image and name. -   Clicking on a character opens the detailed character sheet for that character for editing.| Must-Have |
| [#12](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/12) | As a **site user** I can **create a new character** so that **I can share it on the platform**. | -   The Make A Character page includes a form equal to the new 2024 character sheet provided by Wizards of the Coast. -   Characters submitted saves the character to the user profile and shares it on the Home page. -   Characters can be chosen from the Profile page if a User would like to edit them or delete them.| Must-Have |
| [#13](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/13) | As a **site user** I can **freely edit or delete a character sheet** so that **I can customize my characters or delete one of my characters**. | -   All fields on the character sheet are editable, except for titles of fields. -   Changes to the sheet are saved in real-time or upon submitting. -   Accessing a previously created character opens the sheet for editing. -   Clicking on the Delete button makes an alert show up, warning the user before committing to the character deletion. -   Clicking Delete again deletes that character.| Must-Have |
| [#14](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/14) | As a **user** I can **navigate between pages using the navigation bar** so that **I can quickly access different features**. | -   The navigation bar is always visible and consistent across all pages. -   For a visitor, it includes links to the Home and to Register / Log In. -   For a site user, it includes links to the Home, Profile, Make A Character and Log Out. -   Clicking a link takes the user to the corresponding page.| Must-Have |
| [#15](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/15) | As a **site admin** I can **create, read, update and delete posts** so that **I can manage my platform content**. | -   Given a logged in user, they can create a character. -   Given a logged in user, they can read a character sheet. -   Given a logged in user, they can update a character sheet. -   Given a logged in user, they can delete a character sheet.| Must-Have |
| [#16](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/16) | As a **site admin** I can **approve comments** so that **I can filter out objectionable comments**. | -   Given a logged in user, thy can approve a comment. -   Given a logged in user, they can disapprove a comment.| Should-Have |
| [#17](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/17) | As a **site user** I can **click on the "To Top" button or "Feedback" button** so that **I can either return to the top of the current page or access the Feedback page**. | -   The Footer is always visible and consistent across all pages. -   Clicking on The Top button loads the current page so that the user can return to the top of the page. -   Clicking on the Feedback button loads the Feedback page for the user.| Must-Have |
| [#18](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/18) | As a **site user** I can **compile a form** so that **I can provide feedback to the site admin**. | -   Leaving any input field blank will provide an error message. | Could-Have |
| [#19](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/19) | As a **site admin** I can **store feedback forms in the database** so that **I can review them**. |  | Should-Have |
| [#20](https://github.com/BiagiarelliAdriano/HeroesOfTheUniverse/issues/20) | As a **site admin** I can **mark feedback forms as "read"** so that **I can see how many I still need to process**. |  | Should-Have |

Most of the functionalities described in these User Stories were actually implemented and are present in the final project. The User Stories marked as Won't Have are the functionalities that were not implemented due to a lack of time.

## Technologies used

 - ### Languages:
	 - [Python 3.12.2](https://www.python.org/downloads/release/python-3122/): the primary language used to develop the server-side of the website.
	 - [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
	 - [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
	 - [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS): the styling language used to style the website.
- ### Framework:
	- [Django](https://www.djangoproject.com/): python framework used to create all the logic.
- ### Database:
	- [SQLite](https://www.sqlite.org/): was used as a development database.
- ### Other tools:
	- [Git](https://git-scm.com/): the version control system used to manage the code.
	- [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
	- [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
	- [Spycopg2](https://peps.python.org/pep-0249/): the database driver used to connect to the database.
	- [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
	- [Heroku](https://www.heroku.com/): the cloud platform used to host the website.
	- [GitHub](https://github.com/): used to host the website's source code.
	- [CodeInstituteIDE](https://codeinstitute-ide.net/workspaces): the IDE used to develop the website.
	- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
	- [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.
	- [StackEdit](https://stackedit.io/): was used to write markdown code for the README file.
	- [Coolors](https://coolors.co/): was used to make a color palette for the website.
	- [Wallpaperaccess](https://wallpaperaccess.com/): was used to search the landing background image.
	- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
	- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
	- [JShint](https://jshint.com/): was used to validate JS code for the website.
	- [Heroku PEP8](https://pep8ci.herokuapp.com/#): was used to validate Python code for the website.
	- [MockFlow](https://mockflow.com/): was used for wireframes design templates and project structure.
	- [Flaticon](https://www.flaticon.com/): was used to get the favicon for the website tab icon.
	- [OwlbearRodeo](https://www.owlbear.rodeo/): used for character classes images.
	- [Google Fonts](https://fonts.google.com/): was used for the chosen font throughout the page.

## Features
Heroes Of The Universe application has the following pages:
- landing page
- home page
- registration / login page
- feedback page
- profile page
- make a character page
- character details page

A user visitor that enters the website without being logged in a user profile will have access to the following pages:
- landing page
- home page
- registration / login page
- feedback page

A user registered and logged in a user profile will have access to all of the website pages.
- The first page a visitor will view is the landing page.
![Landing Page](https://i.ibb.co/5rwtzkM/landingpage.png)

After clicking on the title "Heroes Of The Universe", the user will have access to two new buttons: the "Home" button and the "Register / Log In" button.
![Landing page after clicking the title button](https://i.ibb.co/pZbsQ9Q/landingpageafterclickingtitle.png)

After clicking on either one of the two buttons, the user will have access to the main page.

- Each page has a navbar and a footer

**Navbar**
![Navbar](https://i.ibb.co/WKtdG98/navbar.png)
Navbar has the following links:
- home page
- profile page
- make a character page
- register / log in page

The title on the top left of the Navigation bar can also function as a link to return to the home page.
The simplistic design of the navbar is based on the decision to make the use of the webapp easy and understandable for any user.
When the user is logged in, the navbar looks as follows.
![Navbar as logged in user](https://i.ibb.co/8gCqyQK/navbarloggedin.png)

The only noticeable difference is the change of the Register / Log In button into the Log Out button, which users can safely press to log out of their user account and return to the home page.
The Navigation bar has the following buttons:
- Heroes Of The Universe (which leads to the main home)
- Home (which is the easier way to return to the main home)
- Profile (which leads to the user profile page)
- Make A Character (which leads to the character form to create a new character)
- Register / Log In (which leads to the registration or log in page)
- Log Out (which logs out the user from their current account and renders the main home)

**Footer**
![Footer](https://i.ibb.co/mcnWtY9/footer.png)

The Footer is consistent throughout the entire website and always has the same functionalities.
Footer has the following functionalities:
- To Top button: the user can click on this button when they find themselves at the bottom of a certain page after scrolling to be smoothly brought back to the top of the current page without needing to reload the page.
- Feedback button: opens in a new tab the Feedback application.
- Credits: simple text that works as fictious copyright claimer.

**Home page**
![Home Page view](https://i.ibb.co/ZVNJ0p5/homepage.png)
The Home Page welcomes users with an interesting background that inspires players of tabletop roleplaying games with the triangular pattern and the sword icon. This was done with the following CSS code:

    body {
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #4B3C31;
    font-family: 'Macondo', sans-serif;
    padding: 0;
    box-sizing: border-box;
    background-image: linear-gradient(45deg, transparent 25%, rgba(0, 0, 0, 0.1) 25%),
					  linear-gradient(-45deg, transparent 25%, rgba(0, 0, 0, 0.1) 25%),
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100' height='100' viewBox='0 0 100 100'%3E%3Ctext x='0' y='50' font-size='30' fill='%23D4AF37' fill-opacity='0.2' font-family='Arial'%3E⚔️%3C/text%3E%3C/svg%3E");
    background-size: 150px  150px, 150px  150px, 150px  150px;
    background-repeat: repeat, repeat, repeat;
    background-position: 0  0, 0  0, -31px  1px;
    }
The Home Page also directly starts showing the user the latest character created by the community. Scrolling will display all the different characters.
![Character template](https://i.ibb.co/C6cpGG0/charactertemplate.png)
All characters are displayed with the following template that offers the user various possibility of interactions.
- The user can safely click on the user name at the top of the character template, and opening in a new tab will be the profile page of that specific user.
- The user can safely click on the class image displayed in the center of the character template, and opening in a new tab will be the character sheet of that specific character to view.
- Under the character class image is that character's name.
- The user can click on the Add Comment button to open the Comment Section of that specific character.
![Character template with comment section open](https://i.ibb.co/R4MwCgj/charactertemplatecommentsectionopen.png)
- Once the user has clicked on the Add Comment button, the Comment section for that character will be displayed and the user can view the comments published for that character, with specifics informations about each comment. Commenter name, comment content and time of comment posting.
- A warming message tells the user that if they want to leave a comment, they will need to log in first.
- Clicking on the Add Comment button again will close the specific Comment section if it was open.
![Character template with comment section open while user is logged in](https://i.ibb.co/jyXNyY5/charactertemplatecommentsectionopenloggedin.png)
- If the user is logged in a registered account, the Comment form will be displayed.
- A visible warning lets users know that the functionality to be able to edit or delete comments is not yet available to users, so they'll need to think thoroughly before leaving a comment.
- The comment editing and deleting functionality was planned but was not able to be implemented due to lack of time.
