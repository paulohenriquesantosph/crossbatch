import math

import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮")
st.title("🧮 Calculadora")

OPERATIONS = {
    "Soma (+)": lambda a, b: a + b,
    "Subtração (−)": lambda a, b: a - b,
    "Multiplicação (×)": lambda a, b: a * b,
    "Divisão (÷)": lambda a, b: a / b,
    "Potência (^)": lambda a, b: a**b,
    "Resto (%)": lambda a, b: a % b,
    "Raiz n-ésima de A": lambda a, b: a ** (1 / b),
    "Logaritmo de A na base B": lambda a, b: math.log(a, b),
}

col1, col2 = st.columns(2)
a = col1.number_input("A", value=0.0, format="%.6g")
b = col2.number_input("B", value=0.0, format="%.6g")
op = st.selectbox("Operação", list(OPERATIONS))

if st.button("Calcular", type="primary"):
    try:
        result = OPERATIONS[op](a, b)
        if isinstance(result, complex):
            raise ValueError("resultado não é um número real")
        st.success(f"Resultado: **{result:,.10g}**")
        st.session_state.setdefault("history", []).insert(0, f"{a:g} {op} {b:g} = {result:,.10g}")
    except (ZeroDivisionError, ValueError, OverflowError) as e:
        st.error(f"Erro: {e}")

if st.session_state.get("history"):
    st.subheader("Histórico")
    for line in st.session_state["history"][:10]:
        st.text(line)
    if st.button("Limpar histórico"):
        st.session_state["history"] = []
        st.rerun()
