# octopwn-ide-language-server
Language server to help octopwn plugin developement.  
This project constains the latest stubs for octopwn and its plugins, allowing the integrated Monaco IDE in OctoPwn's editor util to give code suggestions and speed up developement.

# Deploy
The users have two (supported) way of deploying this tool.  

## Deploy via docker (preferred)
We provide a public docker image that has everything set up. After installing docker, just run the following command:  
`docker run -p 8082:8082 europe-west1-docker.pkg.dev/octopwn-ea2a4/public/octopwn-ide-language-server:latest`

## Deploy in a venv
Clone this repository, then use the `setup.sh` and `run.sh` scripts.  
It will start listening on `ws://localhost:8082`  
Be careful, the stup will require `sudo` privileges!  

```
git clone https://github.com/octopwn/octopwn-ide-language-server
cd octopwn-ide-language-server
./setup.sh
./run.sh
```

