# teardown
teardown:
	make predictor_down
	make mlflow_down

# mlflow
mlflow_up:
	docker compose -f deployment/mlflow/docker-compose.yml up -d
	
mlflow_down:
	docker compose -f deployment/mlflow/docker-compose.yml down

# predictor
predictor_up:
	PORT=5040 docker compose -f deployment/model_predictor/docker-compose.yml up -d

predictor_down:
	PORT=5040 docker compose -f deployment/model_predictor/docker-compose.yml down

predictor_restart:
	PORT=5040 docker compose -f deployment/model_preddocker compose version
	PORT=5040 docker compose -f deployment/model_predictor/docker-compose.yml start

predictor_curl:
	curl -X POST http://localhost:5040/phase-1/prob-1/predict -H "Content-Type: application/json" -d @data/curl/phase-1/prob-1/payload-1.json
	curl -X POST http://localhost:5040/phase-1/prob-1/predict -H "Content-Type: application/json" -d @data/curl/phase-1/prob-1/payload-2.json
	curl -X POST http://localhost:5040/phase-1/prob-2/predict -H "Content-Type: application/json" -d @data/curl/phase-1/prob-2/payload-1.json

