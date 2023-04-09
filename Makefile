dev:
	uvicorn main:app --reload
build:
	pyinstaller main.spec