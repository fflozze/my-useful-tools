# Cookie-Parser

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Parse `Cookie` header and populate `req.cookies` with an object keyed by the cookie names. Optionally you may enable signed cookie support. It is a standard middleware for handling cookies in Express applications.

## Website / Link
- [Repository](https://github.com/expressjs/cookie-parser)
- [NPM](https://www.npmjs.com/package/cookie-parser)

## Installation
```bash
# Install cookie-parser
npm install cookie-parser
```

## Useful Commands / Tips
- `app.use(cookieParser())`: Mounts the middleware in an Express app.
- `req.cookies`: Access cookies in your routes.
- `req.signedCookies`: Access signed cookies (if a secret was provided).

## Configuration
- Can be initialized with a `secret` string for signing cookies.
  ```javascript
  app.use(cookieParser('mySecret'));
  ```

## Notes
Essential for any Express app that needs to read cookies from the client.

---

# Version Française

## Description
Analyse l'en-tête `Cookie` et remplit `req.cookies` avec un objet indexé par les noms de cookies. Vous pouvez éventuellement activer la prise en charge des cookies signés. C'est un middleware standard pour gérer les cookies dans les applications Express.

## Site Web / Lien
- [Dépôt](https://github.com/expressjs/cookie-parser)
- [NPM](https://www.npmjs.com/package/cookie-parser)

## Installation
```bash
# Installer cookie-parser
npm install cookie-parser
```

## Commandes Utiles / Astuces
- `app.use(cookieParser())`: Monte le middleware dans une application Express.
- `req.cookies`: Accéder aux cookies dans vos routes.
- `req.signedCookies`: Accéder aux cookies signés (si un secret a été fourni).

## Configuration
- Peut être initialisé avec une chaîne `secret` pour signer les cookies.
  ```javascript
  app.use(cookieParser('monSecret'));
  ```

## Notes
Essentiel pour toute application Express qui a besoin de lire des cookies provenant du client.
