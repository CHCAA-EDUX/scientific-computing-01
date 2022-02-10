# An introduction to Git: what it is, and how to use it

Git is a free and open-source distributed version control system which can record/save snapshots (instances of files) and track them as it changes over time. Breaking that down:

- Version Control System: The code which is stored in Git keeps changing as more code is added. Also, many developers can add code in parallel. So Version Control System helps in handling this by maintaining a history of what changes have happened.
- Distributed Version Control System: Git has a remote repository which is stored in a server and a local repository which is stored in the computer of each developer. This means that the code is not just stored in a central server, but the full copy of the code is present in all the developers’ computers. Git is a Distributed Version Control System since the code is present in every developer’s computer. 
Git is a version control system: can record/save snapshots and track the content of a folder as it changes over time.

# Why version control?

## Roll-back functionality

Mistakes happen - without recorded snapshots you cannot easily undo mistakes and go back to a working version.

## Branching

Often you need to work on several issues/features in one code - without branching this can be messy and confusing.
You can simulate branching by copying the entire code to multiple places but also this will be messy and confusing.

## Collaboration

With version control, none of these are needed anymore (or have much simpler answers):

- “I will just finish my work and then you can start with your changes.”
- “Can you please send me the latest version?”
- “Where is the latest version?”
- “Which version are you using?”
- “Which version have the authors used in the paper I am trying to reproduce?”

## Reproducibility

- How do you indicate which version of your code you have used in your paper?
- When you find a bug, how do you know when precisely this bug was introduced (Are published results affected? Do you need to inform collaborators or users of your code?).

## Compare with Dropbox or Google Drive

- What if you want to work on multiple versions at the same time? Do you make a copy? How do you merge copies?
- What if you don’t have internet?


# What is a Git repository?
Git is a version control system: can record/save snapshots and track the content of a folder as it changes over time.
Every time we commit a snapshot, Git records a snapshot of the entire project, saves it, and assigns it a version.
These snapshots are kept inside a sub-folder called `.git` (typically a hidden folder).

If we remove `.git`, we remove the repository and history (but keep the working directory).
`.git` uses relative paths - you can move the whole thing somewhere else and it will still work
Git doesn’t do anything unless you ask it to (it does not record anything automatically).
Multiple interfaces to Git exist (command line, graphical interfaces, web interfaces).
We will focus on the command line as this this is the most general interface.




'
https://cbea.ms/git-commit/




# Acknowledgement:
This borrows from:
https://www.freecodecamp.org/news/what-is-git-and-how-to-use-it-c341b049ae61/

and 

https://coderefinery.github.io/git-intro