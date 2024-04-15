# **Creature Feature API - Testing**

## **Table of Contents (Testing):**

1. [**Testing Overview**](#testing-overview)
1. [**Testing Throughout Development**](#testing-throughout-development)
   - [**Manual Testing**](#manual-testing)
   - [**Automated Tests**](#automated-tests)
   - [**Noteworthy Bugs During Development**](#noteworthy-bugs-during-development)
1. [**Post Development Testing**](#post-development-testing)
   - [**Code Validation**](#site-validation)
   - [**Unresolved Bugs**](#unresolved-bugs)

## **Testing Overview**

Below I have documented the testing undertaken throughout development for this respository's code.

For information on front-end testing, please follow the link to this project's [**_front end respository's TESTING.md document_**](https://github.com/emmacadavra/creature-feature-react/blob/main/TESTING.md).

## **Testing Throughout Development**

### **Manual Testing**

Throughout development, I used a variety of methods to test my API code as I went along, in particular using print statements (_a LOT of print statements!_) to help me identify not only exactly what code was being passed from one place to another, but also to discover where things were going wrong if things weren't working as intended. Using a print statement on each step of the code's journey in some cases really helped me solidify my understanding about how data is passed between functions, between models and views, and so on.

Whilst I was writing the API code, it was also very rare for me to be doing so without first having run the `python3 manage.py runserver` command, so that I could see exactly how my code was being returned by the API, and identify where some errors or conflicts may arise.

As the API is largely URL based, I often tested URL paths by entering incorrect URLs, or logging out/logging in as a different user to make sure that errors were handled correctly.

When working with both the back-end and the front-end, I was always sure to have my local server running, even when the front-end was accessing the deployed API, so that I could cross reference the objects being returned in each API call with what I was expecting to receive into my React app.

### **Automated Tests**

As part of the course content provided by Code Institute, we were introduced to automated testing in Python, and I have demonstrated some of this in the posts app's 'tests.py' file. These tests were to ensure that users could create and update their own posts, but that other users who did not own that post were not able to update or delete them.

I would have liked to experiment more with automated testing in this project, but due to the scale of the project I needed to devote as much time as possible to working on the project itself. In future I plan to take the time to learn more about automated testing so that I can really understand it and appreciate its value to projects such as this one.

### **Noteworthy Bugs During Development**

As this is the largest and most complex project I have worked on to date, it goes without saying that I faced a great many bugs throughout development. Some of these were the result of using newer versions of Frameworks than I was used to, or that were being used in the CI course content, and many of them were down to not connecting models to views correctly, or adding too many/too few fields into serializers. Additionally, although I have used Django before, I was new to Django REST at the start of this project and there were many occasions on which I thought I was experiencing a bug, but it was in fact just the way that the Django REST development server us presented.

For example, when testing the Post model, I found that the post status was always set to 'Draft' first, despite the default being 'Published'. The same thing occurred with image filters, where the default is 'normal' but the first option was always '1977'. It took me a while to get used to the fact that the first option in the dropdown on the back end was just the first item in the list, and it didn't reflect what I'd set as the default.

Aside from this, below are some of the noteworthy bugs I encountered throughout the development process.

#### Post Categories

I had a tremendous amount of trouble with the post categories in the early stages of development, due to conflicting (and sometimes outdated) information available about the best way to go about it.

Originally, I had set the post categories as a separate class outside of the Post model, as 'model.TextChoices' class, with each category being declared as a single-word variable assigned to the string I wanted to display in the front-end. However, I found that this was causing the string value to be collected as the data, and the variable to be displayed to the user (the opposite of what I was trying to achieve).

I then moved the category choices inside the Post model, still as a class, and found I had the same issue. Changing the contents to sets of tuples, and changing the model type to 'model.Model' appeared to work as intended, until I began fleshing out the front-end where I realised the same thing was happening again.

I fixed this by amending the tuples to contain the same string twice, matching the value in the front- and back-end.

Eventually I realised that, due to the changes I had made, I was unable to edit any posts with the 'Facinorous Fluffballs' category as it was set to the default, but existing posts showed 'fluffy' as their category:

![Error updating existing posts with default category](docs/images/fluffy-undefined.png)

For this, I used dBeaver to access to my database and amend the post categories manually, which fixed the issue.

#### Reactions

I came across quite a few bugs when trying to get Reactions right. Originally, even though I provided the choices from the start, I followed a similar pattern to categories in that I found myself in situations where the wrong things were being pulled through to the API. Once I had fixed that, the reactions were working, but I realised I'd only included a single 'count' field in the post view, so I was unable to pull through how many of each reaction there were - only how many there were in total. To fix this, I added individual count fields to the queryset.

Another bug relating to reactions was that, when attempting to filter posts by only ones a user had reacted to, I was still getting all posts in the list, regardless of whether or not I'd reacted to them. This bug was caused by me incorrectly adding 'reactions**owner**profile' to the 'ordering_fields' in the post view, rather than the 'filterset_fields'.

Quite late into development, when testing the front-end reaction functionality, I came back to the API code to discover I had caused two more bugs relating to reactions. The first was that I was only collecting the reaction ID to send to the front-end, and it wasn't being specifically linked to the reaction type. I fixed this by adding the post serializer field 'current_user_reaction', and defining the 'get_current_user_reaction' function, which would return an object containing both the ID and the type.

Lastly, again in the view for posts, I discovered very late into development that I had forgotten to declare 'distinct=True' on each of the individual reaction counts. This caused a very peculiar bug, where a post could have 1 reaction, but if the same post had 3 comments, the reaction count in the front-end would update to reflect the same number as the comments, even though there was only 1 reaction stored in the database. Naturally this was fixed by adding this into each of the reaction type counts.

## **Post Development Testing**

### **Code Validation**

The two resources I used to validate my Python code were the VSCode extension 'Flake8', and the [**_Code Institute Python Linter_**](https://pep8ci.herokuapp.com/#).

The majority of this project's code came back without any issues, and where there were issues, they were all occasions on which a line was considered too long. However, these only occured in my main settings.py file, and some of the urls.py files. Looking into the matter, I found that it is advised not to shorted items in settings.py (especially where they have automatically been set by Django), and for some of the url files there seemed to be no way for me to cleanly shorten them.

Other than this, my code passes PEP8 guidelines.

### **Unresolved Bugs**

At this time, to the best of my knowledge, I am unaware of any unresolved bugs in the code within this repository.

Please click the following link to return to the [**_README.md_**](README.md) document.
