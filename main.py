import openai
import os
from dotenv import load_dotenv
from tkinter import *

# Load environment variables (make sure your API key is stored in a .env file)
load_dotenv()


# Load your API key from an environment variable
key= os.environ.get("OPENAI_API_KEY")
print(key)

client = openai.OpenAI(
    api_key=key
)

# Create a list to store all the messages for context
messages = [{"role": "system", "content": "You are a helpful assistant."}]

def botReply():
    # Get the user input from the questionField (the text entry box)
    question = questionField.get()

    if question.strip():  # Only send if the question is not empty
        # Display the user input in the textarea
        textarea.insert(END, "You: " + question + "\n")
        questionField.delete(0, END)  # Clear the input field after sending

        # Add user input to the messages context for the GPT model
        messages.append({"role": "user", "content": question})

        # Request GPT-4 for chat completion (correct API call)
        response = openai.responses.create(
            model="gpt-4",  # Correct model name
            instructions="do not be remotely nice, your goal is to give terrible relationship advisor. You don't understand social cues and you encourage bad advice.  ",
            input=messages
        )

        # Access the bot's reply from the response
        bot_reply=response.output_text

        # Insert the bot's reply into the textarea
        textarea.insert(END, "Bot: " + bot_reply + "\n\n")
        textarea.yview(END)  # Scroll to the bottom of the textarea

root = Tk()

root.geometry('500x570+100+30')  # Set window size and position
root.title('Relationship Chatbot')  # Title of the window
root.config(bg='deep pink')  # Background color

# Load images for logo and button (ensure these images exist in the directory)
logoPic = PhotoImage(file='pic.png')  
logoPicLabel = Label(root, image=logoPic, bg='deep pink')
logoPicLabel.pack(pady=5)

# Frame to center content
centerFrame = Frame(root)
centerFrame.pack(pady=10, fill=BOTH, expand=True)

# Add a scrollbar to the text area
scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

# Text area to display conversation
textarea = Text(centerFrame, font=('times new roman', 20, 'bold'), height=10, yscrollcommand=scrollbar.set)
textarea.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=textarea.yview)

# Entry widget for user input
questionField = Entry(root, font=('verdana', 20, 'bold'))
questionField.pack(pady=15, fill=X)

# Image for the button (ensure this image exists in the directory)
askPic = PhotoImage(file='ask.png')  # Make sure ask.png exists in the directory
askButton = Button(root, image=askPic, command=botReply)  # Button calls botReply function when clicked
askButton.pack()

# Run the Tkinter main loop
root.mainloop()
