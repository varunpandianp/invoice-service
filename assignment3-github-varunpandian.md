###TASK-01

# -01 Create ~/assignment3/invoice-service and initialise a repository inside it.

## Repository Initialization 

## commands 

```bash

mkdir -p assignments3/invoice-service 

cd /assignment3/invoice-service

git init 

git status 
```

```
### Execution of commands

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ pwd
/e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git init
Reinitialized existing Git repository in E:/paperlive-assignments/git-hub-assignments/assignment3/invoice-service/.git/

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   assignment3-github-varunpandian.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   assignment3-github-varunpandian.md

```
# 2-Create README.md describing the project in two sentences, and commit it on its own.

```
Create README.md describing the project in two sentences, and commit it on its own.

command 

touch README.md 

echo content > README.md
```

# 3-Create app.py (or App.java) with a few lines of code, 
and a config.ini file. Commit them as two separate commits
 with meaningful messages.
```
vi app.py  

code def calculate_invoice(subtotal, tax_rate):
    tax = subtotal * tax_rate / 100
    total = subtotal + tax
    return total


invoice_total = calculate_invoice(1000, 18)
print(f"Invoice Total: {invoice_total}")

vp config.ini
[application]
name = invoice-service
environment = development
port = 8080


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline
ed225e8 (HEAD -> main) added application configuration
cbd354d Add invoice calculation logic
1df56d6 asigment github markedown answer update
45b2d72 Readme File invoice- service

```


# 4 -Create a file named .env containing the line API_KEY=not-a-real-secret,
and a directory build/ containing any file.
```
$ echo "API_KEY=not-a-real-secret" > .env
$ git add .env 

$ mkdir -p build

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ echo "Build output sample" > build/output.txt

```


# 5-Add a .gitignore that excludes .env and build/. Commit the .gitignore.
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
```$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   assignment3-github-varunpandian.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        build/

no changes added to commit (use "git add" and/or "git commit -a")


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   assignment3-github-varunpandian.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

no changes added to commit (use "git add" and/or "git commit -a")

```

# 6-Prove that git status no longer reports either of them.
```
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main
nothing to commit, working tree clean

```


# 7-Modify README.md. Show the difference before staging, stage it, then show the difference again and explain why the second command shows something different.
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
```$ git diff
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
diff --git a/README.md b/README.md
index d3a5d65..549cdae 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,3 @@
 invoice service is the small application billing service to generate gst sgst bill to the customer ,it help organize invoce details and maintain the e accurate billing records
+
+The application currently supports invoice total calculation with tax.
:


git add README.md 


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git diff
diff --git a/assignment3-github-varunpandian.md b/assignment3-github-varunpandian.md
index 7534f7c..666ddb9 100644
--- a/assignment3-github-varunpandian.md
+++ b/assignment3-github-varunpandian.md
@@ -135,6 +135,31 @@ Untracked files:
 
 no changes added to commit (use "git add" and/or "git commit -a")
 
+```
#git diff --staged 
+```
:

git diff --staged
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git diff --staged
diff --git a/README.md b/README.md
index d3a5d65..549cdae 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,3 @@
 invoice service is the small application billing service to generate gst sgst bill to the customer ,it help organize invoce details and maintain the e accurate billing records
+
+The application currently supports invoice total calculation with tax.

```

# 8 Show the history in a compact one-line format and paste it into your write-up.
```
git log --online


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline
ebdcca2 (HEAD -> main) update the ans for que 5
30dbefc Add gitignore for local files
10eaae5 add .env file
c18ec0b update the answer for task 1 thirs question
ed225e8 added application configuration
cbd354d Add invoice calculation logic
1df56d6 asigment github markedown answer update
45b2d72 Readme File invoice- service


```

# Task 2 — Work on two things at once

# Branching and merging

# Create and switch to a branch named feature/currency-format. Make two commits on it.

```
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git switch -c feature/currency-format
Switched to a new branch 'feature/currency-format'


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (feature/currency-format)
$ git branch
* feature/currency-format
  main

```
# 2 Return to main. Confirm that the files from the feature branch are not present, and explain in one sentence why.
```
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (feature/currency-format)
$ git switch main
M       assignment3-github-varunpandian.md
Switched to branch 'main'

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git branch
feature/currency-format
* main
```
# 3 -Create a branch named bugfix/rounding-error from main, make one commit, and merge it into main.

```
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git switch -c bugfix/rounding-error
Switched to a new branch 'bugfix/rounding-error'

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (bugfix/rounding-error)
$ git branch
* bugfix/rounding-error
  feature/currency-format
  main
  
  Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (bugfix/rounding-error)
$ git log --oneline -3
82cf0e2 (HEAD -> bugfix/rounding-error) Fix invoice amount rounding
6efe9b7 (main, feature/currency-format) updated task 1 notes and commands
ebdcca2 update the ans for que 5

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git merge bugfix/rounding-error
Updating 6efe9b7..82cf0e2
Fast-forward
 app.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
 
 

```
# 4 Show the history as a graph and identify whether that merge was a fast-forward or created a merge commit. Explain why.

```
$ git log --oneline --graph --all
* 82cf0e2 (HEAD -> main, bugfix/rounding-error) Fix invoice amount rounding
* 6efe9b7 (feature/currency-format) updated task 1 notes and commands
* ebdcca2 update the ans for que 5
* 30dbefc Add gitignore for local files
* 10eaae5 add .env file
* c18ec0b update the answer for task 1 thirs question
* ed225e8 added application configuration
* cbd354d Add invoice calculation logic
* 1df56d6 asigment github markedown answer update
* 45b2d72 Readme File invoice- service

The bugfix/rounding-error branch was created from main. I made one commit on the bugfix branch and merged it into main.

Since main had not received any new commits during this time Git performed a fast-forward merge It moved the main branch pointer forward to the bugfix commit without creating an additional merge commit.

```
# 5: Merge feature/currency-format into main

