## Developper Guide

In this guide the structure of the app and its different files purposes will be reviewed and explained.

### Root

```bash
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

**Dockerfile** 
: The Dockerfile contains the required commands to do before launching the app. In this case it allows to install the required Python packages, create the application image and create a small workflow for the data scraped from the web.

**docker-compose.yml**
: This file is used because we want our app to be executed with the `docker-compose up`command. It contains the configurations of our project and the dependent images linked to it. in our case it contains the configuration for our **Flask** and **MongoDB**.

**README.md**
: Just the basic README.md file that explains quickly the application, mostly used for **GitHub**.

**assets**
: A folder containing some miscellaneous pictures for the README.md.

**data**
: Temporary folder used during the beginning worlflow.

**docs**
: The folder containing this documentation!

**requirements.txt**
: This text file contains the name of the many differents **Python** packages needed for ***Leco***.

**[app](dev_guide/app.md)**
: This folder contains the application.



