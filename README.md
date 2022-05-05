# Pull Request Status

This python program helps you in getting last week pull requests status. Days range can be changed in python file `days = 7`. It required a public github repository.

#URL Format
https://github.com/{owner}/{reponame}

`github_url = "https://github.com/microsoft/vstest"`
## Creating docker Image
**Before you start using commands make sure docker is installed on your machine.**

Below command will help you in create docker image.

```bash
docker build -t <image name> -f Dockerfile .
```
e.g. - `docker build -t prstatus -f Dockerfile`.

![alt text](https://i.ibb.co/84M6FvX/build-image.jpg)
## Usage
### For executing python program in docker container
```python
docker run -it --rm --name <container name> <image name> 
```
eg. - `docker run -it --rm -name prstatus prstatus`

#Result:
![alt text](https://i.ibb.co/wwJ66dr/build-image2.jpg)
