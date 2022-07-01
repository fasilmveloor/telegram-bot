from datetime import datetime

def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! Wh o goes you!!!"

    if user_message in ("who are you", "can you help me", "who are you"):
        return "I am a bot, how can i help you!!!"

    if user_message in ("time", "time?", "date?"):
        now = datetime.now()
        date_time = now.strtime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "Please type something the human mind can comprehend"