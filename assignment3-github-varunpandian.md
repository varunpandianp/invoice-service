###TASK-01

###STEP -01

##Repository Initialization 

##commands 

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
```STEP 2
Create README.md describing the project in two sentences, and commit it on its own.

command 

touch README.md 

echo content > README.md
```

```
STEP 3

Create app.py (or App.java) with a few lines of code, 
and a config.ini file. Commit them as two separate commits
 with meaningful messages.

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

```
4 -Create a file named .env containing the line API_KEY=not-a-real-secret,
and a directory build/ containing any file.





```