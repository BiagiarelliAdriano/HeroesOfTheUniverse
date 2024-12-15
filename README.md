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

**Registration / Log In page**
![Registration Page](https://i.ibb.co/hVVQq1L/registrationpage.png)
The registration presents simple and easily understandable web design, with a small description of the use of the page and two buttons:
-	The Register button, which opens the registration form.
-	The Log In button which opens the log in form.

![Registration Form](https://i.ibb.co/10hVMvZ/registrationform.png)

After clicking on the Register button, the Registration form will dynamically replace the Register button and Log In button, allowing the user to submit their own registration data. After a successful submit of data, the user will be automatically registered, logged in and be redirected to the home page to continue navigation.

![Login form](https://i.ibb.co/c26Y8rZ/loginform.png)

After clicking on the Log In button, the Log In form will dynamically replace the Register button and Log In button, allowing the user to submit their own log in informations data. After a successful submit of data, the user will be automatically logged in and be redirected to the home page to continue navigation.

![Empty field warning](https://i.ibb.co/jRBnXmP/registrationemptyfieldwarning.png)

If the user mistakingly leaves any form field empty, the page will warn the user of that and asks the user to fully fill out the form.
![Same name error](https://i.ibb.co/LRdSs1W/samenameerror.png)

If a user tries to register an account with the same name of an already registered account, the user will be redirected to the main registration page with an error message to either try register an account with a different name, or try to log in that account, if they own an account with that name.

![Log In error](https://i.ibb.co/vYDKcgQ/loginerror.png)
If a user tries to log in with a username that does not match any of the already registered accounts or with an invalid password, they will be redirected to the main registration page with an error message to either try again or try to register a different account with new data.

**Profile Page**
![Profile page](https://i.ibb.co/42LH4N3/profilepage.png)

This is the view of the profile page if the user owns the current profile page. This offers the possibility to edit the various elements data of the user.
- The user username:
- 
![Profile username](https://i.ibb.co/ZBYqk81/profileusername.png)

Here the user can freely edit their Username by clicking on the input, change it, then safely clicking the Save button.

![Profile successfully edited](https://i.ibb.co/7RjZXNj/profilepageupdated.png)

After successfully saving any edit the user has made in their profile page, the page reloads with the new informations and tells the user that their edits were successful.

![User's Favorite Tabletop Roleplaying game](https://i.ibb.co/gycTyqB/profilefavoritettrpg.png)

In the Favorite TTRPG section of the profile page, the user can freely edit their favorite Tabletop Roleplaying Game of choice.

![Profile about me section](https://i.ibb.co/7pGxBg7/profilepageaboutme.png)

The About Me section in the profile page represents the possibility of the user to briefly write a description of themselves and their experience with Tabletop Roleplaying Games, maybe with some fun anecdotes about their past adventures.

![User's characters displayed in the profile page](https://i.ibb.co/wsVcxwc/profilepagecharacters.png)

The My Characters section in the profile page presents the user a list of all the characters that were created by them. Here the users can take two actions:
- The user can click on the X button on the top left of each different character template to view the deletion confirmation modal.
- The user can safely click on the class image of a specific character to open in a new tab the character detail sheet of that character for editing.
- 
![Character deletion modal](https://i.ibb.co/Q6fCs3K/profilepagecharacterdeletionmodal.png)

After pressing any of the X buttons, the user is shown the character deletion modal. This explains to the user that they are about to delete one of their characters. Here, they can either choose to click on the Cancel button to safely return to their profile page without deleting their character. Or, they choose to click on the DELETE button and delete the chosen character for ever.

![Deletion message](https://i.ibb.co/1dq57qz/profilepagecharacterdeletemessage.png)

After clicking on the second DELETE button, the character will be permanently delete from the database and the profile page will reload. The confirmation message "Character '{{ character.name }}' was successfully sent to the Nine Hells!" tells the user that the deletion process was successful.

There is no known functionality for the user to delete their own account. Future updates could change this.

![Profile page of user not owned](https://i.ibb.co/Dz1vTKy/profilepagenotowned.png)

By clicking on a username on the main home page, any user can open the profile page of any user. This is the view of the profile page of an account not owned by the current user. The various data are displayed correctly and not editable. The user can still click on the various character class images to open those characters sheets to view them.

![Profile page after trying to delete a character not owned by the current user](https://i.ibb.co/dm6rbmT/profilepagedeletecharacternotowned.png)

Users are still able to click on the X buttons of characters in profile pages not of their own. This will display the deletion modal. After trying to press the DELETE button, the user will be safely redirected to their own profile page for security and an error message will be displayed, warning the user that they are not able to delete characters that they do not own.

**Make A Character page**

![Make A Character page](https://i.ibb.co/Bc7MjFY/makeacharacterpage.png)

The Make A Character page, or character creation page, displays every single piece of information a character from Dungeons & Dragons 2024 rules may need to play. Every single input is editable to the user, representing each information.
The first page presents the following features:
- Character Class Image
- Character Name
- Character Background
- Character Species
- Character Class
- Character Subclass
- Character Level
- Character Experience Points (XP)
- Character Armor Class
- Character Shield Choice
- Character Current Hit Points (HP)
- Character Maximum HP
- Character Temporary HP
- Character Spent Hit Dice
- Character Max Hit Dice
- Character Death Saves Successes
- Character Death Saves Failures
- Character Ability Scores
- Character Saving Throws
- Character Abilities Proficiencies
- Character Initiative
- Character Speed
- Character Size
- Character Passive Perception
- Character Armor Training
- Character Weapons Proficiencies
- Character Tools Proficiencies
- Character Weapons & Damage Cantrips
- Character Class Features
- Character Species Traits
- Character Feats

![Make A Character pagination buttons](https://i.ibb.co/F6jBByr/makeacharacterpageselection.png)

The Make A Character page presents two different pages. These pagination buttons can be safely pressed to change the page viewed by the user. The page will not be reloaded upon pressing either of these buttons, but instead the form will dynamically change presenting the content of the first page or the second page.

![Make A Character class image selection](https://i.ibb.co/TqvLjcy/makeacharacterclassimage.png)

Pressing on the Select Character Image button will display the radio form for the character class image that is meant to be a placehoder for the character's image. Each icon represents faithfully a class can be chosen by the Dungeons & Dragons rules. Clicking on any of the radio buttons will dynamically change the icon shown on the right to reflect the user's choice in real time.

![Make A Character second page](https://i.ibb.co/x5Xdddt/makeacharactersecondpage.png)

The second page of the Make A Character page presents the following features:
- Character Spellcasting Ability
- Character Spellcasting Modifier
- Character Spell Save Difficulty Class (DC)
- Character Spell Attack Bonus
- Character Available Spell Slots
- Character Spell List
- Character Appearance
- Character Backstory & Personality
- Character Alignment
- Character Known Languages
- Character Equipment
- Character Magic Attunements
- Character Coins

![Make A Character Spell List](https://i.ibb.co/zG2sfp9/makeacharacterspelllist.png)

The user can safely press the Spell List button to display underneath five templates representing each a different available spell for the user to fill out.
No more spells are available after the five.

![Make A Character only required field](https://i.ibb.co/zXYvB3L/makeacharacterrequiredfield.png)

The only input field that is actually required by the user to fill out to successfully create a new character, is the name. An error shows up successfully if the user tries to submit without the name.

![Make A Character Bad value error](https://i.ibb.co/QHWCdfw/makeacharacterbadvalue.png)

Users will be warned if they are trying to submit a character with bad values.

![Make A Character successful character creation](https://i.ibb.co/TRPmyW4/makeacharactersuccessfulcreationmessage.png)

After trying to save a character with correct values and filling out at least the name of the character, the page will reload, the character will be created and a success message will be displayed to let the user know of their success.
Now users can freely choose to either go to home page to view their new character enty there, access their profile page to view the character details of the newly created character, or stay in the Make A Character page to continue editing for the character.
