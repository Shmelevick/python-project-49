install:
	uv sync

brain-games:
	uv run brain-games

brain-calc:
	uv run brain-calc

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games