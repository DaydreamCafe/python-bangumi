import unittest

from pybangumi import User, format_print, get_url


class UtilsTestCase(unittest.TestCase):
    def test_get_url(self):
        user = User(
            "653154",
            "WhitePaper/BangumiAPI (https://github.com/WhitePaper233/BangumiAPI)",
        )
        self.assertEqual(get_url(user), "https://api.bgm.tv/user/653154")

    @staticmethod
    def test_format_print():
        user = User(
            "653154",
            "WhitePaper/BangumiAPI (https://github.com/WhitePaper233/BangumiAPI)",
        )
        format_print(user.fetch())


if __name__ == "__main__":
    unittest.main()
