# ClaimsKG Statistical Observatory

ClaimsKG Statistical Observatory is an interface for ClaimsKG statistics exploration. It is made with a Flask application and use the plotly library to render dynamic interactive graphs.

## About

For a presentation of this project you can take a look at [ClaimsKG_Statistical_Observatory_Report](https://github.com/claimskg/claimskg-statistical-observatory/blob/master/ClaimsKG_Statistical_Observatory_Report.pdf). For perspectives and what to do next prefere look at [Perspectives](https://github.com/claimskg/claimskg-statistical-observatory/blob/master/Perspectives.pdf). 


## How to run

The application is the app.py file and you can run it with:

```python
flask run
```
By default in development mode it will run on [http://127.0.0.1:5000/](https://github.com/user/repo/blob/branch/other_file.md)

At first run or in case of updates in the ClaimsKG graph, you must generate the dataframes csv files which are used as data source to feed the application .

Three specific routes which consists in http calls, are dedicated to csv generation.

For the main dataframe use [http://127.0.0.1:5000/dataframe_generation](http://127.0.0.1:5000/dataframe_generation).
For the per label dataframe use [http://127.0.0.1:5000/dataframe_per_label_generation](http://127.0.0.1:5000/dataframe_per_label_generation).
For the theme part use [http://127.0.0.1:5000/generation_csv_themes](http://127.0.0.1:5000/generation_csv_themes). Please note that the generation may take a certain time, particularly the theme part which could take a couple of hours.  

In addition, if you wish use it in development mode locally please consider make a virtual environment with python to avoid python language and libraries compatibility issues.
 
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
