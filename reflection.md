# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game setup looked fine when I first ran it, at first glance, nothing looked wrong. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were wrong, for instance, the target number was 83, and I typed in 50, and it otld me to go lower. And then when i typed in 40 ,it told me to go lower once more. Then on another try, the number was 53, I typed in 70 and it told me to go higher. 
When you click new game, it doesn't load a  new game. It still shows whether or not you've won or lost, and it shows the history of the past guesses you had. 
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |   When the guess  | The hints tell the     I don't know what type of error this is called.            
            below or higher   user to go in the 
            than the secret    wrong direction
            number,
            then the proper hints 
            will tell the user
            to go higher or 
            lower accordingly.
| | | | |
| | | | |  The secret number   It remains the same The error is a TypeError
           will remain the     but gets passed as 
           same through the    a string on even
           game                attempts, which 
                              leads to incorrect
                              guessing turns.       

          The game status     The game status      I don't know what type of error this is called
          refreshes when the  does not refresh
          user hits the       and the history of 
          button              attempts still 
                              shows 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used claude code as my teammate on this project.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
A suggestion that the AI gave me that was correct was
The AI suggested __ , the suggestion was correct,  I verfied this through
The AI suggested that the agme wouldn't refresh due to the game status not being updated. It was correct and I verified that through looking at the code, and then adding the AI's suggestions and retrying it through the streamlit app. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I don't think that I experienced a time where it was incorrect. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided that it would be fixed by running the app and testing out if it the outcome had changed or not. 
If the same problem had arised, then I would go back and change the code.
Then I would do the same process of goin back to the app and seeing if the expected outcome happens. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested out the backwards hints, I would purposefully put in a number that is higher or lower than the hint, and it would give the wrong hints. That told me that the logic for the code for the hints it flawed, and I thought it was probably a flawed if statement in the code. 

- Did AI help you design or understand any tests? How?
AI constructed the tests for me, I followed the instructions on the project list, and asked it to make me pytests for the recent fixes I did. Then I ran the tests, which I had trouble with running because for some reason it kept telling me it couldn't find my file. But it finally ran, and it came back with all my tests being passed. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would say that everytime something changes in the app (like if the user clicks a button) Streamlit will read the whole code pver again which re-executes and starts fresh every time. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I think I was good at prompting the AI so that way it was specific, yet short. I didn't want it to fill in any gaps, so I really made sure to be intentional with my prompts.

- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think I would go through it again with a more discerning lense, I feel like this time I just accepted what AI was telling me, and I didn't take the time to see if it was wrong or right. 
I thinki I need to learn to question it, because I trusted it too much, and relied on it too much. 
