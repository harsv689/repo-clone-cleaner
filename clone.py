import os
import shutil
import subprocess

def run_command(command, cwd=None):
    """Runs a shell command and prints output."""
    result = subprocess.run(command, shell=True, cwd=cwd, text=True, capture_output=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
    else:
        print(result.stdout)
    return result.returncode, result.stdout.strip()

def main():
    repo_url = input("Enter the GitHub repository URL to clone: ").strip()
    if not repo_url:
        print("No URL entered. Exiting...")
        return
    
    # Extract repo name from URL
    repo_name = repo_url.rstrip('/').split('/')[-1].replace('.git', '')

    # Clone the repo
    temp_dir = repo_name
    if run_command(f"git clone {repo_url} {temp_dir}")[0] != 0:
        return
    
    os.chdir(temp_dir)  # Change to repo directory

    # Remove all Git history
    shutil.rmtree(".git")

    # Create a new public repository with the same name on GitHub
    print(f"Creating a new public repository: {repo_name}")
    run_command(f"gh repo create {repo_name} --public")

    # Reinitialize as a fresh repo
    run_command("git init")
    run_command("git branch -m main")  # Rename to main if needed
    run_command(f"git remote add origin git@github.com:harsv689/{repo_name}.git")  # Replace with your GitHub username

    # Add all files, commit, and push
    run_command("git add .")
    run_command('git commit -m "Initial Commit"')
    run_command("git push -u origin main")  # Change 'main' if needed

    # Cleanup
    os.chdir("..")
    shutil.rmtree(temp_dir)
    print(f"Repository '{repo_name}' successfully uploaded to your GitHub and cleaned up.")

if __name__ == "__main__":
    main()
