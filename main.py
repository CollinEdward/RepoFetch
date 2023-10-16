import os
import subprocess
import logging
import argparse
import json
from colorama import Fore, Style, init
from inquirer import Checkbox, prompt
from concurrent.futures import ThreadPoolExecutor

# Constants
SETUP_SCRIPTS = ["setup.sh", "install.sh", "configure.sh"]
REQUIREMENT_FILES = ["requirements.txt", "deps.txt", "prerequisites.txt"]

# Initialize colorama
init()

# Function to display colored messages
def display_message(message, color):
    print(f"{color}{message}{Style.RESET_ALL}")
    logging.info(message)

# Function to check for and execute setup scripts
def run_setup_scripts(directory, repo_name):
    for script in SETUP_SCRIPTS:
        setup_script = os.path.join(directory, script)
        if os.path.exists(setup_script):
            display_message(f"Running {script} for {repo_name}...", Fore.GREEN)
            try:
                subprocess.run(["chmod", "+x", setup_script], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                subprocess.run([setup_script], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                display_message(f"{script} completed successfully for {repo_name}.", Fore.GREEN)
            except subprocess.CalledProcessError as e:
                display_message(f"Error running {script} for {repo_name}. {e.stderr}", Fore.RED)

# Function to check for and install requirements
def install_requirements(directory, repo_name):
    for req_file in REQUIREMENT_FILES:
        requirements_file = os.path.join(directory, req_file)
        if os.path.exists(requirements_file):
            display_message(f"Installing requirements for {repo_name}...", Fore.GREEN)
            try:
                subprocess.run(["pip", "install", "-r", requirements_file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                display_message(f"Requirements installed successfully for {repo_name}.", Fore.GREEN)
            except subprocess.CalledProcessError as e:
                display_message(f"Error installing requirements for {repo_name}. {e.stderr}", Fore.RED)

# Interactive interface for selecting repositories
def select_repositories(repos):
    questions = [Checkbox('selected_repos', message='Select repositories to clone and set up', choices=repos)]
    answers = prompt(questions)
    return answers['selected_repos']

# User input validation
def validate_input(repos):
    if not repos:
        display_message("No repositories are available for cloning.", Fore.RED)
        exit(1)

# Clone and set up a repository
def clone_and_setup(repo, base_directory):
    repo_name = repo.split("/")[-1].replace(".git", "")
    clone_dir = os.path.join(base_directory, repo_name)

    if not os.path.exists(clone_dir):
        display_message(f"Cloning {repo_name}...", Fore.GREEN)
        try:
            subprocess.run(["git", "clone", repo, clone_dir], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            display_message(f"Cloning completed successfully for {repo_name}.", Fore.GREEN)
        except subprocess.CalledProcessError as e:
            display_message(f"Error cloning {repo_name}. {e.stderr}", Fore.RED)
    else:
        display_message(f"{repo_name} is already cloned.", Fore.GREEN)

    run_setup_scripts(clone_dir, repo_name)
    install_requirements(clone_dir, repo_name)

def main():
    parser = argparse.ArgumentParser(description='Automate GitHub repository setup')
    parser.add_argument('--base-directory', default='tools', help='Base directory for cloning repositories')
    parser.add_argument('--log-file', default='github_tool_automation.log', help='Log file path')
    parser.add_argument('--repositories', help='Path to a JSON file with repository URLs')

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(filename=args.log_file, level=logging.INFO)

    # Load repositories from a JSON file or use default repositories
    if args.repositories:
        with open(args.repositories, 'r') as file:
            repositories = json.load(file)
    else:
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
            "https://github.com/rapid7/metasploit-framework",
            "https://github.com/snort3/snort3",
            "https://github.com/nmap/nmap",
            "https://github.com/wireshark/wireshark",
            "https://github.com/bro/bro",
            "https://github.com/openssl/openssl",
            "https://github.com/OISF/suricata",
            "https://github.com/magnumripper/JohnTheRipper",
            "https://github.com/aircrack-ng/aircrack-ng",
            "https://github.com/zaproxy/zaproxy",
            "https://github.com/OWASP/OWASP-WebScarab",
            "https://github.com/SpiderLabs/ModSecurity",
            "https://github.com/andresriancho/w3af",
            "https://github.com/ossec/ossec-hids",
            "https://github.com/MISP/MISP",
            "https://github.com/philstuart/stunnel",
            "https://github.com/achillean/shodan",
            "https://github.com/fail2ban/fail2ban",
            "https://github.com/BRO-MAGAZINE/Bro_IDS",
            "https://github.com/cuckoosandbox/cuckoo",
            "https://github.com/zeek/zeek",
            "https://github.com/sans-dfir/sift",
            "https://github.com/AliasIO/Wappalyzer",
            "https://github.com/M4sc3r4n0/Evil-Droid",
            "https://github.com/j3ssie/Osmedeus",
            "https://github.com/dxa4481/truffleHog",
            "https://github.com/zricethezav/gitleaks",
            "https://github.com/sqlmapproject/sqlmap",
            "https://github.com/PowerShellMafia/PowerSploit",
            "https://github.com/BC-SECURITY/Empire",
            "https://github.com/byt3bl33d3r/MITMf",
            "https://github.com/s0md3v/XSStrike",
            "https://github.com/chenjj/CORScanner",
            "https://github.com/m4ll0k/WPSeku",
            "https://github.com/tenable/nessus",
            "https://github.com/gchq/CyberChef",
            "https://github.com/lanmaster53/recon-ng",
            "https://github.com/sullo/nikto",
            "https://github.com/OWASP/Amass",
            "https://github.com/sans-dfir/sift-files",
            "https://github.com/beefproject/beef",
            "https://github.com/gophish/gophish",
            "https://github.com/lgandx/Responder",
            "https://github.com/bettercap/bettercap",
            "https://github.com/CISOfy/lynis",
            "https://github.com/vanhauser-thc/thc-hydra",
            "https://github.com/owtf/owtf",
            "https://github.com/blabla1337/skf",
            "https://github.com/Arachni/arachni",
            "https://github.com/wifiphisher/wifiphisher",
            "https://github.com/hakluke/hakrawler",
            "https://github.com/OJ/gobuster",
            "https://github.com/gentilkiwi/mimikatz",
            "https://github.com/rebootuser/LinEnum",
            "https://github.com/byt3bl33d3r/CrackMapExec",
            "https://github.com/lockfale/osint",
            "https://github.com/Abysssec/PeekABoo",
            "https://github.com/riscure/killchain",
            "https://github.com/VirusTotal/yara",
            "https://github.com/secdev/scapy",
            "https://github.com/MISP/MISP",
            "https://github.com/rapid7/nexpose-community",
            "https://github.com/h4cc/BeEF-XSS",
            "https://github.com/webpwnized/mutillidae",
            "https://github.com/0xInfection/JShielder",
            "https://github.com/aboul3la/Sublist3r",
            "https://github.com/appliedsec/dnschef",
            "https://github.com/1N3/BruteX",
            "https://github.com/Moham3dRiahi/XAttacker",
            "https://github.com/Dionach/CMSmap",
            "https://github.com/OffensiveSecurity/kali-linux-iso",
            "https://github.com/laramies/theHarvester",
            "https://github.com/censys/censys",
            "https://github.com/paralax/awesome"
        ]

    validate_input(repositories)
    selected_repositories = select_repositories(repositories)

    os.makedirs(args.base_directory, exist_ok=True)

    # Determine the number of workers based on the CPU count
    max_workers = os.cpu_count() or 4

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(clone_and_setup, selected_repositories, [args.base_directory] * len(selected_repositories))

    display_message("All selected repositories cloned and setup completed.", Fore.GREEN)

if __name__ == "__main__":
    main()
