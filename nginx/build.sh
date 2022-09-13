docker build --tag simple-nginx .
docker tag simple-nginx gerroldk/simple-nginx:latest
docker push gerroldk/simple-nginx:latest