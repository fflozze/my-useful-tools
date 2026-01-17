# Nodemailer

> [!TIP]
> [Passer à la version française](#version-française)

## Description
Nodemailer is a module for Node.js applications to allow easy as cake email sending. The project got started back in 2010. It is a single module with zero dependencies.

## Website / Link
- [Official Website](https://nodemailer.com/)
- [Repository](https://github.com/nodemailer/nodemailer)

## Installation
```bash
# Install nodemailer
npm install nodemailer
```

## Useful Commands / Tips
- `createTransport(options)`: Create a transporter object using the default SMTP transport.
- `transporter.sendMail(data)`: Sends an email using the preconfigured transport object.

## Configuration
- Supports various services (Gmail, Outlook) via predefined services or custom SMTP settings (host, port, secure, auth).

## Notes
For testing, you can use `Ethereal Email` which Nodemailer can automatically generate accounts for.

---

# Version Française

## Description
Nodemailer est un module pour les applications Node.js permettant d'envoyer des e-mails aussi facilement que de dire bonjour. Le projet a débuté en 2010. C'est un module unique avec zéro dépendance.

## Site Web / Lien
- [Site Officiel](https://nodemailer.com/)
- [Dépôt](https://github.com/nodemailer/nodemailer)

## Installation
```bash
# Installer nodemailer
npm install nodemailer
```

## Commandes Utiles / Astuces
- `createTransport(options)`: Crée un objet transporteur utilisant le transport SMTP par défaut.
- `transporter.sendMail(data)`: Envoie un e-mail en utilisant l'objet de transport préconfiguré.

## Configuration
- Prend en charge divers services (Gmail, Outlook) via des services prédéfinis ou des paramètres SMTP personnalisés (hôte, port, sécurisé, auth).

## Notes
Pour les tests, vous pouvez utiliser `Ethereal Email` pour lequel Nodemailer peut générer automatiquement des comptes.
