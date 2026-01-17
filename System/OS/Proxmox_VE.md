# Proxmox VE (Virtual Environment)
**Domain:** Server & Virtualization

> [!TIP]
> [Passer à la version française](#version-française)

## Description
An enterprise-class virtualization solution based on Debian. It transforms a standard computer into a powerful server capable of hosting multiple virtual machines (VMs) utilizing KVM and containers (LXC). It offers a web-based interface for managing everything from networking to storage.

## Website / Link
- [Official Website](https://www.proxmox.com/)
- [Documentation (Wiki)](https://pve.proxmox.com/wiki/Main_Page)
- [Community Forum](https://forum.proxmox.com/)

## Installation
1.  Download the Proxmox VE ISO from the official website.
2.  Flash it to a USB drive using [Ventoy](./../Utilities/Ventoy.md) or Rufus.
3.  Boot your server from the USB drive and follow the installation wizard.

## Useful Commands / Tips
-   **Terminal Management:**
    -   `qm list`: List all VMs and their status.
    -   `qm start <vmid>`: Start a specific VM.
    -   `qm stop <vmid>`: Stop a specific VM.
    -   `pct list`: List all LXC containers.
    -   `pct enter <vmid>`: Enter the shell of an LXC container.
-   **Updates:**
    -   Proxmox uses Debian repositories. You can edit `/etc/apt/sources.list` to use the "no-subscription" repository for free updates if you don't have an enterprise license.
-   **Removing Subscription Notice:**
    -   There are scripts available online (like tteck's Proxmox scripts) to remove the "You do not have a valid subscription" login banner.

## Configuration
-   **Web Interface:** Accessed via `https://<YOUR-IP>:8006`.
-   **ZFS (RAIDZ):** Proxmox has native support for ZFS. This is a huge feature for data integrity, offering protection against bit rot (silent data corruption). It's highly recommended for homelabs, allowing you to create robust storage arrays without a dedicated hardware RAID controller.

## Notes
-   Great for Homelabs because it's free and powerful.
-   Supports clustering if you have multiple nodes.

---

# Version Française

## Description
Une solution de virtualisation de classe entreprise basée sur Debian. Elle permet de transformer un ordinateur en serveur capable d'héberger plusieurs machines virtuelles (VM) et conteneurs (LXC). Elle offre une interface web complète pour gérer le réseau, le stockage et les instances.

## Site Web / Lien
- [Site Officiel](https://www.proxmox.com/)
- [Documentation (Wiki)](https://pve.proxmox.com/wiki/Main_Page)
- [Forum Communautaire](https://forum.proxmox.com/)

## Installation
1.  Téléchargez l'ISO de Proxmox VE depuis le site officiel.
2.  Flashez-le sur une clé USB en utilisant [Ventoy](./../Utilities/Ventoy.md) ou Rufus.
3.  Démarrez votre serveur sur la clé USB et suivez l'assistant d'installation.

## Commandes Utiles / Astuces
-   **Gestion en Terminal :**
    -   `qm list` : Lister toutes les VM et leur statut.
    -   `qm start <vmid>` : Démarrer une VM spécifique.
    -   `qm stop <vmid>` : Arrêter une VM spécifique.
    -   `pct list` : Lister tous les conteneurs LXC.
    -   `pct enter <vmid>` : Entrer dans le shell d'un conteneur LXC.
-   **Mises à jour :**
    -   Proxmox utilise les dépôts Debian. Vous pouvez modifier `/etc/apt/sources.list` pour utiliser le dépôt "no-subscription" pour des mises à jour gratuites si vous n'avez pas de licence entreprise.
-   **Supprimer la notification d'abonnement :**
    -   Il existe des scripts (comme les "Proxmox Helper Scripts" de tteck) pour supprimer la bannière de connexion "You do not have a valid subscription".

## Configuration
-   **Interface Web :** Accessible via `https://<VOTRE-IP>:8006`.
-   **Fonctionnalité Clé : ZFS (RAIDZ)**
    -   Sa gestion native de **ZFS** est un atout majeur. Contrairement au RAID matériel classique, le RAIDZ protège contre la "corruption silencieuse" des données (bit rot). C'est idéal pour recycler du vieux matériel en un serveur domestique (Homelab) ultra-robuste.

## Notes
-   Excellent pour les Homelabs car c'est gratuit et très puissant.
-   Supporte le clustering si vous avez plusieurs serveurs (nœuds).
