init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the Flask app..."
	python app.py

test:
	@echo "Running tests..."
	pytest

build:
	@echo "Building Docker image..."
	docker build -t health-app .

clean:
	@echo "Cleaning up Docker..."
	docker system prune -f
