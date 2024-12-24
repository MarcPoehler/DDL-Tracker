import streamlit as st

st.title("DDL Gametracker")

# Spieler-Auswahl
st.write("Willkommen zum DDL Gametracker - wer spielt?")
player_one = st.selectbox("Spieler 1", ("Sven", "Takeshi", "Markus", "Marc"))
player_two = st.selectbox("Spieler 2", ("Sven", "Takeshi", "Markus", "Marc"))
game_mode = st.radio("301 oder 501?", [301, 501])

if "player_one" not in st.session_state:
    st.session_state["player_one"] = player_one
if "player_two" not in st.session_state:
    st.session_state["player_two"] = player_two
if "players_info" not in st.session_state:
    st.session_state["players_infos"] = [
        {'player_name': player_one, 'points_left': game_mode, 'last_throw': []}, 
        {'player_name': player_two, 'points_left': game_mode, 'last_throw': []}
    ]


if player_one and player_two and game_mode:
    st.write(f"Es spielt {player_one} gegen {player_two}. Gamemode: {game_mode}. Viel Erfolg!")