# Python assessment

## Description

This Python application can be used to generate a Microsoft PowerPoint presentation from a json configuration file.

## Prerequisites

- The system must have `git` and `Python` with `pip` installed.
- The application has been tested on Windows 11 22H2 and on Ubuntu 22.04.2 LTS
- On Windows systems it's recommended to use [Git BASH](https://gitforwindows.org/)

## Installation

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/konczosi/python-assessment.git
    ```
1. Navigate to the repo:
    ```bash
    cd python-assessment/
    ```
2. Create a virtual Python environment in the repo (e.g. with venv):
    ```bash
    python3 -m venv .venv
    ```
3. Activate the virtual environment
    
    Linux
    ```bash
    source .venv/bin/activate 
    ```
    Windows
     ```bash
    source .venv/Scripts/activate
    ```

4. Install the required packages with pip:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage
- Simply run the `app.py` python file with the name of the configuration file, or its absolute/relative path
    ```bash
    python app.py config-file
    ```
- For example, to generate the example presentation run:
    ```bash
    python app.py Task1_PPTX_report/sample.json
    ```
- The generated report can be found in the root directory of the application as `output.pptx`

## Caveats
- The program searches for csv and image files in the Task1_PPTX_report folder. These files must be put here.
- The app currently resizes images to the same width. Manual scaling may be required after report generation.

## Roadmap
- Use Docker to containerize the application.
- Write extensive unit tests.
- Find a better solution to handle image and data files.
- Find a better way to resize the images to fit in the slides.
