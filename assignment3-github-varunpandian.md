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