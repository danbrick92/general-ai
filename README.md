# General AI
<b>Author</b>: Dan Brickner </br>
<b>Project Description</b>: This project interfaces several state-of-the-art AI libraries and APIs together to perform interesting AI activities. </br>

<i>Note: this project is very much a work in progress.</i>

# Installation and Requirements
For now this has to be built from src code

## GCP
You will need a GCP Account, with a Service Account, and a credentials file.
You will also need the following APIs enabled:
- Speech to Text
- Text to Speech

## OpenAI
In order to use Chat, you will need an OpenAI account with a pay-as-you-go subscription. 
Once you have an API Key, you can reference it in the code. 

## Manual
The following installs must be performed on your Operating System:
- ffmpeg
    - Windows: choco install ffmpeg
    - Linux Debian/Ubuntu: sudo apt-get install ffmpeg
    - Linux CentOs: sudo yum install ffmpeg
    - MacOS: brew install ffmpeg
- python 3.11+

Additionally, make sure to install the requirements with:
<code>pip install -r requirements.txt </code>

# Configuration
There is not a config file yet, but I will provide one later.

# Running it
Run this project by going to the src folder and running: <code>python main.py </code>

# Design
### Current Design
The current design is focused on Chat. In the future, I plan to add Vision modules and much more.

The project is broken down into three pieces:
- Sensors - things used to "read" information from the environment
  - Human Examples: Vision, Hearing, Smelling, Tasting, Feeling
  - AI Examples: Listening (Speech to Text), Camera, Radar, LiDAR, etc...
- Actuators - things used to "write" information to the environment
  - Human Examples: Muscle Movement, Eye Movement, Speech...
  - AI Examples: Audio Output, Display, etc...
- Tasks - activities that utilize Sensors, Actuators, and the Processing of these
  - IE: Conversation - requires (typically) Hearing and Vision, Language Understanding, Language Processing, and Speaking

Each of these are abstract classes that are concretely implemented with real technology, but can be swapped out.
Why? For example, for the Text to Speech actuator, you can swap Google's TTS with PyTTSX3, which is more robotic but also not require network connectivity.

### For Raspberry Pi
For conversation, to start, I have used a Raspberry PI.
Please refer to PI_README.md for more, including schematics and software installation.

# Limitations
- There is no config file yet
- There is very little error handling at this point in time
- No unit tests at this time
- Currently, this is focused on Chat (including Text To Speech, Speech to Text)
