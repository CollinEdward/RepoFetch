# Repository Fetch and Setup Script

This Python script is designed to simplify the process of cloning GitHub repositories and setting up various tools, frameworks, and applications from these repositories for cybersecurity and reconnaissance purposes.

![GitHub repo size](https://img.shields.io/github/repo-size/CollinEdward/RepoFetch)
![GitHub license](https://img.shields.io/github/license/CollinEdward/RepoFetch)

## Features

- **Interactive Interface:** This script provides an interactive interface that allows you to select which repositories to clone and set up.

- **User Input Validation:** Before running, the script validates user input, ensuring that provided URLs are well-formed and the base directory is accessible.

- **Progress Indicators:** The script includes progress indicators to show that it is actively working, providing users with more feedback on the process.

- **Logging:** All actions and results are logged, making it easier to troubleshoot and understand the script's execution.

## Installation

1. Clone this repository:

   ```shell
   git clone https://github.com/CollinEdward/RepoFetch.git
   cd RepoFetch
   ```

2. Install the required Python libraries:

   ```shell
   pip install -r requirements.txt
   ```

3. Run the script:

   ```shell
   python3 main.py
   ```

## Usage

1. Upon running the script, you will be prompted to select the repositories you want to clone and set up. Use the arrow keys to navigate and the spacebar to select.

2. The script will then proceed to clone the selected repositories and run setup scripts (e.g., "setup.sh," "install.sh," or "configure.sh") if available.

3. It will also check for and install any specified requirements listed in files like "requirements.txt," "deps.txt," or "prerequisites.txt."

4. The script logs all actions and results in a file named "github_tool_automation.log" for your reference.

5. After the process is completed, you will receive a summary of the status of the selected repositories.

## Contributing

If you would like to contribute to this project, please open an issue or create a pull request with your suggestions or changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the authors and maintainers of the GitHub repositories that this script helps set up.

Happy hacking and reconnaissance!

