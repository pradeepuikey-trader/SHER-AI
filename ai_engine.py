from gemini_ai import analyze_image

def analyze_chart(image):

    try:

        analysis = analyze_image(image)

        return {
            "success": True,
            "analysis": analysis
        }

    except Exception as e:

        return {
            "success": False,
            "analysis": str(e)
        }
