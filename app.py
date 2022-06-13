import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


st.sidebar.title("Our-Data")
st.sidebar.image(Image.open('logo.jpg'))

selected = option_menu(menu_title = "Menú de opciones", options = ["Inicio", "Formulario de diagnósitco de la empresa", "Contáctenos"], 
                       icons = ["house", "book", "envelope"], orientation= "horizontal")


if selected == "Inicio":
    st.title("¿Qué es Our-Data? :globe_with_meridians:")

    st.markdown("Según un estudio realizado por la superintendencia de Industria y Comercio, de 33.593 organizaciones públicas y privadas analizadas en Colombia, el 50.7% aún no han implementado medidas apropiadas y efectivas para garantizar la seguridad de los datos personales que manejan. Resolver este problema requiere un planteamiento diferenciador con respecto a las entidades que se dedican actualmente a ofrecer soluciones a las empresas para cumplir con la ley 1581 de 2012 (Ley de protección de datos personales). ")
    st.markdown("De esta problemática nace **Our-Data**, una empresa dedicada a consultoría especializada en temas de seguridad y protección en las empresas garantizando el cumplimiento de la ley 1581 de 2012. Adicionalmente, **Our-Data** brinda asesoramiento y guia para la renovación de los esquemas de seguridad de la empresa con el fin de mantener la satisfacción de los clientes y evitar las sanciones por el uso incorrecto de datos personales.")

    st.image(Image.open('protecdata.png'))

    st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

    st.title("¿Quienes somos?")

    cols = st.columns(3)

    with cols[0]:
        st.subheader("Ivonne Nathalia Uribe")
        st.image(Image.open('nathalia.jpg'), caption = "CEO: Chief executive officer")

        st.subheader("Juan David Correa")
        st.image(Image.open('david.jpg'), caption = "CMO: Chief marketing officer")


    with cols[2]:
        st.subheader("Nicolás Merchán Rodríguez")
        st.image(Image.open('nicolas.jpg'), "COO: Chief operating officer")

        st.subheader("Juan Sebastían Rodríguez")
        st.image(Image.open('sebastian.jpg'), "CTO: Chief technology officer")

    with cols[1]:
        st.subheader("Cesar Augusto Torres")
        st.image(Image.open('cesar.jpg'), "CCO: Chief comunication officer")




if selected == "Formulario de diagnósitco de la empresa":
    data = {}

    st.header("Datos de la empresa :page_with_curl:")

    cols = st.columns(2)

    with cols[0]:
        data["nombre"] = st.text_input("Nombre comercial")
        data["tipo"] = st.radio("Sector", ["Público", "Privado"])
        data["ne"] = st.number_input("Número de empleados", value = 0, step=1)
        data["fecha"] = st.date_input("Fecha de creación de la empresa")

    with cols[1]:
        data["razon"] = st.selectbox("Razón social", ["Ninguna", "Sociedad en Comandita", "Sociedad Limitada", "Sociedad Anónima","Sociedad por Acciones Simplificada","Sociedad Colectiva"])
        data["nit"] = st.text_input("NIT")
        data["nc"] = st.number_input("Número estimado de clientes actuales", value = 0, step=1)
        data["nombre_dil"] = st.text_input("Nombre de quien diligencia")

    if len(data["nombre"]) > 0:
        st.header("Preguntas de diagnóstico :memo:")
        nombre = data["nombre"]
        cols = st.columns(2)

        with cols[0]:

            data["P1"] = st.radio("¿" + nombre + " posee un proceso establecido de consulta de información personal en sus bases de datos?", ["No", "Si" , "No aplica"])
            
            if data["P1"] == "Si":

                data["P2"] = st.radio("¿" + nombre + " mantiene pruebas y registros de las consultas que se hacen a los datos personales de los usuarios por parte del responsable o encargado del tratamiento?", ["No", "Si"])
                data["P5"] = st.number_input("¿En qué plazo en días hábiles la empresa cumple las consultas de datos personales solicitadas?", value = 1, step = 1)  


            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)
            
            data["P8"] = st.radio("¿El responsable del trantamiento de datos personales de la empresa solicita autorización clara al usuario para el uso de estos?", ["No", "Si" , "No aplica"])

            if data["P8"] == "Si":
                data["P9"] = st.radio("¿Informa debidamente al Titular sobre la finalidad de la recolección y los derechos que le asisten por virtud de la autorización otorgada?", ["No", "Si"])
            
            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P10"] = st.radio("¿La empresa posee las medidas de seguridad necesarias sobre los datos personales que impidan la adulteración, perdida, consulta, uso y acceso no autorizado o fraudulento?", ["No", "Si"])

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P13"] = st.radio("¿Usa la empresa en sus bases de datos las leyendas 'reclamo en trámite' o 'información en discusión judicial' para marcar la información que lo requiera?", ["No", "Si"])

            



        with cols[1]:

            data["P3"] = st.radio("¿Se tiene establecido quienes son los responsables y encargados del tratamiento de los datos personales de los usuarios?", ["No", "Si", "No aplica"])

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P4"] = st.radio("¿La empresa " + nombre + " tiene un proceso de reclamo por parte de los usuarios sobre su información personal frente al responsable o encargado del tratamiento? (actualización, corrección, suspensión o incumplimiento)", ["No", "Si" , "No aplica"])

            if data["P4"] == "Si":
                data["P6"] = st.radio("¿Tiene la empresa un registro de los reclamos referentes a los datos personales donde se especifica que el reclamo está en tramite o ya fue solucionado?", ["No", "Si"])
                data["P7"] = st.number_input("¿En qué plazo en días hábiles cumple la empresa con los reclamos recibidos? ", value = 1, step = 1)

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P11"] = st.radio("¿La empresa tiene un proceso periódico establecido de actualización y rectificación de datos?", ["No", "Si"])

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P12"] = st.radio("¿Se exige al encargado de los datos el respeto a las condiciones de privacidad y seguridad de los datos?", ["No", "Si"])

