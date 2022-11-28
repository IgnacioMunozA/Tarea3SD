## Comandos a utilizar

Para buildear el docker
```sh
docker build -t hadoop
```

Luego, se debe hacer el docker run

```sh
docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```
Entrar al contenedor de hadoop

```sh
docker exec -it hadoop bash
```

Dentro del contenedor, se deben crear los directorios

```sh 
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input	
```
Luego, se deben dar los permisos a hduser

```sh
sudo chown -R hduser .
```
Hay que pasar los archivos a input

```sh
cd examples/
hdfs dfs -put 1/0.txt input
hdfs dfs -put 1/0.txt input
....
```

Ejecución de MapReduce

```sh
mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output hduser/outhadoop/ -mapper ./mapper.py -reducer ./reducer.py
```

Para mover los archivos de hadoop a nuestro folder
```sh
hdfs dfs -get /user/hduser/hduser/outhadoop/ /home/hduser/examples
```
```sh
docker cp hadoop:/home/hduser/examples/outhadoop examples
```
Ejecutar main.py en el buscador, y ahí ingresar a ThunderClient, Insomnia, etc a 127.0.0.1:5000/buscador?buscador=small (es un ejemplo)






