import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from neo4j import GraphDatabase
from PIL import Image
import plotly.graph_objects as go
st.set_page_config(layout="wide")

plt.style.use('seaborn')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Konekdi Database
drivers = GraphDatabase.driver(uri = "neo4j+s://d4f6a837.databases.neo4j.io", auth = ("neo4j","efnDAFw4yr2ODSk2cqfUBCD0BlsnAtxscFdVOVSx6Xc"))
session = drivers.session(database='neo4j')

#Query tarik data I
q1 = """
match (n:Sublead_CG1) return n.Rain as Rain, n.Holiday as Holiday, n.Customer_Problem as Customer_Problem, n.Slippery as Slippery, n.Produksi as Produksi
"""
result1 = session.run(q1)
data1 = result1.data()
result_cg1 = pd.DataFrame(data1)

#Query tarik data II
q2 = """
match (n:Sublead_CG2) return n.Wait_Operator_EXC as Wait_Operator_EXC, n.Shift_Change as Shift_Change, n.Internal_Problem as Internal_Problem, n.Wait_Hauler_or_Truck as Wait_Hauler_or_Truck, n.Meal_And_Rest as Meal_And_Rest, n.Produksi as Produksi
"""
result2 = session.run(q2)
data2 = result2.data()
result_cg2 = pd.DataFrame(data2)

#Query tarik data III
q3 = """
match (n:Sublead_CG3) return n.No_Material as No_Material, n.Produksi as Produksi
"""
result3 = session.run(q3)
data3 = result3.data()
result_cg3 = pd.DataFrame(data3)

#Query tarik data IV
q4 = """
match (n:Sublead_OB1) return n.Rain as Rain, n.Slippery as Slippery, n.Wait_Support as Wait_Support, n.Produksi as Produksi
"""
result4 = session.run(q4)
data4 = result4.data()
result_ob1 = pd.DataFrame(data4)

#Query tarik data I
q5 = """
match (n:Sublead_OB2) return n.Praying as Praying, n.Shift_Change as Shift_Change, n.Equipment_Travel as Equipment_Travel, n.Meal_And_Rest as Meal_And_Rest, n.Internal_Problem as Internal_Problem, n.Wait_Hauler_or_Truck as Wait_Hauler_or_Truck, n.Produksi as Produksi
"""
result5 = session.run(q5)
data5 = result5.data()
result_ob2 = pd.DataFrame(data5)

#Query tarik data I
q6 = """
match (n:Sublead_OB3) return n.Front_And_Disposal_Repair as Front_And_Disposal_Repair, n.Produksi as Produksi
"""
result6 = session.run(q6)
data6 = result6.data()
result_ob3 = pd.DataFrame(data6)

#Query tarik data Multiple CG
q7 = """
match (n:Multiple_CG) return n.date as date,	n.Bad_Visibility as Bad_Visibility,	n.Blasting as Blasting,	n.Customer_Problem as Customer_Problem,	n.Equipment_Travel as Equipment_Travel,	n.External_Issues as External_Issues, 
	n.Fasting as Fasting,	n.Friday_Praying as Friday_Praying,	n.Front_And_Disposal_Repair as Front_And_Disposal_Repair,	n.Hazard as Hazard,	n.Holiday as Holiday,	n.Internal_Problem as Internal_Problem, 
    	n.Meal_And_Rest as Meal_And_Rest,	n.No_Hauler_Or_Truck as No_Hauler_or_Truck,	n.No_Material as No_Material,	n.No_Operator_EXC as No_Operator_EXC, 	n.No_Work_Location as No_Work_Location, n.Praying as Praying, 
        	n.Rain as Rain,	n.Refueling as Refueling,	n.Relocation as Relocation,	n.Road_Repair as Road_Repair,	n.Safety as Safety,	n.Safety_Talk as Safety_Talk,	n.Shift_Change as Shift_Change,	n.Slippery as Slippery,	n.Wait_Hauler_Or_Truck as Wait_Hauler_or_Truck, 
            	n.Wait_Operator_EXC as Wait_Operator_EXC, n.Wait_Support as Wait_Support
                """

