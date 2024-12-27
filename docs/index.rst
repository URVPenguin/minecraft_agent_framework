.. Minecraft Agent Framework documentation master file, created by
   sphinx-quickstart on Wed Dec 18 17:46:22 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Minecraft Agent Framework documentation
=======================================

This is the main index of the documentation for **Minecraft Agent Framework**. Here you will find an overview of the project, its structure, modules, classes, and other important details.

===============
Getting Started
===============

Project Setup
-------------
At the command line:

.. code-block:: bash

    git clone https://github.com/URVPenguin/minecraft_agent_framework.git
    cd minecraft_agent_framework
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt


Running Framework
-----------------

At the command line:

.. code-block:: bash

   python3 src/main.py

Framework Usage
---------------

1. Create your module
*********************
First create a package inside src/ and create your bot file.

.. code-block:: bash

   mkdir agents && cd agents
   touch __init__.py
   touch your_bot.py

2. Configure
************
Configure src/config.yml, with the path of your bot module.

.. code-block:: yaml

   agents:
     insult_bot: "agents.insult_bot"
     tnt_bot: "agents.tnt_bot"
     chat_bot: "agents.chat_bot"

3. Create your first bot
************************
3.1 Basic Structure
~~~~~~~~~~~~~~~~~~~
All your bots need to have a function called ``def create_agent()`` . This function will return ``Agent`` instance.
This example will create Agent without any behavior.

.. code-block:: python

   def create_agent():
    return Agent("HelloBot")

3.2 Adding Action
~~~~~~~~~~~~~~~~~
Your bot needs to execute some logic, so you can create an ``ActionPoo`` class that implements the ``Action`` interface, to put the code that the agent should use.

.. note::

   Note that in the execute method you pass your own agent.

.. important::

   This code does not run by itself, you need to call Agent's run method.

.. code-block:: python

   class ActionPoo(Action):
      def execute(self, agent: Agent):
        agent.minecraft.send_message("Hello guys!!!")

    def create_agent():
      return Agent("HelloBot", ActionPoo())

3.3 Adding EventHandler
~~~~~~~~~~~~~~~~~~~~~~~
In order for your agent to react to events that occur in Minecraft, you can create your own ``EventHandler``, by implementing the ``EventHandler`` interface or by extending ``DefaultEventHandler``

You have 3 types of events:
 - chat_event: new message in the chat
 - block_event: block hit by player
 - command_event: player sends command

.. important::

   By default, the ``DefaultEventHandler`` class has the command event configured to call your agent's command_handler.

In this example our ``CustomEventHandler`` extends ``DefaultEventHandler``, and configures the behavior that for each message it receives (users writing in the chat), it will respond with a "Hello guys!!!"

.. code-block:: python

   class CustomEventHandler(DefaultEventHandler):
      def handle_chat_event(self, event: ChatEventAdapter, agent: Agent):
        agent.run()

   class ActionPoo(Action):
      def execute(self, agent: Agent):
        agent.minecraft.send_message("Hello guys!!!")

    def create_agent():
      return Agent("HelloBot", ActionPoo(), CustomEventHandler())

3.4 Adding Command/s
~~~~~~~~~~~~~~~~~~~~
As we said before, there is an event that is launched when a command is placed. You can register commands that your agent will intercept and program logic based on them.

.. note::

   Note that you can pass arguments to your commands, either unnamed or named like @command 1 time=4, @command name="player" ....

.. important::

   All command need to start with **@**

You can register as many commands as you want, just create a class that implements the ``Command`` interface. Then in ``create_agent()``, you register the Commands with their respective names.
This command runs the agent if it has no parameters. If you pass the times and optionally the time that the agent has to run, it will do so. Ex: @hello 2 time=4

.. warning::

   The loop of this command is blocking, consider using threads, so as not to block other bots. You have an example in ``chat_bot.py``

.. code-block:: python

   class CustomEventHandler(DefaultEventHandler):
      def handle_chat_event(self, event: ChatEventAdapter, agent: Agent):
        agent.run()

   class ActionPoo(Action):
      def execute(self, agent: Agent):
        agent.minecraft.send_message("Hello guys!!!")

   class HelloCommand(Command):
    def execute(self, agent, args, kwargs):
        if len(args) > 0 and args[0].isdigit():
            for i in range(int(args[0])):
                agent.run()
                sleep(1.5 if kwargs.get("time") is None else float(kwargs.get("time")))
        else:
            agent.run()

    def create_agent():
      agent = Agent("HelloBot", ActionPoo(), CustomEventHandler())
      agent.register_command("@hello", HelloCommand())
      return agent

=======================
Framework Documentation
=======================

.. toctree::
   :maxdepth: 2
   :caption: Skeleton

   modules

=======
Support
=======

The easiest way to get help with the project is to open an issue on Github_.

.. _Github: https://github.com/URVPenguin/minecraft_agent_framework/issues

============
Contributing
============

If you'd like to contribute to the development of **Minecraft Agent Framework**, please check out the guidelines below to get started.

1. Clone the repository.
2. Create a branch with your proposed change.
3. Submit a pull request.

=======
License
=======

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details.