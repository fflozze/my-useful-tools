# CrystalDiskInfo

> [!TIP]
> [Passer à la version française](#version-française)

## Description
CrystalDiskInfo is a comprehensive HDD/SSD health monitoring utility designed to help users avoid data loss by predicting drive failures. It reads S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology) data to provide a detailed health status of your storage devices. It supports HDD, SSD, and external USB drives.

It is particularly useful for:
- Monitoring drive temperature to prevent overheating.
- Checking the "Health Status" summary (Good, Caution, Bad).
- Viewing raw S.M.A.R.T. attribute values.
- Controlling AAM (Automatic Acoustic Management) and APM (Advanced Power Management) settings.

## Website / Link
- [Official Website](https://crystalmark.info/en/software/crystaldiskinfo/)
- [Source Code (OSDN)](https://osdn.net/projects/crystaldiskinfo/)

## Installation
```bash
# Via Winget
winget install CrystalDEWWorld.CrystalDiskInfo

# Or download portable/installer version from the website
# https://crystalmark.info/en/download/
```

## Useful Commands / Tips
- **Health Status Indicator**: The most important feature.
    - **Blue**: Good.
    - **Yellow**: Caution (e.g., Reallocated Sectors, Current Pending Sectors). Back up data immediately.
    - **Red**: Bad (Failure Imminent).
    - **Gray**: Unknown.
- **Resident Mode**: `Function > Resident` keeps the tool in the system tray to monitor temperature and health in real-time.
- **Startup**: `Function > Startup` ensures it runs automatically when Windows boots.
- **Alert Features**: Configure email or sound alerts via `Function > Alert Features` to be notified of temperature spikes or health degradation.
- **AAM/APM Control**: Adjust noise levels (AAM) or power consumption (APM) via `Function > Advanced Feature > AAM/APM Control`.

## Configuration
- **Refresh Rate**: Adjust how often the data updates via `Function > Auto Refresh Target`.
- **Temperature Unit**: Toggle between Celsius and Fahrenheit in the `Function` menu.
- **Themes**: Switch between various visual themes, including Dark Mode support (`Theme` menu).

## Notes
- CrystalDiskInfo is the de facto standard for quickly checking used hardware. If you buy a used drive, this is the first tool you should run to check its "Power On Count" and "Power On Hours".
- The "Shizuku Edition" features anime themes and voices, offering the same functionality with a different aesthetic.

---

# Version Française

## Description
CrystalDiskInfo est un utilitaire complet de surveillance de l'état de santé des disques durs (HDD) et SSD, conçu pour aider les utilisateurs à éviter la perte de données en prédisant les pannes. Il lit les données S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology) pour fournir un statut de santé détaillé de vos périphériques de stockage. Il prend en charge les HDD, les SSD et les disques USB externes.

Il est particulièrement utile pour :
- Surveiller la température du disque pour éviter la surchauffe.
- Vérifier le résumé de l'état de santé ("État de santé" : Correct, Prudence, Mauvais).
- Afficher les valeurs brutes des attributs S.M.A.R.T.
- Contrôler les paramètres AAM (Gestion acoustique) et APM (Gestion avancée de l'alimentation).

## Site Web / Lien
- [Site Officiel](https://crystalmark.info/en/software/crystaldiskinfo/)
- [Code Source (OSDN)](https://osdn.net/projects/crystaldiskinfo/)

## Installation
```bash
# Via Winget
winget install CrystalDEWWorld.CrystalDiskInfo

# Ou télécharger la version portable/installateur depuis le site web
# https://crystalmark.info/en/download/
```

## Commandes Utiles / Astuces
- **Indicateur d'État de Santé** : La fonctionnalité la plus importante.
    - **Bleu** : Correct (Good).
    - **Jaune** : Prudence (Caution) (par ex., secteurs réalloués). Sauvegardez vos données immédiatement.
    - **Rouge** : Mauvais (Bad) (Panne imminente).
    - **Gris** : Inconnu.
- **Mode Résident** : `Fonctions > Résident` garde l'outil dans la barre système pour surveiller la température et la santé en temps réel.
- **Démarrage** : `Fonctions > Démarrage` assure qu'il se lance automatiquement avec Windows.
- **Fonctionnalités d'Alerte** : Configurez des alertes par e-mail ou sonores via `Fonctions > Fonctionnalités d'alerte`.
- **Contrôle AAM/APM** : Ajustez le bruit (AAM) ou la consommation d'énergie (APM) via `Fonctions > Fonctionnalités avancées > Contrôle AAM/APM`.

## Configuration
- **Taux de Rafraîchissement** : Ajustez la fréquence de mise à jour des données via `Fonctions > Taux de rafraîchissement auto`.
- **Unité de Température** : Basculez entre Celsius et Fahrenheit.
- **Thèmes** : Basculez entre différents thèmes visuels, y compris le mode sombre (Menu `Thème`).

## Notes
- CrystalDiskInfo est le standard de facto pour vérifier rapidement le matériel d'occasion. Si vous achetez un disque usagé, c'est le premier outil à exécuter pour vérifier le "Nombre d'allumages" et les "Heures de fonctionnement".
- L'édition "Shizuku" propose des thèmes et des voix d'anime, offrant la même fonctionnalité avec une esthétique différente.
