# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This is a guessing game so the purpose is for the user to guess the hidden number and enter it into the app. Based on how the hints provided by the game, the user will either increase the number, or decrease it to reach the right value of the number. You get a limited number of tries (7), if you guess the number under the amount of tries then you win, but points will be deducted with every try. 

- [ ] Detail which bugs you found.
1. The hints were wrong, and it would tell you to guess a higher number when you really should've guess a lower number. 2. The game wouldn't refresh when the button was clicked on, so you just had the same amount of attempts. 
- [ ] Explain what fixes you applied.
The game wasn't resetting so the Ai suggested to rest the who hamebord. The status is changed to playing so that way when streamlit rereads the script, it doesn't stop at playing and will actually refresh. For the hints, the hints were backwards, so it was a simple fix of changing the if statements. The secret also turned into a string on even attempts, even though our guesses re ints. Int>Str can result in TypeError, so the AI fixed this through changing how the checkguess recivevd the number. It made to that check_guess will always receive an int. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User will enter a number of 60
2. The agme will return "Too high! Go lower."
3.The user enters a guess of 52.
4. The score updates after a guess, 
5. The previous guess will be listed in the attempts history
6. The game ends after the correct guess or after the user has used all of the attempts. 

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
caitlynbennett@Estelles-MacBook-Pro a110module2 % PYTHONPATH=. pytest tests/test_game_logic.py
======================================= test session starts =======================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/caitlynbennett/ai_engineering1101/module2/a110module2
plugins: anyio-4.7.0
collected 4 items                                                                                 

tests/test_game_logic.py ....                                                               [100%]

======================================== 4 passed in 0.02s ========================================
caitlynbennett@Estelles-MacBook-Pro a110module2 % 
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
