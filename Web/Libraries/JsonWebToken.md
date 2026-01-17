# JsonWebToken

> [!TIP]
> [Passer à la version française](#version-française)

## Description
An implementation of JSON Web Tokens (JWT). It was developed against `draft-ietf-oauth-json-web-token-08`. It allows for signing, decoding, and verifying JWTs. It is the de-facto standard library for working with JWTs in Node.js.

## Website / Link
- [Repository](https://github.com/auth0/node-jsonwebtoken)
- [NPM](https://www.npmjs.com/package/jsonwebtoken)

## Installation
```bash
# Install jsonwebtoken
npm install jsonwebtoken
```

## Useful Commands / Tips
- `jwt.sign(payload, secret, options)`: Creates a new token.
- `jwt.verify(token, secret)`: Verifies a token's validity and returns the payload.
- `jwt.decode(token)`: Decodes a token without verifying (useful for inspection on client side too).

## Configuration
- Configuration usually involves setting expiry times (`expiresIn`) and choosing algorithms (e.g., HS256, RS256).

## Notes
Crucial for stateless authentication mechanisms.

---

# Version Française

## Description
Une implémentation des JSON Web Tokens (JWT). Il a été développé contre `draft-ietf-oauth-json-web-token-08`. Il permet de signer, décoder et vérifier des JWT. C'est la bibliothèque standard de facto pour travailler avec des JWT dans Node.js.

## Site Web / Lien
- [Dépôt](https://github.com/auth0/node-jsonwebtoken)
- [NPM](https://www.npmjs.com/package/jsonwebtoken)

## Installation
```bash
# Installer jsonwebtoken
npm install jsonwebtoken
```

## Commandes Utiles / Astuces
- `jwt.sign(payload, secret, options)`: Crée un nouveau token.
- `jwt.verify(token, secret)`: Vérifie la validité d'un token et renvoie la charge utile (payload).
- `jwt.decode(token)`: Décode un token sans vérifier (utile aussi pour l'inspection côté client).

## Configuration
- La configuration implique généralement de définir des délais d'expiration (`expiresIn`) et de choisir des algorithmes (par exemple, HS256, RS256).

## Notes
Crucial pour les mécanismes d'authentification sans état (stateless).
