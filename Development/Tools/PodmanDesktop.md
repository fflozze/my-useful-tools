# Podman Desktop

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Podman Desktop is an open-source graphical tool for managing containers and Kubernetes. It provides a user-friendly interface for working with Podman, Docker, and other container engines, offering a lightweight and free alternative to Docker Desktop. It allows developers to build, run, and manage containers, samples, and work with Kubernetes pods and clusters directly from their local machine.

## Website / Link
- [Official Website](https://podman-desktop.io/)
- [GitHub Repository](https://github.com/containers/podman-desktop)

## Installation
```bash
# Windows (via Chocolatey)
choco install podman-desktop

# Windows (via Winget)
winget install -e --id RedHat.Podman-Desktop

# macOS (via Brew)
brew install podman-desktop

# Linux (Flatpak)
flatpak install flathub io.podman_desktop.PodmanDesktop
```

## Useful Commands / Tips
- **Manage Containers**: Easily start, stop, restart, and delete containers via the GUI.
- **Kubernetes**: Create and run Kubernetes pods from containers; generate K8s YAML manifests.
- **Extensions**: Supports Docker Desktop extensions and has its own extension system.
- **Compatibility**: Works seamlessly with Podman, Docker, Lima, Kind, Red Hat OpenShift, etc.

## Configuration
- **Preferences**: Accessible via the gear icon. Configure proxies, container engines, and Kubernetes contexts.
- **Registries**: Manage image registries (Docker Hub, Quay.io, etc.) under Settings > Registries.

## Notes
- Excellent for those looking to migrate away from Docker Desktop due to licensing changes.
- Provides a "tray" icon for quick access to status and common actions.
- Often works best when Podman is already installed on the system.

---

# Version Française

## Description
Podman Desktop est un outil graphique open source pour gérer les conteneurs et Kubernetes. Il offre une interface conviviale pour travailler avec Podman, Docker et d'autres moteurs de conteneurs, offrant une alternative légère et gratuite à Docker Desktop. Il permet aux développeurs de construire, exécuter et gérer des conteneurs, des exemples, et de travailler avec des pods et clusters Kubernetes directement depuis leur machine locale.

## Site Web / Lien
- [Site Officiel](https://podman-desktop.io/)
- [Dépôt GitHub](https://github.com/containers/podman-desktop)

## Installation
```bash
# Windows (via Chocolatey)
choco install podman-desktop

# Windows (via Winget)
winget install -e --id RedHat.Podman-Desktop

# macOS (via Brew)
brew install podman-desktop

# Linux (Flatpak)
flatpak install flathub io.podman_desktop.PodmanDesktop
```

## Commandes Utiles / Astuces
- **Gérer les conteneurs** : Démarrez, arrêtez, redémarrez et supprimez facilement des conteneurs via l'interface graphique.
- **Kubernetes** : Créez et exécutez des pods Kubernetes à partir de conteneurs ; générez des manifestes YAML K8s.
- **Extensions** : Prend en charge les extensions Docker Desktop et possède son propre système d'extensions.
- **Compatibilité** : Fonctionne de manière transparente avec Podman, Docker, Lima, Kind, Red Hat OpenShift, etc.

## Configuration
- **Préférences** : Accessible via l'icône d'engrenage. Configurez les proxys, les moteurs de conteneurs et les contextes Kubernetes.
- **Registres** : Gérez les registres d'images (Docker Hub, Quay.io, etc.) sous Paramètres > Registres.

## Notes
- Excellent pour ceux qui cherchent à migrer depuis Docker Desktop en raison des changements de licence.
- Fournit une icône dans la barre des tâches pour un accès rapide à l'état et aux actions courantes.
- Fonctionne souvent mieux lorsque Podman est déjà installé sur le système.
