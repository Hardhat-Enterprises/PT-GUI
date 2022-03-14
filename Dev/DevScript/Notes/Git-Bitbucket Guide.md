# Introduction to Git and Bitbucket
___

This write-up will be covering how to use Git and Bitbucket for the purposes of this project. Note that Git is very extensive and this guide should allow you to contribute to the project without any prior Git experience.

The guide covers the following:
1. How to contribute to the Bitbucket repository.
2. How to use a Terminal Git environment.
3. How to use a GUI Git environment (Sourcetree).

Additionally, [this](https://i.redd.it/8341g68g1v7y.png) diagram shows the key terminology that Git uses. Try to become familiar with this as it will help a lot with your understanding of this document.

Note: I am by no means a "Git Guru", I still have a lot to learn myself. This guide was made to try and keep things as simple and as easy for all to contribute to this project. It is important that everyone adds their own contributions to the Bitbucket repository as it tracks the history of who uploaded/changed/removed what. This is used as evidence for the reflection assessments to show that you have contributed what you claim to.

If there are any changes you wish to make to this document that you believe would be beneficial to others, please feel free to add them.

<br>

## 1 Forking the Repository
___

### 1.1 Bitbucket fork
Simply put, a **fork** is a "your version" of a given repository. This is used for version control which allows you to make changes and create a **pull request**, which the repository owner/admin can view and approve changes.

To fork a repository:
1. Navigate to the repository on Bitbucket.
2. On the left-hand toolbar; click the **Create fork** button.
3. Change the repository name if you wish, otherwise leave everything at default and hit the **Fork repository** button.
4. You will now have a personal copy of the repository. This will be used by you to make changes (either additions, modifications or deletions) and a repository administrator can view and approve the changes when you create a pull request.

### 1.2 Cloning the fork
As is discussed in sections 2 and 3 for the respective Git environments, you will be cloning the repository in order to add/modify/remove content. Make sure you clone your fork of the repository and **NOT** the original repository.

### 1.3 Submitting your changes
To submit your changes for review, you will need to create a pull request. This can be done as follows:
1. Follow any of the two Git Environment sections (2 or 3).
2. Once you have pushed your changes to your own fork of the repository, navigate to the Bitbucket website.
3. Once there, navigate to your fork of the repository.
4. On the left hand side, you will see a button labelled **Create pull request**; click it.
5. Select "**master**" for both the source and destination branches (unless you specifically created a new branch for development, in which case you probably know what you're doing) and hit the **continue** button.
6. There will now be a page with the following information to fill out:
```
Title: [This should be a short summary of the pull request; E.g. Updated README.md of master branch]
Description: [Assuming you used good commit messages, the description can be a list of the commit messages]
Reviewers: [Leave blank]
```
7. Once everything is filled out, hit the **Create** button.
8. Now its up to someone else to view the changes and merge them into the original repository.

<br>

## 2 Git Environment - Terminal
___

### 2.1 Login to Git
In order to push any changes, you will need to login to the Git client. This is done using the following two commands:
```
git config --global user.email [yourEmail@deakin.edu.au]
```
```
git config --global user.name [Your Name]
```
<br>

### 2.2 Cloning the repository
To clone this repository to a local machine, execute the following command in the directory you wish to clone it to:
```
git clone [Your-forked-repository-URL.git]
```
<br>

### 2.3 Modifying and creating new files
After cloning the repository, all changes and new files that have **NOT** been committed can be viewed using:
```
git status 
```

To stage (add) a new file, such as "*program.py*", use the following:
```
git add program.py
```

You can also stage all changed files using:
```
git add .
```
<br>

### 2.4 Committing changes
Before uploading your files to the Bitbucket, you first have to "commit" the changes you have staged. This can be done simply by using:
```
git commit -am [commit message here]
```
This command commits all tracked files to the Git history (changes can be seen by all) with the specified message. The message should be short and to the point, for example; "*Fixed typo in README.md*".
<br>

### 2.5 Deploying your changes
Changes that have been committed can be pushed to the origin simply with the command:
```
git push
```
This will likely ask for your Bitbucket password.
<br>

### 2.6 Fetching changes
If you have any errors when pushing changes, it will likely be because your local copy of the repository is out of sync with the remote one. 

The simplest way to fetch changes is by using:
```
git pull
```
This will get and merge the latest changes from the remote repository.
<br>
<br>

## 3 Git Environment - Sourcetree
___

### 3.1 Cloning the repository
In Sourcetree, go to **File > Clone/New...** (CTRL + N):
* Input `[Your-forked-repository-URL.Git]` as the source path/URL.
* Select a location on your computer using the **Browse** button to save the repository. This will need to be accessible as you will need to add new files to the folder.
* Choose any name for the repository as that is the local name, e.g. "*Network Recovery Tools*".
* Hit the **Clone** button. 
<br>

### 3.2 Modifying and adding files
Any changes to existing files or addition of new files anywhere within the local repository folder will show up in the **WORKSPACE > File Status** tab on the left-hand side of Sourcetree.

There are two panes split horizontally, one titled "*Staged files*" and the other "*Unstaged files*". You can select any of the unstaged files and view additions, deletions and creations that will be visible in the history if pushed.

To stage the files, simply press the **Stage All** button. If you only wish to stage certain files, select them and press the **Stage Selected** button.
<br>

### 3.3 Committing and pushing changes
To commit changes on Sourcetree, make sure there is at least one staged file; i.e. at least something has been changed.

After staging your relevant files, at the bottom of Sourcetree's window, enter your commit message. The message should be short and to the point, for example; "*Fixed typo in README.md*".

Then tick the box reading "*Push changes immediately to origin/master*". Lastly, press the **Commit** button to push the changes.

Note: You can commit the changes and push them later using the **Push** button in the top toolbar of Sourcetree.
<br>

### 3.4 Fetching changes
To sync your local repository with the remote one, press the **Pull** button in the top toolbar of Sourcetree.

Leave the dialog box's values at default and hit the **Pull** button to sync your local repository.
<br>
<br>

## 4 Errors
___
If you have any errors that you cannot fix, contact Cam Boyd either by [email](mailto:cjboyd@deakin.edu.au) or on MS Teams.
<br>
<br>

## 5 References
___
Simon Maple, 2016, *Git Cheat Sheet: Commands and Best Practices*, JRebel, retrieved 20 July 2020, https://www.jrebel.com/blog/git-cheat-sheet