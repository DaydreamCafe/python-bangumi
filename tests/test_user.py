import unittest

from pybangumi.user import User, UserData


class UserTestCase(unittest.TestCase):
    def test_user(self):
        self.assertEqual(
            User('653154', 'WhitePaper/BangumiAPI (https://github.com/WhitePaper233/BangumiAPI)').fetch(),
            UserData(
                {
                    'id': 653154,
                    'url': 'http://bgm.tv/user/653154',
                    'username': '653154',
                    'nickname': 'WhitePaper233',
                    'avatar': {
                        'large': 'http://lain.bgm.tv/pic/user/l/000/65/31/653154.jpg?r=1639906848',
                        'medium': 'http://lain.bgm.tv/pic/user/m/000/65/31/653154.jpg?r=1639906848',
                        'small': 'http://lain.bgm.tv/pic/user/s/000/65/31/653154.jpg?r=1639906848'
                    },
                    'sign': '',
                    'usergroup': 10
                }
            )
        )


if __name__ == '__main__':
    unittest.main()
