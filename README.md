# Projet-QCMs-info

## Project Overview

This project is designed to create a software tool that generates multiple-choice questions (MCQs) in both AMC (Auto Multiple Choice) and Moodle formats from given code snippets. This tool aims to assist educators in generating quizzes for assessing student knowledge in programming courses effectively and efficiently.

## Features

- **Generation of MCQs in AMC and Moodle formats:** Supports the creation of quizzes in two popular formats which can be imported directly into corresponding platforms.
- **Support for multiple programming languages:** Utilizes Docker to run snippets in various programming languages, ensuring flexibility in question generation.
- **Web-based and CLI versions:** Provides both a command-line interface for quick generation and a web-based interface for ease of use with a graphical user interface.
- **Customizable Question Generation:** Allows users to define custom function calls and input code snippets to generate tailored questions and answers in LaTeX format.

## Installation

### Prerequisites

- **Python:** [Download Python](https://www.python.org/downloads)
- **Docker:** For desktop interface installation, visit [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Required Python Libraries

```bash
pip install docker
pip install mako
pip install argparse
pip install flask  # Only for the web-based version
```

### Running the Application

#### Command Line Interface

1. Navigate to the `ShellProgram` directory.
2. Run `main.py` with the necessary arguments to generate the MCQs.

   ```bash
   python main.py [arguments]
   ```

   The required arguments include:
   - Question name
   - Output format (AMC or Moodle)
   - Programming language key
   - Path to the code file
   - Path to the execution file
   - Path to the incorrect answers file
   - Question type (only for Moodle)

#### Web-based Interface

To use the web-based interface, you can utilize the provided scripts depending on your operating system:

##### For Windows:

1. Navigate to the `GUI` directory.
2. Run the `[WEB-UI] run.cmd` script to start the web application. This script will automatically open your default web browser to the application and start the server.
   
   ```cmd
   [WEB-UI] run.cmd
   ```

##### For Linux:

1. Navigate to the `GUI` directory.
2. Run the `[Linux_only].sh` script to start the web application. This script initializes the server and you may need to manually open a web browser and navigate to `http://127.0.0.1:5000`.
   
   ```bash
   bash [Linux_only].sh
   ```

3. Access the web interface through your browser to input the details and generate the MCQs. If the script does not automatically open your browser, you can manually enter the URL `http://127.0.0.1:5000` in your browser to access the application.

## Usage

- **Generate MCQs:** Input the code snippet, function calls, and incorrect answers. The tool generates questions in LaTeX format which can then be compiled to PDF for AMC or exported to XML for Moodle.
- **Customize Questions:** Through the provided interfaces, you can customize the MCQs by changing the programming languages, types of questions, and more.

## Output

The generated files will be placed in the `Outputs` directory or can be downloaded directly from the web interface, depending on the version used. These include LaTeX files and code snippets prepared for import into AMC or Moodle.

## GitHub Repository

The project is available on GitHub at the following URL: [Project QCMs Info](https://github.com/Frenox/Projet-QCMs-info)

## License

This project is released under the GNU General Public License v3.0, which is a free, copyleft license for software and other kinds of works. The full text of the license can be found at the [GNU website](https://www.gnu.org/licenses/gpl-3.0.html).

### Key Points of the GNU GPL v3.0 License:

- **Freedom to Share and Change:** The GPL v3.0 is designed to guarantee your freedom to share and modify the software—to ensure the software remains free for all its users.
  
- **Protection of Your Rights:** To protect your rights, we need to prevent others from denying you these rights or asking you to surrender them. If you distribute copies of the software, or if you modify it, you must pass on to the recipients the same freedoms that you received.

- **Developer and Author Protection:** The GPL clearly explains that there is no warranty for this free software.

### Responsibilities Under the GPL v3.0:

- When you convey or distribute the software, you must include the complete Corresponding Source or a legally-binding offer to provide the Corresponding Source.
  
- You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy.

- If the software includes interactive user interfaces, each must display Appropriate Legal Notices to the extent that it includes a convenient and prominently visible feature that displays an appropriate copyright notice and tells the user that there is no warranty for the work.

### Conclusion:

By using, modifying, or distributing this software, you accept and agree to be bound by the terms of the GNU General Public License v3.0. For detailed terms and conditions, please refer to the [full license](https://www.gnu.org/licenses/gpl-3.0.html).

Feel free to clone the repository, participate in its development, and suggest improvements or report issues. This license ensures