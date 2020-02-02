all: pic.py
	python pic.py
	convert pic.ppm pic.png
	display pic.png
clean:
	rm *.ppm
	rm *.png
