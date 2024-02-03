import streamlit as st
import random

def determine_winner(user_input, computer_input):
    if computer_input == user_input:
        return "Draw"
    elif (user_input == "paper" and computer_input == "rock") or \
         (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "scissors" and computer_input == "paper"):
        return "You Won"
    else:
        return "You Lost"

def main():
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    st.title("Rock, Paper, Scissors Game")

    user_input = st.selectbox("Select your move:", options, help="Please select your move")

    if st.button("Play"):
        random_number = random.randint(0, 2)
        computer_input = options[random_number]

        result = determine_winner(user_input, computer_input)

        st.image(f"{user_input}.svg", width=100, caption=f"You selected {user_input}")
        st.image(f"{computer_input}.svg", width=100, caption=f"Computer selected {computer_input}")
        st.write(result)

        if result == "You Won":
            user_wins += 1
        elif result == "You Lost":
            computer_wins += 1

        st.write(f"You Wins: {user_wins}")
        st.write(f"Computer Wins: {computer_wins}")

if __name__ == "__main__":
    main()
