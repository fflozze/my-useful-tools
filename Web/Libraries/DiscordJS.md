# Discord.js

> [!TIP]
> [Passer à la version française](#version-française)

## Description
discord.js is a powerful node.js module that allows you to interact with the Discord API very easily. It takes a much more object-oriented approach than most other JS Discord libraries, making your bot's code significantly tidier and easier to comprehend.

## Website / Link
- [Official Website](https://discord.js.org/)
- [Repository](https://github.com/discordjs/discord.js)

## Installation
```bash
# Install discord.js
npm install discord.js
```

## Useful Commands / Tips
- `client.on('ready', ...)`: Event triggered when the bot is logged in.
- `client.on('interactionCreate', ...)`: Standard event for handling slash commands.

## Configuration
- Requires a BOT_TOKEN from the Discord Developer Portal.
- Uses `Intents` to define what events the bot receives.

## Notes
Make sure to keep your token secret! Use environment variables.

---

# Version Française

## Description
discord.js est un puissant module node.js qui vous permet d'interagir avec l'API Discord très facilement. Il adopte une approche beaucoup plus orientée objet que la plupart des autres bibliothèques Discord JS, rendant le code de votre bot considérablement plus propre et plus facile à comprendre.

## Site Web / Lien
- [Site Officiel](https://discord.js.org/)
- [Dépôt](https://github.com/discordjs/discord.js)

## Installation
```bash
# Installer discord.js
npm install discord.js
```

## Commandes Utiles / Astuces
- `client.on('ready', ...)`: Événement déclenché lorsque le bot est connecté.
- `client.on('interactionCreate', ...)`: Événement standard pour gérer les commandes slash.

## Configuration
- Nécessite un BOT_TOKEN du portail développeur Discord.
- Utilise des `Intents` pour définir quels événements le bot reçoit.

## Notes
Assurez-vous de garder votre jeton secret ! Utilisez des variables d'environnement.
