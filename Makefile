init:
	curl -LsSf https://astral.sh/uv/install.sh | sh
	uv tool install ruff

format:
	uv run ruff format .

lint:
	uv run ruff check .