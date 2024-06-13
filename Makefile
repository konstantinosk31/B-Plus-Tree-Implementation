all: backend.js

backend.js: backend.c
	emcc backend.c -o backend.js -s WASM=1 -s EXPORTED_FUNCTIONS='["_insert_and_export_dot_file", "_delete_and_export_dot_file", "_generate_dot", "_search_and_export_bool", "_change_order"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["cwrap", "getValue", "setValue"]'
