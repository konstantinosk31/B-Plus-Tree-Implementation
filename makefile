all: backend.so

backend.so: backend.c
	gcc -shared -o backend.so -fPIC -Wall backend.c