import streamlit as st

# 1. CONFIGURACIÓN E IDENTIDAD VISUAL
st.set_page_config(page_title="Software de formulas farmaceuticas", layout="wide")

# Encabezado con Logos
col_izq, col_der = st.columns([5, 1])

with col_izq:
    # Aquí va tu título principal y descripción
    st.markdown("<h1 style='color: #1E3A5F;'>Laboratorio Virtual</h1>", unsafe_allow_html=True)
    st.markdown("<p>Validación de Fórmulas e Incompatibilidades Químicas</p>", unsafe_allow_html=True)

with col_der:
    # Aquí ponemos el logo pequeño a la derecha
    st.image("Logo_modulares.png", width=150)

st.markdown("---")

# 2. AUTORES EN LA BARRA LATERAL
st.sidebar.image("Logo_uteg.png", width=200)

st.sidebar.header("🔬 Equipo de Desarrollo")
st.sidebar.info("""
**Profesor:**
Daniel Zatarain
                
**Alumnos:**
* Rodriguez Villa Juan Carlos
* Hernandez Leal Fatima Daniela 
* Sanchez Ramirez Guillermo

**Institución:** UTEG
""")


st.sidebar.header("Licenciatura en Químico Farmacéutico Biólogo")

# 3. SELECCIÓN DE ACTIVOS POR GRUPOS
st.write("### 🧪 Módulo de fichas técnica")

# Diccionario de grupos y sus activos
menu_farmacia = {
    "Analgésicos, Antiinflamatorios y Antipiréticos": ["Acetaminofén", "Aspirina", "Salicilato de Metilo"],
    "Dermatológicos y Protectores de la Piel": ["Ácido Salicílico", "Alantoína", "Alcanfor y Mentol", "Óxido de Zinc", "Resorcinol", "Urea pura", "Aceite de Trementina, Ácido Tánico y Aceite de Ricino"],
    "Filtros Solares (Protectores UV)": ["Benzofenona y Dióxido de Titanio", "Octil Salicilato y Octil Metoxicinamato"],
    "Gastrointestinales (Antiácidos, Adsorbentes y Laxantes)": ["Bicarbonato de Sodio y Carbonato de Calcio", "Carbón Activado", "Hidróxidos de Magnesio y Aluminio"],
    "Vitaminas y Suplementos Minerales": ["Ácido Ascórbico (Vit C) y Sulfato Ferroso", "Vitaminas A y E"],
    "Cuidado Oral y Otros": ["Fluoruro de Sodio", "Ácido Bórico y Borato de Sodio"]
}

# Primer selector: Grupo
grupo_seleccionado = st.selectbox("1. Seleccione el Grupo Farmacéutico:", ["Seleccionar..."] + list(menu_farmacia.keys()))

