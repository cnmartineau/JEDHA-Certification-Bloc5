# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# layout
st.set_page_config(layout = "wide")

st.markdown(""" 
<style>

    /* above the header */
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }

    /* central part */
    [data-testid="stAppViewContainer"] {
    background-color: white;
    }

    /* sidebar menu */
    [data-testid="stSidebarNav"] {
    background-color: #044389;
    }

    /* sidebar*/
    [data-testid="stSidebar"] {
    background-color: #044389;
    }

    /* Sidebar links*/
    .css-17lntkn {
    color:white;
    font-size: 20px;
    }
    .css-17lntkn:hover {
    color:#FF4B4B !important;
    font-size: 20px;
    }
    .css-pkbazv {
    color:white;
    font-size: 20px;
    }
    .css-pkbazv:hover {
    color:#FF4B4B !important;
    font-size: 20px;
    }
    
    /* Titles*/
    .css-10trblm {
    color:#044389;
    }

    /* Streamlit link*/
    .css-1vbd788 {
    color:#044389 !important;
    text-decoration-line:underline;
    }
    .css-1vbd788:hover {
    color:#FF4B4B !important;
    }

    /* Links*/
    a {
    color:#044389 !important;
    }
    a:hover {
    color:#FF4B4B !important;
    }

</style>       
""",unsafe_allow_html=True)

# load and cache data
@st.cache_data
def load_data1():
    data = pd.read_csv("cnm_bloc5_data_plot1.csv")
    return data
def load_data2():
    data = pd.read_csv("cnm_bloc5_data_plot2.csv")
    return data
def load_data3():
    data = pd.read_csv("cnm_bloc5_data_plot3.csv")
    return data
def load_data4():
    data = pd.read_csv("cnm_bloc5_data_plot4.csv")
    return data
def load_data5():
    data = pd.read_csv("cnm_bloc5_data_plot5.csv")
    return data
def load_data6():
    data = pd.read_csv("cnm_bloc5_data_plot6.csv")
    return data
def load_data7():
    data = pd.read_csv("cnm_bloc5_data_plot7.csv")
    return data
def load_data8():
    data = pd.read_csv("cnm_bloc5_data_plot8.csv")
    return data
def load_data9():
    data = pd.read_csv("cnm_bloc5_data_plot9.csv")
    return data
def load_data10():
    data = pd.read_csv("cnm_bloc5_data_plot10.csv")
    return data
def load_data11():
    data = pd.read_csv("cnm_bloc5_data_plot11.csv")
    return data
data_plot1 = load_data1()
data_plot2 = load_data2()
data_plot3 = load_data3()
data_plot4 = load_data4()
data_plot5 = load_data5()
data_plot6 = load_data6()
data_plot7 = load_data7()
data_plot8 = load_data8()
data_plot9 = load_data9()
data_plot10 = load_data10()
data_plot11 = load_data11()

# title
st.title("Getaround analysis")

# subtitle
st.write("<p style='font-size:20px;'>Impact of implementing a minimum delay between two \
    car rentals</p>",unsafe_allow_html=True)

# comment on dataset
st.markdown("Note: more than 90% of the provided data did not contain any information about \
    previous shares. The decision was made to keep this data for the current analysis, following the \
    assumption that these shares might correspond to episodic shares, new users of the service, \
    or possibly unsatisfied users who share their car only once (45% of the dataset). However, \
    the same kind of analysis would be perfectly transferable to a subset of the data.")
st.markdown("")
st.markdown("")

# question 1 - report results
st.subheader("Late check-outs and their impact on the next driver")
st.markdown("- 57.5% of the drivers return the car late (Figure 1).")
st.markdown("- More than 50.0% of the delays are below 60 minutes (Figure 2).")
st.markdown("- 12.4% of the users who follow a late check-out cancel their booking (Figure 3).")

# question 1 - plot figures
col1, col2, col3 = st.columns(3)
with col1:
    # plot figure 1
    fig1 = px.pie(
        data_plot1, 
        names = "checkout",
        color_discrete_sequence = px.colors.qualitative.Vivid,
        hole = 0.3)
    fig1.update_traces(
        textposition = 'inside', 
        textinfo = 'percent+label',
        textfont_size = 12,
        showlegend = False)
    fig1.update_layout(
            title_text = "Fig 1. Check-outs",
            title_x = 0.25,
            title_font_size = 18,
            height = 300)
    fig1.show()
    st.plotly_chart(fig1, use_container_width = True)
