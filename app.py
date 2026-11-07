
import streamlit as st

st.set_page_config(
    page_title="Tic Tac Toe",
    page_icon="🎮",
    layout="centered"
)

# Custom design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10172a, #243b55);
}
h1, h2, h3, p, label {
    color: white !important;
}
.stButton button {
    height: 90px;
    font-size: 35px;
    font-weight: bold;
    border-radius: 15px;
    background-color: #ffffff;
    color: #172554;
    border: 2px solid #38bdf8;
}
.stButton button:hover {
    background-color: #bae6fd;
    color: #0f172a;
    border-color: #0ea5e9;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 TIC TAC TOE")
st.markdown("### ✨ Two Player Game")
st.write("Player X vs Player O")

# Initialize game
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "player" not in st.session_state:
    st.session_state.player = "X"

if "winner" not in st.session_state:
    st.session_state.winner = ""

if "draw" not in st.session_state:
    st.session_state.draw = False

# Winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Check winner
def check_winner():
    for a, b, c in winning_combinations:
        if (
            st.session_state.board[a]
            == st.session_state.board[b]
            == st.session_state.board[c]
            != ""
        ):
            return st.session_state.board[a]
    return ""

# Display current player
if st.session_state.winner:
    st.success(f"🏆 Player {st.session_state.winner} Wins!")
elif st.session_state.draw:
    st.warning("🤝 Match Draw!")
else:
    st.info(f"👉 Player {st.session_state.player}'s Turn")

# Game board
for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        index = row * 3 + col

        with cols[col]:
            if st.button(
                st.session_state.board[index] or " ",
                key=f"cell_{index}",
                use_container_width=True,
                disabled=(
                    st.session_state.board[index] != ""
                    or st.session_state.winner != ""
                    or st.session_state.draw
                )
            ):
                st.session_state.board[index] = st.session_state.player

                winner = check_winner()

                if winner:
                    st.session_state.winner = winner

                elif "" not in st.session_state.board:
                    st.session_state.draw = True

                else:
                    st.session_state.player = (
                        "O" if st.session_state.player == "X" else "X"
                    )

                st.rerun()

# Restart button
st.write("")

if st.button("🔄 RESTART GAME", use_container_width=True):
    st.session_state.board = [""] * 9
    st.session_state.player = "X"
    st.session_state.winner = ""
    st.session_state.draw = False
    st.rerun()

st.markdown("---")
st.caption("Made with ❤️ using Python and Streamlit")
