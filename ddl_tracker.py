import streamlit as st

st.title("DDL Gametracker")
st.write("Willkommen zum DDL Gametracker - wer spielt?")

# Spieler-Auswahl
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

# Session State für Multiplikator, Treffer und Wurf-Speicher initialisieren
if "multiplier" not in st.session_state:
    st.session_state["multiplier"] = 1
if "number_hits" not in st.session_state:
    st.session_state["number_hits"] = [0, 0, 0]  # Drei Treffer initialisieren
if "current_throw" not in st.session_state:
    st.session_state["current_throw"] = 0  # Aktueller Wurf (0, 1, 2)

with st.container():
    col1, col2 = st.columns(2)

    # Multiplikator-Buttons
    is_triple = col1.button("Triple", use_container_width=True)
    single_bull = col1.button("Single bull", use_container_width=True)
    is_double = col2.button("Double", use_container_width=True)
    bullseye = col2.button("Bullseye", use_container_width=True)

    if is_triple:
        st.session_state["multiplier"] = 3
    elif is_double:
        st.session_state["multiplier"] = 2
    elif single_bull:
        st.session_state["number_hits"][st.session_state["current_throw"]] = 25
    elif bullseye:
        st.session_state["number_hits"][st.session_state["current_throw"]] = 50

    # Nummern-Buttons
    left, middle_left, middle_right, right = st.columns(4)
    columns = [left, middle_left, middle_right, right]

    for i in range(1, 21):
        col_index = (i - 1) % len(columns)
        column = columns[col_index]

        if column.button(f"{i}", key=f"button_{i}", use_container_width=True):
            st.session_state["number_hits"][st.session_state["current_throw"]] = i

    # Nächster Wurf (maximal 3 Würfe)
    if st.session_state["current_throw"] < 2:
        if st.button("Nächster Wurf"):
            st.session_state["current_throw"] += 1
    else:
        st.write("Alle drei Würfe abgeschlossen!")

# Werte der Würfe berechnen
throws = st.session_state["number_hits"]
total_value = sum(throw * st.session_state["multiplier"] for throw in throws)

# Ausgabe
st.write("Treffer der drei Würfe:", throws)
st.write("Gesamtpunktzahl:", total_value)

points_left = st.session_state["players_infos"][0]['points_left'] - total_value
st.session_state["players_infos"][0]['points_left'] = points_left

st.write(f"Restpunkte: {points_left}")