with col2:
    # plot figure 2
    fig2 = px.histogram(
        data_plot2, 
        x = "delay",
        histnorm = "probability",
        color_discrete_sequence = px.colors.qualitative.Vivid)
    fig2.update_traces(
        showlegend = False)
    fig2.update_layout(
            title_text = "Fig 2. Delays",
            title_x = 0.37,
            title_font_size = 18,
            xaxis_title = "Delay in minutes",
            xaxis = dict(tickmode = "linear", tick0 = 0, dtick = 500),
            yaxis_title = "Probability",
            height = 300)
    st.plotly_chart(fig2, use_container_width = True)
with col3:
    # plot figure 3
    fig3 = px.pie(
        data_plot3, 
        names = "state",
        color_discrete_sequence = px.colors.qualitative.Vivid[3:],
        hole = 0.3)
    fig3.update_traces(
        textposition = 'inside', 
        textinfo = 'percent+label',
        textfont_size = 12,
        rotation = 112,
        showlegend = False)
    fig3.update_layout(
            title_text = "Fig 3. Next drivers",
            title_x = 0.25,
            title_font_size = 18,
            height = 300)
    fig3.show()
    st.plotly_chart(fig3, use_container_width = True)

# question 2 - report results
st.markdown("")
st.subheader("New feature and its benefits for car drivers and car owners")
st.markdown("The new feature consists in applying a minimum delay betwen two car rentals.")
st.markdown("- 4.4% of the car drivers would benefit from the new feature (Figure 4).")
st.markdown("- 1.3% of the car owners would benefit from the new feature (Figure 5).")
st.markdown("- For car owners who would potentially benefit from the new feature, the current \
    median proportion of lost rentals due to delays in check-outs is of 14.3% (Figure 6).")

# question 2 - plot figures
col4, col5, col6 = st.columns(3)
with col4:
    # plot figure 4
    fig4 = px.pie(
        data_plot4, 
        names = "benefit",
        color_discrete_sequence = px.colors.qualitative.Vivid,
        hole = 0.3)
    fig4.update_traces(
        textinfo = 'percent+label',
        textfont_size = 12,
        rotation = 188,
        showlegend = False)
    fig4.update_layout(
            title_text = "Fig 4. Car drivers",
            title_x = 0.25,
            title_font_size = 18,
            height = 300)
    fig4.show()
    st.plotly_chart(fig4, use_container_width = True)
with col5:
    # plot figure 5
    fig5 = px.pie(
        data_plot5, 
        names = "benefit",
        color_discrete_sequence = px.colors.qualitative.Vivid,
        hole = 0.3)
    fig5.update_traces(
        textinfo = 'percent+label',
        textfont_size = 12,
        rotation = 182,
        showlegend = False)
    fig5.update_layout(
            title_text = "Fig 5. Car owners",
            title_x = 0.25,
            title_font_size = 18,
            height = 300)
    fig5.show()
    st.plotly_chart(fig5, use_container_width = True)
with col6:
    # plot figure 6
    fig6 = px.box(
        data_plot6, 
        y = "percent_canceled_delay",
        color_discrete_sequence = px.colors.qualitative.Vivid[1:])
    fig6.update_traces(
        showlegend = False)
    fig6.update_layout(
            title_text = "Fig 6. Car owners' benefit",
            title_x = 0.20,
            title_font_size = 18,
            xaxis_title = "Canceled rentals due to delay",
            yaxis_title = "Pecentage of rentals per owner",
            yaxis = dict(tickmode = "linear", tick0 = 0, dtick = 10),
            height = 300)
    st.plotly_chart(fig6, use_container_width = True)

# question 3 - report results
st.markdown("")
st.subheader("New feature scope and threshold - Global impact")
st.markdown("Global impact of the new feature on all rentals and all cancelations.")
st.markdown("- Only 3.3% of all cancelations are due to a delay of the previous driver (Figure 7).")
st.markdown("- Only 4.4% of all rentals are concerned by the new feature (consecutive rentals \
    with late check-out of the first driver) (Figure 8).")
st.markdown("- The new feature applied only on Connect cars would affect at most 1.5% of all \
    rentals (Figure 8).")
st.markdown("- The new feature would concern 1.7% of all cancelations if only applied to Connect \
    cars (Figure 9).")

# question 3 - plot figures
col7, col8, col9 = st.columns(3)
with col7:
    # plot figure 7
    fig7 = px.pie(
        data_plot7, 
        names = "cause",
        color_discrete_sequence = px.colors.qualitative.Vivid,
        hole = 0.3)
    fig7.update_traces(
        textinfo = 'percent+label',
        textfont_size = 12,
        rotation = 192,
        showlegend = False)
    fig7.update_layout(
            title_text = "Fig 7. Cancelations' cause",
            title_x = 0.15,
            title_font_size = 18,
            height = 300)
    fig7.show()
    st.plotly_chart(fig7, use_container_width = True)

