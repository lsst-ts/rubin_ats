.PHONY: html linkcheck clean

html:
	uv run --group docs sphinx-build -c . docs _build/html

linkcheck:
	uv run --group docs sphinx-build -c . -b linkcheck docs _build/linkcheck

clean:
	rm -rf _build
