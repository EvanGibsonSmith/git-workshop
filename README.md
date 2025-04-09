# Git Workshop

This interactive workshop is to teach the basics of Git, including cloning, branching, and merging (and of course commiting). This repo serves as a way of introducing those issues with a chaotic version of the snake game.

## Requirements

You'll need a recent version of Python, as well as `pip`, to install `pygame`, which is needed to run Snake.

What You'll Do:
Clone this repo with a buggy snake game.

Make your own changes to the game on the snake_bug_fix branch.

Merge your changes with the main branch that has conflicting updates.

🚀 Getting Started

0. Downloads
## 🚀 Getting Started

### 0. Downloads

**Git:**

If you haven’t already, download Git from [https://git-scm.com/downloads](https://git-scm.com/downloads).

**VSCode:**

While other IDEs can work, we’ll be using VSCode for this workshop. Download it from [https://code.visualstudio.com/Download](https://code.visualstudio.com/Download).

**Python:**

We will use Python with `pip` for package management. If you don’t have it yet, install it from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to include `pip` during installation.

**Code Setup:**

The project uses `pygame` for the Snake game, so after installing Python, run:
    ```
    pip install pygame
    ```

1. Initialize the repository 
Using the following command initalizes a git repo in this folder (under the hood it creates a .git file that manages everyhing).

```
git init
```

2. Clone the Repo
Clone the repository and navigate to our project folder. Then, type this command in the terminal at this folder
(if you are in vs code the integrate terminal should already be in the right spot)

```
git clone <this_repo_url>
cd chaotic_snake
```

3. Create a branch for bug fixes
First, switch to the snake branch that contains the pre-made changes (these are the ones you’ll be merging into):

```
git checkout -b snake_bug_fix
```

This branch has the snake game without the needed bug fixes. The -b flag creates the new branch locally.


4. Modify the Game
Go through the code on this new branch and make the bug fixes needed. These bug fixes will be marked by comments
# TODO
so command F for those to find the changes needed.

4. Commit Your Changes
Once you've made your edits, commit your changes on this new branch:

git add main.py
(just adds the file to be in this commit)
git commit -m "bug fixes"
(git commit commits it, with -m and then "description of commit". Keep these desciptions short and informative if possible)

5. Merge changes into Main
Take these bug fixes and merge them into main. 

First, you want to go checkout the main branch to merge into

```
git checkout main
```

Then, you want to merge the changes of the snake_bug_fix into main.

```
git merge snake_bug_fix
```


6. Resolving the Merge Conflict
You’ll see Git’s conflict markers inside the main.py file :

<<<<<< HEAD
print("Hello Current Change")
======
print("Hello Incoming Change")
>>>>>> main

To resolve the conflict:

Edit the file to combine both changes in a way that makes sense (or choose one version over the other).
For this workshop, you will want to select the new changes from the snake_bug_fix branch.

Remove the conflict markers (<<<<<<<, =======, >>>>>>>).

Stage the resolved file:

```
git add main.py
git commit
```

Git Merge Points:

Merge Conflicts: When two branches change the same part of a file, Git doesn’t know what to do — that’s when you need to step in and resolve the conflict manually.

Branching and Merging Best Practices: It’s great to work on separate branches, but knowing how to handle merge conflicts when combining them is just as important.


7.

After the merge conflict is resolved:

Push your changes back to your GitHub with 

```
git push 
```

If this is the first time pushing to the GitHub repo, you may get an error because git doesn't know where to push
your local changes. The terminal gives this fix, but is is also below:

git push --set-upstream origin main

This command does two things:

It pushes your local main branch to the remote repository (origin).

It sets the remote main branch as the upstream branch for your local main, so future pushes and pulls will be automatic.

Now it should work, so you can push changes to GitHub with:

```
git push
```
