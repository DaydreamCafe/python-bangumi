import unittest

from pybangumi import get_url, User


class UtilsTestCase(unittest.TestCase):
    def test_get_url(self):
        user = User('653154', 'WhitePaper/BangumiAPI (https://github.com/WhitePaper233/BangumiAPI)')
        self.assertEqual(get_url(user), 'https://api.bgm.tv/user/653154')


if __name__ == '__main__':
    unittest.main()
