from gemini_ai import analyze_image

def analyze_chart(image):
    try:
        response = analyze_image(image)

        return {
            "success": True,
            "analysis": response
        }

    except Exception as e:
        return {
            "success": False,
            "analysis": str(e)
        }
