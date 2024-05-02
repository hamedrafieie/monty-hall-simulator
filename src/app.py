import streamlit as st
from src.monty_hall import game_simulation
import time
st.title('Monty Hall game simulator')
st.image("/home/hamed/personal-projects/monty-hall-simulator/images/_c496d4ec-3181-41e0-ad62-c9d86a598431.jpeg", width=400)

number_of_games = st.number_input(
    "Enter number of games to simulate",
    min_value=1, max_value=100000,
    value=100
)

col1, col2 = st.columns(2)
col1.subheader('Win Percentage without Switching')
col2.subheader('Win Percentage with Switching')

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_no_switch = 0
wins_switch = 0

for i in range(number_of_games):
    switch_wins, keep_wins = game_simulation(1)
    wins_no_switch += keep_wins
    wins_switch += switch_wins

    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])

    time.sleep(0.01)