with col8:    
    # plot figure 8
    fig8 = px.line(
        data_plot8, 
        x = "threshold",
        y = "percent_total",
        color = "type",
        markers = True,
        color_discrete_sequence = px.colors.qualitative.Vivid[3:])
    fig8.update_traces(
        showlegend = True)
    fig8.update_layout(
            title_text = "Fig 8. Rentals",
            title_x = 0.28,
            title_font_size = 18,
            xaxis_title = "Threshold in minutes",
            xaxis = dict(tickmode = "linear", tick0 = 0, dtick = 60),
            yaxis_title = "Pecentage of total rentals",
            legend = dict(
                title = "",
                yanchor = "top",
                y = 0.95,
                xanchor = "left",
                x = 0.50),
            height = 300)
    st.plotly_chart(fig8, use_container_width = True)
with col9:
    # plot figure 9
    fig9 = px.line(
        data_plot9, 
        x = "threshold",
        y = "percent_total",
        color = "type",
        markers = True,
        color_discrete_sequence = px.colors.qualitative.Vivid[3:])
    fig9.update_traces(
        showlegend = True)
    fig9.update_layout(
            title_text = "Fig 9. Cancelations",
            title_x = 0.28,
            title_font_size = 18,
            xaxis_title = "Threshold in minutes",
            xaxis = dict(tickmode = "linear", tick0 = 0, dtick = 60),
            yaxis_title = "Pecentage of total cancelations",
            legend = dict(
                title = "",
                yanchor = "top",
                y = 0.95,
                xanchor = "left",
                x = 0.50),
            height = 300)
    st.plotly_chart(fig9, use_container_width = True)

# question 4 - report results
st.markdown("")
st.subheader("New feature scope and threshold - Problem solving")
st.markdown("Problematic cases are defined as rentals with late check-outs for which the next \
    driver canceled its booking.")
st.markdown("Affected rentals are defined as rentals for which the time elapsed after the previous \
    rental is below the threshold.")
st.markdown("- A delay of 1 hour would solve more than 50% of problematic cases if applied to all\
    cars (Figure 10).")
st.markdown("- This result would drop to 25% of problematic cases if the delay is only applied \
    to Connect cars (Figure 10).")
st.markdown("- In both cases, the percentage of solved cases plateaus after a delay of 4 hours \
    and 30 minutes (about 90% of solved cases for all cars and 47% for Connect cars) (Figure 10).")
st.markdown("- For the most extreme case (delay of 4 hours and 30 minutes applied to all cars), \
    the percentage of rentals that would be affected by the new feature would peak at 4.5% \
    (Figure 11).")

# question 4 - plot figures
col10, col11, col12 = st.columns(3)
with col10:
    # plot figure 10
    fig10 = px.line(
        data_plot10, 
        x = "threshold",
        y = "percent_total",
        color = "type",
        markers = True,
        color_discrete_sequence = px.colors.qualitative.Vivid[3:])
    fig10.update_traces(
        showlegend = True)
    fig10.update_layout(
            title_text = "Fig 10. Solved cases",
            title_x = 0.30,
            title_font_size = 18,
            xaxis_title = "Threshold in minutes",
            xaxis = dict(tickmode = "linear", tick0 = 0, dtick = 60),
            yaxis_title = "Pecentage of problematic cases",
            yaxis = dict(tickmode = "linear", tick0 = 0, dtick = 25),
            legend = dict(
                title = "",
                yanchor = "top",
                y = 0.33,
                xanchor = "left",
                x = 0.50),
            height = 300)
    st.plotly_chart(fig10, use_container_width = True)
with col11:
    # plot figure 11
    fig11 = px.line(
        data_plot11, 
        x = "threshold",
        y = "percent_total",
        color = "type",
        markers = True,
        color_discrete_sequence = px.colors.qualitative.Vivid[3:])
    fig11.update_traces(
        showlegend = True)
    fig11.update_layout(
            title_text = "Fig 11. Affected rentals",
            title_x = 0.22,
            title_font_size = 18,
            xaxis_title = "Threshold in minutes",
            xaxis = dict(tickmode = "linear", tick0 = 0, dtick = 60),
            yaxis_title = "Pecentage of total rentals",
            yaxis = dict(tickmode = "linear", tick0 = 0, dtick = 1),
            legend = dict(
                title = "",
                yanchor = "top",
                y = 0.33,
                xanchor = "left",
                x = 0.50),
            height = 300)
    st.plotly_chart(fig11, use_container_width = True)
