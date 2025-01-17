## Easy Python2



This script simplifies the creation of Python 2 virtualenv for compatabiltiy with older scripts.
I have seen a lot of people asking how to make a python2 virtualenv with python3 so I made this script to make the process easy

  - Automatic Python 2 Installation: Checks if Python 2.7 is installed and installs it if necessary.
  - Flexible Environment Location: Allows specifying the directory where virtual environments are created.
  - Python 3 and Python 2 Virtual Environments: Sets up a Python 3 virtual environment and uses it to create a Python 2 virtual environment.
  - Version Compatibility: Ensures the correct version of virtualenv (20.16.7) is used for Python 2 compatibility.


---

# Requirements

    Python 3.x
    Python 2.7 (if not installed, the script will attempt to install it)
    Supported OS:
        Linux (Debian/Ubuntu, Red Hat/CentOS)
        Windows (manual Python 2 installation required)


---

Installation

    Clone the repository:

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

    Ensure Python 3 is installed on your system:

    python3 --version

    Install any missing dependencies (e.g., pip for Python 3).


---

# Usage

Basic Syntax

python3 create_envs.py <base_path> <py3_env_name> <py2_env_name>

Arguments

    <base_path>: The directory where virtual environments will be created.
    <py3_env_name>: Name of the Python 3 virtual environment.
    <py2_env_name>: Name of the Python 2 virtual environment.

Optional Flags

    --python3 <path>: Path to the Python 3 interpreter (default: python3).
    --python2 <path>: Path to the Python 2 interpreter (default: python2).

Example

python3 create_envs.py /home/user/envs py3_env py2_env --python2 /usr/bin/python2.7

This will create the following structure:
```
/home/user/envs/
  |- py3_env/  # Python 3 virtual environment
  |- py2_env/  # Python 2 virtual environment
```
Troubleshooting
Error: failed to find interpreter for Builtin discover of python_spec='python2'

This occurs when virtualenv cannot find Python 2. Ensure that:

    Python 2 is installed and accessible via python2 or python2.7.
    Use the --python2 flag to provide the full path to the Python 2 interpreter.

Error: SyntaxError: invalid syntax

This occurs when an incompatible version of virtualenv is used. The script automatically installs virtualenv==20.16.7, which supports Python 2. If the error persists:

    Manually install the compatible version:

    /path/to/py3_env/bin/pip install virtualenv==20.16.7

    Retry creating the Python 2 environment:

    /path/to/py3_env/bin/virtualenv -p /path/to/python2 /path/to/py2_env



---

# Support

If you have found this useful please donate

BTC `bc1qtezfajhysn6dut07m60vtg0s33jy8tqcvjqqzk`
	
