# Microservices
Implemented with Python and Flask

## How to run
Go to each service folder and run `python app.py`. Services will run in debug mode with ports 5000, 5001 and 5002 assigned to facade, logging and messages services relatively. Be sure that these ports are not used by other programs before running this project. Alternatively, you can change ports, but be careful to change ports everywhere throughout the project

То do requests, you can use curl:

Example of get request: `curl -X GET ' http://localhost:5000/`

Example of post request: `curl -X POST -H "Content-Type: application/json" -d '{"msg": "One"}' http://localhost:5000/`

## Notes
*Note that microservices relies on port, e.g. it is expected that messages service is run on port 5002 of localhost and logging service on port 5001 of localhost

*If the there were no POST requests to facade service (meaning that there's no saved messages), empty line will be printed for messages when GET request was made to facade service. Otherwise, messages will be printed, separated by comma. Next line will be response from message service
