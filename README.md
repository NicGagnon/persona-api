
# Getting Started

Download and install Docker Community Edition. If you have Homebrew-Cask, just type brew cask install docker. Or Download and install Docker Toolbox.

Steps to run container:
1. Download persona-api on machine
2. Cd into the persona-api directory
3. Run the following commands 
 
```buildoutcfg
docker-compose up --build -d
docker-compose up
```


# Format

All responses will have the form 

```json
{
    "data": "Mixed type holding the content of the repsonse",
    "message": "Explanation of the content"
}
```

### Functions

The following definitions only detail the expected value from the 'data field'

### Find a User

*** Definition ***

'GET /search/{username}'

*** Responses ***

- '404 Not Found' if the username doesn't exist
- '200 OK' on success

```json
{
    "job": "Solicitor",
    "company": "Smith, Haynes and Hooper",
    "ssn": "ZZ376803T",
    "residence": "1 Bruce alley\nNew Justin\nL07 2TE",
    "current_location": [-66.491849, -69.512524],
    "blood_group": "AB+",
    "website": [
        "https://www.holmes-saunders.com/",
         "http://foster-ford.com/",
         "https://www.farrell-evans.com/",
         "http://white-kelly.net/"
         ],
    "username": "mauriceharris",
    "name": "Dr. Mohamed Newton",
    "sex": "F",
    "address": "09 Knight parkways\nWest Yvonneshire\nHD23 5NJ",
    "mail": "jshort@hotmail.com",
    "birthdate": "1989-07-07"
}
```

### List all people with pagination

*** Definition ***

'GET /people'

*** Responses ***

```json
[
    {
        "job": "Radiographer, therapeutic",
        "company": "Jones Ltd",
        "ssn": "ZZ017201T",
        "residence": "Flat 52C\nShaun mills\nMorrisfurt\nBL50 0YG",
        "current_location": [-12.119129, -133.859534],
        "blood_group": "0+",
        "website": 
            [
                "http://douglas.com/",
                "https://www.lewis-thomas.com/"
            ],
        "username": "twong",
        "name": "Graeme Davis",
        "sex": "F",
        "address": "71 Katy mountain\nLake Dennisbury\nB11 5TS",
        "mail": "andrewsian@gmail.com",
        "birthdate": "1994-04-04"
    }, 
    {
        "job": "Advertising art director",
        "company": "Flynn LLC",
        "ssn": "ZZ230873T",
        "residence": "Flat 9\nLewis points\nHillchester\nL3F 2JT",
        "current_location": [-74.774152, -153.777782],
        "blood_group": "B+",
        "website": 
            [
                "https://harding.org/",
                "http://www.doyle.net/"
            ],
        "username": "ocole",
        "name": "Ashley Potts",
        "sex": "F",
        "address": "79 Gerald course\nWest Jeanport\nTW4 5LT",
        "mail": "joannaclarke@gmail.com",
        "birthdate": "2000-11-09"
    },
]
```

### Delete a person

*** Definition ***

'DELETE /people/{username}'

*** Responses

- '404 Not Found' User does not exist
- '204 No Content' on success


# TODO
- Implement pagination for list of people
- Add additional security features 
