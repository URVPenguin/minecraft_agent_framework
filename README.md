# Minecraft Agent Framework

[![codecov](https://codecov.io/github/URVPenguin/minecraft_agent_framework/graph/badge.svg?token=RSVFAKBZ0Q)](https://codecov.io/github/URVPenguin/minecraft_agent_framework)

## Getting Started

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine as shown below;

```bash
git clone https://github.com/URVPenguin/minecraft_agent_framework.git
```

## Dependencies

Before you begin playing with the source code, you might need to install dependencies just as shown below;
> [!TIP]
> I recommend to create a venv before installing project dependencies.

```bash
pip install -r requirements.txt
```

## Running Framework

To run this code, you need to make sure that your Minecraft server is running and that you are also logged into the game through a client like TLauncher. Finally, run this command from the root of the project:
```bash
foo@bar:/minecraft_agent_framework$  python src/main.py
```

## Documentation 

Generated with [sphinx](https://www.sphinx-doc.org/en/master/), you can find the html file in the **docs** folder of the project.

To view it, simple run index.html, that you can found in docs/html/index.html

You can build it from scratch running: 
> [!WARNING]
> First delete all .rst files in docs/, except index.rst.

> [!NOTE]
> If you have problem with de generation of docs, delete src/__init__.py temporally.

```bash
foo@bar:/minecraft_agent_framework$  sphinx-apidoc -o docs src/ 
foo@bar:/minecraft_agent_framework$  cd docs
foo@bar:/minecraft_agent_framework/docs$ make clean && make html 
```