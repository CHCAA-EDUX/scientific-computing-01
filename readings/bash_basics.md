# Introduction to Bash and Unix #

* Unix is a set of programs to act as a link between the computer and user
* Kernel/OS: programs that allocate system resources
  * shell is used to communicate with the kernel (terminal is CLI interpreter)


* Prompt, check calendar
```sh
$ cal
    August 2021
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

* list directories and files, all data are organized into files, all files into directories, directories are organized into a tree-like structure, _the filesystem_

```sh
$ ks -l
total 36
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 12:34 dat
drwxrwxr-x 2 knielbo knielbo 4096 Jul 27 15:28 docs
drwxrwxr-x 2 knielbo knielbo 4096 Jul 27 13:51 figs
drwxrwxr-x 2 knielbo knielbo 4096 Aug 22 14:54 lessons
-rw-rw-r-- 1 knielbo knielbo 1110 Jul 12 10:38 LICENSE.md
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 12:34 literature
-rw-rw-r-- 1 knielbo knielbo  590 Jul 12 12:56 README.md
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 10:35 slides
drwxrwxr-x 2 knielbo knielbo 4096 Aug 15 16:23 src
```
* listings with `d` represent directories

* login identity (user)
```sh
$ whoami
knielbo

$ users
knielbo im

$ who
knielbo  :0 2021-08-21 09:30 (:0)
im       :0 2021-08-21 11:15 (:0)
```

* system shutdown

| command | description |
| - | - |
| halt | system shutdown immediately |
| init 0 | power off with synchronize and clean up |
| init 6 | reboors by shutting down completely and then restart |
| poweroff | system shutdown by powering off |
| reboot | system reboot |
| shutdown | system shotdown |

### Listing files

```sh
$ ls
dat  docs  figs  lessons  LICENSE.md  literature  README.md  slides  src


