# Mini Voice AI Assistant
 AI Voice Assistant using LiveKit

## Getting started

Run the following command inside `Mini-Voice-AI-Assistant` to activate the virtual environment 

For Windows
```bash
cd Mini-Voice-AI-Assistant
.\venv\Scripts\activate
python3 -m pip install -r requirements.txt
python3 agent.py dev
```

or for Mac

```bash
cd Mini-Voice-AI-Assistant
source venv/Scripts/activate
python3 -m pip install -r requirements.txt
python3 agent.py dev
```

Run the following command inside `frontend` to activate the frontend environment

```bash
cd frontend
npm install
npm run dev
```

And open http://localhost:3000 in your browser.

## Usage

Upon entering the webpage. select `Start Chat`
Once selected, a voice should be heard saying "Hello, I am your personal assistant, how may I help you?"

> [!NOTE]
> If this is not the case, ensure that the virtual environment is properly running with `python3 agent.py dev` in `Mini-Voice-AI-Assistant` directory.

Ask the assistant a question! For example, `What is 5 + 5?` or `Where is San Francisco located?`.
User may verbally say the question or type the question through the chat provided. 

The Assistant will then respond back with the proper answer. 
