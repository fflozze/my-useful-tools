# IORedis

> [!TIP]
> [Passer à la version française](#version-française)

## Description
A robust, performance-focused and full-featured Redis client for Node.js. It supports Redis Cluster, Sentinel, Pipelining and Lua scripting.

## Website / Link
- [Official Documentation](https://ioredis.readthedocs.io/)
- [Repository](https://github.com/redis/ioredis)

## Installation
```bash
# Install ioredis
npm install ioredis
```

## Useful Commands / Tips
- `new Redis()`: Connects to localhost:6379 by default.
- `redis.set('key', 'value')`: Sets a key.
- `redis.get('key')`: Gets a key.

## Configuration
- Supports URL connection strings: `new Redis('redis://user:password@redis-service.com:6379')`
- Support for Cluster mode: `new Redis.Cluster(nodes, options)`

## Notes
Often preferred over `node_redis` for its built-in Promise support (historically) and robust feature set.

---

# Version Française

## Description
Un client Redis robuste, axé sur les performances et complet pour Node.js. Il prend en charge Redis Cluster, Sentinel, Pipelining et le scripting Lua.

## Site Web / Lien
- [Documentation Officielle](https://ioredis.readthedocs.io/)
- [Dépôt](https://github.com/redis/ioredis)

## Installation
```bash
# Installer ioredis
npm install ioredis
```

## Commandes Utiles / Astuces
- `new Redis()`: Se connecte à localhost:6379 par défaut.
- `redis.set('key', 'value')`: Définit une clé.
- `redis.get('key')`: Récupère une clé.

## Configuration
- Prend en charge les chaînes de connexion URL : `new Redis('redis://user:password@redis-service.com:6379')`
- Prise en charge du mode Cluster : `new Redis.Cluster(nodes, options)`

## Notes
Souvent préféré à `node_redis` pour son support Promise intégré (historiquement) et son ensemble de fonctionnalités robuste.
