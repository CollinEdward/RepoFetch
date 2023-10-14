import os
import subprocess
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

# List of GitHub repository URLs
repositories = [
    "https://github.com/OWASP/Amass.git",
    "https://github.com/zaproxy/zaproxy.git",
    "https://github.com/aboul3la/Sublist3r.git",
    "https://github.com/FortyNorthSecurity/EyeWitness.git",
    "https://github.com/1N3/Sn1per.git",
    "https://github.com/projectdiscovery/subfinder.git",
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
RESET = Style.RESET_ALL

# Function to display colored messages
def display_message(message, color):
    print(f"{color}{message}{RESET}")

# Function to check for and execute setup scripts
def run_setup_script(directory, repo_name):
    setup_scripts = ["setup.sh", "install.sh", "configure.sh"]  # Add more if needed
    for script in setup_scripts:
        setup_script = os.path.join(directory, script)
        if os.path.exists(setup_script):
            display_message(f"Running {script} for {repo_name}...", GREEN)
            subprocess.run(["chmod", "+x", setup_script])
            subprocess.run([setup_script])
            return True
    return False

# Function to check for and install requirements
def install_requirements(directory, repo_name):
    requirement_files = ["requirements.txt", "deps.txt", "prerequisites.txt"]  # Add more if needed
    for req_file in requirement_files:
        requirements_file = os.path.join(directory, req_file)
        if os.path.exists(requirements_file):
            display_message(f"Installing requirements for {repo_name}...", GREEN)
            subprocess.run(["pip", "install", "-r", requirements_file])
            return True
    return False

# Clone the repositories
for repo in repositories:
    repo_name = repo.split("/")[-1].replace(".git", "")
    clone_dir = os.path.join(base_directory, repo_name)

    if not os.path.exists(clone_dir):
        display_message(f"Cloning {repo_name}...", GREEN)
        subprocess.run(["git", "clone", repo, clone_dir])
    else:
        display_message(f"{repo_name} is already cloned.", GREEN)

    # Check and run setup scripts
    if not run_setup_script(clone_dir, repo_name):
        display_message(f"No setup scripts found for {repo_name}.", GREEN)

    # Check and install requirements
    if not install_requirements(clone_dir, repo_name):
        display_message(f"No requirements found for {repo_name}.", GREEN)

display_message("All repositories cloned and setup completed successfully.", GREEN)
