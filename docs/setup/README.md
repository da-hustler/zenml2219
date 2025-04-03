# 🛠️ ZenML Setup Guide for Local Development (PyCharm & CLI)

It's **tool-agnostic**, so users can adapt it for VS Code, terminal-only, or notebooks too.

---

## ✅ Prerequisites

- Python **3.9 – 3.12** (⚠️ ZenML does not support 3.13)
- Git installed and added to `PATH`
- PyCharm (or any IDE / CLI)
- Internet access

---

## 🧱 1. Clone the Forked Repository

```bash
cd C:/Users/<YourName>/zenml-docs-contrib
git clone https://github.com/da-hustler/zenml2219.git
cd zenml2219
```




# 🔧 Setup Instructions for ZenML Documentation

## This guide will walk you through setting up your local development environment to contribute to the ZenML documentation.

---

> 💡 PyCharm users still benefit from extra tips, but this guide is tool-agnostic (terminal friendly).

3. Open the Project in PyCharm
 ------------------
- Launch PyCharm
- File > Open > Select `zenml2219` folder

4. Create a Virtual Environment in PyCharm
------------------
- File > Settings > Python Interpreter
- ⚙️ > Add > New Environment using Virtualenv
- Location: `.venvxx` (or your choice)
- Base Interpreter: Select Python 3.12
- Uncheck "Inherit global site-packages"
- (Optional) Check "Make available to all projects"
### - Click OK

## 5. Activate the Virtual Environment in Terminal
## ------------------------------------
```bash
.venvxx\Scripts\activate
```


## 6. Install ZenML in Editable Mode
## Navigate to the root project folder:
## cd C:/Users/<YourUsername>/zenml-docs-contrib/zenml2219

```bash 
pip install -e .
```



## Note: If you get an error about unsupported Python version,
## make sure you're using Python 3.12, not 3.13

### 7. Verify ZenML Installation
- zenml version
- Output:
- version: 0.80.1


## 8. (Optional) Upgrade pip
### python -m pip install --upgrade pip
## 9. (Optional) Configure Git in PyCharm
### File > Settings > Version Control > Git
### - Ensure path to git.exe is detected
### - Test connection

---

## 🧱 Directory Structure

### This is the recommended structure for contributors:

#### zenml2219/
#### ├── docs/
#### ├── setup/
#### ├── mkdocs/
#### ├── scripts/
#### ├── tests/
#### ├── notebooks/
#### ├── examples/
#### ├── unit_tests/
#### ├── configs/
#### └── README.md


### python -m venv .venvxx
```bash
.venvxx\Scripts\activate
```  
# PowerShell

### pip install --upgrade pip
### pip install zenml

### zenml init


---
# ✅ You’re All Set!
# ------------------
## Now you can:
## - Explore the ZenML codebase
## - Write or run pipelines
## - Add unit tests
## - Contribute to open GitHub issues 🚀
## ✅ What’s Next?


- ✅ Stage + commit this as `docs: setup instructions added`
- 🔜 Start working on the first unit test step inside `tests/` folder
---
---

## 🧠 CLI Commands Cheat Sheet

Here's a quick-reference table for common terminal commands when working with ZenML or Python projects:

| Command                        | Description                                                  |
|-------------------------------|--------------------------------------------------------------|
| `pwd`                         | Shows the current directory (Print Working Directory)       |
| `ls`                          | Lists files/folders in the current directory                |
| `cd folder_name`              | Changes into a directory                                    |
| `cd ..`                       | Goes up one level                                           |
| `clear`                       | Clears the terminal screen                                  |
| `mkdir myfolder`             | Creates a new directory called 'myfolder'                   |
| `touch myfile.py`            | Creates a new empty file named 'myfile.py'                  |
| `rm myfile.py`               | Deletes a file (careful!)                                   |
| `rm -r myfolder`             | Deletes a folder and everything inside                      |
| `python --version`           | Check installed Python version                              |
| `python -m venv .venv`       | Create a virtual environment                                |
| `source .venv/Scripts/activate` | Activate venv (Git Bash / WSL)                           |
| `.venv\Scripts\activate`     | Activate venv (PowerShell)                                  |
| `pip install package_name`   | Installs a Python package                                   |
| `pip freeze`                 | Lists all installed packages                                |
| `pip install -r requirements.txt` | Installs from requirements file                     |
| `git --version`              | Check Git version                                           |
| `git clone <repo-url>`       | Clone a repo to your machine                                |
| `git status`                 | Check repo status                                           |
| `git add .`                  | Stage all changes                                           |
| `git commit -m "Message"`    | Commit staged changes                                       |
| `git push`                   | Push changes to GitHub                                      |
| `exit`                       | Exit the terminal session                                   |
| `code .`                     | Opens VS Code in current folder (if installed)              |

> 💡 Tip: Use `Ctrl + L` to clear your terminal screen quickly.

---
---

## 🙌 You're Ready to Roll!

Feel free to use this CLI cheat sheet, explore the ZenML architecture, and start contributing 🎯

If you spot a bug, improvement, or typo — open a PR!  
We appreciate your contribution.

# Happy coding and welcome to ZenML Docs Contribution 🚀💻✨

> 🧠 *"I strive to fail, and through my failure I will achieve my success."* — Adel P.
