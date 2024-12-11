import os
import subprocess
import json

CONFIG_FILE = "docker_envs.json"

ASCII_ART = """
 ______ _____ _____  _   __ ___________ 
|  _  \  _  /  __ \| | / /|  ___| ___ \
| | | | | | | /  \/| |/ / | |__ | |_/ /
| | | | | | | |    |    \ |  __||    / 
| |/ /\ \_/ / \__/\| |\  \| |___| |\ \ 
|___/  \___/ \____/\_| \_/\____/\_| \_|   
"""

def load_config():
    """Load environment configurations from a JSON file."""
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w") as f:
            json.dump({}, f, indent=4)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    """Save environment configurations to a JSON file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def list_environments(config):
    """List all available environments."""
    if not config:
        print("No environments available.")
        return
    print("Available environments:")
    for name, details in config.items():
        print(f"- {name}: {details['image']} (ports: {details['ports']})")

def create_environment(config):
    """Create a new Docker environment."""
    name = input("Enter a name for the environment: ")
    image = input("Enter the Docker image (e.g., python:3.9): ")
    ports = input("Enter port mappings (e.g., 8080:80, optional): ")

    if name in config:
        print(f"Environment '{name}' already exists.")
        return

    config[name] = {
        "image": image,
        "ports": ports
    }
    save_config(config)
    print(f"Environment '{name}' created.")

def start_environment(config):
    """Start a Docker environment."""
    name = input("Enter the environment name to start: ")
    if name not in config:
        print(f"Environment '{name}' does not exist.")
        return

    details = config[name]
    ports = ""
    if details["ports"]:
        ports = " ".join([f"-p {p}" for p in details["ports"].split(",")])

    cmd = f"docker run -d --name {name} {ports} {details['image']}"
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True)

def stop_environment():
    """Stop a running Docker environment."""
    name = input("Enter the environment name to stop: ")
    cmd = f"docker stop {name} && docker rm {name}"
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True)

def update_environment(config):
    """Update an existing Docker environment configuration."""
    name = input("Enter the name of the environment to update: ")
    if name not in config:
        print(f"Environment '{name}' does not exist.")
        return

    print(f"Current configuration: {config[name]}")
    image = input(f"Enter new Docker image (leave blank to keep '{config[name]['image']}'): ")
    ports = input(f"Enter new port mappings (leave blank to keep '{config[name]['ports']}'): ")

    if image:
        config[name]['image'] = image
    if ports:
        config[name]['ports'] = ports

    save_config(config)
    print(f"Environment '{name}' updated.")

def check_environment_status():
    """Check the status of running Docker containers."""
    cmd = "docker ps"
    print("Checking running containers:")
    subprocess.run(cmd, shell=True)

def main():
    print(ASCII_ART)
    config = load_config()

    while True:
        print("\nDockerized Environment Manager")
        print("1. List environments")
        print("2. Create a new environment")
        print("3. Start an environment")
        print("4. Stop an environment")
        print("5. Update an environment")
        print("6. Check environment status")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            list_environments(config)
        elif choice == "2":
            create_environment(config)
        elif choice == "3":
            start_environment(config)
        elif choice == "4":
            stop_environment()
        elif choice == "5":
            update_environment(config)
        elif choice == "6":
            check_environment_status()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
