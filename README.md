
### run docker
```
docker-compose build
docker-compose up 
```

python manage.py runserver 0.0.0.0:8000
http://localhost:8000/


### access container
```
docker exec -it containerId bash   
```

### more docker 
```
docker stop $(docker ps -aq)    
docker rm $(docker ps -aq)    
docker rmi $(docker images -q)
```


### reference
https://hub.docker.com/_/django/   
https://docs.docker.com/compose/django/





