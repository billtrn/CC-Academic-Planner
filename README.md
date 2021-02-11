# Academic Planner
Connecticut College CS Research project 2020-2021

Researcher: Chelsea Vickers, advised by Professor Christine Chung

## Instructions for how to download and extract the code files:
1. On the GitHub repository page for this project (presumably the page you are currently reading this on: https://github.com/cvickers23/CC-Academic-Planner), click the green "Code" download button near the top right. In the drop down menu that appears, click "Download ZIP" and a compressed folder in the form of a ZIP file with all the project files will begin to download.

2. Once the file has downloaded, extract the folder from the ZIP file in your "Downloads" folder, or wherever your downloaded files are saved on your machine, by doing one of the following:
    - Mac: Double click on the ZIP file to extract it.
    - Windows: Right click the ZIP file and select "Extract all" to extract it.
    
3. Right-click on the extracted folder (it should be called "CC-Academic-Planner-master" or "CC-Academic-Planner") and do one of the following:
    - Mac Option 1: Right-click on the folder and select "New Terminal at Folder" from the drop down menu.
    - Mac Option 2: Open up Terminal and cd to the folder.
    - Windows Option 1: Press Shift + right-click the folder and then select "Open command window here" from the drop down menu. If this option is not available, you can add it by following the steps given here: https://www.groovypost.com/howto/microsoft/vista/add-command-prompt-option-to-explorer-context-menu/.
    - Windows Option 2: Open up Command Prompt and cd to the folder.
    
## Instructions on how run the program:
**NOTE: Make sure that you use pip on the same version of python as the version you run the program on! You may have issues if you are using Python 3.9, so try to use 3.8 or below.**

1. Once you are in Command Prompt or Terminal and at the project directory, type the following each of the following commands (if using a conda virtual environment, replace pip with conda), pressing Enter after each command:
    - pip install Flask
    - pip install Flask-WTF
    - pip install pandas
    
2. Continue through any prompts that come up when the packages are downloading and installing.

3. Once the package installation is complete, type the following command and then press Enter to run the program (specify python version if necessary):
    - Mac: python app.py
    - Windows: py app.py

4. The following output will print out:
     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 179-082-709

5. Either copy and paste the link into your web browser to open up the web application, or click on one of the following links (if one doesn't work, try another):
    - http://0.0.0.0:5000/
    - http://127.0.0.1:5000/
    - http://localhost:5000/
