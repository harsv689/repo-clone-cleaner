**`repo-cloner-cleaner`** *(A script to clone a repository without its Git history and re-upload it to a new GitHub repository.)*

---

# **Repo Cloner & Cleaner**
### *A Python script to clone a GitHub repository, remove all Git history, and re-upload it as a fresh repository.*

## **Features**
✅ Clone a GitHub repository without leaving any trace of its commit history.  
✅ Completely remove the `.git` folder to detach the repository from its original source.  
✅ Automatically create a new **public GitHub repository** with the same name.  
✅ Reinitialize Git, add a new remote, commit all files, and push to the fresh repository.  
✅ Cleans up all local traces after successful execution.  

---

## **Prerequisites**
Make sure you have the following installed on your system before running the script:

1️⃣ **Python 3.7+**  
2️⃣ **Git** (Must be installed and configured)  
3️⃣ **GitHub CLI (`gh`)** (For automatic repo creation)  

---

## **Installation & Usage**
1️⃣ **Clone this repository (or download the script)**  
```sh
git clone https://github.com/yourusername/repo-cloner-cleaner.git
cd repo-cloner-cleaner
```

2️⃣ **Install dependencies (if required)**  
```sh
pip install subprocess
```

3️⃣ **Run the script**  
```sh
python clone_clean.py
```

4️⃣ **Enter the repository URL when prompted**  
```sh
Enter the GitHub repository URL to clone: https://github.com/example/repo.git
```

5️⃣ **The script will:**
   - Clone the repository
   - Remove all Git history
   - Create a new public repository with the same name
   - Reinitialize Git and push the code
   - Clean up all local traces

---

## **Example Output**
```
Enter the GitHub repository URL to clone: https://github.com/example/repo.git
Cloning into 'repo'...
Creating a new public repository: repo
Initialized empty Git repository
Added remote origin: git@github.com:yourusername/repo.git
Committing files...
Pushing to GitHub...
Repository 'repo' successfully uploaded to your GitHub and cleaned up.
```

---

## **Potential Use Cases**
🔹 **Duplicating repositories without keeping history**  
🔹 **Creating fresh forks without old commits**  
🔹 **Starting over with a clean repo**  
🔹 **Sharing only the latest version of a project**  

---

## **To-Do / Future Enhancements**
✔️ Add support for **private repositories**  
✔️ Allow users to specify a **different repository name**  
✔️ Automate **GitHub authentication** via OAuth  

---

## **License**
📜 MIT License - Free to use and modify!  