result7 = session.run(q7)
data7 = result7.data()
result_multi_cg = pd.DataFrame(data7)

#Query tarik data Multiple OB
q8 = """
match (n:Multiple_OB) return n.date as date,	n.Bad_Visibility as Bad_Visibility,	n.Blasting as Blasting,	n.Customer_Problem as Customer_Problem,	n.Equipment_Travel as Equipment_Travel,	n.External_Issues as External_Issues, 
	n.Fasting as Fasting,	n.Friday_Praying as Friday_Praying,	n.Front_And_Disposal_Repair as Front_And_Disposal_Repair,	n.Hazard as Hazard,	n.Holiday as Holiday,	n.Internal_Problem as Internal_Problem, 
    	n.Meal_And_Rest as Meal_And_Rest,	n.No_Hauler_Or_Truck as No_Hauler_Or_Truck,	n.No_Material as No_Material,	n.No_Operator_EXC as No_Operator_EXC, 	n.No_Work_Location as No_Work_Location, n.Praying as Praying, 
        	n.Rain as Rain,	n.Refueling as Refueling,	n.Relocation as Relocation,	n.Road_Repair as Road_Repair,	n.Safety as Safety,	n.Safety_Talk as Safety_Talk,	n.Shift_Change as Shift_Change,	n.Slippery as Slippery,	n.Wait_Hauler_Or_Truck as Wait_Hauler_Or_Truck, 
            	n.Wait_Operator_EXC as Wait_Operator_EXC, n.Wait_Support as Wait_Support
                """

result8 = session.run(q8)
data8 = result8.data()
result_multi_ob = pd.DataFrame(data8)

# st.write(df_ob)
image = Image.open('logo.png')
# containers = st.
st.image(image, width=200)

#Judul
st.title("Sistem Pendukung Keputusan untuk Menganalisis Penyebab Tidak Tercapainya Target Produksi Batu Bara")

# def st.sidebar.subheader('Pilih Kategori')
# sublead
sublead = st.selectbox(
    ' Pilih Kategori',
    ('Sublead Signifikan','Sublead Kurang Signifikan','Sublead Tidak Signifikan')
)
# st.markdown(
#     'Keterangan :\n')
# st.sidebar.title("Filter")
# options = st.sidebar.radio('Menu', options=['Home', 'Distribusi Data'])

# def home():
plt.style.use('seaborn')


def header1():
    st.header("Sublead Signifikan Mempengaruhi Turunnya Produksi Batu Bara")
def header2():
    st.header("Sublead Kurang Signifikan Mempengaruhi Turunnya Produksi Batu Bara")
def header3():
    st.header("Sublead Tidak Signifikan Mempengaruhi Turunnya Produksi")
# sublead = st.radio("Filter Kategori Sublead",('Sublead Signifikan','Sublead Kurang Signifikan','Sublead Tidak Signifikan'))
def indicator():
    left_col, right_col = st.columns(2)
    with left_col:
        st.subheader("Lag Indicator CG")
    with right_col:
        st.subheader("Lag Indicator OB")

#  =====================        
#Signifikan

