.DEFAULT_TARGET: $(build_directory)/index.html
.PHONY: copy_static_files

build_directory  = build
static_directory = static

$(build_directory)/index.html: $(build_directory) app copy_static_files
	venv/bin/python3 -c "import app.website; app.website.main(build_directory='$(build_directory)')"

$(build_directory): venv
	@echo "Building..."
	mkdir -p $@
	touch $@

venv:
	@echo "Setting up virtual environment..."
	python3 -m venv venv; venv/bin/pip3 install -r requirements.txt;

copy_static_files: $(build_directory) $(static_directory)
	cp -r $(static_directory)/* $(build_directory)/

clean:
	@echo "Removing build directory ($(build_directory))..."
	rm -r build
