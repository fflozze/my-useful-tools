# Alpine Linux

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Alpine Linux is a security-oriented, lightweight Linux distribution based on musl libc and busybox. It is popular for Docker containers due to its small footprint.

## Website / Link
- [Official Website](https://alpinelinux.org/)
- [Wiki](https://wiki.alpinelinux.org/)

## Installation
```bash
# For a standard install:
setup-alpine
```

## Useful Commands / Tips
- `apk update`: Update package list
- `apk add [package]`: Install a package
- `apk del [package]`: Remove a package
- `rc-service [service] [command]`: Manage services (OpenRC)

## Configuration
- `/etc/apk/repositories`: List of repositories.
- `/etc/network/interfaces`: Network configuration.

## Notes
Alpine uses OpenRC instead of systemd and musl instead of glibc, which can lead to compatibility issues with some software.

---

# Version Française

## Description
Alpine Linux est une distribution Linux légère et axée sur la sécurité, basée sur musl libc et busybox. Elle est très populaire pour les conteneurs Docker en raison de sa petite taille.

## Site Web / Lien
- [Site Officiel](https://alpinelinux.org/)
- [Wiki](https://wiki.alpinelinux.org/)

## Installation
```bash
# Pour une installation standard :
setup-alpine
```

## Commandes Utiles / Astuces
- `apk update` : Mettre à jour la liste des paquets
- `apk add [paquet]` : Installer un paquet
- `apk del [paquet]` : Supprimer un paquet
- `rc-service [service] [commande]` : Gérer les services (OpenRC)

## Configuration
- `/etc/apk/repositories` : Liste des dépôts.
- `/etc/network/interfaces` : Configuration réseau.

## Notes
Alpine utilise OpenRC au lieu de systemd et musl au lieu de glibc, ce qui peut entraîner des problèmes de compatibilité avec certains logiciels.
