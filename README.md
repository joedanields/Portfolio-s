# Number Guessing Game with Streamlit

## Description
This project is a **Number Guessing Game** implemented using Python and Streamlit. The app provides two gameplay modes:

1. **User Guess Mode:** The user guesses a randomly chosen number by the machine.
2. **Machine Guess Mode:** The user thinks of a number, and the machine attempts to guess it.

## Features
- User-friendly interface with Streamlit.
- Interactive gameplay with real-time feedback.
- Separate tabs for two game modes.
- Tracks the number of attempts taken in both modes.

## How to Run the Project

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.7+
- Streamlit library

### Installation
1. Clone this repository or download the source code.
2. Navigate to the project directory:
   
3. Install required libraries:
   ```bash
   pip install streamlit
   ```

### Running the Application
1. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open the URL shown in your terminal (usually `http://localhost:8501`) in a web browser.
3. Play the game by selecting your desired mode!

## Game Modes

### 1. User Guess Mode
- The machine selects a random number between 1 and 50.
- The user guesses the number and receives feedback: **Higher**, **Lower**, or **Correct**.
- The game tracks the number of attempts taken to guess correctly.

### 2. Machine Guess Mode
- The user thinks of a number between 1 and 50.
- The machine tries to guess the number.
- The user provides guidance using **Higher**, **Lower**, or **Correct** buttons.
- The machine tries to guess the number in the minimum attempts.



## Technologies Used
- **Python**: Backend programming.
- **Streamlit**: Web framework for building the interactive app.
- **Random Module**: Used to generate random numbers.

## Customization
You can modify the code to:
- Change the range of numbers (default: 1 to 50).
- Add more game modes or enhance the UI using Streamlit widgets.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

## Author
- [Joe Daniel A](https://github.com/joedanields)

## Contributions
Contributions are welcome! Feel free to fork this project and submit pull requests for improvements.

## Feedback
If you have any feedback or questions, please contact [joedanielajd@gmail.com].
