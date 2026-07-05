from gemini_ai import analyze_image

def analyze_chart(image):
    try:
        return {"success":True,"analysis":analyze_image(image)}
    except Exception as e:
        return {"success":False,"analysis":str(e)}
