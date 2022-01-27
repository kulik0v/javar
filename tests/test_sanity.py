from unittest import TestCase

from javar import Javar


class TestJavaRun(TestCase):
    def test_cmd(self):
        jr = Javar(
            bin='/bin/java8',
            class_path='some.jar:onemore.jar',
            class_path_items=['j.jar'],
            sys_properties={
                'sun.java2d.noddraw': 'true'
            },
            sys_args=[
                '-Xmx768m'
            ],
            main_class='Main',
            main_args=['arg1', 'arg2']
        )
        cmd = jr.as_str()

        self.assertIn('java8', cmd)
        self.assertIn('j.jar:some.jar:onemore.jar', cmd)
        self.assertIn('-Xmx768m', cmd)

    def test_main_args_list(self):
        jr = Javar(
            main_class='Main',
            main_args=[
                'arg1',
                'arg2',
            ]
        )
        cmd = jr.as_str()
        self.assertIn('arg1', cmd)
        self.assertIn('arg2', cmd)

    def test_main_args_dict(self):
        jr = Javar(
            main_class='Main',
            main_args={
                '--host': 'localhost',
                '--port': '8080',
            },
        )
        cmd = jr.as_str()
        self.assertIn('--host=localhost', cmd)
        self.assertIn('--port=8080', cmd)
