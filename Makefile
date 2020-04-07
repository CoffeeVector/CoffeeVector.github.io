.DEFAULT_TARGET: $(build_directory)/index.html
.PHONY: copy_static_files

theme = allure

build_directory  = build
static_directory = static

all: $(build_directory) copy_static_files

$(build_directory)/index.html: $(build_directory) venv app
	venv/bin/python3 -c "import app.website; app.website.main(build_directory='$(build_directory)', theme='$(theme)')"

$(build_directory):
	@echo "Building..."
	mkdir -p $@
	touch $@

venv:
	@echo "Setting up virtual environment..."
	python3 -m venv venv; venv/bin/pip3 install -r requirements.txt;

copy_static_files: $(build_directory) $(static_directory) $(build_directory)/index.html
	xargs -I{} -n1 cp -r --parents {} $(build_directory)/ < $(build_directory)/static_files.txt
	cp CNAME $(build_directory)/

clean:
	@echo "Removing contents of $(build_directory) (leaving .git/ untouched)..."
	rm -r build/*

clean_hard:
	@echo "Removing build directory ($(build_directory))..."
	rm -rf build
