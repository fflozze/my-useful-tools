# DrawDB

> [!TIP]
> [Passer à la version française](#version-française)

## Description
DrawDB is a robust, user-friendly, and free open-source database entity-relationship (DB diagram) editor. It runs entirely in the browser, allowing developers to visually design, edit, and visualize database schemas. It distinguishes itself by not requiring an account to use and providing a modern, intuitive interface.

## Website / Link
- [Official Application](https://drawdb.vercel.app/)
- [GitHub Repository](https://github.com/drawdb-io/drawdb)

## Installation
**Web Version:**
No installation is required. Access the tool directly at [drawdb.vercel.app](https://drawdb.vercel.app/).

**Local Development (Self-Hosted):**
To run DrawDB locally from the source:

```bash
git clone https://github.com/drawdb-io/drawdb.git
cd drawdb
npm install
npm run dev
```

## Useful Commands / Tips
- **Export to SQL**: You can generate and export DDL scripts for major database systems (MySQL, PostgreSQL, SQLite, MariaDB, SQL Server).
- **Import/Reverse Engineer**: Import an existing SQL script to automatically generate the visual diagram.
- **Export Diagrams**: Save your design as an image (PNG, SVG) or PDF for documentation.
- **Work Offline**: Since it runs in the browser, it can work offline once loaded (or when running locally).

## Configuration
- **Custom Templates**: Create and save custom templates for tables or columns.
- **UI Customization**: Adjust editor appearance and snap-to-grid settings.

## Notes
- Excellent for quick prototyping without the overhead of heavy desktop tools.
- All data is stored locally in the browser (IndexedDB) unless you explicitly export it, ensuring privacy.
- Supports "Smart Detect" for relationships when importing scripts.

---

# Version Française

## Description
DrawDB est un éditeur de diagramme entité-association (diagramme de base de données) open source, robuste, convivial et gratuit. Il s'exécute entièrement dans le navigateur, permettant aux développeurs de concevoir, éditer et visualiser visuellement des schémas de base de données. Il se distingue en ne nécessitant pas de compte pour être utilisé et en offrant une interface moderne et intuitive.

## Site Web / Lien
- [Application Officielle](https://drawdb.vercel.app/)
- [Dépôt GitHub](https://github.com/drawdb-io/drawdb)

## Installation
**Version Web :**
Aucune installation requise. Accédez directement à l'outil sur [drawdb.vercel.app](https://drawdb.vercel.app/).

**Développement Local (Auto-hébergé) :**
Pour exécuter DrawDB localement à partir des sources :

```bash
git clone https://github.com/drawdb-io/drawdb.git
cd drawdb
npm install
npm run dev
```

## Commandes Utiles / Astuces
- **Export vers SQL** : Vous pouvez générer et exporter des scripts DDL pour les principaux systèmes de base de données (MySQL, PostgreSQL, SQLite, MariaDB, SQL Server).
- **Importer/Reverse Engineer** : Importez un script SQL existant pour générer automatiquement le diagramme visuel.
- **Exporter des diagrammes** : Sauvegardez votre conception sous forme d'image (PNG, SVG) ou PDF pour la documentation.
- **Travailler hors ligne** : Puisqu'il s'exécute dans le navigateur, il peut fonctionner hors ligne une fois chargé (ou lors de l'exécution locale).

## Configuration
- **Modèles personnalisés** : Créez et enregistrez des modèles personnalisés pour les tables ou les colonnes.
- **Personnalisation de l'interface** : Ajustez l'apparence de l'éditeur et les paramètres de grille.

## Notes
- Excellent pour le prototypage rapide sans la lourdeur des outils de bureau.
- Toutes les données sont stockées localement dans le navigateur (IndexedDB) sauf si vous les exportez explicitement, garantissant la confidentialité.
- Prend en charge la "Détection intelligente" des relations lors de l'importation de scripts.
