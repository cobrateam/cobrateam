import index
import unittest

class CobraTeamTestCase(unittest.TestCase):

    def setUp(self):
        self.app = index.app.test_client()

    def test_index(self):
        request = self.app.get('/')
        assert 'Projects' in request.data

    def test_should_minify_the_rendered_content_from_view_using_a_decorator(self):
        from decorators import minified_response

        @index.app.route("/bla-bla-bla")
        @minified_response
        def bla_bla_bla():
            return '<html>    <body>Hello world</body>    </html>'

        response = self.app.get('/bla-bla-bla')
        self.assertEqual('<html><body>Hello world</body></html>', response.data)

if __name__ == '__main__':
    unittest.main()
