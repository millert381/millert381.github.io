To avoid conflicts between Python versions and their dependencies, it's a good practice to use virtual environments for your projects. Create a separate virtual environment for each project and choose the Python version for that environment.

Here's how to run your local mkdocs server for testing:

```bash
# Activate the virtual environment (Windows)
myenv\Scripts\activate

# Change to directory where your mkdocs config (.yml) file is located
cd "G:\My Drive\mkdocs\everything-in-one-place"

# Run command to start local server
mkdocs serve
```

Now, open a browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)