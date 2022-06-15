import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(page_title="Our-Data", page_icon=":globe_with_meridians:")

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
    data1 = {}
    data = {}

    


    st.header("Datos de la empresa :page_with_curl:")

    cols = st.columns(2)

    with cols[0]:
        data1["nombre"] = st.text_input("Nombre comercial")
        data1["tipo"] = st.radio("Sector", ["Público", "Privado"])
        data1["ne"] = st.number_input("Número de empleados", value = 0, step=1)
        data1["fecha"] = st.date_input("Fecha de creación de la empresa")

    with cols[1]:
        data1["razon"] = st.selectbox("Razón social", ["Ninguna", "Sociedad en Comandita", "Sociedad Limitada", "Sociedad Anónima","Sociedad por Acciones Simplificada","Sociedad Colectiva"])
        data1["nit"] = st.text_input("NIT")
        data1["nc"] = st.number_input("Número estimado de clientes actuales", value = 0, step=1)
        data1["nombre_dil"] = st.text_input("Nombre de quien diligencia")



    if len(data1["nombre"]) > 0:
        st.header("Preguntas de diagnóstico :memo:")
        nombre = data1["nombre"]
        cols = st.columns(2)

        with cols[0]:

            data["P1"] = st.radio("¿" + nombre + " posee un proceso establecido de consulta de información personal en sus bases de datos?", ["No", "Si"])
            
            

            if data["P1"] == "Si":

                

                data["P2"] = st.radio("¿" + nombre + " mantiene pruebas y registros de las consultas que se hacen a los datos personales de los usuarios por parte del responsable o encargado del tratamiento?", ["No", "Si"])
                data["P5"] = st.number_input("¿En qué plazo en días hábiles la empresa cumple las consultas de datos personales solicitadas?", value = 1, step = 1)  


            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)
            
            data["P8"] = st.radio("¿El responsable del trantamiento de datos personales de la empresa solicita autorización clara al usuario para el uso de estos?", ["No", "Si"])

            if data["P8"] == "Si":
                data["P9"] = st.radio("¿Informa debidamente al Titular sobre la finalidad de la recolección y los derechos que le asisten por virtud de la autorización otorgada?", ["No", "Si"])
            
            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P10"] = st.radio("¿La empresa posee las medidas de seguridad necesarias sobre los datos personales que impidan la adulteración, perdida, consulta, uso y acceso no autorizado o fraudulento?", ["No", "Si"])

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P13"] = st.radio("¿La empresa tiene un manual interno de políticas y procedimientos para garantizar el adecuado cumplimiento de la ley 1581 de 2012 y en especial, para la atención de consultas y reclamos?", ["No", "Si"])

            



        with cols[1]:

            data["P3"] = st.radio("¿Se tiene establecido quienes son los responsables y encargados del tratamiento de los datos personales de los usuarios?", ["No", "Si"])

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P4"] = st.radio("¿La empresa " + nombre + " tiene un proceso de reclamo por parte de los usuarios sobre su información personal frente al responsable o encargado del tratamiento? (actualización, corrección, suspensión o incumplimiento)", ["No", "Si"])

            if data["P4"] == "Si":
                data["P6"] = st.radio("¿Usa la empresa en sus bases de datos las leyendas 'reclamo en trámite' o 'información en discusión judicial' para marcar la información que lo requiera?", ["No", "Si"])
                data["P7"] = st.number_input("¿En qué plazo en días hábiles cumple la empresa con los reclamos recibidos? ", value = 1, step = 1)

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P11"] = st.radio("¿La empresa tiene un proceso periódico establecido de actualización y rectificación de datos?", ["No", "Si"])

            st.markdown("""<hr style="border:2px dashed Salmon;border-radius:5px;" /> """, unsafe_allow_html=True)

            data["P12"] = st.radio("¿Se exige al encargado de los datos el respeto a las condiciones de privacidad y seguridad de los datos?", ["No", "Si"])

        

        llaves = list(data.keys())

        score = 0

        puntajes = {"P1": 5, "P2": 3, "P3": 5, "P4":5, "P5": 3, "P6":3, "P7":3, "P8":9, "P9":5, "P10":8, "P11":4, "P12":4, "P13":3}

        total_posible = np.sum(list(puntajes.values()))
        num_si = np.sum(np.array(list(data.values())) == "Si")
        num_no = np.sum(np.array(list(data.values())) == "No")

        for i in llaves:
            if i == "P5":
                if data[i] <= 10:
                    score += 3
                elif data[i] <= 15:
                    score += 2

            elif i == "P7":
                if data[i] <= 15:
                    score += 3
                elif data[i] <= 23:
                    score += 2
            else:
                if data[i] == "Si":
                    score += puntajes[i]

        st.title("Visualización de resultados")

        if st.checkbox("Desplegar resultados"):

            st.header("Puntaje general")

            cols = st.columns(2)
            cols[0].metric("Puntaje obtenido (sobre 60 puntos)", score)
            
            if score < 38:
                cols[1].error("Según las respuestas al formulario, la empresa debe mejorar diferentes aspectos en materia de tratamiento, seguridad y protección de datos.")
            elif score < 60:
                cols[1].info("Según las respuestas al formulario, la empresa cumple diferentes requerimientos en materia de tratamiento, seguridad y protección de datos. Sin embargo, se podrían mejorar algunos aspectos.")
            elif score == 60:
                cols[1].success("Según las respuestas al formulario, la empresa cumple todos los requerimientos en materia de tratamiento, seguridad y protección de datos.")

            st.header("Análisis de cada respuesta según la Ley 1581 de 2012 :mag:")

            st.markdown("**Pregunta: ¿" + nombre + " posee un proceso establecido de consulta de información personal en sus bases de datos?**")
            if data["P1"] == "Si":
                st.success("Cumple con Artículo 14. Ley 1581 de 2012. Consultas. Los Titulares o sus causahabientes podrán consultar la información personal del Titular que repose en cualquier base de datos, sea esta del sector público o privado. El Responsable del Tratamiento o Encargado del Tratamiento deberán suministrar a estos toda la información contenida en el registro individual o que esté vinculada con la identificación del Titular.")
                st.markdown("**Pregunta: ¿" + nombre + " mantiene pruebas y registros de las consultas que se hacen a los datos personales de los usuarios por parte del responsable o encargado del tratamiento?**")
                if data["P2"] == "Si":
                    st.success("Cumple con Artículo 14. Ley 1581 de 2012. Consultas. La consulta se formulará por el medio habilitado por el Responsable del Tratamiento o Encargado del Tratamiento, siempre y cuando se pueda mantener prueba de esta.")
                else:
                    st.error("No cumple con Artículo 14. Ley 1581 de 2012. Consultas. La consulta se formulará por el medio habilitado por el Responsable del Tratamiento o Encargado del Tratamiento, siempre y cuando se pueda mantener prueba de esta.")
                
                st.markdown("**Pregunta: ¿En qué plazo en días hábiles la empresa cumple las consultas de datos personales solicitadas?**")
                if data["P5"] <= 10:
                    st.success("Cumple satisfactoriamente con Artículo 14. Ley 1581 de 2012. Consultas. La consulta será atendida en un término máximo de diez (10) días hábiles contados a partir de la fecha de recibo de la misma. Cuando no fuere posible atender la consulta dentro de dicho término, se informará al interesado, expresando los motivos de la demora y señalando la fecha en que se atenderá su consulta, la cual en ningún caso podrá superar los cinco (5) días hábiles siguientes al vencimiento del primer término.")
                elif data["P5"] <= 15:
                    st.warning("Cumple pero se debe revisar la acción de la empresa con Artículo 14. Ley 1581 de 2012. Consultas. La consulta será atendida en un término máximo de diez (10) días hábiles contados a partir de la fecha de recibo de la misma. Cuando no fuere posible atender la consulta dentro de dicho término, se informará al interesado, expresando los motivos de la demora y señalando la fecha en que se atenderá su consulta, la cual en ningún caso podrá superar los cinco (5) días hábiles siguientes al vencimiento del primer término.")
                else:
                    st.error("No cumple con Artículo 14. Ley 1581 de 2012. Consultas. La consulta será atendida en un término máximo de diez (10) días hábiles contados a partir de la fecha de recibo de la misma. Cuando no fuere posible atender la consulta dentro de dicho término, se informará al interesado, expresando los motivos de la demora y señalando la fecha en que se atenderá su consulta, la cual en ningún caso podrá superar los cinco (5) días hábiles siguientes al vencimiento del primer término.")

            else:
                st.error("No Cumple con Artículo 14. Ley 1581 de 2012. Consultas. Los Titulares o sus causahabientes podrán consultar la información personal del Titular que repose en cualquier base de datos, sea esta del sector público o privado. El Responsable del Tratamiento o Encargado del Tratamiento deberán suministrar a estos toda la información contenida en el registro individual o que esté vinculada con la identificación del Titular.")

            st.markdown("**Pregunta: ¿Se tiene establecido quienes son los responsables y encargados del tratamiento de los datos personales de los usuarios?**")
            if data["P3"] == "Si":
                st.success("Cumple con Artículo 12. Ley 1581 de 2012. Deber de informar al Titular. El Responsable del Tratamiento, al momento de solicitar al Titular la autorización, deberá informarle de manera clara y expresa lo siguiente: ... d) La identificación, dirección física o electrónica y teléfono del Responsable del Tratamiento.")
            else:
                st.error("No cumple con Artículo 12. Ley 1581 de 2012. Deber de informar al Titular. El Responsable del Tratamiento, al momento de solicitar al Titular la autorización, deberá informarle de manera clara y expresa lo siguiente: ... d) La identificación, dirección física o electrónica y teléfono del Responsable del Tratamiento.")
            
            st.markdown("**Pregunta: ¿La empresa " + nombre + " tiene un proceso de reclamo por parte de los usuarios sobre su información personal frente al responsable o encargado del tratamiento? (actualización, corrección, suspensión o incumplimiento)**")

            if data["P4"] == "Si":
                st.success("Cumple con Artículo 15. Ley 1581 de 2012. Reclamos. El Titular o sus causahabientes que consideren que la información contenida en una base de datos debe ser objeto de corrección, actualización o supresión, o cuando adviertan el presunto incumplimiento de cualquiera de los deberes contenidos en esta ley, podrán presentar un reclamo ante el Responsable del Tratamiento o el Encargado del Tratamiento")
                st.markdown("**Pregunta: ¿Usa la empresa en sus bases de datos las leyendas 'reclamo en trámite' o 'información en discusión judicial' para marcar la información que lo requiera?**")
                if data["P6"] == "Si":
                    st.success("Cumple con Artículo 18. Deberes de los Encargados del Tratamiento. Los Encargados del Tratamiento deberán cumplir los siguientes deberes, sin perjuicio de las demás disposiciones previstas en la presente ley y en otras que rijan su actividad: ... g) Registrar en la base de datos las leyenda 'reclamo en trámite' en la forma en que se regula en la presente ley... h) Insertar en la base de datos la leyenda 'información en discusión judicial' una vez notificado por parte de la autoridad competente sobre procesos judiciales relacionados con la calidad del dato personal.")
                else:
                    st.error("No cumple con Artículo 18. Deberes de los Encargados del Tratamiento. Los Encargados del Tratamiento deberán cumplir los siguientes deberes, sin perjuicio de las demás disposiciones previstas en la presente ley y en otras que rijan su actividad: ... g) Registrar en la base de datos las leyenda 'reclamo en trámite' en la forma en que se regula en la presente ley... h) Insertar en la base de datos la leyenda 'información en discusión judicial' una vez notificado por parte de la autoridad competente sobre procesos judiciales relacionados con la calidad del dato personal.")
                

                st.markdown("**Pregunta: ¿En qué plazo en días hábiles cumple la empresa con los reclamos recibidos?**")
                if data["P7"] <= 15:
                    st.success("Cumple satisfactoriamente con Artículo 15. Ley 1581 de 2012. Reclamos. 3. El término máximo para atender el reclamo será de quince (15) días hábiles contados a partir del día siguiente a la fecha de su recibo. Cuando no fuere posible atender el reclamo dentro de dicho término, se informará al interesado los motivos de la demora y la fecha en que se atenderá su reclamo, la cual en ningún caso podrá superar los ocho (8) días hábiles siguientes al vencimiento del primer término.")
                elif data["P7"] <= 23:
                    st.warning("Cumple pero se debe revisar la acción de la empresa con Artículo 15. Ley 1581 de 2012. Reclamos. 3. El término máximo para atender el reclamo será de quince (15) días hábiles contados a partir del día siguiente a la fecha de su recibo. Cuando no fuere posible atender el reclamo dentro de dicho término, se informará al interesado los motivos de la demora y la fecha en que se atenderá su reclamo, la cual en ningún caso podrá superar los ocho (8) días hábiles siguientes al vencimiento del primer término.")
                else:
                    st.error("No cumple con Artículo 15. Ley 1581 de 2012. Reclamos. 3. El término máximo para atender el reclamo será de quince (15) días hábiles contados a partir del día siguiente a la fecha de su recibo. Cuando no fuere posible atender el reclamo dentro de dicho término, se informará al interesado los motivos de la demora y la fecha en que se atenderá su reclamo, la cual en ningún caso podrá superar los ocho (8) días hábiles siguientes al vencimiento del primer término.")

            
            else:
                st.error("No cumple Artículo 15. Ley 1581 de 2012. Reclamos. El Titular o sus causahabientes que consideren que la información contenida en una base de datos debe ser objeto de corrección, actualización o supresión, o cuando adviertan el presunto incumplimiento de cualquiera de los deberes contenidos en esta ley, podrán presentar un reclamo ante el Responsable del Tratamiento o el Encargado del Tratamiento.")
            
            st.markdown("**Pregunta: ¿El responsable del trantamiento de datos personales de la empresa solicita autorización clara al usuario para el uso de estos?**")
            if data["P8"] == "Si":
                st.success("Cumple con Artículo 9. Autorización del Titular. Sin perjuicio de las excepciones previstas en la ley, en el Tratamiento se requiere la autorización previa e informada del Titular, la cual deberá ser obtenida por cualquier medio que pueda ser objeto de consulta posterior.")
                st.markdown("**Pregunta: ¿Informa debidamente al Titular sobre la finalidad de la recolección y los derechos que le asisten por virtud de la autorización otorgada?**")
                if data["P9"] == "Si":
                    st.success("Cumple con Artículo 12. Deber de informar al Titular. El Responsable del Tratamiento, al momento de solicitar al Titular la autorización, deberá informarle de manera clara y expresa lo siguiente: a) El Tratamiento al cual serán sometidos sus datos personales y la finalidad del mismo.")
                else: 
                    st.error("No cumple con Artículo 12. Deber de informar al Titular. El Responsable del Tratamiento, al momento de solicitar al Titular la autorización, deberá informarle de manera clara y expresa lo siguiente: a) El Tratamiento al cual serán sometidos sus datos personales y la finalidad del mismo.")
            else:
                st.error("No cumple con Artículo 9. Autorización del Titular. Sin perjuicio de las excepciones previstas en la ley, en el Tratamiento se requiere la autorización previa e informada del Titular, la cual deberá ser obtenida por cualquier medio que pueda ser objeto de consulta posterior.")

            st.markdown("**Pregunta: ¿La empresa posee las medidas de seguridad necesarias sobre los datos personales que impidan la adulteración, perdida, consulta, uso y acceso no autorizado o fraudulento?**")
            if data["P10"] == "Si":
                st.success("Cumple con Artículo 4. Principios para el Tratamiento de datos personales... g) Principio de seguridad: La información sujeta a Tratamiento por el Responsable del Tratamiento o Encargado del Tratamiento a que se refiere la presente ley, se deberá manejar con las medidas técnicas, humanas y administrativas que sean necesarias para otorgar seguridad a los registros evitando su adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento.")
            else: 
                st.error("No cumple con Artículo 4. Principios para el Tratamiento de datos personales... g) Principio de seguridad: La información sujeta a Tratamiento por el Responsable del Tratamiento o Encargado del Tratamiento a que se refiere la presente ley, se deberá manejar con las medidas técnicas, humanas y administrativas que sean necesarias para otorgar seguridad a los registros evitando su adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento.")

            st.markdown("**Pregunta: ¿La empresa tiene un proceso periódico establecido de actualización y rectificación de datos?**")
            if data["P11"] == "Si":
                st.success("Cumple con Artículo 17. Deberes de los Responsables del Tratamiento. f) Actualizar la información, comunicando de forma oportuna al Encargado del Tratamiento, todas las novedades respecto de los datos que previamente le haya suministrado y adoptar las demás medidas necesarias para que la información suministrada a este se mantenga actualizada...  g) Rectificar la información cuando sea incorrecta y comunicar lo pertinente al Encargado del Tratamiento.")
            else:
                st.error("No cumple con Artículo 17. Deberes de los Responsables del Tratamiento. f) Actualizar la información, comunicando de forma oportuna al Encargado del Tratamiento, todas las novedades respecto de los datos que previamente le haya suministrado y adoptar las demás medidas necesarias para que la información suministrada a este se mantenga actualizada...  g) Rectificar la información cuando sea incorrecta y comunicar lo pertinente al Encargado del Tratamiento.")
            
            st.markdown("**Pregunta: ¿Se exige al encargado de los datos el respeto a las condiciones de privacidad y seguridad de los datos?**")
            if data["P12"] == "Si":
                st.success("Cumple con Artículo 17. Deberes de los Responsables del Tratamiento. i) Exigir al Encargado del Tratamiento en todo momento, el respeto a las condiciones de seguridad y privacidad de la información del Titular.")
            else:
                st.error("No cumple con Artículo 17. Deberes de los Responsables del Tratamiento. i) Exigir al Encargado del Tratamiento en todo momento, el respeto a las condiciones de seguridad y privacidad de la información del Titular.")
            
            st.markdown("**Pregunta: ¿La empresa tiene un manual interno de políticas y procedimientos para garantizar el adecuado cumplimiento de la ley 1581 de 2012 y en especial, para la atención de consultas y reclamos?**")
            
            if data["P13"] == "Si":
                st.success("Cumple con Artículo 17. Deberes de los Responsables del Tratamiento. k) Adoptar un manual interno de políticas y procedimientos para garantizar el adecuado cumplimiento de la presente ley y en especial, para la atención de consultas y reclamos.")
            else:
                st.error("No cumple con Artículo 17. Deberes de los Responsables del Tratamiento. k) Adoptar un manual interno de políticas y procedimientos para garantizar el adecuado cumplimiento de la presente ley y en especial, para la atención de consultas y reclamos.")
            



