# MongoDB

```
docker run -it --rm mongo:6.0.2 mongosh --help
docker run -it --rm mongo:6.0.2 mongosh mongodb://host.docker.internal:27017
docker run -it --rm mongo:6.0.2 mongosh mongodb://172.17.0.14:27017 -u root -p password --authenticationDatabase admin
```

## MongoDB shell

```
show databases
use foo
show collections
```

```
db.inventory.insertOne(
   { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
)
```

```
db.inventory.findOne()
```
