# Docker Desktop

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Docker Desktop is a one-click-install application for your Mac, Linux, or Windows environment that enables you to build and share containerized applications and microservices. It provides an easy-to-use GUI (Graphical User Interface) that lets you manage your containers, applications, and images directly from your machine. It includes Docker Engine, Docker CLI client, Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper.

## Website / Link
- [Official Website](https://www.docker.com/products/docker-desktop/)
- [Documentation](https://docs.docker.com/desktop/)

## Installation
Docker Desktop is available for Windows, Mac, and Linux.
1. Download the installer from the [official download page](https://www.docker.com/products/docker-desktop/).
2. Run the installer and follow the on-screen instructions.
3. Once installed, start Docker Desktop to initialize the Docker engine.

## Useful Commands / Tips
- `docker ps`: List all running containers.
- `docker ps -a`: List all containers (running and stopped).
- `docker images`: List all locally stored Docker images.
- `docker build -t <name> .`: Build a Docker image from a Dockerfile in the current directory.
- `docker run -p <host_port>:<container_port> <image_name>`: Run a container mapping a host port to a container port.
- `docker-compose up -d`: Start services defined in `docker-compose.yml` in detached mode (background).
- `docker-compose down`: Stop and remove containers, networks, images, and volumes created by `up`.
- `docker exec -it <container_id_or_name> /bin/bash` (or `sh`): Open an interactive shell inside a running container.
- `docker logs <container_id_or_name>`: Fetch the logs of a container.
- `docker system prune`: Remove unused data (stopped containers, unused networks, dangling images, build cache).

## Configuration
- Docker Desktop settings can be accessed via the gear icon in the GUI.
- You can configure:
    - **Resources**: CPU, Memory, Swap, Disk image size.
    - **Docker Engine**: JSON configuration for the daemon.
    - **Kubernetes**: Enable/disable the local Kubernetes cluster.
    - **Extensions**: Add third-party tools to Docker Desktop.

## Notes
- Essential for ensuring development environments match production.
- Greatly simplifies setting up dependencies (databases, redis, etc.) locally without polluting the host OS.
- The "Dev Environments" feature allows sharing work-in-progress code with team members.

---

# Version Française

## Description
Docker Desktop est une application d'installation en un clic pour votre environnement Mac, Linux ou Windows qui vous permet de créer et de partager des applications conteneurisées et des microservices. Il fournit une interface graphique facile à utiliser pour gérer vos conteneurs, applications et images directement depuis votre machine. Il inclut Docker Engine, le client Docker CLI, Docker Compose, Docker Content Trust, Kubernetes et Credential Helper.

## Site Web / Lien
- [Site Officiel](https://www.docker.com/products/docker-desktop/)
- [Documentation](https://docs.docker.com/desktop/)

## Installation
Docker Desktop est disponible pour Windows, Mac et Linux.
1. Téléchargez l'installateur depuis la [page de téléchargement officielle](https://www.docker.com/products/docker-desktop/).
2. Exécutez l'installateur et suivez les instructions à l'écran.
3. Une fois installé, démarrez Docker Desktop pour initialiser le moteur Docker.

## Commandes Utiles / Astuces
- `docker ps` : Lister tous les conteneurs en cours d'exécution.
- `docker ps -a` : Lister tous les conteneurs (en cours d'exécution et arrêtés).
- `docker images` : Lister toutes les images Docker stockées localement.
- `docker build -t <nom> .` : Construire une image Docker à partir d'un Dockerfile dans le répertoire actuel.
- `docker run -p <port_h>:<port_c> <nom_image>` : Exécuter un conteneur en mappant un port hôte à un port conteneur.
- `docker-compose up -d` : Démarrer les services définis dans `docker-compose.yml` en mode détaché (arrière-plan).
- `docker-compose down` : Arrêter et supprimer les conteneurs, réseaux, images et volumes créés par `up`.
- `docker exec -it <id_ou_nom> /bin/bash` (ou `sh`) : Ouvrir un shell interactif dans un conteneur en cours d'exécution.
- `docker logs <id_ou_nom>` : Récupérer les journaux d'un conteneur.
- `docker system prune` : Supprimer les données inutilisées (conteneurs arrêtés, réseaux inutilisés, images, cache).

## Configuration
- Les paramètres de Docker Desktop sont accessibles via l'icône d'engrenage dans l'interface graphique.
- Vous pouvez configurer :
    - **Ressources** : CPU, Mémoire, Swap, Taille d'image disque.
    - **Docker Engine** : Configuration JSON pour le démon.
    - **Kubernetes** : Activer/désactiver le cluster Kubernetes local.
    - **Extensions** : Ajouter des outils tiers à Docker Desktop.

## Notes
- Essentiel pour garantir que les environnements de développement correspondent à la production.
- Simplifie grandement la mise en place des dépendances (bases de données, redis, etc.) localement sans polluer l'OS hôte.
- La fonctionnalité "Dev Environments" permet de partager le code en cours avec les membres de l'équipe.
