import os
import subprocess
import logging
from colorama import Fore, Style, init
from inquirer import Checkbox, prompt


# Initialize colorama
init()

# Initialize logging
logging.basicConfig(filename='github_tool_automation.log', level=logging.INFO)

# List of GitHub repository URLs
repositories = [
    "https://github.com/OWASP/Amass.git",
    "https://github.com/zaproxy/zaproxy.git",
    "https://github.com/aboul3la/Sublist3r.git",
    "https://github.com/FortyNorthSecurity/EyeWitness.git",
    "https://github.com/1N3/Sn1per.git",
    "https://github.com/projectdiscovery/subfinder.git",
    "https://github.com/m4ll0k/infoga.git",
    "https://github.com/michenriksen/aquatone.git",
    "https://github.com/smicallef/spiderfoot.git",
    "https://github.com/lanmaster53/recon-ng.git",
]

# Directory where repositories will be cloned
base_directory = "tools"

# Create the base directory if it doesn't exist
os.makedirs(base_directory, exist_ok=True)

# Color constants
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Style.RESET_ALL

# Function to display colored messages
def display_message(message, color):
    print(f"{color}{message}{RESET}")
    logging.info(message)

# Function to check for and execute setup scripts
def run_setup_script(directory, repo_name):
    setup_scripts = ["setup.sh", "install.sh", "configure.sh"]  # Add more if needed
    for script in setup_scripts:
        setup_script = os.path.join(directory, script)
        if os.path.exists(setup_script):
            display_message(f"Running {script} for {repo_name}...", GREEN)
            result = subprocess.run(["chmod", "+x", setup_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                result = subprocess.run([setup_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if result.returncode == 0:
                    display_message(f"{script} completed successfully for {repo_name}.", GREEN)
                else:
                    display_message(f"Error running {script} for {repo_name}.", RED)
            else:
                display_message(f"Error setting execute permissions for {script} in {repo_name}.", RED)
            return True
    return False

# Function to check for and install requirements
def install_requirements(directory, repo_name):
    requirement_files = ["requirements.txt", "deps.txt", "prerequisites.txt"]  # Add more if needed
    for req_file in requirement_files:
        requirements_file = os.path.join(directory, req_file)
        if os.path.exists(requirements_file):
            display_message(f"Installing requirements for {repo_name}...", GREEN)
            result = subprocess.run(["pip", "install", "-r", requirements_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                display_message(f"Requirements installed successfully for {repo_name}.", GREEN)
            else:
                display_message(f"Error installing requirements for {repo_name}.", RED)
            return True
    return False

# Interactive interface for selecting repositories
def select_repositories(repos):
    questions = [Checkbox('selected_repos', message='Select repositories to clone and set up', choices=repos)]
    answers = prompt(questions)
    return answers['selected_repos']

# User input validation
def validate_input():
    if not repositories:
        display_message("No repositories are available for cloning.", RED)
        exit(1)

# Clone the repositories
def main():
    validate_input()
    selected_repositories = select_repositories(repositories)

    for repo in selected_repositories:
        repo_name = repo.split("/")[-1].replace(".git", "")
        clone_dir = os.path.join(base_directory, repo_name)

        if not os.path.exists(clone_dir):
            display_message(f"Cloning {repo_name}...", GREEN)
            result = subprocess.run(["git", "clone", repo, clone_dir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                display_message(f"Cloning completed successfully for {repo_name}.", GREEN)
            else:
                display_message(f"Error cloning {repo_name}.", RED)
        else:
            display_message(f"{repo_name} is already cloned.", GREEN)

        # Check and run setup scripts
        if not run_setup_script(clone_dir, repo_name):
            display_message(f"No setup scripts found for {repo_name}.", GREEN)

        # Check and install requirements
        if not install_requirements(clone_dir, repo_name):
            display_message(f"No requirements found for {repo_name}.", GREEN)

    display_message("All selected repositories cloned and setup completed.", GREEN)

if __name__ == "__main__":
    main()