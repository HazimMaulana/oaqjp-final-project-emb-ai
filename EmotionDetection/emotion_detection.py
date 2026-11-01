"""Analyze text with the Watson NLP emotion detection service."""
import json
import requests


def emotion_detector(text_to_analyze):
    """Return emotion scores, or None values when input cannot be analyzed."""
    emotions = ("anger", "disgust", "fear", "joy", "sadness")
    invalid_result = dict.fromkeys((*emotions, "dominant_emotion"))
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
    except requests.RequestException:
        return invalid_result
    if response.status_code == 400:
        return invalid_result
    if response.status_code != 200:
        return invalid_result
    try:
        formatted_response = json.loads(response.text)
        scores = formatted_response["emotionPredictions"][0]["emotion"]
        result = {emotion: scores[emotion] for emotion in emotions}
        result["dominant_emotion"] = max(result, key=result.get)
        return result
    except (ValueError, KeyError, IndexError, TypeError):
        return invalid_result