if sublead == 'Sublead Signifikan' :
    
    #CG
    header1()
    indicator()
    
    fitur_cg1 = result_cg1.columns.values.tolist()
    fitur_cg1 = fitur_cg1[:4]
    count=1
    fig_cg = plt.figure(figsize=(10, 17))
    
    for fitur_cg in fitur_cg1:
        plt.subplot(5,1,count)
        sns.scatterplot(result_cg1[fitur_cg],result_cg1["Produksi"],cmap="Blues", alpha=0.6, edgecolor='red', linewidth=1)
        count+=1
    #OB
    fitur_ob1 = result_ob1.columns.values.tolist()
    fitur_ob1 = fitur_ob1[:3]
    count=1
    fig_ob = plt.figure(figsize=(10, 20))
    for fitur_ob in fitur_ob1:
        plt.subplot(6,1,count)
        sns.scatterplot(result_ob1[fitur_ob],result_ob1["Produksi"],cmap="Blues", alpha=0.6, edgecolor='red', linewidth=1)
        count+=1

    container1 = st.container()
    col1, col2 = st.columns(2)

    with container1:
        with col1:
            st.pyplot(fig_cg)
        with col2:
            st.pyplot(fig_ob)
    # Keterangan
    st.markdown(
    '\n Sublead Signifikan bermakna korelasi negatif tinggi dan sublead masuk kategori signifikan dalam mempengaruhi naik/turunnya produksi')
    
    # Timeseries Kejadian Sublead
    figg = go.Figure()
    for idx, fitur_cg in enumerate(fitur_cg1) :  
        figg.add_trace(
            go.Scatter(x=list(result_multi_cg['date']), y=list(result_multi_cg[fitur_cg]),
                    name=fitur_cg ))

    # Set title
    figg.update_layout(
        title_text="Detail Timeseries Kejadian Sublead Per Bulan - CG"
    )

    # Add range slider
    figg.update_layout(
        xaxis=dict(
            rangeselector=dict( 
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                ])
            ),
            rangeslider=dict(
                visible=True
            )
            # type="date"
        )
    )

    # with containers:
    st.plotly_chart(figg, use_container_width=True)
        
    # Create figure OB3
    figg = go.Figure()
    for idx, fitur_ob in enumerate(fitur_ob1) :  
        figg.add_trace(
            go.Scatter(x=list(result_multi_ob['date']), y=list(result_multi_ob[fitur_ob]),
                    name=fitur_ob ))

    # Set title
    figg.update_layout(
        title_text="Detail Timeseries Kejadian Sublead Per Bulan - OB"
    )

    # Add range slider
    figg.update_layout(
        xaxis=dict(
            rangeselector=dict( 
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                ])
            ),
            rangeslider=dict(
                visible=True
            )
            # type="date"
        )
    )

    st.plotly_chart(figg, use_container_width=True)

#  =====================        
# Sublead Kurang Signifikan

elif sublead == 'Sublead Kurang Signifikan':
    #Kurang Signifikan
    header2()
    indicator()
    #CG
    
    fitur_cg2 = result_cg2.columns.values.tolist()
    fitur_cg2 = fitur_cg2[:5]
    # list_fitur_cg2 = fitur_cg2
    count=1
    fig_cg2 = plt.figure(figsize=(10, 17))
    for fitur_cg in fitur_cg2:
        plt.subplot(5,1,count)
        sns.scatterplot(result_cg2[fitur_cg],result_cg2["Produksi"],cmap="Blues", alpha=0.6, edgecolor='blue', linewidth=1)
        count+=1        
    #OB
    fitur_ob2 = result_ob2.columns.values.tolist()
    fitur_ob2 = fitur_ob2[:6]
    count=1
    fig_ob2 = plt.figure(figsize=(10, 20))
    for fitur_ob in fitur_ob2:
        plt.subplot(6,1,count)
        sns.scatterplot(result_ob2[fitur_ob],result_ob2["Produksi"],cmap="Blues", alpha=0.6, edgecolor='blue', linewidth=1)
        count+=1

    container2 = st.container()
    col3, col4 = st.columns(2)

    with container2:
        with col3:
            st.pyplot(fig_cg2)
        with col4:
            st.pyplot(fig_ob2)
    
    # Keterangan
    st.markdown(
    '\n Sublead Kurang Signifikan bermakna korelasi positif tinggi dan sublead masuk kategori signifikan dalam mempengaruhi naik/turunnya produksi.'
    '\n   Dari kategori ini ditemukan keanehan bahwa tidak mungkin ada sublead yang berkorelasi positif (semakin lama terjadinya sublead, maka semakin tinggi nilai produksi)')
    # Create figure CG3
    # col1, col2 = st.columns(2)
    figg = go.Figure()
    for idx, fitur_cg in enumerate(fitur_cg2) :  
        figg.add_trace(
            go.Scatter(x=list(result_multi_cg['date']), y=list(result_multi_cg[fitur_cg]),
                    name=fitur_cg ))

    # Set title
    figg.update_layout(
        title_text="Sublead UA CG"
    )

    # Add range slider
    figg.update_layout(
        xaxis=dict(
            rangeselector=dict( 
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                ])
            ),
            rangeslider=dict(
                visible=True
            )
            # type="date"
        )
    )

    # with containers:
    # with col1:
    st.plotly_chart(figg, use_container_width=True)
        
    # Create figure OB3
    figg = go.Figure()
    for idx, fitur_ob in enumerate(fitur_ob2) :  
        figg.add_trace(
            go.Scatter(x=list(result_multi_ob['date']), y=list(result_multi_ob[fitur_ob]),
                    name=fitur_ob ))

    # Set title
    figg.update_layout(
        title_text="Sublead UA OB"
    )

    # Add range slider
    figg.update_layout(
        xaxis=dict(
            rangeselector=dict( 
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                ])
            ),
            rangeslider=dict(
                visible=True
            )
            # type="date"
        )
    )

    # with containers:
    # with col2:
    st.plotly_chart(figg, use_container_width=True)

