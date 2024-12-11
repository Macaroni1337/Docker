# Dockerized Environment Manager

The Dockerized Environment Manager is a Python-based tool designed to simplify the creation, management, and control of Docker environments. With this program, users can easily manage Docker containers using a simple text-based interface.

---

## Features

1. **List Environments**:
   - View all available Docker environments stored in the configuration file.

2. **Create New Environments**:
   - Define new Docker environments with an image and optional port mappings.

3. **Start Environments**:
   - Launch Docker containers for the defined environments.

4. **Stop Environments**:
   - Stop and remove running Docker containers by name.

5. **Update Environments**:
   - Modify existing environment configurations (e.g., change the Docker image or ports).

6. **Check Environment Status**:
   - View all running Docker containers using the `docker ps` command.

---

## How to Use

### Prerequisites
- Ensure Docker is installed and running on your system.
- Ensure Python 3.6 or later is installed.
- Place the `docker_envs.json` configuration file in the same directory as the script.

### Running the Program
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `docker_env_manager.py` script.
3. Run the script using:
   ```bash
   python docker_env_manager.py
   ```
4. Upon launch, you will see an ASCII art banner displaying "Docker" and a menu with options.

### Basic Functions

#### 1. List Environments
   - Select option `1` from the menu.
   - The program will display all configured environments along with their images and port mappings.

#### 2. Create a New Environment
   - Select option `2`.
   - Provide a name for the environment.
   - Specify the Docker image (e.g., `python:3.9`).
   - Optionally, provide port mappings in the format `host_port:container_port` (e.g., `8080:80`).

#### 3. Start an Environment
   - Select option `3`.
   - Enter the name of the environment to start.
   - The program will execute a `docker run` command to launch the container.

#### 4. Stop an Environment
   - Select option `4`.
   - Enter the name of the running environment to stop.
   - The program will stop and remove the container.

### Advanced Features

#### 5. Update an Environment
   - Select option `5`.
   - Provide the name of the environment to update.
   - Modify the Docker image or port mappings as needed.
   - The changes will be saved to the configuration file.

#### 6. Check Environment Status
   - Select option `6`.
   - The program will display all running Docker containers using the `docker ps` command.

---

## Configuration File: `docker_envs.json`
The program uses a JSON file to store environment configurations. Below is an example structure:

```json
{
    "example_env": {
        "image": "nginx:latest",
        "ports": "8080:80"
    }
}
```
- **Key**: Environment name.
- **Value**: Dictionary containing:
  - `image`: Docker image name.
  - `ports`: Port mappings (comma-separated for multiple mappings).

---

## Example Usage
1. Create a new environment named `web_server` using the `nginx:latest` image and map port `8080` to `80`:
   ```
   Choose an option: 2
   Enter a name for the environment: web_server
   Enter the Docker image (e.g., python:3.9): nginx:latest
   Enter port mappings (e.g., 8080:80, optional): 8080:80
   ```

2. Start the `web_server` environment:
   ```
   Choose an option: 3
   Enter the environment name to start: web_server
   ```

3. Stop the `web_server` environment:
   ```
   Choose an option: 4
   Enter the environment name to stop: web_server
   ```

---

## Notes
- The program assumes Docker is installed and accessible via the `docker` command.
- Port mappings are optional; containers can be started without them.
- Changes to the `docker_envs.json` file are immediate and persistent.

---

## Troubleshooting
1. **Docker Not Found**:
   - Ensure Docker is installed and added to your system's PATH.

2. **Permission Errors**:
   - Run the script with appropriate permissions or ensure your user has access to the Docker CLI.

3. **Invalid Commands**:
   - Verify the Docker commands used in the script are valid for your version of Docker.

---

Enjoy managing your Docker environments efficiently!

