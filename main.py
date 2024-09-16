import streamlit as st
from math import sqrt

import streamlit.components.v1 as components #necesario para Google Analytics

def calcular_op_z(orelleta_z, orelleta_x, orelleta_y, CdG_X, CdG_Y, Lonxitude_min_Eslinga):
    a = 1
    b = -2 * orelleta_z
    c = orelleta_z**2 + (CdG_X - orelleta_x)**2 + (CdG_Y - orelleta_y)**2 - Lonxitude_min_Eslinga**2
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        st.error("Discriminante negativo, non hay solución real.")
        return None
    
    z1 = (-b + sqrt(discriminant)) / (2 * a)
    z2 = (-b - sqrt(discriminant)) / (2 * a)

    return max(z1, z2)

def main():
################################################################################
################################################################################    
    #st.title("Cálculos de Orelletas")
    st.title("Cálculos Diego")

    st.header("Cálculo de lonxitudes de eslingas, cubrir os seguintes datos")

    # Inicialización de session_state para evitar errores
    orelletas = ['1', '2', '3', '4']
    for o in orelletas:
        if f'Orelleta {o} X' not in st.session_state:
            st.session_state[f'Orelleta {o} X'] = 0.0
        if f'Orelleta {o} Y' not in st.session_state:
            st.session_state[f'Orelleta {o} Y'] = 0.0
        if f'Orelleta {o} Z' not in st.session_state:
            st.session_state[f'Orelleta {o} Z'] = 0.0
    if 'CdG_X' not in st.session_state:
        st.session_state['CdG_X'] = 0.0
    if 'CdG_Y' not in st.session_state:
        st.session_state['CdG_Y'] = 0.0
    if 'CdG_Z' not in st.session_state:
        st.session_state['CdG_Z'] = 0.0

    # Entradas organizadas en formato tabla con expander
    for i in range(1, 5):
        with st.expander(f"Coordenadas Orelleta {i}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("X")
                globals()[f'Orelleta_{i}_X'] = col1.number_input("", key=f'Orelleta {i} X', value=0.0, format="%.2f", label_visibility="collapsed")
            with col2:
                st.write("Y")
                globals()[f'Orelleta_{i}_Y'] = col2.number_input("", key=f'Orelleta {i} Y', value=0.0, format="%.2f", label_visibility="collapsed")
            with col3:
                st.write("Z")
                globals()[f'Orelleta_{i}_Z'] = col3.number_input("", key=f'Orelleta {i} Z', value=0.0, format="%.2f", label_visibility="collapsed")

    with st.expander("Coordenadas Centro de Gravidade"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("X")
            CdG_X = col1.number_input("", key='CdG_X', value=st.session_state['CdG_X'], format="%.2f", label_visibility="collapsed")
        with col2:
            st.write("Y")
            CdG_Y = col2.number_input("", key='CdG_Y', value=st.session_state['CdG_Y'], format="%.2f", label_visibility="collapsed")
        with col3:
            st.write("Z")
            CdG_Z = col3.number_input("", key='CdG_Z', value=st.session_state['CdG_Z'], format="%.2f", label_visibility="collapsed")

    # Separación e campo de lonxitude mínima de eslinga
    st.write(" ")
    Lonxitude_min_Eslinga = st.number_input("Lonxitude mínima de eslinga", value=0.0, format="%.2f")

    if st.button("Calcular"):
        try:
            # Calcular OP_Z para cada Orelleta
            OP_1_Z = calcular_op_z(st.session_state['Orelleta 1 Z'], st.session_state['Orelleta 1 X'], st.session_state['Orelleta 1 Y'], CdG_X, CdG_Y, Lonxitude_min_Eslinga)
            OP_2_Z = calcular_op_z(st.session_state['Orelleta 2 Z'], st.session_state['Orelleta 2 X'], st.session_state['Orelleta 2 Y'], CdG_X, CdG_Y, Lonxitude_min_Eslinga)
            OP_3_Z = calcular_op_z(st.session_state['Orelleta 3 Z'], st.session_state['Orelleta 3 X'], st.session_state['Orelleta 3 Y'], CdG_X, CdG_Y, Lonxitude_min_Eslinga)
            OP_4_Z = calcular_op_z(st.session_state['Orelleta 4 Z'], st.session_state['Orelleta 4 X'], st.session_state['Orelleta 4 Y'], CdG_X, CdG_Y, Lonxitude_min_Eslinga)

            if None in [OP_1_Z, OP_2_Z, OP_3_Z, OP_4_Z]:
                st.error("Error en el cálculo de OP_Z. Revisa las entradas.")
                return

            OP_1_X, OP_1_Y = CdG_X, CdG_Y
            OP_2_X, OP_2_Y = CdG_X, CdG_Y
            OP_3_X, OP_3_Y = CdG_X, CdG_Y
            OP_4_X, OP_4_Y = CdG_X, CdG_Y

            # Calcular las longitudes para cada Orelleta con los puntos OP
            OL_1 = [
                sqrt((OP_1_X - st.session_state['Orelleta 1 X'])**2 + (OP_1_Y - st.session_state['Orelleta 1 Y'])**2 + (OP_1_Z - st.session_state['Orelleta 1 Z'])**2),
                sqrt((OP_2_X - st.session_state['Orelleta 1 X'])**2 + (OP_2_Y - st.session_state['Orelleta 1 Y'])**2 + (OP_2_Z - st.session_state['Orelleta 1 Z'])**2),
                sqrt((OP_3_X - st.session_state['Orelleta 1 X'])**2 + (OP_3_Y - st.session_state['Orelleta 1 Y'])**2 + (OP_3_Z - st.session_state['Orelleta 1 Z'])**2),
                sqrt((OP_4_X - st.session_state['Orelleta 1 X'])**2 + (OP_4_Y - st.session_state['Orelleta 1 Y'])**2 + (OP_4_Z - st.session_state['Orelleta 1 Z'])**2)
            ]

            OL_2 = [
                sqrt((OP_1_X - st.session_state['Orelleta 2 X'])**2 + (OP_1_Y - st.session_state['Orelleta 2 Y'])**2 + (OP_1_Z - st.session_state['Orelleta 2 Z'])**2),
                sqrt((OP_2_X - st.session_state['Orelleta 2 X'])**2 + (OP_2_Y - st.session_state['Orelleta 2 Y'])**2 + (OP_2_Z - st.session_state['Orelleta 2 Z'])**2),
                sqrt((OP_3_X - st.session_state['Orelleta 2 X'])**2 + (OP_3_Y - st.session_state['Orelleta 2 Y'])**2 + (OP_3_Z - st.session_state['Orelleta 2 Z'])**2),
                sqrt((OP_4_X - st.session_state['Orelleta 2 X'])**2 + (OP_4_Y - st.session_state['Orelleta 2 Y'])**2 + (OP_4_Z - st.session_state['Orelleta 2 Z'])**2)
            ]

            OL_3 = [
                sqrt((OP_1_X - st.session_state['Orelleta 3 X'])**2 + (OP_1_Y - st.session_state['Orelleta 3 Y'])**2 + (OP_1_Z - st.session_state['Orelleta 3 Z'])**2),
                sqrt((OP_2_X - st.session_state['Orelleta 3 X'])**2 + (OP_2_Y - st.session_state['Orelleta 3 Y'])**2 + (OP_2_Z - st.session_state['Orelleta 3 Z'])**2),
                sqrt((OP_3_X - st.session_state['Orelleta 3 X'])**2 + (OP_3_Y - st.session_state['Orelleta 3 Y'])**2 + (OP_3_Z - st.session_state['Orelleta 3 Z'])**2),
                sqrt((OP_4_X - st.session_state['Orelleta 3 X'])**2 + (OP_4_Y - st.session_state['Orelleta 3 Y'])**2 + (OP_4_Z - st.session_state['Orelleta 3 Z'])**2)
            ]

            OL_4 = [
                sqrt((OP_1_X - st.session_state['Orelleta 4 X'])**2 + (OP_1_Y - st.session_state['Orelleta 4 Y'])**2 + (OP_1_Z - st.session_state['Orelleta 4 Z'])**2),
                sqrt((OP_2_X - st.session_state['Orelleta 4 X'])**2 + (OP_2_Y - st.session_state['Orelleta 4 Y'])**2 + (OP_2_Z - st.session_state['Orelleta 4 Z'])**2),
                sqrt((OP_3_X - st.session_state['Orelleta 4 X'])**2 + (OP_3_Y - st.session_state['Orelleta 4 Y'])**2 + (OP_3_Z - st.session_state['Orelleta 4 Z'])**2),
                sqrt((OP_4_X - st.session_state['Orelleta 4 X'])**2 + (OP_4_Y - st.session_state['Orelleta 4 Y'])**2 + (OP_4_Z - st.session_state['Orelleta 4 Z'])**2)
            ]

            # Calcular o mínimo dos primeros elementos de cada lista
            min_01 = min(OL_1[0], OL_2[0], OL_3[0], OL_4[0])

            # Determinar coord_o basado no valor mínimo
            if min_01 == OL_1[0]:
                coord_o_X, coord_o_Y, coord_o_Z = OP_1_X, OP_1_Y, OP_1_Z
            elif min_01 == OL_2[0]:
                coord_o_X, coord_o_Y, coord_o_Z = OP_2_X, OP_2_Y, OP_2_Z
            elif min_01 == OL_3[0]:
                coord_o_X, coord_o_Y, coord_o_Z = OP_3_X, OP_3_Y, OP_3_Z
            else:
                coord_o_X, coord_o_Y, coord_o_Z = OP_4_X, OP_4_Y, OP_4_Z

            # Calcular lonxitudes
            Lonx_eslinga_orelleta_1 = sqrt((coord_o_X - st.session_state['Orelleta 1 X'])**2 + (coord_o_Y - st.session_state['Orelleta 1 Y'])**2 + (coord_o_Z - st.session_state['Orelleta 1 Z'])**2)
            Lonx_eslinga_orelleta_2 = sqrt((coord_o_X - st.session_state['Orelleta 2 X'])**2 + (coord_o_Y - st.session_state['Orelleta 2 Y'])**2 + (coord_o_Z - st.session_state['Orelleta 2 Z'])**2)
            Lonx_eslinga_orelleta_3 = sqrt((coord_o_X - st.session_state['Orelleta 3 X'])**2 + (coord_o_Y - st.session_state['Orelleta 3 Y'])**2 + (coord_o_Z - st.session_state['Orelleta 3 Z'])**2)
            Lonx_eslinga_orelleta_4 = sqrt((coord_o_X - st.session_state['Orelleta 4 X'])**2 + (coord_o_Y - st.session_state['Orelleta 4 Y'])**2 + (coord_o_Z - st.session_state['Orelleta 4 Z'])**2)

            # Mostrar resultados de distancias con etiquetas en negrita se cumplen a condición
            for i, lonx_eslinga in enumerate([Lonx_eslinga_orelleta_1, Lonx_eslinga_orelleta_2, Lonx_eslinga_orelleta_3, Lonx_eslinga_orelleta_4], start=1):
                if round(lonx_eslinga, 2) == round(Lonxitude_min_Eslinga, 2):
                    #st.success(f"**Lonx_eslinga_orelleta_{i}:** **{lonx_eslinga:.2f}**")
                    st.success(f"**Lonxitude eslinga orelleta {i}:** **{lonx_eslinga:.2f}**")
                else:
                    #st.success(f"Lonx_eslinga_orelleta_{i}: {lonx_eslinga:.2f}")
                    st.success(f"Lonxitude eslinga orelleta {i}: {lonx_eslinga:.2f}")

            #st.success(f"Coordenadas de coord_o: X={coord_o_X:.2f}, Y={coord_o_Y:.2f}, Z={coord_o_Z:.2f}")
            st.success(f"Coordenadas gancho (unión eslingas): X={coord_o_X:.2f}, Y={coord_o_Y:.2f}, Z={coord_o_Z:.2f}")

        except Exception as e:
            st.error(f"Ocorreu un erro: {e}")

if __name__ == "__main__":
    main()
