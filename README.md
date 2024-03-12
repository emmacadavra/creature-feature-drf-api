# Creature Feature

## **Project Overview**

Creature Feature is a quirky and fun interactive photo-sharing app dedicated to our often smaller - but by no means lesser - animal companions. Although it shares its name with the famous horror/sci-fi genre of films known as 'Creature Features', the creatures featured on this platform are anything but spooky… Unless they want to be, of course! That said, despite the cutesy aesthetic this app employs, the spirit of the genre is subtly kept alive through the unusual names of the post categories users must pick from to let the world know what type of creature it is they’re featuring! The thematic combining of the _’creepy & kooky’_ with the charming & adorable provides a truly distinctive, engaging platform for users to _sink their claws into_.

The Creature Feature API is the back-end portion of the Creature Feature app, and has been developed using Django's REST Framework. The app aims to provide users with the ability to share pictures of their pets and/or favourite animals with other like-minded users, build up a profile and follow other profiles they enjoy. This API has been created to ensure that users can enjoy a smooth and seamless user experience, by providing the front-end app with the core functionality it needs.

To view the deployed API, [**_please follow this link_**](https://creature-feature-api-43ea2b93451a.herokuapp.com/).

This is the back-end repository for this project. To go to the front-end repository, [**_please follow this link_**](https://github.com/emmacadavra/creature-feature-react).

To view and explore the deployed Creature Feature front-end app, [**_please follow this link_**](https://creature-feature-react-fb85071d4bc2.herokuapp.com/).

## **Table of Contents:**

1. [**Project Overview**](#project-overview)
1. [**Project Planning**](#project-planning)
   - [**Project Aims (API)**](#project-aims-api)
   - [**User Stories**](#user-stories)
1. [**Database Schema**](#database-schema)
1. [**Data Models**](#data-models)
1. [**API Endpoints**](#api-endpoints)
1. [**Technologies Used**](#technologies-used)
   - [**Frameworks**](#frameworks)
   - [**Libraries**](#libraries)
1. [**Testing**](#testing)
1. [**Deployment**](#deployment)
1. [**Credits**](#credits)
   - [**Honourable Mentions**](#honourable-mentions)
   - [**Code and Content References**](#code-and-content-references)

## **Project Planning**

### **Project Aims (API):**

- To provide the front-end app with a robust back-end counterpart that allows communication between React/JavaScript and Python.
- To implement user authorisation through the use of Django AllAuth and Django Rest Auth, allowing users to create accounts, login and logout on the front-end
- To provide CRUD functionality to users on the front-end in relation to posts and comments:
  - Logged in users can create, edit and delete their own posts.
  - Logged in users can create, edit and delete their own comments.
  - Logged in users can choose one of three reactions to any post that is not their own, and they can change or undo these reactions at will.
  - Logged in users can like any comment that is not their own, and unlike it at will.
- To provide CRUD functionality to users on the front-end in relation to their profiles and following other profiles:
  - Logged in users can edit their own profile by uploading a profile image and amending their profile's content whenever they wish.
  - Logged in users can follow the profiles of other users, and unfollow at will.
- To provide the front-end with a number of options that allow logged in users to control the posts they see, by applying filters (such as posts by category, only showing posts by users they follow, or viewing the posts they have reacted to) or using the search bar to search for posts that use specific keywords, or are by specific profiles.
- To allow logged out users to view posts, though without access to post filters or the ability to create, edit or delete posts.

### **User Stories**

The User Stories for this project can be accessed by following this link to [**_the front-end repository’s project board_**](https://github.com/users/emmacadavra/projects/5). Further information on these User Stories an be found in the separate [**_AGILE.md document_**](https://github.com/emmacadavra/creature-feature-react/blob/main/AGILE.md), also within the front-end repository.

## **Database Schema**

Below is a diagram that provides a visual overview of the database tables for this project (created using [**_DrawSQL_**](https://drawsql.app/)):

[diagram]

### **Data Models**

#### **User**

#### **Profiles**

#### **Followers**

#### **Posts**

#### **Reactions**

#### **Comments**

#### **Like Comments**

### **API Endpoints**

[diagrams...?]

## **Technologies Used**

_"Frameworks, libraries & dependencies"_

### **Frameworks**

### **Libraries**

## **Testing**

_Link to separate TESTING.md doc, with details of both manual and automated testing as well as resolved and unresolved bugs_

## **Deployment**

#### **Cloning/Forking**

_How to download and set up project locally, and how it can be deployed - remember the following:_
_"If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
pip install -r requirements.txt
IMPORTANT - If developing locally on your device, ensure you set up/activate the virtual environment (see below) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk"_

#### **Project Setup**

- Cmd for setting up venv: python3 -m venv [your_venv_name] (source [your_venv_name]/bin/activate to activate venv)
- Follow instructions on project set up cheatsheet EXCEPT FOR:
  - pip install Pillow==8.2.0 - **USE pip install Pillow==9.3.0 INSTEAD**
- pip3 freeze --local > requirements.txt

#### **Database Setup**

- ElephantSQL

#### **Environment Variables and Settings**

#### **Cloudinary**

#### **Deployment to Heroku**

## **Credits**

### **Honourable Mentions**

- [**_Damon Kreft_**](https://github.com/damon-kreft)
- [**_Richard Wells_**](https://github.com/D0nni387)
- All of my wonderful friends who helped me populate the database/app with profiles and content!

### Code and Content References

- Entire Profiles app (model, serializer, views + urls), and IsOwnerOrReadOnly (permissions.py) taken from course content