if grupo_seleccionado != "Seleccionar...":
    # Segundo selector: Activo (se filtra según el grupo elegido)
    activo = st.selectbox(f"2. Seleccione el activo de {grupo_seleccionado}:", menu_farmacia[grupo_seleccionado])

    # CREACIÓN DE PESTAÑAS
    tab_fundamento, tab_interraciones, tab_propiedades, tab_reacciones_adversas = st.tabs(["📚 Fundamento Científico", "🧮 Interacciones", "🧪 Propiedades Fisicoquímicas", "⚠️ Reacciones medicamentosas"])
    with tab_fundamento:
        if activo == "Acetaminofén":
            st.subheader("📋 Ficha Técnica: Acetaminofén (Paracetamol)")
            st.info("Uso: Analgésico y antipirético.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El acetaminofén es un fármaco ampliamente utilizado por su efecto analgésico y antipirético.
                Actúa principalmente a nivel del sistema nervioso central inhibiendo la síntesis de prostaglandinas,
                lo que reduce la percepción del dolor y la fiebre. (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Solubilidad: 1:70 en agua y 1:10 en alcohol.
                - Punto de fusión: 168–172 °C.
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable en condiciones normales.
                - Contenido máximo de agua permitido: 0.5%.
                """)
            st.markdown("### 🧪 Importancia en formulación")
            st.write("""
                - Puede emplearse en formas sólidas y líquidas.
                - Su solubilidad moderada requiere selección adecuada de vehículo en soluciones.
                - Es ideal para enseñanza de cálculos farmacéuticos y compatibilidad.
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Degradación en presencia de agentes oxidantes.
                - Posible formación de productos de degradación en condiciones extremas de pH.
                """)
            st.caption("Referencia: Allen, 2016, p. 667; p. 28. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Acetaminofén":
            st.subheader("🧮 Interacciones del Acetaminofén")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Agentes oxidantes fuertes")
            st.error("Incompatibilidad crítica")
            st.write("""
            **Tipo de interacción:** Reacción química de oxidación

            **Qué ocurre:**
            El acetaminofén es incompatible con agentes oxidantes fuertes, los cuales pueden degradar
            el principio activo y disminuir su estabilidad.

            **Impacto farmacéutico:**
            - Pérdida de potencia del fármaco
            - Disminución de estabilidad química
            - Riesgo de formación de productos de degradación

            **Acción recomendada:**
            - Evitar peróxidos, permanganatos y otros oxidantes fuertes en la formulación
            - Seleccionar excipientes y materias primas químicamente inertes
            - Proteger la formulación de condiciones que favorezcan oxidación
            """)
            st.markdown("#### 🟠 pH extremos")
            st.warning("Incompatibilidad moderada a crítica, según la formulación")
            st.write("""
            **Tipo de interacción:** Degradación química por hidrólisis

            **Qué ocurre:**
            En condiciones de pH extremos, el acetaminofén puede sufrir hidrólisis y formar
            **p-aminofenol**, un producto de degradación no deseado.

            **Impacto farmacéutico:**
            - Disminución de la estabilidad del principio activo
            - Pérdida de calidad del preparado
            - Posible riesgo toxicológico si la degradación es significativa

            **Acción recomendada:**
            - Evitar medios demasiado ácidos o demasiado alcalinos
            - Mantener el sistema en un rango de pH controlado
            - Vigilar especialmente formulaciones líquidas
            """)
            st.markdown("#### 🟡 Humedad")
            st.warning("Factor de riesgo para estabilidad")
            st.write("""
            **Tipo de interacción:** Factor físico que favorece deterioro

            **Qué ocurre:**
            Aunque el acetaminofén es estable en condiciones normales, el control de humedad es importante,
            ya que el contenido máximo de agua permitido es de 0.5%.

            **Impacto farmacéutico:**
            - Puede comprometer la estabilidad del material
            - Aumenta el riesgo de degradación durante almacenamiento

            **Acción recomendada:**
            - Almacenar en envases bien cerrados
            - Evitar excipientes muy higroscópicos si no están justificados
            - Controlar humedad durante pesado y elaboración
            """)
            st.markdown("#### 🟢 Compatibilidad general con excipientes comunes")
            st.success("Compatible en condiciones controladas")
            st.write("""
            **Tipo de interacción:** Compatibilidad fisicoquímica general

            **Qué ocurre:**
            El acetaminofén puede formularse adecuadamente con excipientes farmacéuticos comunes
            siempre que no aporten carácter oxidante ni sometan al sistema a pH extremos.

            **Importancia en formulación:**
            - Permite su uso en tabletas, cápsulas y algunas formulaciones líquidas
            - Requiere selección racional del vehículo y control de estabilidad

            **Acción recomendada:**
            - Usar excipientes químicamente estables
            - Confirmar compatibilidad en formulaciones líquidas o de larga vida útil
            """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
            El principal riesgo del acetaminofén en formulación no suele ser una incompatibilidad múltiple
            con muchos excipientes, sino su **degradación por oxidación** y su **inestabilidad en pH extremos**.
            Por ello, el control del medio químico y de la humedad es clave para conservar su calidad.
            """)
            st.caption("Referencia: Allen, 2016, p. 667; p. 28, tomado del archivo base del proyecto.")
    with tab_propiedades:
        if activo == "Acetaminofén":
            st.subheader("🧪 Propiedades Fisicoquímicas del Acetaminofén")
            col1, col2, col3 = st.columns(3)
            col1.metric("Fórmula química", "C8H9NO2")
            col2.metric("Peso molecular", "151.16 g/mol")
            col3.metric("Estado físico", "Sólido cristalino")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Agua: 1:70
                - Alcohol: 1:10
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Punto de fusión: 168–172 °C
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable en condiciones normales.
                - Sensible a agentes oxidantes.
                - Puede degradarse en pH extremos.
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Adecuado para tabletas, cápsulas y soluciones.
                - Requiere control de humedad.
                - Puede necesitar ajuste de vehículo en formulaciones líquidas.
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con excipientes comunes.
                - Evitar condiciones oxidantes o extremos de pH.
                """)
            st.success("💡 Dato clave: El límite de humedad (0.5%) es crítico para su estabilidad.")
            st.caption("Referencia: Allen, 2016, p. 667; p. 28. Complementado para fines didácticos.")    
    with tab_reacciones_adversas:
        if activo == "Acetaminofén":
            st.subheader("⚠️ Reacciones medicamentosas")
            st.write("""
                    - 🔴 El uso simultáneo de ASPIRINA y AINE puede aumentar el riesgo de hemorragia, reducir la función renal y aumentar el riesgo de efectos adversos gastrointestinales.
                    - 🔴 El uso simultáneo de PARACETAMOL y ETANOL puede aumentar el riesgo de hepatotoxicidad.
                    - 🔴 El uso simultáneo de sustratos del CYP1A2 y tabaco puede dar lugar a una menor exposición a los sustratos del CYP1A2.
                """)    
            st.markdown("### 🍴 Interacciones con alimentos")
            st.write("""
                    - El uso simultáneo de PARACETAMOL y COL puede reducir la eficacia del paracetamol.
                """)    
            st.caption("Referencia: Micromedex.")

    

    with tab_fundamento:
        if activo == "Aspirina":
            st.subheader("📋 Ficha Técnica: Ácido Acetilsalicílico (Aspirina)")
            st.info("Uso: Analgésico, antipirético y antiinflamatorio no esteroideo (AINE).")
            st.markdown("### 🔬 Mecanismo de acción")
            st.write("""
                Inhibe de manera irreversible la enzima ciclooxigenasa (COX-1 y COX-2), 
                reduciendo la síntesis de prostaglandinas responsables del dolor, fiebre e inflamación.
                """)
            st.markdown("### 💊 Aplicación farmacéutica")
            st.write("""
                - Tabletas y comprimidos
                - Tabletas efervescentes
                - Cápsulas
                """)
            st.markdown("### ⚗️ Justificación en formulación")
            st.write("""
                - Es sensible a la humedad, por lo que requiere formulaciones en ambientes secos.
                - Se puede recubrir (entérico) para evitar irritación gástrica.
                - Se formula en tabletas sólidas para mejorar su estabilidad.
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Se hidroliza fácilmente en presencia de humedad formando ácido salicílico y ácido acético.
                - Olor a vinagre indica degradación.
                - Puede formar mezclas eutécticas con otros sólidos.
                """)
            st.info("💡 Dato clave: La estabilidad de la aspirina depende fuertemente del control de humedad y temperatura.")
    with tab_interraciones:
        if activo == "Aspirina":
            st.subheader("🧮 Interacciones del Ácido Acetilsalicílico (Aspirina)")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Sustancias alcalinas (bicarbonato, carbonato)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción química (hidrólisis alcalina)

                **Qué ocurre:**
                La aspirina (éster) se hidroliza en presencia de bases formando **ácido salicílico** y **ácido acético**.

                **Impacto farmacéutico:**
                - Pérdida de potencia del fármaco
                - Generación de olor a vinagre (indicador de degradación)
                - Disminución de estabilidad y vida útil

                **Acción recomendada:**
                - Evitar excipientes alcalinos (bicarbonato de sodio, carbonato de calcio)
                - Mantener pH controlado (no alcalino)
                - Considerar recubrimiento entérico cuando aplique
                """)
            st.markdown("#### 🔴 Humedad")
            st.error("Factor crítico de degradación")
            st.write("""
                **Tipo de interacción:** Hidrólisis química favorecida por agua

                **Qué ocurre:**
                La aspirina es **muy sensible a la humedad**; el agua acelera su hidrólisis a ácido salicílico y acético.

                **Impacto farmacéutico:**
                - Pérdida de estabilidad
                - Disminución de potencia
                - Cambio organoléptico (olor característico)

                **Acción recomendada:**
                - Formular y almacenar en condiciones **secas**
                - Usar envases herméticos (blíster alu-alu o frascos bien sellados)
                - Evitar excipientes higroscópicos o controlar su uso
                """)
            st.markdown("#### 🟠 Estearato de magnesio")
            st.warning("Incompatibilidad moderada (cataliza degradación)")
            st.write("""
                **Tipo de interacción:** Catalítica (medio ligeramente alcalino)

                **Qué ocurre:**
                El estearato de magnesio, por su naturaleza básica, **acelera la degradación** de la aspirina.

                **Impacto farmacéutico:**
                - Disminución de estabilidad
                - Posible variabilidad en la dosis efectiva

                **Acción recomendada:**
                - Minimizar su concentración
                - Reducir tiempo de mezclado
                - Evaluar lubricantes alternativos si es crítico
                """)
            st.markdown("#### 🔴 Alcanfor, Mentol, Resorcinol, Fenol")
            st.error("Incompatibilidad crítica (mezclas eutécticas)")
            st.write("""
                **Tipo de interacción:** Interacción física (formación de mezcla eutéctica)

                **Qué ocurre:**
                La aspirina forma **mezclas eutécticas** con estos compuestos, provocando **licuefacción** de la mezcla sólida.

                **Impacto farmacéutico:**
                - Pérdida de forma farmacéutica (tabletas blandas o pegajosas)
                - Problemas de manufactura (flujo/compresión)
                - Inestabilidad física del producto

                **Acción recomendada:**
                - Evitar combinación directa en formas sólidas
                - Separar fases o usar adsorbentes (p. ej., sílica) si es imprescindible
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                La aspirina puede formularse con excipientes comunes **si se controlan humedad y pH**.

                **Importancia en formulación:**
                - Adecuada para tabletas/cápsulas con excipientes secos
                - Requiere control estricto de proceso y almacenamiento

                **Acción recomendada:**
                - Usar excipientes **secos e inertes**
                - Controlar ambiente (HR y temperatura)
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                La aspirina presenta **alta sensibilidad a la humedad y a medios alcalinos**, siendo la **hidrólisis**
                su principal vía de degradación. Además, las **mezclas eutécticas** representan un riesgo físico importante.
                El éxito de la formulación depende del **control de humedad, pH y selección de excipientes**.
                """)
            st.caption("Referencia: Allen, 2016, p. 667, 28, 179, 209, 265; tomado del archivo base del proyecto.")
    with tab_propiedades:    
            if activo == "Aspirina":
                st.subheader("🧪 Propiedades Fisicoquímicas del Ácido Acetilsalicílico")
                col1, col2, col3 = st.columns(3)
                col1.metric("Fórmula química", "C9H8O4")
                col2.metric("Peso molecular", "180.16 g/mol")
                col3.metric("Estado físico", "Sólido cristalino")
                st.markdown("### 💧 Solubilidad")
                st.write("""
                    - Agua: Baja (1:300)
                    - Alcohol: Alta (1:5)
                    - Éter: Soluble
                    """)
                st.markdown("### 🌡️ Propiedades físicas")
                st.write("""
                    - Punto de fusión: ~135 °C
                    - pKa: ~3.5
                    """)
                st.markdown("### ⚠️ Estabilidad")
                st.warning("""
                    - Muy sensible a la humedad.
                    - Se hidroliza en presencia de agua.
                    - Sensible a altas temperaturas.
                    """)
                st.markdown("### ⚗️ Comportamiento en formulación")
                st.write("""
                    - Puede formar mezclas eutécticas (licuefacción).
                    - Requiere condiciones anhidras.
                    - Puede necesitar recubrimiento para proteger el fármaco.
                    """)
                st.markdown("### 🧠 Compatibilidad fisicoquímica")
                st.write("""
                    - Compatible con excipientes secos.
                    - Incompatible con bases.
                    """)
                st.success("💡 Dato clave: La aspirina debe almacenarse en envases herméticos para evitar su degradación.")
    with tab_reacciones_adversas:
        if activo == "Aspirina":
            st.subheader("⚠️ Reacciones medicamentosas")
            st.write("""
                    - 🔴 El uso simultáneo de ASPIRINA y AINE puede aumentar el riesgo de hemorragia, reducir la función renal y aumentar el riesgo de efectos adversos gastrointestinales.
                    - 🔴 El uso simultáneo de ASPIRINA y ETANOL puede aumentar el riesgo de hemorragia gastrointestinal.
                    - 🟠 El uso simultáneo de ASPIRINA y productos que contengan ALUMINIO, CALCIO O MAGNESIO puede reducir la eficacia del salicilato.
                """)
            st.markdown("### 🍴 Interacciones con alimentos")
            st.write("""
                    - El uso simultáneo de AGENTES ANTIPLAQUETARIOS y APIO puede aumentar el riesgo de hemorragia.
                """)    
            st.caption("Referencia: Micromedex.")



    with tab_fundamento:
        if activo == "Salicilato de Metilo":
            st.subheader("📋 Ficha Técnica: Salicilato de Metilo")
            st.info("Uso: Analgésico tópico y rubefaciente.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El salicilato de metilo es un éster del ácido salicílico utilizado principalmente en aplicaciones tópicas.
                Actúa como rubefaciente, produciendo vasodilatación local que genera sensación de calor y ayuda a aliviar
                el dolor muscular y articular. 
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Líquido aceitoso
                - Miscible con alcohol y aceites fijos
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Ungüentos y pomadas
                - Cremas tópicas
                - Soluciones oleosas
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Puede interactuar con materiales de envase (plásticos).
                - Se emplea principalmente en sistemas lipofílicos.
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Puede reaccionar con contaminantes metálicos (hierro).
                - Puede deteriorar envases plásticos inadecuados.
                """)
            st.caption("Referencia: Allen, 2016, p. 669; p. 104; p. 15. Complementado para fines didácticos.")       
    with tab_interraciones:
        if activo == "Salicilato de Metilo":
            st.subheader("🧮 Interacciones del Salicilato de Metilo")
            st.markdown("### ⚗️ Tipo de interacciones")
            st.markdown("#### 🔴 Interacción con metales (hierro)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo:** Reacción química (formación de complejos)
                **Mecanismo:**
                El salicilato de metilo puede reaccionar con trazas de hierro formando complejos coloreados,
                generando un cambio a color violeta.
                     
                **Impacto farmacéutico:**
                - Alteración visual del producto
                - Indica contaminación o reacción química
                - Puede afectar la calidad del preparado
                **Acción recomendada:**
                - Evitar contacto con utensilios metálicos
                - Utilizar equipo de vidrio o acero inoxidable grado farmacéutico
                """)
            st.markdown("#### 🔴 Interacción con envases plásticos")
            st.error("Incompatibilidad crítica")
            st.write("""
                
                **Tipo:** Interacción físico-química con material de envase
                     
                **Mecanismo:**
                El compuesto puede disolver o ablandar ciertos plásticos debido a su naturaleza lipofílica.
                     
                **Impacto farmacéutico:**
                - Pérdida de estabilidad del producto
                - Contaminación por migración de componentes del envase
                - Riesgo de pérdida de dosis
                     
                **Acción recomendada:**
                    - Usar envases de vidrio ámbar
                    - Evitar plásticos no farmacéuticos
                """)
            st.markdown("#### 🟢 Compatibilidad con solventes")
            st.success("Compatible")
            st.write("""
                     
                **Tipo:** Compatibilidad fisicoquímica
                     
                **Comportamiento:**
                - Miscible con alcohol
                - Miscible con aceites fijos
                     
                **Importancia en formulación:**
                - Ideal para formulaciones tópicas oleosas
                - Facilita su incorporación en cremas y ungüentos
                     
                **Recomendación:**
                - Usar bases lipofílicas para mayor estabilidad
                """)
            st.markdown("### ⚠️ Conclusión farmacéutica")
            st.info("""
                El principal riesgo del salicilato de metilo no es su reactividad química intensa,
                sino su interacción con materiales (hierro y plásticos), por lo que la selección de equipo
                y envase es crítica en su formulación.
                """)
            st.caption("Referencia: Allen, 2016, p. 104; p. 15. Mejorado con enfoque didáctico.")
    with tab_propiedades:
        if activo == "Salicilato de Metilo":
            st.subheader("🧪 Propiedades Fisicoquímicas del Salicilato de Metilo")
            col1, col2, col3 = st.columns(3)
            col1.metric("Fórmula química", "C8H8O3")
            col2.metric("Peso molecular", "152.15 g/mol")
            col3.metric("Estado físico", "Líquido aceitoso")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Insoluble en agua
                - Miscible con alcohol
                - Miscible con aceites fijos
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Líquido transparente
                - Olor característico (tipo gaulteria)
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Relativamente estable en condiciones normales.
                - Puede reaccionar con ciertos materiales (plásticos).
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se incorpora fácilmente en bases oleosas.
                - No es adecuado para sistemas acuosos sin emulsionantes.
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con alcoholes y aceites.
                - Incompatible con algunos materiales de envase.
                """)
            st.success("💡 Dato clave: La elección del envase es crítica para evitar degradación o pérdida del producto.")
            st.caption("Referencia: Allen, 2016, p. 669. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Salicilato de Metilo":
                st.subheader("No hay informacion con los principios activos disponibles")


    with tab_fundamento:
        if activo == "Ácido Salicílico":
            st.subheader("📋 Ficha Técnica: Ácido Salicílico")
            st.info("Uso: Agente queratolítico en dermatología (acné, psoriasis, verrugas).")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El ácido salicílico es un ácido orgánico con propiedades queratolíticas, capaz de romper
                las uniones entre células del estrato córneo, facilitando la descamación de la piel.
                Esto lo hace útil en el tratamiento de afecciones dermatológicas. (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Solubilidad: 1:460 en agua y 1:2.7 en alcohol
                - Punto de fusión: 158–161 °C
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Cremas y pomadas
                - Soluciones alcohólicas
                - Preparaciones tópicas queratolíticas
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Baja solubilidad en agua → requiere alcohol u otros solventes
                - Puede generar reacciones químicas con bases y metales
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Formación de precipitados en sistemas acuosos
                - Efervescencia con carbonatos
                - Cambios de color en presencia de metales
                """)
            st.info("💡 Dato clave: Su comportamiento ácido lo hace altamente reactivo con bases y algunos excipientes.")
            st.caption("Referencia: Allen, 2016, p. 671, 179, 36, 35. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Ácido Salicílico":
            st.subheader("🧮 Interacciones del Ácido Salicílico")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Carbonatos (bicarbonato, carbonato de calcio)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido-base

                **Qué ocurre:**
                El ácido salicílico reacciona con carbonatos liberando CO₂, produciendo efervescencia.

                **Impacto farmacéutico:**
                - Pérdida del principio activo
                - Inestabilidad de la formulación
                - Formación de gas → riesgo en envase cerrado

                **Acción recomendada:**
                - Evitar bases y carbonatos
                - No formular en sistemas efervescentes sin control
                """)
            st.markdown("#### 🟠 Sales de hierro")
            st.warning("Incompatibilidad moderada")
            st.write("""
                **Tipo de interacción:** Formación de complejos

                **Qué ocurre:**
                Reacciona con sales de hierro formando un complejo de color violeta.

                **Impacto farmacéutico:**
                - Cambio de color (indicador de reacción)
                - Posible alteración de estabilidad

                **Acción recomendada:**
                - Evitar contaminación con metales
                - Usar utensilios adecuados (vidrio o acero farmacéutico)
                """)
            st.markdown("#### 🔴 Alcanfor y Mentol")
            st.error("Incompatibilidad crítica (mezcla eutéctica)")
            st.write("""
                **Tipo de interacción:** Interacción física (mezcla eutéctica)

                **Qué ocurre:**
                Forma mezclas eutécticas con alcanfor y mentol, causando licuefacción.

                **Impacto farmacéutico:**
                - Pérdida de forma sólida
                - Problemas de manufactura (tabletas pegajosas)
                - Inestabilidad física

                **Acción recomendada:**
                - Evitar combinación directa en formas sólidas
                - Usar adsorbentes si es necesario
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible bajo condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Puede formularse adecuadamente en sistemas alcohólicos o bases dermatológicas compatibles.

                **Importancia en formulación:**
                - Ideal para soluciones alcohólicas
                - Uso común en dermatología

                **Acción recomendada:**
                - Usar solventes adecuados (alcohol)
                - Evitar medios acuosos sin ajuste
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El ácido salicílico presenta alta reactividad como ácido, siendo sus principales riesgos
                las reacciones con bases (efervescencia) y la formación de mezclas eutécticas.
                La selección de solvente y excipientes es crítica para su estabilidad.
                """)
            st.caption("Referencia: Allen, 2016, p. 179, 36, 35. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Ácido Salicílico":
            st.subheader("🧪 Propiedades Fisicoquímicas del Ácido Salicílico")
            col1, col2, col3 = st.columns(3)
            col1.metric("Fórmula química", "C7H6O3")
            col2.metric("Peso molecular", "138.12 g/mol")
            col3.metric("Estado físico", "Sólido cristalino")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Agua: 1:460 (baja)
                - Alcohol: 1:2.7 (alta)
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Punto de fusión: 158–161 °C
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable en condiciones normales
                - Reactivo frente a bases
                - Sensible a interacciones con metales
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Requiere solventes adecuados por su baja solubilidad en agua
                - Se emplea principalmente en soluciones alcohólicas o bases tópicas
                - Puede formar sistemas inestables si no se controla el pH
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con alcoholes
                - Incompatible con carbonatos y bases
                - Puede reaccionar con metales
                """)
            st.success("💡 Dato clave: La baja solubilidad en agua y su carácter ácido determinan su comportamiento en formulación.")
            st.caption("Referencia: Allen, 2016, p. 671. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
        if activo == "Ácido Salicílico":
            st.subheader("⚠️ Reacciones medicamentosas")
            st.write("""
                    - 🔴 El uso simultáneo de ASPIRINA y AINE puede aumentar el riesgo de hemorragia, reducir la función renal y aumentar el riesgo de efectos adversos gastrointestinales.
                """)
            st.caption("Referencia: Micromedex.")



    with tab_fundamento:
        if activo == "Alcanfor y Mentol":
            st.subheader("📋 Ficha Técnica: Alcanfor y Mentol")
            st.info("Uso: Agentes rubefacientes, analgésicos tópicos y descongestionantes.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El alcanfor y el mentol son compuestos orgánicos volátiles que actúan principalmente
                como agentes tópicos, produciendo sensaciones de frío o calor en la piel. Su acción
                se relaciona con la estimulación de receptores sensoriales, generando alivio del dolor
                y sensación refrescante. (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Sustancias volátiles
                - Se subliman a temperatura ambiente
                - Naturaleza lipofílica
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Ungüentos y pomadas
                - Cremas tópicas
                - Preparaciones descongestionantes
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Alta volatilidad → pueden perderse durante el proceso
                - Sensibles a temperatura
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Sublimación durante pesado o calentamiento
                - Formación de mezclas líquidas con otros sólidos
                """)
            st.info("💡 Dato clave: Aunque son sólidos, pueden comportarse como líquidos al mezclarse con ciertos compuestos.")
            st.caption("Referencia: Allen, 2016, p. 668, 669, 179. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Alcanfor y Mentol":
            st.subheader("🧮 Interacciones del Alcanfor y Mentol")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Resorcinol y Ácido Salicílico")
            st.error("Incompatibilidad crítica (mezcla eutéctica)")
            st.write("""
                **Tipo de interacción:** Interacción física (mezcla eutéctica)

                **Qué ocurre:**
                El alcanfor y el mentol forman mezclas eutécticas con resorcinol y ácido salicílico,
                lo que provoca que los sólidos se conviertan en una mezcla líquida.

                **Impacto farmacéutico:**
                - Licuefacción del sistema
                - Pérdida de forma farmacéutica (tabletas, polvos)
                - Problemas de manufactura (mezcla pegajosa)

                **Acción recomendada:**
                - Evitar la mezcla directa en formas sólidas
                - Usar adsorbentes (ej. sílica, almidón) para estabilizar
                - Incorporar en fases separadas si es necesario
                """)
            st.markdown("#### 🟠 Temperatura y exposición al ambiente")
            st.warning("Factor crítico de pérdida")
            st.write("""
                **Tipo de interacción:** Pérdida física (sublimación)

                **Qué ocurre:**
                Debido a su alta volatilidad, el alcanfor y mentol pueden sublimarse
                a temperatura ambiente o durante el calentamiento.

                **Impacto farmacéutico:**
                - Pérdida de principio activo
                - Variabilidad en la dosis
                - Disminución de eficacia del producto

                **Acción recomendada:**
                - Evitar calentamiento innecesario
                - Añadirlos al final del proceso
                - Mantener envases bien cerrados
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en sistemas adecuados")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Son compatibles con sistemas lipofílicos como aceites y bases de ungüentos.

                **Importancia en formulación:**
                - Ideales para formulaciones tópicas
                - Se disuelven bien en fases oleosas

                **Acción recomendada:**
                - Usar bases oleosas o emulsiones adecuadas
                - Controlar condiciones de almacenamiento
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El principal problema del alcanfor y mentol no es su reactividad química,
                sino su comportamiento físico: **formación de mezclas eutécticas y volatilidad**.
                Estos factores pueden comprometer la estabilidad y forma farmacéutica si no se controlan.
                """)
            st.caption("Referencia: Allen, 2016, p. 179. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Alcanfor y Mentol":
            st.subheader("🧪 Propiedades Fisicoquímicas del Alcanfor y Mentol")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólidos volátiles")
            col2.metric("Naturaleza", "Lipofílica")
            col3.metric("Característica clave", "Sublimación")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Insolubles en agua
                - Solubles en alcohol
                - Solubles en aceites
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Volátiles a temperatura ambiente
                - Olor característico intenso
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Sensibles a temperatura
                - Se subliman fácilmente
                - Pueden perderse durante almacenamiento
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Pueden licuarse al mezclarse con otros sólidos (eutécticos)
                - Se incorporan mejor en bases oleosas
                - Deben añadirse al final del proceso
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatibles con aceites y alcoholes
                - Incompatibles con algunos sólidos por formación de eutécticos
                """)
            st.success("💡 Dato clave: La formación de mezclas eutécticas es el principal problema en formulación sólida.")
            st.caption("Referencia: Allen, 2016, p. 668, 669, 179. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Alcanfor y Mentol":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Alantoína":
            st.subheader("📋 Ficha Técnica: Alantoína")
            st.info("Uso: Agente cicatrizante, regenerador celular y protector de la piel.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                La alantoína es un compuesto orgánico con propiedades epitelizantes y queratolíticas suaves,
                que favorece la regeneración celular y la cicatrización de la piel. Es ampliamente utilizada
                en formulaciones dermatológicas por su capacidad para promover la renovación del tejido.
                (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Solubilidad: 1:190 en agua
                - Prácticamente insoluble en alcohol
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Cremas y lociones dermatológicas
                - Productos para piel sensible
                - Preparaciones cicatrizantes
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Solubilidad limitada → requiere buena dispersión
                - Sensible a temperatura elevada
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Precipitación si no se disuelve correctamente
                - Pérdida de actividad por calentamiento excesivo
                """)
            st.info("💡 Dato clave: Su estabilidad depende principalmente del pH y la temperatura del sistema.")
            st.caption("Referencia: Allen, 2016, p. 668, 348. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Alantoína":
            st.subheader("🧮 Interacciones de la Alantoína")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 pH fuera de rango (ácido o alcalino extremo)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Degradación química dependiente de pH

                **Qué ocurre:**
                La alantoína es estable en un rango de pH de 4 a 9. Fuera de este rango,
                puede degradarse y perder su actividad.

                **Impacto farmacéutico:**
                - Pérdida de eficacia del activo
                - Disminución de estabilidad del producto
                - Posible alteración de la formulación

                **Acción recomendada:**
                - Formular dentro del rango de pH 4–9
                - Evitar excipientes que alteren significativamente el pH
                """)
            st.markdown("#### 🔴 Temperatura elevada (>80°C)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Degradación térmica

                **Qué ocurre:**
                La alantoína se descompone cuando se somete a calor prolongado por encima de 80°C.

                **Impacto farmacéutico:**
                - Pérdida de actividad biológica
                - Disminución de eficacia del producto final

                **Acción recomendada:**
                - Evitar calentamiento prolongado
                - Incorporar en fases de enfriamiento
                """)
            st.markdown("#### 🟠 Solubilidad limitada")
            st.warning("Factor de riesgo en formulación")
            st.write("""
                **Tipo de interacción:** Problema físico (disolución)

                **Qué ocurre:**
                La alantoína tiene solubilidad limitada en agua y es prácticamente insoluble en alcohol,
                lo que puede generar precipitación.

                **Impacto farmacéutico:**
                - Formación de cristales
                - Mala distribución del activo
                - Problemas de uniformidad de dosis

                **Acción recomendada:**
                - Disolver completamente antes de incorporar
                - Usar agitación adecuada
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Es compatible con la mayoría de excipientes dermatológicos si se mantiene en condiciones adecuadas.

                **Importancia en formulación:**
                - Ideal para cremas y lociones
                - Buena tolerancia en piel

                **Acción recomendada:**
                - Controlar pH y temperatura
                - Asegurar buena dispersión
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                La alantoína es un activo estable y seguro, pero su desempeño depende del
                control del pH y la temperatura. Su principal reto en formulación es su
                solubilidad limitada y sensibilidad al calor.
                """)
            st.caption("Referencia: Allen, 2016, p. 348, 668. Basado en el archivo del proyecto.")

    with tab_propiedades:
        if activo == "Alantoína":
            st.subheader("🧪 Propiedades Fisicoquímicas de la Alantoína")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólido cristalino")
            col2.metric("Solubilidad", "1:190 en agua")
            col3.metric("Estabilidad pH", "4 – 9")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Moderadamente soluble en agua
                - Prácticamente insoluble en alcohol
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Sólido blanco cristalino
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable entre pH 4 y 9
                - Se descompone por calor prolongado (>80°C)
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Puede precipitar si no se disuelve correctamente
                - Se incorpora mejor en fase acuosa
                - Requiere control de temperatura
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con excipientes dermatológicos comunes
                - Sensible a condiciones extremas de pH y temperatura
                """)
            st.success("💡 Dato clave: La alantoína debe añadirse en fases finales para evitar degradación térmica.")
            st.caption("Referencia: Allen, 2016, p. 668, 348. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Alantoína":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Óxido de Zinc":
            st.subheader("📋 Ficha Técnica: Óxido de Zinc")
            st.info("Uso: Protector cutáneo, astringente y agente dermatológico.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El óxido de zinc es un compuesto inorgánico con propiedades protectoras, astringentes
                y antimicrobianas leves. Actúa formando una barrera física sobre la piel, lo que lo hace
                útil en tratamientos dermatológicos como irritaciones, dermatitis y formulaciones tipo pasta.
                (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Prácticamente insoluble en agua y alcohol
                - Polvo blanco fino
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Pastas dermatológicas (ej. Pasta de Lassar)
                - Cremas protectoras
                - Ungüentos
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - No se disuelve → se dispersa
                - Requiere agentes suspensores o bases adecuadas
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Sedimentación si no se dispersa correctamente
                - Formación de sistemas muy viscosos o duros
                """)
            st.info("💡 Dato clave: El óxido de zinc no se disuelve, su comportamiento depende de la dispersión en la base.")
            st.caption("Referencia: Allen, 2016, p. 672, 251, 471. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Óxido de Zinc":
            st.subheader("🧮 Interacciones del Óxido de Zinc")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Ácidos (citratos, salicilatos, etc.)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido-base

                **Qué ocurre:**
                El óxido de zinc reacciona con ácidos formando sales de zinc.

                **Impacto farmacéutico:**
                - Cambio en la composición de la formulación
                - Pérdida de la función original del activo
                - Posible alteración de pH

                **Acción recomendada:**
                - Evitar combinar con activos ácidos sin control
                - Ajustar formulación si se requiere interacción controlada
                """)
            st.markdown("#### 🔴 Aceites vegetales")
            st.error("Interacción crítica en formulación")
            st.write("""
                **Tipo de interacción:** Reacción química (saponificación parcial)

                **Qué ocurre:**
                El óxido de zinc puede reaccionar con aceites vegetales formando
                "jabones de zinc", lo que endurece la preparación.

                **Impacto farmacéutico:**
                - Aumento de viscosidad
                - Endurecimiento de la pasta
                - Cambios en textura y extensibilidad

                **Acción recomendada:**
                - Controlar proporciones en formulación
                - Considerar el efecto en la textura final
                """)
            st.markdown("#### 🟠 Insolubilidad")
            st.warning("Factor crítico en formulación")
            st.write("""
                **Tipo de interacción:** Problema físico (dispersión)

                **Qué ocurre:**
                El óxido de zinc no se disuelve, por lo que puede sedimentar si no se
                dispersa adecuadamente.

                **Impacto farmacéutico:**
                - Falta de uniformidad
                - Problemas de dosificación
                - Inestabilidad física

                **Acción recomendada:**
                - Usar agentes suspensores
                - Aplicar buena técnica de dispersión
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Es compatible con muchas bases dermatológicas si no contienen componentes reactivos.

                **Importancia en formulación:**
                - Ideal para pastas protectoras
                - Uso seguro en formulaciones tópicas

                **Acción recomendada:**
                - Seleccionar bases inertes
                - Controlar interacción con otros activos
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El óxido de zinc es un compuesto estable, pero altamente reactivo frente a ácidos
                y capaz de modificar la textura de las formulaciones al reaccionar con aceites.
                Su principal reto es su comportamiento físico como sólido insoluble.
                """)
            st.caption("Referencia: Allen, 2016, p. 251, 471. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Óxido de Zinc":
            st.subheader("🧪 Propiedades Fisicoquímicas del Óxido de Zinc")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Polvo blanco")
            col2.metric("Solubilidad", "Insoluble")
            col3.metric("Naturaleza", "Inorgánico")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Insoluble en agua
                - Insoluble en alcohol
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Polvo fino blanco
                - No volátil
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable en condiciones normales
                - Reactivo frente a ácidos
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se dispersa, no se disuelve
                - Puede sedimentar
                - Puede endurecer formulaciones con aceites
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con bases dermatológicas
                - Incompatible con ácidos
                - Interacciona con aceites vegetales
                """)
            st.success("💡 Dato clave: El óxido de zinc modifica la textura de las formulaciones más que su química en muchos casos.")
            st.caption("Referencia: Allen, 2016, p. 672. Complementado para fines didácticos.")
        with tab_reacciones_adversas:
            if activo == "Óxido de Zinc":
                st.subheader("⚠️ Reacciones medicamentosas")
                st.write("""
                    - 🟠 El uso simultáneo de HIERRO y ZINC puede provocar una disminución de la absorción gastrointestinal del hierro y/o del zinc.
                    """)
                st.markdown("### 🍴 Interacciones con alimentos")
                st.write("""
                    - El consumo simultáneo de zinc y PRODUCTOS lácteos puede provocar una disminución de la concentración de zinc.
                    - El uso simultáneo de zinc y cafeína puede provocar una disminución de los niveles de zinc.
                """)  
                st.caption("Referencia: Micromedex.")





    with tab_fundamento:
        if activo == "Resorcinol":
            st.subheader("📋 Ficha Técnica: Resorcinol")
            st.info("Uso: Agente queratolítico, antiséptico y dermatológico.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El resorcinol es un compuesto fenólico con propiedades queratolíticas y antisépticas,
                utilizado en dermatología para tratar afecciones como acné, dermatitis y otras alteraciones
                de la piel. Su actividad se relaciona con su capacidad para desnaturalizar proteínas
                y afectar la estructura celular. (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Muy soluble en agua y alcohol (1:0.9)
                - Naturaleza fenólica
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Cremas dermatológicas
                - Soluciones tópicas
                - Preparaciones queratolíticas
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Alta reactividad química (fenol)
                - Sensible a oxidación
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Oscurecimiento del producto por oxidación
                - Cambios de color por exposición a luz o aire
                """)
            st.info("💡 Dato clave: El resorcinol es altamente sensible a la oxidación, lo que afecta directamente la apariencia del producto.")
            st.caption("Referencia: Allen, 2016, p. 671, 179. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Resorcinol":
            st.subheader("🧮 Interacciones del Resorcinol")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Luz y aire (oxidación)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Oxidación

                **Qué ocurre:**
                El resorcinol se oxida fácilmente al exponerse a la luz y al aire,
                provocando un oscurecimiento progresivo del producto.

                **Impacto farmacéutico:**
                - Cambio de color (de incoloro a marrón oscuro)
                - Pérdida de estabilidad
                - Disminución de calidad del producto

                **Acción recomendada:**
                - Usar envases ámbar
                - Minimizar exposición al aire
                - Incorporar antioxidantes si es necesario
                """)
            st.markdown("#### 🔴 Álcalis")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción química (medio alcalino)

                **Qué ocurre:**
                El resorcinol es incompatible con álcalis, lo que puede acelerar su degradación
                y afectar su estabilidad.

                **Impacto farmacéutico:**
                - Degradación del activo
                - Alteración del pH de la formulación
                - Pérdida de eficacia

                **Acción recomendada:**
                - Evitar excipientes alcalinos
                - Mantener pH controlado
                """)
            st.markdown("#### 🟠 Sales de hierro")
            st.warning("Incompatibilidad moderada")
            st.write("""
                **Tipo de interacción:** Formación de complejos

                **Qué ocurre:**
                El resorcinol puede reaccionar con sales de hierro produciendo cambios de color.

                **Impacto farmacéutico:**
                - Alteración visual del producto
                - Indicación de reacción química

                **Acción recomendada:**
                - Evitar contaminación con metales
                - Usar utensilios adecuados
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Puede formularse correctamente en sistemas controlados sin exposición a factores oxidantes.

                **Importancia en formulación:**
                - Uso frecuente en dermatología
                - Compatible con sistemas acuosos y alcohólicos

                **Acción recomendada:**
                - Controlar pH
                - Proteger de luz y oxígeno
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El principal problema del resorcinol es su alta susceptibilidad a la oxidación,
                lo que afecta directamente la apariencia y estabilidad del producto.
                El control de luz, aire y pH es fundamental en su formulación.
                """)
            st.caption("Referencia: Allen, 2016, p. 671, 179. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Resorcinol":
            st.subheader("🧪 Propiedades Fisicoquímicas del Resorcinol")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólido cristalino")
            col2.metric("Solubilidad", "Alta (1:0.9)")
            col3.metric("Naturaleza", "Fenólica")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Muy soluble en agua
                - Muy soluble en alcohol
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Sólido cristalino
                - Puede oscurecerse con el tiempo
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Se oxida con luz y aire
                - Sensible a álcalis
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Puede cambiar de color fácilmente
                - Requiere protección contra oxidación
                - Se integra bien en sistemas acuosos y alcohólicos
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con solventes comunes
                - Incompatible con álcalis y metales
                """)
            st.success("💡 Dato clave: El cambio de color es un indicador directo de degradación por oxidación.")
            st.caption("Referencia: Allen, 2016, p. 671. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Resorcinol":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Urea pura":
            st.subheader("📋 Ficha Técnica: Urea")
            st.info("Uso: Humectante, queratolítico y agente dermatológico.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                La urea es un compuesto orgánico altamente soluble que actúa como humectante
                y queratolítico. Su capacidad para retener agua mejora la hidratación de la piel,
                mientras que en concentraciones mayores facilita la descamación del estrato córneo.
                (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Muy soluble en agua (1:1.5)
                - Naturaleza higroscópica
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Cremas hidratantes
                - Preparaciones queratolíticas
                - Lociones dermatológicas
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Altamente higroscópica
                - Puede alterar el pH del sistema
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Absorción de humedad del ambiente
                - Cambios en pH con el tiempo
                """)
            st.info("💡 Dato clave: La urea puede modificar el pH de la formulación debido a su hidrólisis.")
            st.caption("Referencia: Allen, 2016, p. 672. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Urea pura":
            st.subheader("🧮 Interacciones de la Urea")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Agua (hidrólisis)")
            st.error("Incompatibilidad crítica a largo plazo")
            st.write("""
                **Tipo de interacción:** Hidrólisis química

                **Qué ocurre:**
                La urea se hidroliza lentamente en agua liberando **amoníaco (NH₃)**,
                lo que provoca un aumento progresivo del pH.

                **Impacto farmacéutico:**
                - Incremento del pH de la formulación
                - Posible inestabilidad de otros componentes
                - Alteración de la eficacia del producto

                **Acción recomendada:**
                - Controlar pH durante almacenamiento
                - Evaluar estabilidad a largo plazo
                """)
            st.markdown("#### 🔴 Cambio de pH")
            st.error("Riesgo crítico en formulación")
            st.write("""
                **Tipo de interacción:** Alteración del sistema

                **Qué ocurre:**
                La liberación de amoníaco eleva el pH del sistema, afectando la estabilidad
                de otros principios activos y excipientes.

                **Impacto farmacéutico:**
                - Desestabilización de la fórmula
                - Posibles reacciones secundarias
                - Cambios en desempeño del producto

                **Acción recomendada:**
                - Incorporar sistemas buffer si es necesario
                - Monitorear pH en estudios de estabilidad
                """)
            st.markdown("#### 🟠 Humedad ambiental")
            st.warning("Factor crítico")
            st.write("""
                **Tipo de interacción:** Interacción física (absorción de agua)

                **Qué ocurre:**
                La urea es altamente higroscópica, absorbiendo humedad del ambiente.

                **Impacto farmacéutico:**
                - Cambios en textura
                - Aumento de humedad en la formulación
                - Posible degradación acelerada

                **Acción recomendada:**
                - Almacenar en envases herméticos
                - Controlar condiciones ambientales
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Es compatible con sistemas acuosos y dermatológicos si se controla el pH.

                **Importancia en formulación:**
                - Uso amplio en cremas y lociones
                - Buena integración en fase acuosa

                **Acción recomendada:**
                - Controlar pH y humedad
                - Evaluar estabilidad con otros activos
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                La urea es un activo estable en apariencia, pero su hidrólisis lenta puede
                afectar significativamente el pH del sistema, comprometiendo la estabilidad
                de la formulación a largo plazo.
                """)
            st.caption("Referencia: Allen, 2016, p. 672. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Urea pura":
            st.subheader("🧪 Propiedades Fisicoquímicas de la Urea")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólido cristalino")
            col2.metric("Solubilidad", "Muy alta (1:1.5)")
            col3.metric("Característica", "Higroscópica")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Muy soluble en agua
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Sólido cristalino
                - Inodoro
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Sufre hidrólisis lenta en agua
                - Libera amoníaco
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se incorpora fácilmente en fase acuosa
                - Puede modificar el pH con el tiempo
                - Absorbe humedad del ambiente
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con sistemas acuosos
                - Puede afectar otros activos por cambio de pH
                """)
            st.success("💡 Dato clave: La liberación de amoníaco puede alterar la estabilidad de toda la formulación.")
            st.caption("Referencia: Allen, 2016, p. 672. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Urea pura":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Aceite de Trementina, Ácido Tánico y Aceite de Ricino":
            st.subheader("📋 Ficha Técnica: Trementina, Ácido Tánico y Aceite de Ricino")
            st.info("Uso: Vehículos, astringentes y componentes en formulaciones tópicas.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                Este grupo combina tres tipos de compuestos con funciones distintas en formulación:
                
                - **Aceite de trementina:** compuesto volátil con propiedades irritantes y rubefacientes.
                - **Ácido tánico:** compuesto fenólico con propiedades astringentes y capacidad de formar complejos.
                - **Aceite de ricino:** aceite vegetal usado como vehículo lipofílico y emoliente.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Trementina: lipofílica y reactiva
                - Ácido tánico: reactivo con proteínas y metales
                - Aceite de ricino: miscible con alcohol, susceptible a oxidación
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Cremas y ungüentos
                - Vehículos para activos lipofílicos
                - Preparaciones astringentes
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Diferente comportamiento químico entre los tres compuestos
                - Sensibilidad a oxidación (aceites)
                - Reactividad del ácido tánico
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Enranciamiento de aceites
                - Cambios de color por reacciones químicas
                - Interacciones con materiales de envase
                """)
            st.info("💡 Dato clave: La estabilidad del sistema depende principalmente del control de oxidación y compatibilidad química.")
            st.caption("Referencia: Allen, 2016, p. 251, 659, 35, 104, 266, 668.")
    with tab_interraciones:
        if activo == "Aceite de Trementina, Ácido Tánico y Aceite de Ricino":
            st.subheader("🧮 Interacciones de Trementina, Ácido Tánico y Aceite de Ricino")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Aceite de trementina + oxidantes / yodo")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Oxidación / reacción química

                **Qué ocurre:**
                La trementina es incompatible con agentes oxidantes fuertes y con yodo,
                lo que puede provocar reacciones químicas no deseadas.

                **Impacto farmacéutico:**
                - Degradación del compuesto
                - Formación de productos reactivos
                - Riesgo de inestabilidad

                **Acción recomendada:**
                - Evitar oxidantes en la formulación
                - Controlar condiciones de almacenamiento
                """)
            st.markdown("#### 🔴 Trementina + plásticos")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Interacción con material de envase

                **Qué ocurre:**
                La trementina puede atacar o degradar ciertos plásticos.

                **Impacto farmacéutico:**
                - Contaminación del producto
                - Pérdida de integridad del envase

                **Acción recomendada:**
                - Usar envases de vidrio
                """)
            st.markdown("#### 🔴 Ácido tánico + sales de hierro")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Formación de complejos

                **Qué ocurre:**
                El ácido tánico reacciona con sales de hierro formando complejos oscuros
                (similar a tinta negra).

                **Impacto farmacéutico:**
                - Cambio de color intenso
                - Alteración del producto

                **Acción recomendada:**
                - Evitar contaminación metálica
                """)
            st.markdown("#### 🔴 Ácido tánico + proteínas / alcaloides")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Precipitación / complejación

                **Qué ocurre:**
                El ácido tánico forma complejos con proteínas y alcaloides.

                **Impacto farmacéutico:**
                - Precipitación
                - Pérdida de actividad de otros componentes

                **Acción recomendada:**
                - Evaluar compatibilidad antes de formular
                """)
            st.markdown("#### 🟠 Aceite de ricino + aire / calor")
            st.warning("Factor crítico")
            st.write("""
                **Tipo de interacción:** Oxidación (enranciamiento)

                **Qué ocurre:**
                El aceite de ricino se oxida con el aire y el calor, generando rancidez.

                **Impacto farmacéutico:**
                - Mal olor
                - Cambio de color
                - Pérdida de calidad

                **Acción recomendada:**
                - Añadir antioxidantes (ej. vitamina E)
                - Evitar exposición a luz y calor
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible con control adecuado")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Estos compuestos pueden coexistir en formulaciones si se controlan
                oxidación, pH y compatibilidad química.

                **Acción recomendada:**
                - Controlar ambiente
                - Seleccionar excipientes adecuados
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                Este sistema presenta múltiples riesgos: oxidación (aceites),
                formación de complejos (ácido tánico) e incompatibilidad con materiales.
                La formulación requiere control estricto de ambiente y selección de excipientes.
                """)
            st.caption("Referencia: Allen, 2016, p. 251, 659, 35, 104, 266, 668.")
    with tab_propiedades:
        if activo == "Aceite de Trementina, Ácido Tánico y Aceite de Ricino":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Trementina", "Líquido lipofílico")
            col2.metric("Ácido tánico", "Fenólico reactivo")
            col3.metric("Aceite de ricino", "Aceite vegetal")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Trementina: insoluble en agua, soluble en solventes orgánicos
                - Ácido tánico: soluble en agua
                - Aceite de ricino: miscible con alcohol
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Trementina: reactiva con oxidantes
                - Ácido tánico: reactivo con metales
                - Aceite de ricino: susceptible a oxidación
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Aceites → pueden oxidarse (rancidez)
                - Ácido tánico → puede precipitar otros compuestos
                - Trementina → puede interactuar con envases
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Requiere control de oxidación
                - Evitar metales y oxidantes
                - Seleccionar envases adecuados
                """)
            st.success("💡 Dato clave: La oxidación y las reacciones con metales son los principales riesgos de este sistema.")
            st.caption("Referencia: Allen, 2016, p. 251, 659, 35, 104, 266, 668.")
    with tab_reacciones_adversas:
            if activo == "Aceite de Trementina, Ácido Tánico y Aceite de Ricino":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Benzofenona y Dióxido de Titanio":
            st.subheader("📋 Ficha Técnica: Benzofenona y Dióxido de Titanio")
            st.info("Uso: Filtros solares (protección contra radiación UV).")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                Estos compuestos se utilizan como filtros solares con mecanismos distintos:

                - **Benzofenona:** filtro químico que absorbe radiación UV y la transforma en energía menos dañina.
                - **Dióxido de titanio (TiO₂):** filtro físico que refleja y dispersa la radiación UV.

                Esta combinación permite una protección más amplia frente a radiación solar.
                (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Benzofenona: soluble en alcohol, lipofílica
                - Dióxido de titanio: insoluble, sólido inorgánico
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Protectores solares
                - Cremas dermatológicas con filtro UV
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Diferente comportamiento entre ambos compuestos
                - Requiere adecuada dispersión del dióxido de titanio
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Sedimentación del dióxido de titanio
                - Distribución no uniforme del filtro
                """)
            st.info("💡 Dato clave: La eficacia del protector depende de la correcta dispersión del dióxido de titanio.")
            st.caption("Referencia: Allen, 2016, p. 542, 343, 445. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Benzofenona y Dióxido de Titanio":
            st.subheader("🧮 Interacciones de Benzofenona y Dióxido de Titanio")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Dióxido de titanio (sedimentación)")
            st.error("Problema crítico en formulación")
            st.write("""
                **Tipo de interacción:** Problema físico (dispersión)

                **Qué ocurre:**
                El dióxido de titanio es insoluble y tiende a sedimentar si no se mantiene en suspensión.

                **Impacto farmacéutico:**
                - Distribución desigual del filtro solar
                - Disminución de eficacia protectora
                - Producto inestable

                **Acción recomendada:**
                - Usar agentes suspensores (ej. bentonita)
                - Aplicar buena técnica de dispersión
                """)
            st.markdown("#### 🟠 Benzofenona (fase oleosa/alcohólica)")
            st.warning("Factor de formulación")
            st.write("""
                **Tipo de interacción:** Compatibilidad de fase

                **Qué ocurre:**
                La benzofenona es soluble en alcohol y sistemas oleosos, por lo que debe incorporarse
                en la fase adecuada.

                **Impacto farmacéutico:**
                - Mala distribución si se formula incorrectamente
                - Disminución de eficacia

                **Acción recomendada:**
                - Incorporar en fase oleosa o alcohólica
                - Evitar sistemas donde no se disuelva correctamente
                """)
            st.markdown("#### 🟢 Compatibilidad entre filtros")
            st.success("Compatible")
            st.write("""
                **Tipo de interacción:** Complementación funcional

                **Qué ocurre:**
                Ambos compuestos pueden coexistir y complementarse en formulaciones solares.

                **Importancia en formulación:**
                - Mayor espectro de protección UV
                - Mejora de eficacia global del producto

                **Acción recomendada:**
                - Asegurar correcta dispersión y distribución
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El principal reto en esta formulación no es una reacción química,
                sino la correcta distribución de los componentes: el dióxido de titanio
                debe mantenerse disperso, mientras que la benzofenona debe estar en la fase adecuada.
                """)
            st.caption("Referencia: Allen, 2016, p. 343, 445, 542. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Benzofenona y Dióxido de Titanio":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Benzofenona", "Filtro químico")
            col2.metric("TiO₂", "Filtro físico")
            col3.metric("Estado", "Mixto")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Benzofenona: soluble en alcohol
                - Dióxido de titanio: insoluble
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Benzofenona: líquido o sólido según tipo
                - TiO₂: polvo blanco fino
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Benzofenona: estable en fase adecuada
                - TiO₂: estable pero requiere dispersión
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Benzofenona se disuelve en fase oleosa/alcohólica
                - TiO₂ se dispersa, no se disuelve
                - Requiere estabilización del sistema
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible en formulaciones solares
                - Requiere control de fase y dispersión
                """)
            st.success("💡 Dato clave: La eficacia del protector depende más de la distribución que de la reacción química.")
            st.caption("Referencia: Allen, 2016, p. 542, 343, 445. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Benzofenona y Dióxido de Titanio":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Octil Salicilato y Octil Metoxicinamato":
            st.subheader("📋 Ficha Técnica: Octil Salicilato y Octil Metoxicinamato")
            st.info("Uso: Filtros solares orgánicos (protección UV).")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El octil salicilato y el octil metoxicinamato son ésteres orgánicos utilizados como filtros solares.
                Actúan absorbiendo la radiación ultravioleta y disipándola como energía menos dañina.

                Su estructura química tipo éster los hace efectivos como filtros UV, pero también susceptibles
                a hidrólisis en condiciones extremas. (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Ésteres líquidos
                - Insolubles en agua
                - Naturaleza lipofílica
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Protectores solares
                - Cremas y lociones con filtro UV
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Sensibles a pH extremos
                - Requieren fase oleosa para su incorporación
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Degradación por hidrólisis
                - Pérdida de eficacia del filtro solar
                """)
            st.info("💡 Dato clave: Su estabilidad depende directamente del control del pH del sistema.")
            st.caption("Referencia: Allen, 2016, p. 543. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Octil Salicilato y Octil Metoxicinamato":
            st.subheader("🧮 Interacciones de Octil Salicilato y Octil Metoxicinamato")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Ácidos y bases fuertes")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Hidrólisis de éster

                **Qué ocurre:**
                Estos compuestos pueden hidrolizarse en presencia de ácidos o bases fuertes,
                rompiendo el enlace éster.

                **Impacto farmacéutico:**
                - Pérdida de eficacia del filtro solar
                - Formación de productos de degradación
                - Disminución de protección UV

                **Acción recomendada:**
                - Evitar pH extremos
                - Mantener formulación en rango de pH controlado
                """)
            st.markdown("#### 🟠 Presencia de agua")
            st.warning("Factor de riesgo")
            st.write("""
                **Tipo de interacción:** Hidrólisis favorecida

                **Qué ocurre:**
                Aunque son insolubles en agua, la presencia de agua en combinación con pH extremos
                puede favorecer la hidrólisis.

                **Impacto farmacéutico:**
                - Degradación lenta del activo
                - Disminución de estabilidad

                **Acción recomendada:**
                - Controlar fase acuosa en emulsiones
                - Mantener pH estable
                """)
            st.markdown("#### 🟢 Compatibilidad en fase oleosa")
            st.success("Compatible")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Son altamente compatibles con sistemas oleosos y se integran fácilmente en la fase lipofílica.

                **Importancia en formulación:**
                - Ideales para emulsiones tipo O/W o W/O
                - Buen desempeño en protectores solares

                **Acción recomendada:**
                - Incorporar en fase oleosa
                - Evitar exposición a condiciones extremas
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El principal riesgo de estos compuestos es la hidrólisis del enlace éster,
                lo que reduce su eficacia como filtro UV. El control del pH es el factor
                más importante para su estabilidad.
                """)
            st.caption("Referencia: Allen, 2016, p. 543. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Octil Salicilato y Octil Metoxicinamato":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Líquidos")
            col2.metric("Solubilidad", "Insolubles en agua")
            col3.metric("Naturaleza", "Ésteres")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Insolubles en agua
                - Solubles en fase oleosa
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Líquidos aceitosos
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Sensibles a hidrólisis
                - Inestables en pH extremos
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se incorporan en fase oleosa
                - Pueden degradarse en emulsiones mal formuladas
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatibles con aceites
                - Incompatibles con condiciones extremas de pH
                """)
            st.success("💡 Dato clave: La estabilidad del enlace éster define la eficacia del filtro solar.")
            st.caption("Referencia: Allen, 2016, p. 543. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Octil Salicilato y Octil Metoxicinamato":
                st.subheader("No hay informacion con los principios activos disponibles")
            


    with tab_fundamento:
        if activo == "Bicarbonato de Sodio y Carbonato de Calcio":
            st.subheader("📋 Ficha Técnica: Bicarbonato de Sodio y Carbonato de Calcio")
            st.info("Uso: Antiácidos y agentes neutralizantes.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El bicarbonato de sodio y el carbonato de calcio son compuestos alcalinos utilizados
                como antiácidos. Actúan neutralizando el ácido gástrico mediante reacciones ácido-base,
                produciendo sales, agua y dióxido de carbono.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Naturaleza básica (alcalina)
                - Reactividad con ácidos
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Antiácidos orales
                - Formulaciones efervescentes
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Alta reactividad con ácidos
                - Generación de gas (CO₂)
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Efervescencia no controlada
                - Pérdida de estabilidad en presencia de humedad
                """)
            st.info("💡 Dato clave: La liberación de CO₂ es clave para su acción, pero también un riesgo en formulación.")
            st.caption("Referencia: Allen, 2016, p. 36, 129, 35, 104. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Bicarbonato de Sodio y Carbonato de Calcio":
            st.subheader("🧮 Interacciones de Bicarbonato de Sodio y Carbonato de Calcio")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Ácidos (reacción ácido-base)")
            st.error("Interacción crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido-base con liberación de gas

                **Qué ocurre:**
                Estos compuestos reaccionan inmediatamente con ácidos liberando **dióxido de carbono (CO₂)**,
                produciendo efervescencia.

                **Impacto farmacéutico:**
                - Pérdida del principio activo
                - Generación de gas → presión en envases
                - Inestabilidad del producto

                **Acción recomendada:**
                - Evitar contacto con ácidos en almacenamiento
                - Controlar formulaciones efervescentes
                """)
            st.markdown("#### 🔴 Ácido acetilsalicílico (Aspirina)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido-base

                **Qué ocurre:**
                El carbonato de calcio es incompatible con aspirina, favoreciendo su degradación.

                **Impacto farmacéutico:**
                - Pérdida de eficacia del fármaco
                - Formación de productos de degradación

                **Acción recomendada:**
                - Evitar combinación directa
                - Evaluar compatibilidad antes de formular
                """)
            st.markdown("#### 🟠 Humedad")
            st.warning("Factor crítico")
            st.write("""
                **Tipo de interacción:** Activación de reactividad

                **Qué ocurre:**
                La humedad puede iniciar reacciones prematuras con ácidos presentes.

                **Impacto farmacéutico:**
                - Pérdida de estabilidad
                - Activación no deseada de efervescencia

                **Acción recomendada:**
                - Almacenamiento en condiciones secas
                - Uso de envases herméticos
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Son estables en ausencia de ácidos y humedad.

                **Importancia en formulación:**
                - Uso seguro en formulaciones sólidas secas
                - Utilizados en sistemas efervescentes controlados

                **Acción recomendada:**
                - Controlar ambiente
                - Evitar exposición a humedad y ácidos
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El principal riesgo de estos compuestos es su alta reactividad con ácidos,
                generando CO₂. Esto puede ser útil en formulaciones efervescentes, pero
                representa un riesgo si no se controla adecuadamente.
                """)
            st.caption("Referencia: Allen, 2016, p. 36, 129, 35, 104. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Bicarbonato de Sodio y Carbonato de Calcio":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólidos")
            col2.metric("Naturaleza", "Alcalina")
            col3.metric("Reactividad", "Alta con ácidos")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Bicarbonato de sodio: soluble en agua
                - Carbonato de calcio: poco soluble
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Polvos blancos
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Reactivos frente a ácidos
                - Sensibles a humedad
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Reaccionan liberando CO₂
                - Utilizados en sistemas efervescentes
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Incompatibles con ácidos
                - Requieren condiciones secas
                """)
            st.success("💡 Dato clave: La efervescencia es útil solo cuando está controlada.")
            st.caption("Referencia: Allen, 2016, p. 36, 129, 35, 104. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
        if activo == "Bicarbonato de Sodio y Carbonato de Calcio":
            st.subheader("⚠️ Reacciones medicamentosas")
            st.write("""
                    - 🟠 El uso simultáneo de ASPIRINA y productos que contengan ALUMINIO, CALCIO O MAGNESIO puede reducir la eficacia del salicilato.
                    - 🟠 El uso simultáneo de productos que contengan hierro y aluminio, calcio o magnesio puede reducir la eficacia del hierro.
                """)
            st.markdown("### 🍴 Interacciones con alimentos")
            st.write("""
                    - El consumo simultáneo de ALIMENTOS que contienen CALCIO y ÁCIDO FÍTICO puede reducir la eficacia del calcio.
                    - El consumo simultáneo de ALIMENTOS que contienen CALCIO y ÁCIDO OXÁLICO puede reducir la ingesta de calcio.
                """) 
            st.caption("Referencia: Micromedex.")
        



    with tab_fundamento:
        if activo == "Carbón Activado":
            st.subheader("📋 Ficha Técnica: Carbón Activado")
            st.info("Uso: Adsorbente en formulaciones farmacéuticas y tratamiento de intoxicaciones.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El carbón activado es un material con alta área superficial que actúa mediante
                adsorción física, reteniendo moléculas en su superficie.

                Esta propiedad le permite captar toxinas, fármacos y otras sustancias,
                lo que lo hace útil en tratamientos de intoxicación y en ciertas formulaciones.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Alta capacidad de adsorción
                - Gran área superficial
                - Material poroso
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Tratamiento de intoxicaciones
                - Adsorbente en formulaciones
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Puede adsorber no solo toxinas, sino también fármacos y excipientes
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Pérdida de actividad de otros componentes
                - Disminución de eficacia de conservadores
                """)
            st.info("💡 Dato clave: El carbón activado no distingue entre sustancias, adsorbe casi todo.")
            st.caption("Referencia: Allen, 2016, p. 195, 280. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Carbón Activado":
            st.subheader("🧮 Interacciones del Carbón Activado")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Conservadores (Parabenos)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Adsorción física

                **Qué ocurre:**
                El carbón activado adsorbe conservadores como los parabenos,
                atrapándolos en su superficie.

                **Impacto farmacéutico:**
                - Pérdida de acción antimicrobiana
                - Riesgo de contaminación microbiológica
                - Disminución de vida útil del producto

                **Acción recomendada:**
                - Evitar uso conjunto
                - Evaluar sistemas alternativos de conservación
                """)
            st.markdown("#### 🔴 Principios activos")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Adsorción no selectiva

                **Qué ocurre:**
                El carbón activado puede adsorber principios activos,
                reduciendo su concentración disponible.

                **Impacto farmacéutico:**
                - Disminución de eficacia terapéutica
                - Pérdida de dosis real

                **Acción recomendada:**
                - Evitar combinar con otros fármacos activos
                - Usarlo solo cuando la adsorción sea el objetivo
                """)
            st.markdown("#### 🟠 Adsorción general")
            st.warning("Factor crítico")
            st.write("""
                **Tipo de interacción:** Adsorción física

                **Qué ocurre:**
                Puede adsorber colorantes, excipientes y otras moléculas presentes en la formulación.

                **Impacto farmacéutico:**
                - Cambios en color
                - Alteración de composición
                - Variabilidad en la formulación

                **Acción recomendada:**
                - Evaluar compatibilidad completa de la fórmula
                """)
            st.markdown("#### 🟢 Uso controlado")
            st.success("Compatible si se usa correctamente")
            st.write("""
                **Tipo de interacción:** Funcional

                **Qué ocurre:**
                Es útil cuando la adsorción es deseada (ej. intoxicaciones).

                **Importancia en formulación:**
                - Uso dirigido como adsorbente
                - Aplicación terapéutica específica

                **Acción recomendada:**
                - Usarlo solo cuando su función sea adsorber
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El carbón activado es altamente útil, pero también peligroso en formulación,
                ya que puede eliminar la eficacia de otros componentes. Su uso debe ser
                cuidadosamente justificado.
                """)
            st.caption("Referencia: Allen, 2016, p. 280. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Carbón Activado":
            st.subheader("🧪 Propiedades Fisicoquímicas del Carbón Activado")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Polvo negro")
            col2.metric("Propiedad clave", "Adsorción")
            col3.metric("Naturaleza", "Poroso")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Insoluble en agua
                - Insoluble en alcohol
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Polvo fino negro
                - Alta área superficial
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable químicamente
                - Puede interactuar físicamente con otros compuestos
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Adsorbe moléculas
                - Puede eliminar activos o excipientes
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Incompatible con múltiples compuestos por adsorción
                """)
            st.success("💡 Dato clave: Su alta área superficial es responsable tanto de su utilidad como de sus riesgos.")
            st.caption("Referencia: Allen, 2016, p. 195. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Carbón Activado":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Hidróxidos de Magnesio y Aluminio":
            st.subheader("📋 Ficha Técnica: Hidróxidos de Magnesio y Aluminio")
            st.info("Uso: Antiácidos y protectores gástricos.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                Los hidróxidos de magnesio y aluminio son compuestos básicos utilizados como antiácidos.
                Actúan neutralizando el ácido gástrico mediante reacciones ácido–base, formando sales
                y agua.

                Su combinación permite equilibrar efectos secundarios: el magnesio puede causar diarrea,
                mientras que el aluminio puede causar estreñimiento.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Naturaleza alcalina
                - Baja solubilidad en agua
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Suspensiones antiácidas
                - Tabletas masticables
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Pueden alterar el pH del sistema
                - Interaccionan con otros fármacos
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Sedimentación en suspensiones
                - Variabilidad en neutralización
                """)
            st.info("💡 Dato clave: El control del pH es fundamental en formulaciones con estos compuestos.")
            st.caption("Referencia: Allen, 2016, p. 36, 129. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Hidróxidos de Magnesio y Aluminio":
            st.subheader("🧮 Interacciones de Hidróxidos de Magnesio y Aluminio")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Ácidos")
            st.error("Interacción crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido–base

                **Qué ocurre:**
                Los hidróxidos reaccionan con ácidos formando sales de magnesio o aluminio y agua.

                **Impacto farmacéutico:**
                - Neutralización del ácido (efecto deseado)
                - Pérdida del principio activo ácido si no se controla

                **Acción recomendada:**
                - Usar solo cuando la neutralización sea el objetivo
                """)
            st.markdown("#### 🔴 Otros fármacos")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Alteración de absorción

                **Qué ocurre:**
                Pueden unirse o interferir con la absorción de otros fármacos en el tracto gastrointestinal.

                **Impacto farmacéutico:**
                - Disminución de biodisponibilidad
                - Reducción de eficacia terapéutica

                **Acción recomendada:**
                - Separar la administración (2 horas mínimo)
                """)
            st.markdown("#### 🟠 Cambio de pH")
            st.warning("Factor crítico")
            st.write("""
                **Tipo de interacción:** Alteración del medio

                **Qué ocurre:**
                Elevan el pH del sistema, lo que puede afectar la estabilidad de otros compuestos.

                **Impacto farmacéutico:**
                - Inestabilidad de otros activos
                - Posibles reacciones secundarias

                **Acción recomendada:**
                - Controlar pH en formulación
                """)
            st.markdown("#### 🟠 Sedimentación")
            st.warning("Problema físico")
            st.write("""
                **Tipo de interacción:** Problema de dispersión

                **Qué ocurre:**
                Al ser poco solubles, tienden a sedimentar en suspensiones.

                **Impacto farmacéutico:**
                - Dosis no uniforme
                - Inestabilidad física

                **Acción recomendada:**
                - Usar agentes suspensores
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Son estables si se controlan pH y dispersión.

                **Acción recomendada:**
                - Formular adecuadamente la suspensión
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                Estos compuestos son útiles como antiácidos, pero pueden alterar el pH y la absorción
                de otros fármacos, por lo que requieren control en formulación y administración.
                """)
            st.caption("Referencia: Allen, 2016, p. 36, 129. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Hidróxidos de Magnesio y Aluminio":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólidos")
            col2.metric("Solubilidad", "Baja")
            col3.metric("Naturaleza", "Alcalina")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Baja solubilidad en agua
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Polvos blancos
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estables en condiciones normales
                - Reactivos con ácidos
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se utilizan en suspensiones
                - Tienden a sedimentar
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Incompatibles con ácidos
                - Pueden afectar otros fármacos
                """)
            st.success("💡 Dato clave: Su efecto antiácido depende de su reacción con el ácido, pero esto también puede generar interacciones.")
            st.caption("Referencia: Allen, 2016, p. 36, 129. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
        if activo == "Hidróxidos de Magnesio y Aluminio":
            st.subheader("⚠️ Reacciones medicamentosas")
            st.write("""
                    - 🟠 El uso simultáneo de ASPIRINA y productos que contengan ALUMINIO, CALCIO O MAGNESIO puede reducir la eficacia del salicilato.
                    - 🟠 El uso simultáneo de ÁCIDO ASCÓRBICO y ANTIÁCIDOS puede provocar intoxicación por aluminio (cambios de personalidad, convulsiones, coma).
                    - 🟠 El uso simultáneo de productos que contengan hierro y aluminio, calcio o magnesio puede reducir la eficacia del hierro.
                """)
            st.caption("Referencia: Micromedex.")



    with tab_fundamento:
        if activo == "Ácido Ascórbico (Vit C) y Sulfato Ferroso":
            st.subheader("📋 Ficha Técnica: Ácido Ascórbico y Sulfato Ferroso")
            st.info("Uso: Suplementos nutricionales y tratamiento de anemia.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El ácido ascórbico (vitamina C) y el sulfato ferroso (hierro) se utilizan
                en combinación debido a su efecto sinérgico.

                El ácido ascórbico actúa como agente reductor, manteniendo el hierro en su forma
                ferrosa (Fe²⁺), que es más fácilmente absorbida en el organismo.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Ácido ascórbico: antioxidante, soluble en agua
                - Sulfato ferroso: sal de hierro, soluble en agua
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Suplementos de hierro
                - Tratamiento de anemia ferropénica
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Sensibilidad a oxidación
                - Posible cambio de color en el tiempo
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Oxidación del hierro (Fe²⁺ → Fe³⁺)
                - Degradación del ácido ascórbico
                """)
            st.info("💡 Dato clave: El ácido ascórbico protege al hierro de la oxidación y mejora su absorción.")
            st.caption("Referencia: Allen, 2016, p. 35, 104. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Ácido Ascórbico y Sulfato Ferroso":
            st.subheader("🧮 Interacciones de Ácido Ascórbico y Sulfato Ferroso")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Oxidación del hierro")
            st.error("Factor crítico")
            st.write("""
                **Tipo de interacción:** Reacción redox

                **Qué ocurre:**
                El hierro ferroso (Fe²⁺) puede oxidarse a férrico (Fe³⁺), reduciendo su absorción.

                **Impacto farmacéutico:**
                - Disminución de biodisponibilidad
                - Menor eficacia terapéutica

                **Acción recomendada:**
                - Proteger de oxígeno
                - Usar antioxidantes (como ácido ascórbico)
                """)
            st.markdown("#### 🟢 Ácido ascórbico (efecto protector)")
            st.success("Interacción beneficiosa")
            st.write("""
                **Tipo de interacción:** Reducción química

                **Qué ocurre:**
                El ácido ascórbico mantiene el hierro en estado ferroso (Fe²⁺),
                favoreciendo su absorción.

                **Impacto farmacéutico:**
                - Aumento de biodisponibilidad
                - Mejora del efecto terapéutico

                **Acción recomendada:**
                - Formular juntos para mejorar eficacia
                """)
            st.markdown("#### 🔴 Luz, aire y calor")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Oxidación

                **Qué ocurre:**
                El ácido ascórbico es altamente susceptible a oxidarse en presencia de luz,
                oxígeno y calor.

                **Impacto farmacéutico:**
                - Pérdida de actividad antioxidante
                - Disminución de estabilidad

                **Acción recomendada:**
                - Usar envases ámbar
                - Minimizar exposición al aire
                """)
            st.markdown("#### 🟠 Metales")
            st.warning("Factor de riesgo")
            st.write("""
                **Tipo de interacción:** Catalítica

                **Qué ocurre:**
                Los metales pueden catalizar la oxidación del ácido ascórbico.

                **Impacto farmacéutico:**
                - Degradación acelerada
                - Cambio de color

                **Acción recomendada:**
                - Evitar contaminación metálica
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                Esta combinación es beneficiosa, pero inestable. El ácido ascórbico protege
                al hierro, pero también es susceptible a oxidación, por lo que el control
                de ambiente es fundamental.
                """)
            st.caption("Referencia: Allen, 2016, p. 35, 104. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Ácido Ascórbico y Sulfato Ferroso":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Ácido ascórbico", "Antioxidante")
            col2.metric("Sulfato ferroso", "Sal de hierro")
            col3.metric("Naturaleza", "Redox")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Ambos son solubles en agua
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Ácido ascórbico: sólido cristalino
                - Sulfato ferroso: sólido cristalino
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Ácido ascórbico: sensible a oxidación
                - Hierro: puede oxidarse
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Requieren protección contra oxidación
                - Pueden cambiar de color con el tiempo
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Interacción beneficiosa (reducción del hierro)
                - Sensibles a condiciones ambientales
                """)
            st.success("💡 Dato clave: La estabilidad depende del equilibrio entre oxidación y reducción.")
            st.caption("Referencia: Allen, 2016, p. 35, 104. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Ácido Ascórbico y Sulfato Ferroso":
                st.subheader("⚠️ Reacciones medicamentosas")
                st.write("""
                    - 🟠 El uso simultáneo de HIERRO y ZINC puede provocar una disminución de la absorción gastrointestinal del hierro y/o del zinc.
                    - 🟠 El uso simultáneo de ÁCIDO ASCÓRBICO y ANTIÁCIDOS puede provocar intoxicación por aluminio (cambios de personalidad, convulsiones, coma).
                    - 🟠 El uso simultáneo de productos que contengan hierro y aluminio, calcio o magnesio puede reducir la eficacia del hierro.
                    """)
                st.markdown("### 🍴 Interacciones con alimentos")
                st.write("""
                    - El consumo simultáneo de alimentos que contienen hierro y ácido fítico puede reducir la absorción de hierro.
                    - El consumo simultáneo de alimentos ricos en hierro y lácteos puede reducir la biodisponibilidad del hierro.
                    - El consumo simultáneo de hierro y soya puede reducir la absorción de hierro.
                """)
                st.caption("Referencia: Micromedex.")


    with tab_fundamento:
        if activo == "Vitaminas A y E":
            st.subheader("📋 Ficha Técnica: Vitaminas A y E")
            st.info("Uso: Antioxidantes, regeneradores celulares y protectores dermatológicos.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                Las vitaminas A y E son compuestos liposolubles ampliamente utilizados en
                formulaciones dermatológicas.

                - **Vitamina A (retinol):** favorece la regeneración celular y la renovación de la piel.
                - **Vitamina E (tocoferol):** actúa como antioxidante, protegiendo lípidos y otros
                compuestos de la oxidación.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Liposolubles
                - Sensibles a oxidación
                - Sensibles a luz
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Cremas anti-envejecimiento
                - Productos dermatológicos
                - Formulaciones antioxidantes
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Alta sensibilidad a luz, oxígeno y calor
                - Requieren protección antioxidante
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Degradación por oxidación
                - Pérdida de actividad
                - Cambios de color
                """)
            st.info("💡 Dato clave: La vitamina E puede estabilizar a la vitamina A frente a oxidación.")
            st.caption("Referencia: Allen, 2016, p. 280, 542. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Vitaminas A y E":
            st.subheader("🧮 Interacciones de Vitaminas A y E")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Luz, aire y calor")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Oxidación

                **Qué ocurre:**
                Ambas vitaminas son altamente sensibles a la oxidación por exposición a luz,
                oxígeno y calor.

                **Impacto farmacéutico:**
                - Pérdida de actividad biológica
                - Degradación del producto
                - Cambios de color

                **Acción recomendada:**
                - Usar envases ámbar
                - Minimizar exposición al aire
                - Almacenar en condiciones controladas
                """)
            st.markdown("#### 🟢 Vitamina E (efecto protector)")
            st.success("Interacción beneficiosa")
            st.write("""
                **Tipo de interacción:** Antioxidante

                **Qué ocurre:**
                La vitamina E protege a la vitamina A y otros lípidos de la oxidación.

                **Impacto farmacéutico:**
                - Mayor estabilidad de la formulación
                - Prolongación de vida útil

                **Acción recomendada:**
                - Formular conjuntamente cuando sea posible
            """)
            st.markdown("#### 🟠 Metales")
            st.warning("Factor de riesgo")

            st.write("""
                **Tipo de interacción:** Catalítica

                **Qué ocurre:**
                Los metales pueden catalizar la oxidación de estas vitaminas.

                **Impacto farmacéutico:**
                - Degradación acelerada
                - Pérdida de eficacia

                **Acción recomendada:**
                - Evitar contaminación metálica
                """)
            st.markdown("#### 🟢 Compatibilidad en fase oleosa")
            st.success("Compatible")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Ambas vitaminas son liposolubles y se integran adecuadamente en fases oleosas.

                **Importancia en formulación:**
                - Ideales para cremas y emulsiones
                - Buena estabilidad en fase lipofílica

                **Acción recomendada:**
                - Incorporar en fase oleosa
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                Estas vitaminas son altamente beneficiosas, pero muy inestables frente a oxidación.
                La vitamina E juega un papel clave como antioxidante, mejorando la estabilidad del sistema.
                """)
            st.caption("Referencia: Allen, 2016, p. 280, 542. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Vitaminas A y E":
            st.subheader("🧪 Propiedades Fisicoquímicas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Solubilidad", "Liposolubles")
            col2.metric("Estabilidad", "Baja a oxidación")
            col3.metric("Función", "Antioxidante")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Insolubles en agua
                - Solubles en aceites
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Líquidos o aceitosos
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Sensibles a luz
                - Sensibles a oxígeno
                - Sensibles a calor
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se incorporan en fase oleosa
                - Requieren antioxidantes
                - Pueden degradarse fácilmente
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatibles con sistemas lipofílicos
                - Sensibles a metales y oxidación
                """)
            st.success("💡 Dato clave: La vitamina E actúa como protector natural frente a la oxidación.")
            st.caption("Referencia: Allen, 2016, p. 280, 542. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Vitaminas A y E":
                st.subheader("No hay informacion con los principios activos disponibles")



    with tab_fundamento:
        if activo == "Fluoruro de Sodio":
            st.subheader("📋 Ficha Técnica: Fluoruro de Sodio (NaF)")
            st.info("Uso: Agente anticaries en productos odontológicos.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El fluoruro de sodio es un compuesto utilizado para prevenir la caries dental.
                Actúa favoreciendo la remineralización del esmalte y aumentando su resistencia
                frente a los ácidos.

                El ion fluoruro interactúa con el calcio del esmalte dental formando compuestos
                más resistentes a la desmineralización.
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Alta solubilidad en agua
                - Fuente de ion fluoruro (F⁻)
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Pastas dentales
                - Enjuagues bucales
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Sensible a reacciones con calcio
                - Puede perder eficacia si precipita
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Formación de precipitados
                - Pérdida de disponibilidad del ion fluoruro
                """)
            st.info("💡 Dato clave: La eficacia depende de que el fluoruro permanezca libre en solución.")
            st.caption("Referencia: Allen, 2016, p. 35, 104. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Fluoruro de Sodio":
            st.subheader("🧮 Interacciones del Fluoruro de Sodio")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🔴 Calcio (sales de calcio)")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Precipitación química

                **Qué ocurre:**
                El fluoruro reacciona con calcio formando **fluoruro de calcio (CaF₂)**,
                un compuesto insoluble.

                **Impacto farmacéutico:**
                - Disminución de fluoruro disponible
                - Pérdida de eficacia anticaries
                - Inactivación del principio activo

                **Acción recomendada:**
                - Evitar combinar con sales de calcio en la formulación
                - Usar abrasivos compatibles (ej. sílica en pastas dentales)
                """)
            st.markdown("#### 🟠 Magnesio y aluminio")
            st.warning("Incompatibilidad moderada")
            st.write("""
                **Tipo de interacción:** Formación de compuestos poco solubles

                **Qué ocurre:**
                Puede reaccionar con cationes metálicos formando compuestos menos solubles.

                **Impacto farmacéutico:**
                - Reducción de biodisponibilidad
                - Menor eficacia del producto

                **Acción recomendada:**
                - Evaluar compatibilidad con otros minerales
                """)
            st.markdown("#### 🟠 pH ácido")
            st.warning("Factor de riesgo")
            st.write("""
                **Tipo de interacción:** Cambio químico del ion fluoruro

                **Qué ocurre:**
                En medios muy ácidos, el fluoruro puede formar ácido fluorhídrico (HF).

                **Impacto farmacéutico:**
                - Pérdida de ion activo
                - Posible irritación

                **Acción recomendada:**
                - Mantener pH controlado
                """)
            st.markdown("#### 🟢 Compatibilidad general")
            st.success("Compatible en condiciones controladas")
            st.write("""
                **Tipo de interacción:** Compatibilidad fisicoquímica

                **Qué ocurre:**
                Es estable en soluciones acuosas si no hay cationes reactivos.

                **Importancia en formulación:**
                - Uso seguro en productos dentales
                - Alta eficacia si se mantiene soluble

                **Acción recomendada:**
                - Seleccionar excipientes compatibles
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                El principal riesgo del fluoruro de sodio es la precipitación con calcio,
                lo que elimina su eficacia. La selección de excipientes es crítica en su formulación.
                """)
            st.caption("Referencia: Allen, 2016, p. 35, 104. Basado en el archivo del proyecto.")
    with tab_propiedades:
        if activo == "Fluoruro de Sodio":
            st.subheader("🧪 Propiedades Fisicoquímicas del Fluoruro de Sodio")
            col1, col2, col3 = st.columns(3)
            col1.metric("Estado físico", "Sólido cristalino")
            col2.metric("Solubilidad", "Alta en agua")
            col3.metric("Ion activo", "F⁻")
            st.markdown("### 💧 Solubilidad")
            st.write("""
                - Alta solubilidad en agua
                """)
            st.markdown("### 🌡️ Propiedades físicas")
            st.write("""
                - Sólido blanco
                """)
            st.markdown("### ⚠️ Estabilidad")
            st.warning("""
                - Estable en condiciones normales
                - Puede reaccionar con cationes metálicos
                """)
            st.markdown("### ⚗️ Comportamiento en formulación")
            st.write("""
                - Se disuelve fácilmente
                - Puede precipitar con calcio
                """)
            st.markdown("### 🧠 Compatibilidad fisicoquímica")
            st.write("""
                - Compatible con sistemas acuosos
                - Incompatible con calcio
                """)
            st.success("💡 Dato clave: La disponibilidad del ion fluoruro define la eficacia del producto.")
            st.caption("Referencia: Allen, 2016, p. 35. Complementado para fines didácticos.")
    with tab_reacciones_adversas:
            if activo == "Fluoruro de Sodio":
                st.subheader("🍴 Interacciones con alimentos")
                st.write("""
                    - El consumo simultáneo de FLUORURO DE SODIO y PRODUCTOS LÁCTEOS puede provocar una disminución de la concentración máxima.
                    """)
                st.caption("Referencia: Micromedex.")
        



    with tab_fundamento:
        if activo == "Ácido Bórico y Borato de Sodio":
            st.subheader("📋 Ficha Técnica: Ácido Bórico y Borato de Sodio")
            st.info("Uso: Antisépticos suaves y sistemas tampón.")
            st.markdown("### 🔬 Fundamento científico")
            st.write("""
                El ácido bórico es un ácido débil, mientras que el borato de sodio (bórax)
                es su base conjugada. Juntos pueden formar un sistema tampón que ayuda a
                mantener el pH relativamente estable.

                Este sistema se utiliza en formulaciones oftálmicas y dermatológicas
                donde es importante controlar el pH.

                (Complemento didáctico)
                """)
            st.markdown("### ⚗️ Propiedades relevantes")
            st.write("""
                - Ácido bórico: ácido débil
                - Borato de sodio: base débil
                """)
            st.markdown("### 🧪 Aplicación farmacéutica")
            st.write("""
                - Soluciones oftálmicas
                - Antisépticos suaves
                - Sistemas buffer
                """)
            st.markdown("### ⚠️ Consideraciones en formulación")
            st.warning("""
                - Sensibles al pH
                - Requieren balance ácido-base
                """)
            st.markdown("### ⚠️ Problemas comunes en laboratorio")
            st.warning("""
                - Desbalance del sistema tampón
                - Cambios de pH no deseados
                """)
            st.info("💡 Dato clave: La relación ácido/base define el pH del sistema.")
            st.caption("Referencia: Allen, 2016, p. 36, 35. Complementado para fines didácticos.")
    with tab_interraciones:
        if activo == "Ácido Bórico y Borato de Sodio":
            st.subheader("🧮 Interacciones de Ácido Bórico y Borato de Sodio")
            st.markdown("### ⚗️ Evaluación de interacciones relevantes")
            st.markdown("#### 🟢 Sistema tampón (ácido-base)")
            st.success("Interacción funcional")
            st.write("""
                **Tipo de interacción:** Equilibrio ácido-base

                **Qué ocurre:**
                El ácido bórico y el borato de sodio forman un sistema tampón capaz de resistir cambios de pH.

                **Impacto farmacéutico:**
                - Estabilidad del pH
                - Mejora de estabilidad de la formulación
                - Protección de principios activos sensibles

                **Acción recomendada:**
                - Ajustar proporción ácido/base según pH deseado
                """)
            st.markdown("#### 🔴 Ácidos fuertes")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido-base

                **Qué ocurre:**
                Los ácidos fuertes pueden desplazar el equilibrio del sistema,
                eliminando la capacidad tampón.

                **Impacto farmacéutico:**
                - Pérdida de control del pH
                - Inestabilidad del producto

                **Acción recomendada:**
                - Evitar incorporación de ácidos fuertes
                """)
            st.markdown("#### 🔴 Bases fuertes")
            st.error("Incompatibilidad crítica")
            st.write("""
                **Tipo de interacción:** Reacción ácido-base

                **Qué ocurre:**
                Las bases fuertes pueden neutralizar el ácido bórico completamente,
                rompiendo el sistema tampón.

                **Impacto farmacéutico:**
                - Cambio brusco de pH
                - Pérdida de estabilidad

                **Acción recomendada:**
                - Evitar bases fuertes en la formulación
                """)
            st.markdown("#### 🟠 Metales")
            st.warning("Factor de riesgo")
            st.write("""
                **Tipo de interacción:** Formación de complejos

                **Qué ocurre:**
                Pueden formarse complejos con ciertos metales, alterando el equilibrio químico.

                **Impacto farmacéutico:**
                - Posible inestabilidad
                - Alteración del sistema tampón

                **Acción recomendada:**
                - Evitar contaminación metálica
                """)
            st.markdown("### 🧠 Conclusión farmacéutica")
            st.info("""
                Este sistema es útil para mantener el pH, pero es altamente dependiente
                del equilibrio ácido-base. Cualquier alteración puede comprometer la estabilidad
                de la formulación.
                """)
            st.caption("Referencia: Allen, 2016, p. 36, 35. Basado en el archivo del proyecto.")
    with tab_reacciones_adversas:
            if activo == "Ácido Bórico y Borato de Sodio":
                st.subheader("No hay informacion con los principios activos disponibles")

else:
    st.info("Selecciona un grupo y un principio activo para desplegar la información técnica.")