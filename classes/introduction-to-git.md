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

## Type-along: Tracking a guacamole recipe with Git

> **Setup Git**
> If you haven’t already configured Git, please follow the instructions in the [GitHub quickstart](https://docs.github.com/en/get-started/quickstart/set-up-git). 

We will learn how to initialize a Git repository, how to track changes, and how to make delicious guacamole!

This example is inspired by Byron Smith. The motivation for taking a cooking recipe instead of a program is that everybody can relate to cooking but not everybody may be able to relate to a program written in e.g. Python or another language.

> **Note**: This is a type along to please open your terminal and follow along. If you can't get it set up on your own computer do it on UCloud.

One of the basic principles of Git is that it is easy to create repositories:


```console
$ mkdir recipe
$ cd recipe
$ git init
```

That’s it! With git init have now created an empty Git repository.

We will use git status a lot to check out what is going on:

```console
$ git status

On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

We will make sense of this information during this workshop.

Let us now create __two files__.

One file is called `instructions.txt` and contains:

```shell
* chop avocados
* chop onion
* squeeze lime
* add salt
* and mix well
```


The second file is called `ingredients.txt` and contains:

```shell
* 2 avocados
* 1 lime
* 2 tsp salt
```

As mentioned above, in Git you can always check the status of files in your repository using `git status`. It is always a safe command to run and in general a good idea to do when you are trying to figure out what to do next:

```console
$ git status

On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	ingredients.txt
	instructions.txt

nothing added to commit but untracked files present (use "git add" to track)
```

The two files are untracked in the repository (directory). You want to **add the files** to the list of files tracked by Git. Git does not track any files automatically and you need make a conscious decision to add a file. This is essential - when creating a snapshot (a commit), only the files that are tracked (staged) will be part of the snapshot. 

Let’s do what Git hints at and stage the files:

```console
$ git add ingredients.txt
$ git add instructions.txt
$ git status

On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   ingredients.txt
	new file:   instructions.txt
```

Now this change is staged and ready to be committed.

Let us now make a snapshot (commit the change) to the repository:

```console
$ git commit -m "adding ingredients and instructions"

[master (root-commit) aa243ea] adding ingredients and instructions
 2 files changed, 8 insertions(+)
 create mode 100644 ingredients.txt
 create mode 100644 instructions.txt
```

Right after, we query the status to get this useful command into our muscle memory:

```
$ git status
```

What does the `-m` flag mean? Let us check the help page for that command:

```
$ git help commit
```

You should see a very long help page as the tool is very versatile (press q to quit). Do not worry about this now but keep in mind that you can always read the help files when in doubt. Searching online can also be useful, but choosing search terms to find relevant information takes some practice and discussions in some online threads may be confusing. Note that help pages also work when you don’t have a network connection!

## Exercise 1: Record changes

  Add 1/2 onion to `ingredients.txt` and also the instruction
  to "enjoy!" to `instructions.txt`. Do not stage the changes yet.

  When you are done editing the files, try `git diff`:

  ```console
  $ git diff
  ```

  You will see the following. Can you identify in the two added lines?:

  ```diff
  diff --git a/ingredients.txt b/ingredients.txt
  index 2607525..ec0abc6 100644
  --- a/ingredients.txt
  +++ b/ingredients.txt
  @@ -1,3 +1,4 @@
   * 2 avocados
   * 1 lime
   * 2 tsp salt
  +* 1/2 onion
  diff --git a/instructions.txt b/instructions.txt
  index 6a8b2af..f7dd63a 100644
  --- a/instructions.txt
  +++ b/instructions.txt
  @@ -3,3 +3,4 @@
   * squeeze lime
   * add salt
   * and mix well
  +* enjoy!
  ```

  Now first stage, then commit each change separately (what happens when we leave out the `-m` flag?):

  ```console
  $ git add ingredients.txt
  $ git commit -m "add half an onion"
  $ git add instructions.txt
  $ git commit                   # <-- we have left out -m "..."
  ```

  When you leave out the `-m` flag, Git should open an editor where you can edit
  your commit message. This message will be associated and stored with the
  changes you made. This message is your chance to explain what you've done and
  convince others (and your future self) that the changes you made were
  justified. In the case of bugs, it also helps you track down where they occurred. 
  Write a message and save and close the file.

  This will most likely open up Nano (unless you have set another editor): You can "insert using by pressing `I` then write your message to to save and exit the editor press `esc` and write `:wq` which stands for write quit.

  When you are done committing the changes, experiment with these commands:

  ```console
  $ git log
  $ git log --oneline
  ```



## Writing useful commit messages

When using `git log --oneline`, we see that the first line of the commit message is very important.

Good example:

```
increase threshold alpha to 2.0

the motivation for this change is
to enable ...
...
```

Convention: **one line summarizing the commit, then one empty line,
then paragraph(s) with more details in free form, if necessary**.

- **Why something was changed is more important than what has changed.**
- Bad commit messages: "fix", "oops", "save work"
- Bad examples: [http://whatthecommit.com](http://whatthecommit.com)
- Write commit messages in English that will be understood
  15 years from now by someone else than you. Or by your future you.
- Many projects start out as projects "just for me" and end up to be successful projects
  that are developed by 50 people over decades.
- Cross-reference to issues and discussions if possible/relevant, e.g. "Increase threshold to 2.0, closes #41"
- [Commits with multiple authors](https://help.github.com/articles/creating-a-commit-with-multiple-authors/) are possible.

Good references:

- ["My favourite Git commit"](https://fatbusinessman.com/2019/my-favourite-git-commit)
- ["On commit messages"](https://who-t.blogspot.com/2009/12/on-commit-messages.html)
- ["How to Write a Git Commit Message"](https://chris.beams.io/posts/git-commit/)



## Summary

Now we know how to save snapshots:

```console
$ git add <file(s)>
$ git commit
```

If you want to add all changes to a new commit:

```console
$ git add .
```

Here is some of the other commands we looked as a well as some which you might find useful:

```console
$ git init    # initialize new repository
$ git add     # add files or stage file(s)
$ git commit  # commit staged file(s)
$ git status  # see what is going on
$ git log     # see history
$ git diff    # show unstaged/uncommitted modifications
$ git show    # show the change for a specific commit
$ git mv      # move tracked files
$ git rm      # remove tracked files
```


# Acknowledgement:
This borrows heavily from:
https://coderefinery.github.io/git-intro

# Inspiration:
https://cbea.ms/git-commit/

<!-- 
requirements:

navigate using terminal (bash)

 -->
