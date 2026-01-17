# Debian 12 (Bookworm)

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Debian 12, codenamed "Bookworm", is a stable and versatile Linux distribution. It is known for its commitment to free software and its robustness, making it ideal for both servers and desktops.

## Website / Link
- [Official Website](https://www.debian.org/)
- [Debian 12 Release Notes](https://www.debian.org/releases/bookworm/releasenotes)

## Installation
```bash
# Download the "netinst" ISO for a minimal setup or a full DVD ISO
# Use 'dd' or a tool like Ventoy to create a bootable USB
```

## Useful Commands / Tips
- `apt update && apt upgrade`: Basic maintenance
- `apt install [package]`: Install a new package
- `systemctl status [service]`: Check service status

## Configuration
- `/etc/apt/sources.list`: Manage your repositories (non-free-firmware is now a separate component in Debian 12).
- `sudo` setup: If not configured during install, run `su -` then `apt install sudo && usermod -aG sudo [username]`.

## Notes
Debian 12 includes over 11,000 new packages compared to the previous version.

---

# Version Française

## Description
Debian 12, nom de code "Bookworm", est une distribution Linux stable et polyvalente. Elle est réputée pour son engagement envers le logiciel libre et sa robustesse, ce qui la rend idéale aussi bien pour les serveurs que pour les postes de travail.

## Site Web / Lien
- [Site Officiel](https://www.debian.org/)
- [Notes de version Debian 12](https://www.debian.org/releases/bookworm/releasenotes)

## Installation
```bash
# Téléchargez l'ISO "netinst" pour une installation minimale ou un DVD ISO complet
# Utilisez 'dd' ou un outil comme Ventoy pour créer une clé USB bootable
```

## Commandes Utiles / Astuces
- `apt update && apt upgrade` : Maintenance de base
- `apt install [paquet]` : Installer un nouveau paquet
- `systemctl status [service]` : Vérifier l'état d'un service

## Configuration
- `/etc/apt/sources.list` : Gérez vos dépôts (non-free-firmware est désormais un composant séparé dans Debian 12).
- Configuration `sudo` : Si non configuré lors de l'installation, lancez `su -` puis `apt install sudo && usermod -aG sudo [utilisateur]`.

## Notes
Debian 12 comprend plus de 11 000 nouveaux paquets par rapport à la version précédente.
