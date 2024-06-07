all: backend.so backendcpp.so

backendcpp.so: backend.cpp
	g++ -shared -o backendcpp.so -fPIC backend.cpp

backend.so: backend.c
	gcc -shared -o backend.so -fPIC backend.c