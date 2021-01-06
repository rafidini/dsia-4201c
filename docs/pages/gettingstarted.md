## Getting started with Leco

> «***The Earth is what we all have in common***»
> Wendell Berry

### Launch the app

1. Put a terminal in the project folder

Normally the folder structure can be compared to this...
```bash
$ tree -L 1
.
├── Dockerfile
├── README.md
├── app
├── assets
├── data
├── docker-compose.yml
├── docs
└── requirements.txt
```

2. Execute the following command

```bash
$ docker-compose up
```

3. Check if the output correspond to this

```bash
...
web_1      | > X items were saved in the database.
web_1      | > 0 items were not saved in the database.
web_1      |  * Serving Flask app "web" (lazy loading)
web_1      |  * Environment: production
web_1      |    WARNING: This is a development server. Do not use it in a production deployment.
web_1      |    Use a production WSGI server instead.
web_1      |  * Debug mode: off
web_1      |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
...
```

4. Open your web browser to this ip adress : *0.0.0.0:5000*

Now you can check the [User Guide](userguide.md).

### FAQ

#### What is Leco ?

Basically ***Leco*** is a web application focused on our mother Earth. 


#### What does it offer to you ?

***Leco*** offers the following things to its users :
- **Articles** about environment extracted from *The Guardian* with some text sentiment analysis.
- **Facts** about air pollution, protected area (marine, terrestrial and forest) and finally about some
  ressources.

#### What do you need in order to use the app ?

In order to launch the app you will need : 
- A computer, logical right?
- **Docker** especially **Docker Compose**
