import unittest
import identidock


class MyTestCase(unittest.TestCase):
    def setUp(self):
        identidock.app.config["TESTING"] = True
        self.app = identidock.app.test_client()

    def test_get_main_page(self):
        page = self.app.post("/", data=dict(name="Moby Dick"))
        assert page.status_code == 200
        assert 'Hello' in str(page.data)
        assert 'Moby Dick' in str(page.data)

    def test_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>test</b><!--"'))
        assert '<b>'not in str(page.data)


if __name__ == '__main__':
    unittest.main()
