# telegream-bot-template

Tu bot debe intentar encontrar la x que maximice la funcion polinomica f(x), despues de que se use el comando "/duel", la funcion f(x) sera desconocida para todos, tienes 10 intentos.

El juego se complica por que el tiempo sera limitado a 10 segundos y los intentos se haran en el chat grupal "Battlefield".

Luego de cada intento @judgebot respondera con la respuesta para f(x).

En el template tu bot respondera con un numero aleatorio una vez, solo con ponerlo online ya juegas! ;)

Habla con https://t.me/botfather para crear tu bot y conseguir tu token:

El nombre de tu bot debe terminar en "bot" ejemplo: ["judgeBot", "bot", "ANCAPIBOT"] para que @judgebot lo tome en cuenta.

Si sabes python puedes instalar y usar tu bot con pip, si no sabes python, puedes usar docker:

Para crear tu imagen:
```
docker build . -t bot
```

Para iniciar tu imagen en un contenedor:
```
docker run -d --name bot bot
```

Para parar tu contenedor:
```
docker stop bot
```

Para reanudar el conenedor:
```
docker run -d bot
```

