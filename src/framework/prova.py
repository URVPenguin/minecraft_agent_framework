"""
prova.py
====================================
The core module of my example project
"""

import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
mc.postToChat("Hola python")
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)



def a(self, name):
    """
    dfasdfasd fasdf asf dasd f

    Parameters
    ----------
    name : string
        afdasd fasdf ad fad f

    Returns
    -------
    Integer
        sd adsfas dfdsf fa sdfa
    """
    return 1

class Person:
    """Classe Person"""

    def __init__(self, name):
        """
        Return the most important thing about a person.
        Parameters
        ----------
        name
            A string indicating the name of the person.
        """
        self.name = name

    def about_self(self):
        """
        Return the most important thing about a person.
        """
        return "I am a very smart {} object.".format(self.name)