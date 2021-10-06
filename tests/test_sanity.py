from unittest import TestCase

from javarun import Javar


class TestJavaRun(TestCase):
    def test_cmd(self):
        jr = Javar(
            java='/bin/java8',
            class_path='some.jar:onemore.jar',
            class_path_items=['j.jar'],
            sys_args={'splash': 'image.png'},
            sys_properties={'sun.java2d.noddraw': 'true'},
            sys_options=['Xmx768m'],
            main_class='Main',
            main_args=['arg1', 'arg2']
        )
        cmd = jr.cmd

        self.assertIn('-Xmx768m', cmd)


