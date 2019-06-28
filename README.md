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

At first run or in case of updates in the ClaimsKG graph, you must generate the dataframes csv files which are used as data source to feed the application with simple GET requests on the following URIs:

For the main dataframe use [http://localhost:8080/dataframe_generation](http://localhost:8080/dataframe_generation).
For the per label dataframe use [http://localhost:8080/dataframe_per_label_generation](http://localhost:8080/dataframe_per_label_generation).
For the theme part use [http://localhost:8080/generation_csv_themes](http://localhost:8080/generation_csv_themes). Please note that this last query may take up to 2-3 hours.  

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