```aiignore
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline --graph --all
*   8c66d8d (HEAD -> main) Merge branch 'feature/currency-format'
|\  
| * 115cfcd (feature/currency-format) Add currency formatting function
* | 82cf0e2 (bugfix/rounding-error) Fix invoice amount rounding
|/  
* 6efe9b7 updated task 1 notes and commands
* ebdcca2 update the ans for que 5
* 30dbefc Add gitignore for local files
* 10eaae5 add .env file
* c18ec0b update the answer for task 1 thirs question

```
# 6 Delete both merged branches and prove they are gone.

```aiignore
$ git branch -d bugfix/rounding-error
Deleted branch bugfix/rounding-error (was 82cf0e2).

$ git branch -d feature/currency-format
Deleted branch feature/currency-format (was 115cfcd).

$ git branch
* main

```

# 7- Create a branch named experiment/redesign, make one commit, and then delete the branch without merging it. Record the warning Git gives you and what you had to do differently.

```aiignore
$ git switch -c experiment/redesign
Switched to a new branch 'experiment/redesign'

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (experiment/redesign)
$ git branch
* experiment/redesign
  main
  
$ git branch -d experiment/redesign
error: the branch 'experiment/redesign' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D experiment/redesign'
hint: Disable this message with "git config advice.forceDeleteBranch false"

```

# Task 3 — Break things, then recover

# 1 

```aiignore

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git merge feature/staging-config
Auto-merging config.ini
CONFLICT (content): Merge conflict in config.ini
Automatic merge failed; fix conflicts and then commit the result.



name = invoice-service
<<<<<<< HEAD
environment = production
=======
environment = staging
>>>>>>> feature/staging-config
name = invoice-service
environment = development
port = 8080


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline --graph -5
*   1e750c7 (HEAD -> main) Merge branch 'feature/staging-config'
|\  
| * 383a81a (feature/staging-config) set staging environment
* | ab39215 set production environment
* | 326b49e Set staging environment
* | 64fecd2 changed environment to production
|/  


Resolved the conflict in `config.ini` by retaining both production and staging configurations in separate section

```
# Part B — Undo, four ways
# Modify README.md without staging it, then discard the change and restore the committed version.
# Stage a change by mistake, then unstage it while keeping the edit.
# Make a commit with a deliberately wrong message, then correct the message without creating a second commit.
# Make a commit that introduces a bug, then undo it with a command that adds a new commit rather than rewriting history. Record which command you used and explain when this is the only safe option.
# Make two more commits, then move the branch pointer back two commits while keeping the changes staged. Show git status before and after.

```aiignore
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   assignment3-github-varunpandian.md


$ git diff
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
diff --git a/README.md b/README.md
index 549cdae..e659b49 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,5 @@
 invoice service is the small application billing service to generate gst sgst bill to the customer ,it help organize invoce details and maintain the e accurate billing records
 
-The application currently supports invoice total calculation with tax.


$ git restore README.md

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   assignment3-github-varunpandian.md



Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md    
 
 
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git restore --staged README.md

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   assignment3-github-varunpandian.md



Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline
c61c3b6 (HEAD -> main) wrong message
7732292 updated task 2 commands
1e750c7 Merge branch 'feature/staging-config'
383a81a (feature/staging-config) set staging environment
ab39215 set production environment
326b49e Set staging environment

git commit --amend -m "Document Git unstage practice"

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline
9b63e93 (HEAD -> main) Document Git unstage practice
7732292 updated task 2 commands
1e750c7 Merge branch 'feature/staging-config'
383a81a (feature/staging-config) set staging environment
ab39215 set production environment


```
# Part b 5 -5: Move HEAD back two commits while keeping changes staged

```aiignore
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   app.py


$ git log --oneline
089e418 (HEAD -> main) update the app.py addition problem for reset example
1df8e0e update readme for reset command practice
412a562 updated task 3 part A answer and commands
9b63e93 Document Git unstage practice
7732292 updated task 2 commands

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git reset --soft HEAD~2

Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log --oneline
412a562 (HEAD -> main) updated task 3 part A answer and commands
9b63e93 Document Git unstage practice
7732292 updated task 2 commands
1e750c7 Merge branch 'feature/staging-config'
383a81a (feature/staging-config) set staging environmentq


Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        modified:   app.py

```
## Task 3 – Part C: Lose Work and Recover It Using Git Reflog

## Make a commit containing an important change. Note its message.
```aiignore
$ git log -1 --oneline
0d14769 (HEAD -> main) Add important recovery checkpoint
```
## 2 Run a hard reset that discards it, and confirm with the log that the commit is gone.
```aiignore
Varun Pandian@VarunPandian MINGW64 /e/paperlive-assignments/git-hub-assignments/assignment3/invoice-service (main)
$ git log -1 --oneline
0d14769 (HEAD -> main) Add important recovery checkpoint

git reset --hard HEAD~1

```
## 3 Recover a Discarded Commit Using Reflog

```aiignore
git reflog

0d14769 Add important recovery checkpoint

I recovered it using:

git branch recovery/important-checkpoint 0d14769
```

## 4 Write two sentences explaining why the commit was recoverable, and name one kind of work that would not have been.

```aiignore

The commit was recoverable because Git's reflog retained a reference to the previous HEAD allowing me to locate the commit even after git reset --hard Uncommitted changes that were discarded by a hard reset 
```

