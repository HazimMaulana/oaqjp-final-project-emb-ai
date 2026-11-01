"""Validate the five required emotion detection examples."""
import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check the dominant emotion returned by the live Watson model."""

    def assert_emotion(self, text, expected):
        """Check the result's structure and dominant emotion."""
        result = emotion_detector(text)
        print(text, result)
        self.assertEqual(result["dominant_emotion"], expected)
        self.assertEqual(set(result), {
            "anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"
        })

    def test_joy(self):
        """Detect joy in the required positive example."""
        self.assert_emotion("I am glad this happened", "joy")

    def test_anger(self):
        """Detect anger in the required angry example."""
        self.assert_emotion("I am really mad about this", "anger")

    def test_disgust(self):
        """Detect disgust in the required disgusted example."""
        self.assert_emotion("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        """Detect sadness in the required sad example."""
        self.assert_emotion("I am so sad about this", "sadness")

    def test_fear(self):
        """Detect fear in the required fearful example."""
        self.assert_emotion("I am really afraid that this will happen", "fear")


if __name__ == "__main__":
    unittest.main(verbosity=2)
