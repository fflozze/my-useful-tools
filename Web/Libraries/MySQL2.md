# MySQL2

> [!TIP]
> [Passer à la version française](#version-française)

## Description
A MySQL client for Node.js with focus on performance. It supports prepared statements, non-utf8 encodings, binary log protocol, compression, ssl and more. It is mostly API compatible with `mysqljs/mysql`.

## Website / Link
- [Repository](https://github.com/sidorares/node-mysql2)
- [NPM](https://www.npmjs.com/package/mysql2)

## Installation
```bash
# Install mysql2
npm install mysql2
```

## Useful Commands / Tips
- `mysql.createConnection({...})`: Create a connection to the database.
- `connection.execute(sql, params)`: Execute a prepared statement (safer and often faster than `.query`).

## Configuration
- Standard connection options: host, user, password, database, port.
- Pool configuration is recommended for production.

## Notes
Highly recommended over the original `mysql` package due to support for prepared statements and active maintenance.

---

# Version Française

## Description
Un client MySQL pour Node.js axé sur les performances. Il prend en charge les instructions préparées, les encodages non-utf8, le protocole de log binaire, la compression, le ssl et plus encore. Il est en grande partie compatible avec l'API de `mysqljs/mysql`.

## Site Web / Lien
- [Dépôt](https://github.com/sidorares/node-mysql2)
- [NPM](https://www.npmjs.com/package/mysql2)

## Installation
```bash
# Installer mysql2
npm install mysql2
```

## Commandes Utiles / Astuces
- `mysql.createConnection({...})`: Crée une connexion à la base de données.
- `connection.execute(sql, params)`: Exécute une instruction préparée (plus sûr et souvent plus rapide que `.query`).

## Configuration
- Options de connexion standard : hôte, utilisateur, mot de passe, base de données, port.
- La configuration de pool est recommandée pour la production.

## Notes
Hautement recommandé par rapport au paquet `mysql` original en raison de la prise en charge des instructions préparées et de la maintenance active.
