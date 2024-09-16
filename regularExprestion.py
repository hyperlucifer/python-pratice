# it is used to scearch the particular pattern from the given bigger pattern

import re
# visit =="regexr.com"
pattern=r"[A-Z]pen"
text='''
This project aims to develop an AI assistant with real-time object recognition, voice input, and
speaker output, utilizing Java for the backend (Spring Boot) and Angular for the frontend with
integration of Google Gemini API. The system integrates YOLOv8 for object recognition and Open AI
Whisper for voice input. The Java backend orchestrates the processing of video frames from a camera
for object recognition and audio data from a microphone for voice input. YOLOv8 is employed for
real-time object recognition, and Open AI Whisper is utilized for processing voice input. The 
results are then consolidated and presented to the user through the frontend.
The project emphasizes modularity, adaptability, and extensibility for future enhancements and
integration with emerging AI technologies. This abstract serves as an overview of the AI assistant,
offering a glimpse into its architecture, features, and integration with Google Gemini services.
'''
mat=re.search(pattern,text)# it will only return the first occurances
#print(mat)
matc=re.finditer(pattern,text)# it will find all the occurances
for ma in matc:
    print(ma)
# there are many more functions