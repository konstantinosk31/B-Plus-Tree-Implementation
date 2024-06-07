import ctypes
import streamlit as st

frontend = ctypes.CDLL("./backend.so")

frontend.generate_dot.restype = ctypes.c_char_p

dot = ""

def user_input():
    global dot
    st.title("B+ Tree Implementation")
    prompt = st.text_input("Enter key: ")
    if st.button("Insert"):
        frontend.insert_and_export_dot_file(int(prompt))
        dot = frontend.generate_dot().decode('utf-8')
        st.graphviz_chart(dot)
    if st.button("Delete"):
        frontend.delete_and_export_dot_file(int(prompt))
        dot = frontend.generate_dot().decode('utf-8')
        st.graphviz_chart(dot)
    if st.button("Search"):
        result = ""
        if frontend.search_and_export_bool(int(prompt)):
            result = f"Key {prompt} found!"
            st.graphviz_chart(dot)
        else:
            result = f"Key {prompt} not found!"
            st.graphviz_chart(dot)
        st.write(result)
        dot = frontend.generate_dot().decode('utf-8')
        st.graphviz_chart(dot)

def show_names():
    st.write("""\n
    Created for the purposes of the course "Databases" at ECE NTUA.\n
    Authors:\n
    - Sotirios <sakakos> Kakos\n
    - Konstantinos <konstantinosk31> Kritharidis\n
    - Dimitrios <minageus> Minagias\n
    \n
    Large portion of the backend was written by Amittai Aviram (http://www.amittai.com).\n
    The LICENSE file is included in the repository.
    """)

user_input()
show_names()