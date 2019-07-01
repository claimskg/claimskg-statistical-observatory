# ClaimsKG Statistical Observatory

ClaimsKG Statistical Observatory is an interface for ClaimsKG statistics exploration. It is made with a Flask application and use the plotly library to render dynamic interactive graphs.

## About

For a presentation of this project you can take a look at [ClaimsKG_Statistical_Observatory_Report](https://github.com/claimskg/claimskg-statistical-observatory/blob/master/ClaimsKG_Statistical_Observatory_Report.pdf). For perspectives and what to do next prefere look at [Perspectives](https://github.com/claimskg/claimskg-statistical-observatory/blob/master/Perspectives.pdf). 


## How to run

The application is the app.py file and you can run it with:

```python
flask run
```
By default in development mode it will run on [http://localhost:8080/](http://localhost:8080/dataframe_generation)

At first run or in case of updates in the ClaimsKG graph, you must generate the dataframes csv files which are used as data source to feed the application. 

You simply need to run the `regenerate_dataframes.py` script to generate the dataframes. This process can take up to 3-4 hours. 

## Requirements
The version of Python is 3.6.

Before running the application you can use the pip package manager to install the requirements :

```bash
pip install -r /path/to/requirements.txt
```
The requirements file has been generated with the pipreqs command:

```bash
pipreqs /path/to/project
```



## License
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Docker Deployment

A docker version is provided for convenience. 

To build use `docker build . -t claimskg-statistical-observatory`

To run use `docker run -p HOSTPORT:8080 claimskg-statistical-observatory`. Replace host port by the actual port you want to bind locally on the server. 

The route prefix is set at the beginning of app.py in the prefix variable. If you wish to change the prefix you will need to change it there. The default prefix is `/claimskg/observatory`.

The current version only deploys a *DEMO* server running directly with flask as opposed to using a WSGI application server, possible security risks. 

After running the container, please regenerate the dataframes, you may do so directly in the docker container using docker exec: 

`docker exec container_id /usr/bin/python /app/regenerate_dataframes.py`

