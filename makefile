main:
	python main.py

build_bin:
	pyinstaller --onefile main.py