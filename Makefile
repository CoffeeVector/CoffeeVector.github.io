all:
	@echo "Building..."
	./main.py
	cp -r public/* build/

clean:
	@echo "Clean up..."
	rm -r build/*
