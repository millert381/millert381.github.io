## Virtual Env for Python

A Python virtual environment is a self-contained directory that encapsulates a specific Python interpreter and its associated libraries and packages. It allows you to create isolated environments for Python projects, ensuring that dependencies do not interfere with each other. It's considered good practice to use virtual environments for your projects. Here's a brief description of Python virtual environments:

1. **Isolation**: Virtual environments provide a way to isolate different Python projects from each other. This means that you can have one project with specific library versions and dependencies that won't conflict with another project's requirements.

2. **Dependency Management**: You can install and manage project-specific dependencies within a virtual environment, making it easier to keep track of which packages are required for a particular project. This helps prevent version conflicts and keeps your system-wide Python installation clean.

3. **Version Compatibility**: Virtual environments allow you to use different versions of Python for different projects. For example, you can have one project that uses Python 2.7 and another that uses Python 3.8, without conflicts.

4. **Easy Activation/Deactivation**: You can easily activate or deactivate a virtual environment, which changes the Python interpreter and environment variables to work within the isolated environment. This is particularly useful when working on multiple projects simultaneously.

5. **Portability**: Virtual environments can be created and used on different systems. This makes it easier to share projects with colleagues or deploy them to different environments without worrying about dependencies.

To create a virtual environment in Python, you can use tools like `virtualenv` or Python's built-in module called `venv`. Once created, you can activate the virtual environment to start working within it, and deactivate it when you're done.

Here's a basic example of creating and activating a virtual environment using `venv`:

```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment (on Windows)
myenv\Scripts\activate

# Activate the virtual environment (on macOS and Linux)
source myenv/bin/activate
```

Once activated, you can install packages using `pip`, and they will be installed only within the virtual environment, keeping your project's dependencies isolated. To deactivate the environment and return to the system-wide Python, you can simply run `deactivate` in the command prompt.


## Practical Example
On my machine, I have Python 2.7 and Python 3.7 installed. Initially, I was trying to install `mkdocs` and the `mkdocs-material` theme.  However, I was running into errors installing the packages required for the theme. The issue was related to the version of `pip` that was being used during the install. By creating a virtual environment for my mkdocs documentation project, I was able to avoid conflicts between the Python versions.

Here's how to create and activate a virtual environment using Python 3:

```bash
# Create a virtual environment for Python 3.7
python3 -m venv myenv

# Activate the virtual environment (Linux/Mac)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate
```

Now, you're in a virtual environment that uses Python 3. You can use `pip` and `python` without specifying versions, and they will refer to the Python version within the virtual environment.

Install your project's dependencies within this virtual environment:

```bash
pip install mkdocs mkdocs-material
```

When you're done working on the project, deactivate the virtual environment:

```bash
deactivate
```

Using virtual environments helps keep your project dependencies isolated, making it easier to manage multiple Python versions and packages for different projects.