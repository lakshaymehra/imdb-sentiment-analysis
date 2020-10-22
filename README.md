# Deploying a Sentiment Analysis Model as a Web App Using Flask and Containerizing it Using Docker :
Remark : This repo also contains the code for Training a Sentiment Analysis Model On The IMDB Movie Reviews Dataset. 

## Usage Guide:

### File Descriptions:

* ##### 'templates/index.html' :
    contains the HTML code for the web-app.
* ##### 'templates/style.css' :
    contains the CSS code for the web-app.
* ##### 'build_docker.sh' :
    contains the code to build a Docker image.
* ##### 'Dockerfile' :
    contains the DockerFile.
* ##### 'get_package_versions' :
    contains the code to get the versions of all the required packages.
* ##### 'requirements.txt' :
    contains the exact package versions used for this project.
* ##### 'imdb_reviews.h5' : 
    is the trained Keras Model saved as a .h5 File.
* ##### 'docker_run.sh' :
    contains the code to run the Docker Container.
* ##### 'train_model.py' :
    contains the code for training the Keras model.
* ##### 'web_app_predict.py' :
    contains the code for deploying the model as a Flask web app.

#### FOR DOCKER:
To containerize the app and run it using Docker, use :

```bash
bash build_docker.sh
bash run_docker.sh
```
and visit the following link on your web browser : http://192.168.99.100:5001/

#### FOR FLASK:
To deploy as a web app using Flask, use :

```bash
python web_app_predict.py
```
and visit the following link on your web browser : http://127.0.0.1:5001/


## Results:

### WebApp Sample Predictions:
![Alt text](Figure_1.bmp?raw=true "Figure_1")
![Alt text](Figure_2.bmp?raw=true "Figure_2")


### Contact :
For any query/feedback, please contact
```
Lakshay Mehra: mehralakshay2@gmail.com
```

