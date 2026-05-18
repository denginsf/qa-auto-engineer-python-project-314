install:
	uv sync

start:
	docker run --rm -p 5173:5173 hexletprojects/qa_auto_python_testing_kanban_board_project_ru_app

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=. --cov-report=xml --cov-report=term

lint:
	uv run ruff check