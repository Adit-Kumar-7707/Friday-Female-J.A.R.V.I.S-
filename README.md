# Friday AI Assistant

Friday AI Assistant is a Python-based virtual assistant that uses various libraries to perform tasks such as providing the current time, greeting the user, performing web searches, typing predefined texts, and executing specific commands based on voice input.

## Features

- **Current Date and Time:** Displays the current date and time in a user-friendly format.
- **Speech Output:** Converts text to speech using two different methods (`pyttsx3` and `gTTS`).
- **Greeting:** Greets the user based on the current time of day.
- **Automated Typing:** Types predefined text with a delay between each keystroke.
- **Mode Activation:** Opens VS Code using keyboard shortcuts.
- **MS Rewards Automation:** Automates typing random phrases in a browser to earn Microsoft Rewards points.
- **Web Search:** Searches Wikipedia for a given query and reads the summary.
- **Command Execution:** Opens specified websites or applications based on voice commands.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/friday-ai-assistant.git
    cd friday-ai-assistant
    ```

2. Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

    Ensure the following libraries are installed:
    - `pyttsx3`
    - `pyautogui`
    - `wikipedia`
    - `googlesearch-python`
    - `webbrowser`
    - `openai`
    - `gtts`
    - `pygame`
    - `speechrecognition`

## Usage

1. Run the script:
    ```sh
    python friday.py
    ```

2. The assistant will greet you and initialize.

3. Speak the word "Friday" to activate the assistant.

4. After activation, you can give commands such as:
    - "Open Google"
    - "Open YouTube"
    - "Open Typer"
    - "Open GitHub"
    - "Spotify"
    - "VS Code"
    - "GitHub Desktop"
    - "MS Rewards"
    - Any query starting with "How", "Why", "Who", or "What"

5. The assistant will execute the command or perform a web search and read the summary.

## Functions

- **DTnow():** Displays the current date and time.
- **speak_old(ans):** Converts text to speech using `pyttsx3`.
- **speak(text):** Converts text to speech using `gTTS` and plays it using `pygame`.
- **greet():** Greets the user based on the current time of day.
- **Type(x):** Types a given string with a delay between keystrokes.
- **modeC():** Opens VS Code using keyboard shortcuts.
- **ms_rewards():** Automates typing random phrases in a browser to earn Microsoft Rewards points.
- **search(query):** Searches Wikipedia for a given query and reads the summary.
- **processC(c):** Executes specific commands based on the given string.

## Voice Commands

- **General Commands:** Opens specified websites or applications.
- **Search Queries:** Performs a web search and reads the summary.
- **Special Commands:** Activates specific modes or runs automated tasks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
