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
   - [**Data Models**](#data-models)
   - [**API Endpoints**](#api-endpoints)
1. [**Technologies Used**](#technologies-used)
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

Below is a diagram that provides a visual overview of the database tables for this project (created using [**_dBeaver_**](https://dbeaver.com/)):

![dBeaver database schema](docs/images/dbeaver-schema.png)

### **Data Models**

#### **User**

The User model is provided by Django AllAuth, and enabled users to create accounts with a username and password, providing validation and assigning each profle a unique primary key.

#### **Profile**

The Profile model creates a new user profile whenever a new instance of the User model is created. This is possible thanks to the 'create_profile' function within the model. Once created, users are able to update their profile name, its content, and upload a profile image.

#### **Follower**

The Follower model allows logged in Users to follow or unfollow other Users on the front-end. A 'follow' equals the creation of a new Follower instance, whereas an 'unfollow' deletes that instance from the database. A User can only have one unique Follower ID per user followed, preventing Users from being able to follow the same person multiple times.

#### **Post**

The Post model centres around what is arguably the most important part of the Creature Feature app - the ability for users to create, read, update* and delete* (\*if they are the post owner) posts. In addition to the basic expected functionality (such as title, content, image), I have added 'category' as a field, for which there are three choices. These are in line with the overall intention for this app, which is -literally- to feature creatures! I felt that users would appreciate being able to select which variety of creature it is they're featuring, and it also enables users to filter posts based on these categories.

Another custom feature of the Post model is the inclusion of the PostObjects Manager model. A currently hidden feature of the Post model is that it provides users with the ability to store posts they may want to come back to edit later before posting as drafts - this is handled by the PostObjects Manager, and the subsequent 'objects' and 'post_objects' fields. The 'status' field in Post dictates that, by default, all posts are set to 'published' and therefore will appear in any and all searches. Unfortunately at the time of deployment, this feature has not been fully implemented yet, hence being a currently hidden feature. In my Database Schema, there is a field called 'exceprt' which is no longer included in the Post model, but this comes from the same line of thinking as the 'published'/'draft statuses. While currently operating as a single image sharing site, I would like to expand on this in future to implement more blog-like qualities, and create a sort of blog/photo-sharing hybrid. Although I removed 'excerpt', I have decided to keep the PostObjects Manager and the status field where it is, so that I can begin working on this in the near future.

#### **Reaction**

The Reaction model is a custom model that looks after what I would consider to be the most unique and interesting aspect of this app - the ability to 'react' (no pun intended, but welcome all the same) to posts with one of three choices. Each choice is intentionally very cute, and deviates from what users might have come to expect, so it jumps out as a unique selling point. However, users can only select one of the three at a time, and the 'unique_together' field in the model's Meta class takes care of this. The front-end relies on the information received by the Reaction model to perform conditional rendering of the reaction elements based on the user's logged in state, whether they are the owner of the post, and of course which reaction they have chosen.

#### **Comment and LikeComment**

The Comment model enables users to create, read, update* and delete* (\*if they are the comment owners) comments on individual posts. Comments are linked to both posts and profiles, as users are able to access a user's profile by following the link provided through the comment.

The LikeComment model is more in line with what users might usually expect with a social media app like this one, and it operates in a much simpler fashion to the Reaction model. When a user creates a comment, The comment ID is created, which is linked to the post ID. When a user who does not own that comment wishes to 'like' it, the model creates a new LikeComment instance, taking the comment ID (linked to the specific post ID), and then the profile ID of the user wishing to like the comment, rather than the profile ID of the user whose comment it is. If a user wants to undo this action (ie, delete the LikeComment instance), they can click the icon again to unlike it. The front-end uses this information to conditionally render the icon used to like the comment, based on whether a user has liked it or not.

#### **Pagination**

The Creature Feature API uses pagination as a way of preventing too much data from being loaded at once (causing problems for performance). A global rule is set to limit responses from the API to 10 per page, and it will provide links to the next page of 10 results. The use of infinite scroll on the front-end loads this data so that users don't have to click a 'next' button every time they've viewed 10 pages.

The only current exception to this is in Comments. The way I have designed the front-end React app meant that using the infinite scroll component for comments under posts was causing bugs that I struggled to find a sufficient solution to, and so I have had to remove it. As such, in comments/views.py there is a custom PageNumberPagination class which sets the maximum number of comments allowed in a single page to a much higher (and currently very unlikely) number, so that user experience is not ruined by comments and posts bugging out. This is something I wish to solve in future.

### **API Endpoints**

[diagrams...?]

## **Technologies Used**

The language used to write this API is Python. Below is a list of the frameworks and libraries used to create this project, as well as other dependencies:

- Django - the Python framework used to develop this project.
- Django REST Framework - the Django toolkit that enabled the creation of this API.
- Django AllAuth - enabling user authentication and validation.
- Django Rest Auth - to provide endpoints for users to login/logout.
- ElephantSQL - to host the PostgresSQL database used by this project.
- Psychopg2 - a database adaptor that enables interaction between Python and PostgresSQL.
- Cloudinary - to host images and static files that engages seamlessly with the front- and back-end counterparts of this project.
- Pillow - an imaging library that adds image processing capabilities.
- Django Filters - to allow queryset filtering based on model fields.
- Django CORS Headers - to handle the server headers required for Cross-Origin Resource Sharing.
- Heroku - providing a platform in which to host the deployed project.
- dBeaver - a program I have relied on greatly throughout the development process to investigate the data that is being passed between my front- and back-end applications.

## **Testing**

A separate file has been created for information about testing. Please click the following link to access it: [**_TESTING.md_**](TESTING.md)

## **Deployment**

In this section I will explain the steps I took in order to deploy this project.

#### **Cloning/Forking**

If you wish to create a clone of this project to use on your local machine or virtual IDE environment such as Gitpod, first navigate to [this project's GitHub Repository](https://github.com/emmacadavra/creature-feature-drf-api), and follow [GitHub's instructions on how to clone a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). If you are using a local environment, you can enter the following command in the terminal:
`pip install -r requirements.txt`
This will install all the required libraries and packages in one go, meaning you will not have to follow the set-up steps below.

As I developed this project locally, I first created a virtual environment using the command `python -m venv .venv` - if you clone this project to use locally, you must do the same. Ensure that the virtual environment is not tracked by version control by adding it to the .gitignore file.

#### **Project Setup**

Below is a list of the steps and terminal commands I used to install the necessary libraries and packages for this project following the creation of the GitHub repository:

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
