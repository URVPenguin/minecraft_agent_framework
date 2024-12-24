# Minecraft Agent Framework

[![codecov](https://codecov.io/github/URVPenguin/minecraft_agent_framework/graph/badge.svg?token=RSVFAKBZ0Q)](https://codecov.io/github/URVPenguin/minecraft_agent_framework)

## Documentation 

Generated with [sphinx](https://www.sphinx-doc.org/en/master/), you can find the html file in the **docs** folder of the project.

To view it, simple run index.html, that you can found in docs/html/index.html

You can build it from scratch running: 
> [!WARNING]
> First delete all .rst files in docs/, except index.rst.

> [!NOTE]
> If you have problem with de generation of docs, delete src/__init__.py temporally.

```console
foo@bar:/minecraft_agent_framework$  sphinx-apidoc -o docs src/ 
foo@bar:/minecraft_agent_framework$  cd docs
foo@bar:/minecraft_agent_framework/docs$ make clean && make html 
```