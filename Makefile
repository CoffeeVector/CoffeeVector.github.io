all:
	if [ ! -d venv ]; then python3 -m venv venv; venv/bin/pip3 install -r requirements.txt; fi
	@echo "Building..."
	./main.py
	cp -r public/* build/

clean:
	@echo "Clean up..."
	rm -r build/*
