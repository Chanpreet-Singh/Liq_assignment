**Setting up the project**:<br>
Make sure you have python3.8 or python3.9 in your system and create a virtual environment as ***venv*** and all the libraries are installed using,<br>
`source venv/bin/activate; pip install -r requirements.txt`

**For creating synthetic data**,<br>
`source venv/bin/activate; python -m scripts.random_data_generator`

**Pipeline-1: Ingesting data from csvs into duckdb(persisted storage)**<br>
Command to execute: `source venv/bin/activate; dagster dev -m pipelines.ingest_sales_data`

After the execution on pipeline-1, we can perform some queries on the ingested data as given below<br>
![Output of the experiment-1](./output_images/Correlated_Query_Join.png)
