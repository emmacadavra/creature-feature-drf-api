# Creature Feature

## **Project Overview**

Creature Feature is a quirky and fun interactive photo-sharing app dedicated to our often smaller - but by no means lesser - animal companions. Although it shares its name with the famous horror/sci-fi genre of films known as 'Creature Features', the creatures featured on this platform are anything but spooky… Unless they want to be, of course! That said, despite the cutesy aesthetic this app employs, the spirit of the genre is subtly kept alive through the unusual names of the [**_post categories_**](#categories) users must pick from to let the world know what type of creature it is they’re featuring! The thematic combining of the _’creepy & kooky’_ with the charming & adorable provides a truly distinctive, engaging platform for users to _sink their claws into_.

The primary intention of this app is to provide a smooth, user-friendly platform on which registered users can create posts containing pictures of their beloved pets, and engage with posts created by other users. They can view and follow the [**_profiles_**](#profile-page) of other users whose posts they enjoy, control what they see by utilising a variety of [**_post filters_**](#post-filters), and - most importantly - interact with and comment on the posts they can see. What makes this app stand out against others of its kind are the three [**_adorable post reactions_**](#reactions) that replace ‘likes’ or the more traditional kinds of post reactions found on other social media platforms.

This is the back-end repository for this project. To go to the front-end repository, [**_please follow this link_**](https://github.com/emmacadavra/creature-feature-react).

## **Table of Contents:**

1. [**Project Overview**](#project-overview)
1. [**Project Planning**](#project-planning)
   - [**Site Aims**](#site-aims)
   - [**User Stories**](#user-stories)
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

### **Site Aims**

### **User Stories**

_Include link to GitHub board, and link to separate User Stories document for back-end OR to the front-end repo where I could combine the two_

## **Data Models**

## **API Endpoints**

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
