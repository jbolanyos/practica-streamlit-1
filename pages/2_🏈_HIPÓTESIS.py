import streamlit as st

st.header("PROYECTO FIFA - HIPÓTESIS")

opcion = st.selectbox(
    "Escoja la hipótesis a revisar: ",
    ["Hipótesis 1","Hipótesis 2","Hipótesis 3","Hipótsis 4","Hipótesis 5"]
)

if opcion == "Hipótesis 1":
    st.text("Esta es la hipótesis 1")
elif opcion == "Hipótesis 2":
    st.text("Esta es la hipótesis 2")
elif opcion == "Hipótesis 3":
    st.text("Esta es la hipótesis 3")
elif opcion == "Hipótesis 4":
    st.text("Esta es la hipótesis 4")
elif opcion == "Hipótesis 5":
    st.text("Esta es la hipótesis 5")


#def main():
#    pass
#if "__name__" == "__main__":
#    main()