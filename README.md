# Javar: Run java binary from python

Javar allows you to generate java cli with a set of options easily.

## Usage

### Simple

```python
from javar import Javar

javar = Javar(
    # binary to run
    bin='/bin/java',
    # list of single dash options 
    sys_args=['-version'],
)

# /bin/java -version
print(javar.as_str())

import subprocess

subprocess.run(javar.as_list())
```

### Provide class path as string or list

```python
from javar import Javar

javar = Javar(
    bin='/bin/java',
    # class_path: is a cassic way string parameter 
    class_path='/opt/jars/cool_0.1.0.jar:/opt/jars/best_1.0.0.jar',
    # class_path_items: you can also provide a list 
    class_path_items=[
        '/opt/jars/log4j.jar',
        '/opt/jars/locales.jar',
    ],
)
print(javar.as_str())
# You will get all of them joined
# /bin/java -cp /opt/jars/log4j.jar:/opt/jars/locales.jar:/opt/jars/cool_0.1.0.jar:/opt/jars/best_1.0.0.jar
```

### Generate classpath or options

```python
from javar import Javar, list_jars, load_options

javar = Javar(
    # Use list_jars to generate class path from directory.
    class_path_items=list_jars('/opt/jars'),
    # Use load_options to load vmoptions from file.
    sys_args=load_options('/opt/app/production.vmoptions'),
)
```

### With custom environment variables

```python
import os
import subprocess
from javar import Javar

javar = Javar()

java_env = os.environ.copy()
java_env['APP_INI'] = '/opt/app/config.ini'

subprocess.run(javar.as_list(), env=java_env)
```

## Installation

```bash
pip install javar
```

## All available options

```python
from javar import Javar

javar = Javar(
    # path to java binary
    bin='/bin/java',
    # class path string
    class_path='some.jar:onemore.jar',
    # class path list
    class_path_items=['one.jar', 'two.jar'],

    # system properties '-D<name>=<value>' format
    # examples:
    # -Dsun.java2d.noddraw=true will be {'sun.java2d.noddraw': 'true'}
    # -Dsun.java2d.uiScale=2 will be {'sun.java2d.uiScale': '2'}
    sys_properties={
        'sun.java2d.noddraw': 'true',
        'sun.java2d.uiScale': '2',
    },
    # rest of system args 
    sys_args=[
        '-Xmx768m',
        '-splash:image_path.png'
    ],

    # application class
    main_class='Main',
    # or jar
    main_jar='main.jar',
    # application args
    main_args=['arg1', 'arg2']
)
```

Args also can be a dictionary.

```python
from javar import Javar

javar = Javar(
    main_jar='main.jar',
    main_args={
        '--host': 'localhost',
        '--port': '8080',
    }
)
```
