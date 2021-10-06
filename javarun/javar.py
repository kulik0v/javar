from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Javar:
    java: str = 'java'
    class_path: str = ''
    class_path_items: List[str] = ()
    module_path: str = ''
    module_path_items: List[str] = ()

    sys_args: Dict = None
    sys_properties: Dict = None
    sys_options: List[str] = ()

    main_class: str = ''
    main_jar: str = ''
    # main_module: str = ''
    main_args: List[str] = ()

    def cmd_class_path(self) -> list:
        items = list(self.class_path_items)
        if self.class_path:
            items.append(self.class_path)
        if items:
            return ['-cp', ':'.join(items)]

        return []

    def cmd_module_path(self) -> list:
        items = list(self.module_path_items)
        if self.module_path:
            items.append(self.module_path)
        if items:
            return ['--module-path', ':'.join(items)]

        return []

    def cmd_sys_args(self) -> list:
        if self.sys_args:
            return ['-{}:{}'.format(*i) for i in self.sys_args.items()]

        return []

    def cmd_sys_properties(self) -> list:
        if self.sys_properties:
            return ['-D{}={}'.format(*i) for i in self.sys_properties.items()]

        return []

    def cmd_sys_options(self) -> list:
        if self.sys_options:
            return ['-{}'.format(i) for i in self.sys_options]

        return []

    # noinspection PyMethodMayBeStatic
    def cmd_extra_params(self):
        return []

    def cmd_main(self) -> list:
        if self.main_jar:
            return ['-jar', self.main_jar]
        else:
            return [self.main_class, ]

    def cmd_as_list(self) -> list:
        cmd = [self.java]
        cmd += self.cmd_class_path()
        cmd += self.cmd_module_path()
        cmd += self.cmd_sys_args()
        cmd += self.cmd_sys_properties()
        cmd += self.cmd_sys_options()
        cmd += self.cmd_extra_params()
        cmd += self.cmd_main()

        if self.main_args:
            cmd += self.main_args

        return cmd

    @property
    def cmd(self) -> str:
        return ' '.join(self.cmd_as_list())
