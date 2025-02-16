from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        e1 = emotion_detector("I am glad this happened")
        self.assertEqual(e1['dominant_emotion'], 'joy')
        e2 = emotion_detector("I am really mad about this")
        self.assertEqual(e2['dominant_emotion'], 'anger')
        e3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(e3['dominant_emotion'], 'disgust')
        e4 = emotion_detector("I am so sad about this")
        self.assertEqual(e4['dominant_emotion'], 'sadness')
        e5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(e5['dominant_emotion'], 'fear')
        
if __name__ == "__main__":
    unittest.main()