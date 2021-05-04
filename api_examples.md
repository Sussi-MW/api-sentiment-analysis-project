
## API query examples

## Procedure:

```bash
1-(main_lotr.py)
```

Database system: MongoDB
Framework:Flask
Test platform for API development: Postman


#### Endpoints:

- (POST)   /Create route that allows including data

```bash
Receiving data:
{
    "char": "PIPPIN",
    "dialog": "Hmm?",
    "movie": "The Return of the King"
}
```
```bash
Returns:
{
    "_id": "60912043fb4e084738fa0ccc",
    "char": "PIPPIN",
    "dialog": "Hmm?",
    "movie": "The Return of the King"
}
```

- (GET)    /Create a route that allows you to list all documents

```bash
http://localhost:5001/lotr_characters
```
```bash
Returns:
[
    {
        "_id": {
            "$oid": "608f327603dc552820c2da3c"
        },
        "char": "DEAGOL",
        "dialog": "Oh Smeagol Ive got one! , Ive got a fish Smeagol, Smeagol!",
        "movie": "The Return of the King"
    },
    {
        "_id": {
            "$oid": "608f327603dc552820c2da3d"
        },
        "char": "SMEAGOL",
        "dialog": "Pull it in! Go on, go on, go on, pull it in!",
        "movie": "The Return of the King"
    },
 ...]
 ```

- (GET)    /Create a route that allows listing a single document (the first of all)

```bash
http://localhost:5001/lotr_characters/608f327603dc552820c2da45
```
```bash
Returns: 
{
    "_id": {
        "$oid": "608f327603dc552820c2da45"
    },
    "char": "SMEAGOL",
    "dialog": "My precious.",
    "movie": "The Return of the King"
}
```

- (GET)    /Create a route that allows you to list all movie

```bash
http://localhost:5001/lotr_characters/movie/The Two Towers
```
```bash
Returns: 
[
    {
        "_id": {
            "$oid": "608f327603dc552820c2dc0e"
        },
        "char": "GANDALF",
        "dialog": "Sauron's wrath will be terrible, his retribution swift.",
        "movie": "The Two Towers"
    },
    {
        "_id": {
            "$oid": "608f327603dc552820c2dc0f"
        },
        "char": "GANDALF",
        "dialog": "The battle for Helm's Deep is over. The battle for Middle-earth is about to begin.",
        "movie": "The Two Towers"
    },

...]
```

- (GET)    /Create a route that allows you to list all characters

```bash
http://localhost:5001/lotr_characters/char/ARWEN
```
```bash
Returns: 
[
    {
        "_id": {
            "$oid": "608f327603dc552820c2dd4a"
        },
        "char": "ARWEN",
        "dialog": "May the grace of the Valarprotect you.",
        "movie": "The Two Towers"
    },
    {
        "_id": {
            "$oid": "608f327603dc552820c2dd4d"
        },
        "char": "ARWEN",
        "dialog": "I have made my choice.",
        "movie": "The Two Towers"
    },

...]
```

- (GET)    /Create a path that allows the sentiment analysis of a dialogue

```bash
http://localhost:5001/lotr_characters/sa/608f327603dc552820c2da49
```
```bash
Returns: 
{
    "dialog": "Gollum' Gollum' Gollum' , and we wept precious. We wept to be so alone.",
    "polarity": {
        "neg": 0.404,
        "neu": 0.422,
        "pos": 0.174,
        "compound": -0.6015
    }
}
```

- (DELETE) /Create a route that allows you to delete document

```bash
http://localhost:5001/lotr_characters/608f327603dc552820c2da74
```
```bash
Returns: 
{
    "message": "Document 608f327603dc552820c2da74 was deleted successfully"
}
```

- (PUT)    /Create a route to update documents

```bash
http://localhost:5001/lotr_characters/608f327603dc552820c2da3f

Receiving data
{
    "char": "SMEAGOL",
    "dialog": "Deagol! Deagol!",
    "movie": "The Return of the King"
}
```
```bash
Returns: 
{
    "massage": "Document 608f327603dc552820c2da3f was updated successfully"
}
```