# variable
s3_airflow = s3://xxx
plugins_zip = plugins.zip
dag = empty
cluster_id = empty

# command
p:
	rm -f plugins/$(plugins_zip)
	cd plugins && chmod -R 755 . && zip -r $(plugins_zip) .
	aws s3 cp plugins/$(plugins_zip) $(s3_airflow)/plugins/$(plugins_zip)

dag:
	aws s3 cp $(dag) $(s3_airflow)/$(dag)

delete:
	aws s3 rm $(s3_airflow)/$(dag)

r:
	pip freeze > requirements.txt
	aws s3 cp requirements.txt $(s3_airflow)/requirements/requirements.txt

local:
	#./mwaa-local-env build-image
	./mwaa-local-env start



