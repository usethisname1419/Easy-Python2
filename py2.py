import os
import subprocess
import argparse
import sys
import platform

def run_command(command, fail_message, shell=False):
    """Run a shell command and exit on failure."""
    try:
        subprocess.run(command, check=True, shell=shell)
    except subprocess.CalledProcessError:
        print(fail_message)
        exit(1)

def check_and_install_python2():
    """Check if Python 2.7 is installed, and install it if not."""
    print("Checking for Python 2.7...")
    try:
        subprocess.run(["python2", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python 2.7 is already installed.")
    except subprocess.CalledProcessError:
        print("Python 2.7 is not installed. Attempting to install...")
        if os.name == "posix":
            if os.path.exists("/etc/debian_version"):
                run_command(
                    "sudo apt-get update && sudo apt-get install -y python2",
                    "Failed to install Python 2.7 on Debian/Ubuntu.",
                    shell=True
                )
            elif os.path.exists("/etc/redhat-release"):
                run_command(
                    "sudo yum install -y python2",
                    "Failed to install Python 2.7 on Red Hat/CentOS.",
                    shell=True
                )
            else:
                print("Unsupported Linux distribution. Please install Python 2.7 manually.")
                exit(1)
        elif os.name == "nt":
            print("Please install Python 2.7 manually from https://www.python.org/ftp/python/2.7/")
            exit(1)
        else:
            print("Unsupported operating system. Please install Python 2.7 manually.")
            exit(1)

def create_envs(base_path, py3_env, py2_env, python3_path="python3", python2_path="python2"):
    """Create Python 3 and Python 2 virtual environments."""
    # Ensure the base directory exists
    if not os.path.exists(base_path):
        print(f"Creating directory {base_path}...")
        os.makedirs(base_path)

    py3_env_path = os.path.join(base_path, py3_env)
    py2_env_path = os.path.join(py3_env_path, py2_env)  # Python 2 env will be inside the Python 3 env

    # Step 1: Create Python 3 virtual environment
    print(f"Creating Python 3 virtual environment at {py3_env_path}...")
    run_command([python3_path, "-m", "venv", py3_env_path], "Failed to create Python 3 virtual environment.")

    # Step 2: Install virtualenv in Python 3 virtual environment
    py3_pip = os.path.join(py3_env_path, "bin", "pip")  # Linux/macOS
    if os.name == "nt":
        py3_pip = os.path.join(py3_env_path, "Scripts", "pip.exe")  # Windows
    print(f"Installing virtualenv in Python 3 virtual environment using {py3_pip}...")
    run_command([py3_pip, "install", "virtualenv==20.16.7"], "Failed to install virtualenv in Python 3 virtual environment.")

    # Step 3: Create Python 2 virtual environment inside the Python 3 virtual environment
    print(f"Creating Python 2 virtual environment at {py2_env_path}...")
    run_command([py3_pip, "install", "virtualenv"], "Failed to install virtualenv for Python 2.")
    run_command(
        [py3_pip.replace("pip", "virtualenv"), "-p", python2_path, py2_env_path],
        "Failed to create Python 2 virtual environment."
    )

    # Step 4: Print activation instruction
    if platform.system() == "Windows":
        activate_script = os.path.join(py2_env_path, "Scripts", "activate.bat")
        print(f"\nTo activate the Python 2 environment, run the following command:\n")
        print(f"  {activate_script}")
    else:
        activate_script = os.path.join(py2_env_path, "bin", "activate")
        print(f"\nTo activate the Python 2 environment, run the following command:\n")
        print(f"  source {activate_script}")

    print(f"\nSuccess! Python 3 virtual environment '{py3_env_path}' and Python 2 virtual environment '{py2_env_path}' are ready.")
    print("\nYou can now activate the Python 2 environment manually.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Python 2 and Python 3 virtual environments with automatic setup.")
    parser.add_argument("base_path", help="Path to the directory where virtual environments will be created.")
    parser.add_argument("py3_env", help="Name of the Python 3 virtual environment.")
    parser.add_argument("py2_env", help="Name of the Python 2 virtual environment.")
    parser.add_argument("--python3", default="python3", help="Path to Python 3 interpreter (default: python3).")
    parser.add_argument("--python2", default="python2", help="Path to Python 2 interpreter (default: python2).")

    args = parser.parse_args()

    # Step 1: Check and install Python 2.7 if necessary
    check_and_install_python2()

    # Step 2: Create the virtual environments
    create_envs(args.base_path, args.py3_env, args.py2_env, args.python3, args.python2)

