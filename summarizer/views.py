import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def chunk_text(text, max_words=500):
    """
    Splits text into smaller chunks for processing.
    """
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i + max_words])

@csrf_exempt
def summarize_text(request):
    if request.method == "POST":
        data = json.loads(request.body)
        input_text = data.get("text", "")

        if not input_text:
            return JsonResponse({"error": "No text provided"}, status=400)

        api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        input_length = len(input_text.split())
        # Dynamically calculate max_length and min_length
        max_length = min(150, max(50, input_length // 4))
        min_length = max(30, input_length // 10)

        # Process text in chunks
        summaries = []
        for chunk in chunk_text(input_text):
            payload = {
                "inputs": chunk,
                "parameters": {
                    "max_length": max_length,
                    "min_length": min_length,
                    "length_penalty": 2.0,
                    "num_beams": 4
                }
            }
            response = requests.post(api_url, headers=headers, json=payload)

            if response.status_code == 200:
                summary = response.json()[0].get("summary_text", "")
                summaries.append(summary)
            else:
                return JsonResponse({"error": "Failed to summarize text"}, status=response.status_code)

        # Combine summaries
        final_summary = " ".join(summaries)
        return JsonResponse({"summary": final_summary})
