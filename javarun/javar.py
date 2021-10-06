from dataclasses import dataclass
from typing import List, Dict
from .utils import list_jars, load_options


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


if __name__ == '__main__':
    j = Javar(
        java='/bin/java8',
        class_path='some.jar:onemore.jar',
        class_path_items=['j.jar'],
        sys_args={'splash': 'image.png'},
        sys_properties={'sun.java2d.noddraw': 'true'},
        sys_options=['Xmx768m'],
        main_class='Main',
        main_args=['arg1', 'arg2']
    )
    print(j.cmd)


# /home/kaa/.i4j_jres/1.8.0_152-tzdata2019c_64/bin/java -cp /opt/Jts/ibgateway/981/jars/jxbrowser-linux64-7.10.jar:/opt/Jts/ibgateway/981/jars/jts4launch-981.jar:/opt/Jts/ibgateway/981/jars/log4j-api-2.12.0.jar:/opt/Jts/ibgateway/981/jars/twslaunch-install4j-1.10.jar:/opt/Jts/ibgateway/981/jars/log4j-core-2.12.0.jar:/opt/Jts/ibgateway/981/jars/total-2020.jar:/opt/Jts/ibgateway/981/jars/jxbrowser-swing-7.10.jar:/opt/Jts/ibgateway/981/jars/twslaunch-981.jar:/opt/Jts/ibgateway/981/jars/locales.jar:/opt/Jts/ibgateway/981/jars/jxbrowser-7.10.jar -splash:/opt/Jts/ibgateway/981/.install4j/s_1fmt56t.png -Xmx768m -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:ParallelGCThreads=20 -XX:ConcGCThreads=5 -XX:InitiatingHeapOccupancyPercent=70 -Dinstaller.uuid=255742fe-15c5-4692-bd56-c9f191049c90 -DvmOptionsPath=/home/kaa/Jts/ibgateway/981/ibgateway.vmoptions -Dsun.awt.nopixfmt=true -Dsun.java2d.noddraw=true -Dswing.boldMetal=false -Dsun.locale.formatasdefault=true ibgateway.GWClient
