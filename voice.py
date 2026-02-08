import subprocess
import threading
import time
from utils import clean_text_for_speech

# Configuration
PREFERRED_VOICE = "Daniel"  # Default fallback
# Other good options on macOS: Samantha, Tesco, Karen, Rishi, Moira
# You can test them in terminal: say -v Daniel "Hello"

speaking = False
lock = threading.Lock()

def speak(text):
    """
    Speaks the text using the native macOS 'say' command.
    This is blocking and reliable.
    """
    global speaking
    
    # We use the lock to update the global state, ensuring thread safety if expanded later
    with lock:
        speaking = True
        
    try:
        # Clean text
        clean_text = clean_text_for_speech(text)
        if not clean_text:
            return

        # Split into sentences for better pacing, though 'say' handles long text well
        # We process sentence by sentence to allow for potential interruption logic later if needed
        # and to keep the feedback loop tight.
        sentences = clean_text.replace('\n', '. ').split('. ')
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            # Execute the native 'say' command
            # This BLOCKS until the sentence is finished
            subprocess.run(["say", "-v", PREFERRED_VOICE, sentence])
            
            # Small natural pause
            time.sleep(0.1)

    except Exception as e:
        print(f"Error in speech synthesis: {e}")
        
    finally:
        # Ensure state is reset
        with lock:
            speaking = False
        # Small buffer to let audio hardware release
        time.sleep(0.2)