#  =====================        
# Sublead Tidak Signifikan


elif sublead == 'Sublead Tidak Signifikan':
    #Tidak Signifikan
    header3()
    indicator()
    #CG
    
    fitur_cg3 = result_cg3.columns.values.tolist()
    fitur_cg3 = fitur_cg3[:1]
    count=1
    fig_cg3 = plt.figure(figsize=(10, 25))
    for fitur_cg in fitur_cg3:
        plt.subplot(10,1,count)
        sns.scatterplot(result_cg3[fitur_cg],result_cg3["Produksi"],cmap="Blues", alpha=0.6, edgecolor='green', linewidth=1)
        count+=1
    
    #OB
    fitur_ob3 = result_ob3.columns.values.tolist()
    fitur_ob3 = fitur_ob3[:1]
    count=1
    fig_ob3 = plt.figure(figsize=(10, 15))
    for fitur_ob in fitur_ob3:
        plt.subplot(6,1,count)
        sns.scatterplot(result_ob3[fitur_ob],result_ob3["Produksi"],cmap="Blues", alpha=0.6, edgecolor='green', linewidth=1)
        count+=1
    
    container3 = st.container()
    col5, col6 = st.columns(2)

    with container3:
        with col5:
            st.pyplot(fig_cg3)
        with col6:
            st.pyplot(fig_ob3)

    # Keterangan
    st.markdown(
    '\n Sublead Tidak Signifikan bermakna korelasi negatif rendah dan sublead masuk kategori tidak signifikan dalam mempengaruhi turunnya produksi')
    # Create figure CG3
    figg = go.Figure()
    for idx, fitur_cg in enumerate(fitur_cg3) :  
        figg.add_trace(
            go.Scatter(x=list(result_multi_cg['date']), y=list(result_multi_cg[fitur_cg]),
                    name=fitur_cg ))

    # Set title
    figg.update_layout(
        title_text="Sublead UA CG"
    )

    # Add range slider
    figg.update_layout(
        xaxis=dict(
            rangeselector=dict( 
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                ])
            ),
            rangeslider=dict(
                visible=True
            )
            # type="date"
        )
    )

    # with containers:
    st.plotly_chart(figg, use_container_width=True)
        
    # Create figure OB3
    figg = go.Figure()
    for idx, fitur_ob in enumerate(fitur_ob3) :  
        figg.add_trace(
            go.Scatter(x=list(result_multi_ob['date']), y=list(result_multi_ob[fitur_ob]),
                    name=fitur_ob ))

    # Set title
    figg.update_layout(
        title_text="Sublead UA OB"
    )

    # Add range slider
    figg.update_layout(
        xaxis=dict(
            rangeselector=dict( 
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                ])
            ),
            rangeslider=dict(
                visible=True
            )
            # type="date"
        )
    )

    # with containers:
    st.plotly_chart(figg, use_container_width=True)