# PostgreSQL

> [!TIP]
> [Passer à la version française](#version-française)

## Description
PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

## Website / Link
- [Official Website](https://www.postgresql.org/)
- [Documentation](https://www.postgresql.org/docs/)
- [Repository](https://git.postgresql.org/gitweb/)

## Installation

### Windows
Download the installer from the [official download page](https://www.postgresql.org/download/windows/).

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### macOS
```bash
brew install postgresql
```

## Useful Commands / Tips

### General
- `psql -U [username]`: Connect to PostgreSQL shell.
- `\l`: List all databases.
- `\c [database_name]`: Connect to a specific database.
- `\dt`: List all tables in the current database.
- `\d [table_name]`: Describe parts of a table, such as columns, types, and modifiers.
- `\du`: List all users and their roles.
- `\q`: Quit psql.

### SQL Snippets
- `CREATE DATABASE [db_name];`: Create a new database.
- `DROP DATABASE [db_name];`: Delete a database.
- `CREATE USER [user] WITH PASSWORD '[password]';`: Create a new user.
- `GRANT ALL PRIVILEGES ON DATABASE [db_name] TO [user];`: Grant permissions.

## Configuration
- `postgresql.conf`: Main configuration file (settings for memory, connections, etc.).
- `pg_hba.conf`: Client authentication configuration file (controls who can connect from where).
- Default port: `5432`.

## Notes
- It is highly extensible and compliant with SQL standards.
- Often used with tools like pgAdmin or DBeaver for visual management.

---

# Version Française

## Description
PostgreSQL est un système de base de données relationnelle objet open source puissant, avec plus de 35 ans de développement actif qui lui ont valu une solide réputation de fiabilité, de robustesse et de performance.

## Site Web / Lien
- [Site Officiel](https://www.postgresql.org/)
- [Documentation](https://www.postgresql.org/docs/)
- [Dépôt](https://git.postgresql.org/gitweb/)

## Installation

### Windows
Télécharger l'installateur depuis la [page de téléchargement officielle](https://www.postgresql.org/download/windows/).

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### macOS
```bash
brew install postgresql
```

## Commandes Utiles / Astuces

### Général
- `psql -U [username]` : Se connecter au shell PostgreSQL.
- `\l` : Lister toutes les bases de données.
- `\c [database_name]` : Se connecter à une base de données spécifique.
- `\dt` : Lister toutes les tables de la base actuelle.
- `\d [table_name]` : Décrire une table (colonnes, types, etc.).
- `\du` : Lister tous les utilisateurs et leurs rôles.
- `\q` : Quitter psql.

### Snippets SQL
- `CREATE DATABASE [db_name];` : Créer une nouvelle base de données.
- `DROP DATABASE [db_name];` : Supprimer une base de données.
- `CREATE USER [user] WITH PASSWORD '[password]';` : Créer un nouvel utilisateur.
- `GRANT ALL PRIVILEGES ON DATABASE [db_name] TO [user];` : Accorder des permissions.

## Configuration
- `postgresql.conf` : Fichier de configuration principal (mémoire, connexions, etc.).
- `pg_hba.conf` : Fichier de configuration de l'authentification client (contrôle qui peut se connecter et d'où).
- Port par défaut : `5432`.

## Notes
- Il est hautement extensible et conforme aux standards SQL.
- Souvent utilisé avec des outils comme pgAdmin ou DBeaver pour la gestion visuelle.
