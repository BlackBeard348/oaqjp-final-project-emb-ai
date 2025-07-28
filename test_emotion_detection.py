from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # Test case for joy sentiment
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1["dominant_emotion"], 'joy')
        # Test case for anger sentiment
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1["dominant_emotion"], 'anger')
        # Test case for disgust sentiment
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1["dominant_emotion"], 'disgust')
        # Test case for sadness sentiment
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1["dominant_emotion"], 'sadness')
         # Test case for fear sentiment
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1["dominant_emotion"], 'fear')

unittest.main()