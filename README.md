# B+ Plus Tree Implementation

Created for the purposes of the course "Databases" at ECE NTUA.
Authors:
- Sotirios [<sakakos>](https://github.com/sakakos) Kakos
- Konstantinos [<konstantinosk31>](https://github.com/konstantinosk31) Kritharidis
- Dimitrios [<minageus>](https://github.com/minageus) Minagias

Large portion of the backend was written by Amittai Aviram (http://www.amittai.com).
The LICENSE is included in the backend.c file.

## Installation guide:

1.  Clone our repository:
    ```
    git clone https://github.com/minageus/B-Plus-Tree-Implementation.git
    ```

2. Open a localhost. For example using Python3 and port 8000:
    ```
    python3 -m http.server 8000
    ```

3. In a browser, open the page `http://localhost:8000/`.

Now you are ready to use our webpage!

## Compilation guide:

If you want to make changes to the code and need to recompile it, here are the detailed steps on how to do it.

1.  You will need to have installed the Emscripten compiler.
    If it is not installed, execute the following instructions: 

    ```
    git clone https://github.com/emscripten-core/emsdk.git
    cd emsdk
    ./emsdk install latest
    ./emsdk activate latest
    source ./emsdk_env.sh
    ```

2. Run the Makefile using the instruction `make` in the directory of our cloned repository