$ ls -l
total 36
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 12:34 dat
drwxrwxr-x 2 knielbo knielbo 4096 Jul 27 15:28 docs
drwxrwxr-x 2 knielbo knielbo 4096 Jul 27 13:51 figs
drwxrwxr-x 2 knielbo knielbo 4096 Aug 22 14:54 lessons
-rw-rw-r-- 1 knielbo knielbo 1110 Jul 12 10:38 LICENSE.md
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 12:34 literature
-rw-rw-r-- 1 knielbo knielbo  590 Jul 12 12:56 README.md
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 10:35 slides
drwxrwxr-x 2 knielbo knielbo 4096 Aug 15 16:23 src
```
* Col1: file type and permissions
* Col2: memory block taken by file or directory
* Col3: file owner
* Col4: group of the owner
* Col5: file size in bytes
* Col6: date and time when the file was created or modified last time
* Col7: file or directory name

prefixes for  Col1

| prefix | description |
| - | - |
| \- | regular file or hard link |
| b | block special file. block input/output device file, e.g., physical hard drive|
| c | character special file. raw input/output device file, e.g., physical hardd rive|
| d | directory file |
| l | symbolic link file, links on any regular file |
| p | named pipe, mechanism for interprocess communications |
| s | socket used for interprocess communication |

### Metacharacters

* `*`: match 0 or more characters
* `?`: matches with a single character

```sh
$ ls src/*.py
src/bool_examples.py        src/error_examples.py  src/my_first_program.py  src/tracebackerror.py
src/class_intro.py          src/linting.py         src/regex_examples.py    src/var_copy.py
src/class_numpy.py          src/magic_8_balls.py   src/scope_examples.py    src/zigzag.py
src/conway_game_of_life.py  src/modular_prog.py    src/tictactoe.py
```

### Hidden files

* files that start with a dot `.` are used to store configuration information
    - `.profile`, bourne shell (sh) initialization script
    - `.kshrc, Korn shell (ksh)  initialization script
    - `.cshrc`, C shell (csh)  initialization script
    - `.rhosts`, the remote shell configuration file
* hidden file are shown with ´-a´ flag
```sh
ls -a
.  ..  dat  docs  figs  .git  lessons  LICENSE.md  literature  README.md  slides  src
```

* single `.`, current director
* double `.` parent directory

### Creating files

* Creating a file with Vi(sual)
```sh
$ vi dat/somefile
```

Open VI, press `i` for edit mode and add

```sh
unix inferno: abandon hope all ye who enter here...
```
press `esc` and `shift+zz`

### Editing files

```sh
$ vi dat/somefile
```
modes in vi

* command mode: issue vi commands, including commands like insert, append, and delete, and other search and navigation commands that let you move around your file.
* insert mode: `i`, edit mode that allow to edit text and use arrows to navigate, press `esc` to leave
* last line mode: `:` from command model, perform quit, write-quit, and search commands, return to command mode press `esc` `esc`

movement in command mode

* __l__ move right
* __h__ move left
* __k__  move up
* __j__ move down

### Display content of file

```sh
$ cat dat/somefile
unix inferno: abandon hope all ye who enter here...

$ cat dat/somefile -b
1 unix inferno: abandon hope all ye who enter here...
```

* add `b` flag for line number

### Counting words in file

* `wc` counts total number of lines, words and chars in file

```sh
$ wc dat/somefile
1  9 52 dat/somefile
```

```sh
$ wc dat/somefile dat/someotherfile
  1   9  52 dat/somefile
  2  12  69 dat/someotherfile
  3  21 121 total
```

### Copying files

```sh
$ cp source_file destination_file
```

### Renaming files ###

```sh
$ mv old_file new_file
```

### Deleting files ###

```sh
$ rm filename
$ rm filename0 filename1
```

### Standard Unix Streams ###

Unix has three streams (files) opened when it starts up

* `stdin`, read default input from STDIN, associated file descriptor 0
* `stdout`, write to STDOUT, associated file descriptor 1
* `stderr`, write all error messages, associated file descriptor 2

## Directory Management ##

### Home Directory Management ###

* `~`: home dir
* `-`: previous dir
* `cd ~username`: username's home dir

```sh
$ cd ~
$ pwd
/home/knielbo
$ cd -
/home/knielbo/CENTRAL/education/programming-honey-badgers
$ pwd
/home/knielbo/CENTRAL/education/programming-honey-badgers
$cd ~spock
$ pwd
/home/spock
```

### Absolute/Relative Pathnames ###

* Directories are arranged with root `/` at the top
* The position of any file in the hierarchy is described by its pathname
* elements in pathnames are seperated by `/`
* A pathname is **absolute** if it is _described in relation to root, thus absolute filepaths always start with `/`

```sh
/home/knielbo/CENTRAL/education/programming-honey-badgers
```
* a pathname can be relative to the current working directory. *Relative* pathnames never begin with `/`. 

```sh
programming-honey-badgers/src
```

* to determine current location in filesystem hierarchy use `pwd` to print current working directory

```sh
$ pwd
/home/knielbo/CENTRAL/education/programming-honey-badgers
```

### Listing directories ###

```sh
$ ls .
dat  docs  figs  lessons  LICENSE.md  literature  README.md  slides  src
```

```sh
$ ls ~/virtenvs/
boomer  FABULA           H8          postactivate    postmkvirtualenv  predeactivate    prermvirtualenv
cvdeep  FUCKUP           honeyb      postdeactivate  postrmvirtualenv  premkproject
cvgen   get_env_details  initialize  postmkproject   preactivate       premkvirtualenv
```

### Creating directories ###

```sh
$mkdir dirname0 dirname1
```

#### Creating parent directories ####

```sh
$ mkdir adir/anotherdir/yetanotherdir
mkdir: cannot create directory ‘adir/anotherdir/yetanotherdir’: No such file or directory
```

```sh
$ mkdir -p adir/anotherdir/yetanotherdir
$ tree adir/
adir/
└── anotherdir
    └── yetanotherdir

2 directories, 0 files
```

#### Removing directories ####

```sh
rmdir dirname0 dirname1

rm -r dirname0 dirname1
```

#### Changing directories ####

```sh
$ cd dirname
```
* using absolute path
```sh
cd /home/knielbo/CENTRAL/education/programming-honey-badgers
```

* using relative path

```sh
cd ../src
```

#### Renaming directories ####

```sh
mv olddir newdir
```

#### More on listing directories ###

* `l` flag, long list format
* `a` flag, list all

```sh
$ ls -la
total 48
drwxrwxr-x 10 knielbo knielbo 4096 Aug 24 16:18 .
drwxrwxr-x 12 knielbo knielbo 4096 Aug 18 09:32 ..
drwxrwxr-x  2 knielbo knielbo 4096 Aug 24 15:29 dat
drwxrwxr-x  2 knielbo knielbo 4096 Jul 27 15:28 docs
drwxrwxr-x  2 knielbo knielbo 4096 Jul 27 13:51 figs
drwxrwxr-x  8 knielbo knielbo 4096 Aug 24 16:21 .git
drwxrwxr-x  2 knielbo knielbo 4096 Aug 22 14:54 lessons
-rw-rw-r--  1 knielbo knielbo 1110 Jul 12 10:38 LICENSE.md
drwxrwxr-x  2 knielbo knielbo 4096 Jul 12 12:34 literature
-rw-rw-r--  1 knielbo knielbo  590 Jul 12 12:56 README.md
drwxrwxr-x  2 knielbo knielbo 4096 Jul 12 10:35 slides
drwxrwxr-x  2 knielbo knielbo 4096 Aug 15 16:23 src
```

```sh
~$ ls -lh #long format, file size human readable
~$ ls -t # order of latest modification
~$ ls -r # list in reverse order
~$ ls -F # adds '/' to directories
~$ ls -lS # displays files in size order (largest to smallest)
~$ ls -R # directory tree
~$ ls -i # display inode number, index node for each file
~$ man ls
```

## Permissions ##

File ownership is an important component of Unix secure methods for storing files. Every file has the thrre permissions attributes

* Owner permissions - actions of the file owner
* Group permissions - groups members' actions
* Other (world) permissions - others' actions

### Permission indicators

```sh
$ ls -l
total 36
drwxrwxr-x 2 knielbo knielbo 4096 Aug 24 15:29 dat
drwxrwxr-x 2 knielbo knielbo 4096 Jul 27 15:28 docs
drwxrwxr-x 2 knielbo knielbo 4096 Jul 27 13:51 figs
drwxrwxr-x 2 knielbo knielbo 4096 Aug 22 14:54 lessons
-rw-rw-r-- 1 knielbo knielbo 1110 Jul 12 10:38 LICENSE.md
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 12:34 literature
-rw-rw-r-- 1 knielbo knielbo  590 Jul 12 12:56 README.md
drwxrwxr-x 2 knielbo knielbo 4096 Jul 12 10:35 slides
drwxrwxr-x 2 knielbo knielbo 4096 Aug 15 16:23 src

```
First column represents access modes (permissions associated with file/directory). Permissions can be parsed in groups of three, each position in the group denotes a specific permission, in the order: read (`r`), write (`w`), execute (`x`):

* first three characters (2-4) are file owners permissions
* second group (5-7 are group permissions
* third group (8-10) are others' permissions

### File access modes

* Read, grants capability to read (view file content)
* Write, capability to modify or remove file content
* Execute, capability to run file as a program

### Directory access mode

* Read, grants capability to read dir content (see filenames inside)
* Write, add and delete files from directory
* Execute, traverse permission (certain dirs require execute to use functions, e.g., `ls` and `cd` require execute access to `bin`)

### Changing Permissions

Use `chmod` to change file or directory permissions. `chmod` has two modes: sympbolic and absolute

#### chmod symbolic mode

add, delete, or specify permissions using the following operators

| operator | description |
| - | - |
| + | adds designated permission |
| - | removes designated permission |
| = | sets designated permission |

```sh
$ ls -l
total 8
-rw-rw-r-- 1 knielbo knielbo 52 Aug 24 14:59 somefile
-rw-rw-r-- 1 knielbo knielbo 69 Aug 24 15:29 someotherfile

# allow user to execute
$ chmod u+x somefile
# remove user to execute
$ chmod u-x somefile

# remove group to write
$ chmod g-w somefile
# allow group to write
$ chmod g-w somefile

# remove other to read
$ chmod o-r somefile
# allow other to read
$ chmod o+r somefile
```

#### chmod absolute permissions

| number | octal permission representatation | Ref |
| :-: | - | :-: |
| 0 | no permission | \--- |
| 1 | execute permission | \--x |
| 2 | write permission | \-w- |
| 3 | execute and write: 1 + 2 = 3 | \-wx |
| 4 | read permission | r-- |
| 5 | read and execute: 4 + 1 = 5 | r-x |
| 6 | read and write: 2 + 4 = 6| rw- |
| 7 | all permissions: 1 + 2 + 4 = 7| rwx |

```sh
$ chmod 777 somefile
$ ls -l
total 8
-rwxrwxrwx 1 knielbo knielbo 52 Aug 24 14:59 somefile
-rw-rw-r-- 1 knielbo knielbo 69 Aug 24 15:29 someotherfile

$ chmod 664 somefile
$ ls -l
total 8
-rw-rw-r-- 1 knielbo knielbo 52 Aug 24 14:59 somefile
-rw-rw-r-- 1 knielbo knielbo 69 Aug 24 15:29 someotherfile
```

### Changing Owners and Groups ###

Creating an account on unix will assign an _owner ID_ and a _group ID_ to the user. All permissions are also based on the Owner and Groups. Two commands are available to change owner and group of files

* `chown`, 'change owner' of a file
* `chgrp`, 'change group' of a file

#### chown ####

```sh
$ chown user filelist
```

#### chgrp ####

```sh
$ chgrp group filelist
```

## Environment ##

the unix _environment_ is defined by environment variables, some set by the system, others by the shell, a user or any program that loads another program

```sh
$ VAR="Hello World!"
$ echo $VAR
Hello World!
```

* Environment variables are set without using `$` but accessing them require `$` prefix
* shell undergoes _initialization_ to set up the environment, when one logs into the system. This is a two-step process that has the shell reading two files
  * `/etc/profile`
  * `profile`
  * when either or both of these files are readm then shell displays the prompt

### Sending mails from the command line ###

```sh
$ sudo apt update
$ sudo apt install mailutils

# email from your user
$ mail -s "email test" nielbo23@gmail.com < someotherfile

# fake email
$ mail -a FROM:Spock@uss-enterprise.com -s 'From the captain' nielbo23@gmail.com < someotherfile

# manual
$ man mail
```

## Pipes and Filters ##

* When a program takes its input from another program, it performs some operation on that input, and writes the result to the standard output
* `|`, Pipes, connect two commands together (pipe output from one program as input to another)

### `grep` ###

* search file(-s) for lines with patten
* grep: 'globally search for a regular expression and print all lines containing it'

```sh
~$ grep pattern files(s)
```

* search for single string or substring

```sh
$ls -l src | grep class
-rw-rw-r-- 1 knielbo knielbo 2113 Jul 28 14:57 class_intro.py
-rw-rw-r-- 1 knielbo knielbo 1415 Jul 19 18:37 class_numpy.py
```

| Flag | Description |
| :-: | - |
| `-v` | print all lines that do not match pattern |
| `-n` | print matched line and its line number |
| `-l` | print only the names of files with matching lines |
| `-c` | print only the count of matching lines |
| `-i` | match either upper- or lowercase/ignore case |
| `-w` | match exact pattern |

```sh
~$ ls -l src | grep -c class
2
```

### `sort` ###

```sh
$ cat dat/lignes
It was the hour of morning,
when the sun mounts with those stars
that shone with it when God's own love
first set in motion those fair things

$ sort dat|lignes
first set in motion those fair things
It was the hour of morning,
that shone with it when God's own love
when the sun mounts with those stars
```

| Flag | Description |
| :-: | - |
| `n` | sort numerical |
| `r` | reverse order |
| `f` | ignore upper/lowercase |
| `+x` | ignore fields x when sorting |

* ignore 3 fields and make numerical sort on fourth field (size)  

```sh
$ ls -l src | grep class | sort +3n
-rw-rw-r-- 1 knielbo knielbo 1415 Jul 19 18:37 class_numpy.py
-rw-rw-r-- 1 knielbo knielbo 2113 Jul 28 14:57 class_intro.py
```

### `less` and `more` ###

* `less`, terminal pager to view (not edit file)
* `more`, basic terminal pager, allow only forward navigation
* get all instances containint 'py' sorted on alphabetic field (not id in first group)

```sh
history | grep py | sort +1 | more
```
