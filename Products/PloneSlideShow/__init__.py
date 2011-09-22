# -*- coding: utf-8 -*-

#from zope.i18nmessageid import MessageFactory as BaseMessageFactory
from Products.PloneSlideShow import config

#MessageFactory = BaseMessageFactory('Products.PloneSlideShow')

def initialize(context):
    """Initializer called when used as a Zope 2 product.

    This is referenced from configure.zcml. Regstrations as a "Zope 2 product"
    is necessary for GenericSetup profiles to work, for example.

    Here, we call the Archetypes machinery to register our content types
    with Zope and the CMF.
    """
