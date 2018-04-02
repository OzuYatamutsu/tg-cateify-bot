from response_controller import generate_cate_response
from unittest import TestCase

class TestResponseController(TestCase):
    def setUp(self):
        pass

    def test_generate_cate_response_alphanumeric(self):
        query_text = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789"
        )

        expected = (
            "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
            "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
            "０１２３４５６７８９"
        )

        self.assertEqual(
            generate_cate_response(query_text), expected
        )

    def test_generate_cate_response_symbolic(self):
        query_text = "!@#$%^&*()-=\"';:[]{}\\~`,.<>/?"
        expected = "！＠＃＄％＾＆＊（）－＝＼＂＇；：［］｛｝＼＼～｀，．＜＞／？"

        self.assertEqual(
            generate_cate_response(query_text), expected
        )

    def tearDown(self):
        pass

