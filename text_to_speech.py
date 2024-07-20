import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get the list of available voices
voices = engine.getProperty('voices')

# Print available voices to find a deeper one
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.id}")

# Choose a voice that sounds deeper
# This usually depends on the available voices in your system
# For example, we'll choose the second voice in the list (index 1), but you can choose any other
engine.setProperty('voice', voices[0].id)

# Set properties before adding anything to the speaking queue
engine.setProperty('rate', 150)    # Speed of speech
engine.setProperty('volume', 1)    # Volume level (0.0 to 1.0)

# Text you want to convert to speech
text = "Hello, this is a simple text-to-speech conversion using Python with a deeper voice."

# Pass the text to the engine
engine.say(text)

# Run the speech engine
engine.runAndWait()
