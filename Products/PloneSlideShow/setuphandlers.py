# -*- coding: utf-8 -*-
from zope import component
import logging
from Products.CMFCore.utils import getToolByName
from Products.GenericSetup import interfaces as gsinterfaces
from Products.GenericSetup.upgrade import listUpgradeSteps

from Products.ZCatalog.ProgressHandler import ZLogHandler

_PROJECT = 'Products.PloneSlideShow'
_PROFILE_ID = 'Products.PloneSlideShow:default'

def doUpgrades(context):
    """ If exists, run migrations
    """
    if context.readDataFile('Products.PloneSlideShow.txt') is None:
        return
    logger = logging.getLogger(_PROJECT)
    site = context.getSite()
    setup_tool = getToolByName(site,'portal_setup')
    version = setup_tool.getLastVersionForProfile(_PROFILE_ID)
    upgradeSteps = listUpgradeSteps(setup_tool,_PROFILE_ID, version)
    sorted(upgradeSteps,key=lambda step:step['sortkey'])

    for step in upgradeSteps:
        oStep = step.get('step')
        if oStep is not None:
            oStep.doStep(setup_tool)
            msg = "Ran upgrade step %s for profile %s" % (oStep.title,
                                                          _PROFILE_ID)
            setup_tool.setLastVersionForProfile(_PROFILE_ID, oStep.dest)
            logger.info(msg)

def add_publicator_box(site):
    portal_publicator = getToolByName(site, 'portal_publicator')
    boxes = portal_publicator.getPublicationBoxes()
    ids_boxes = []
    for box in boxes:
        ids_boxes.append(box.id)

    if 'slides' not in ids_boxes:
        portal_publicator.addPublicationBox(id='slides',
                                            name='Slides',
                                            content_type=['News Item','Document'],
                                            n_items=5,
                                            search_states=['published'],
                                            with_image=True,)

def installConfigurePublicator(context):
    """
    Install and configure CMFPublicator
    """
    if context.readDataFile('Products.PloneSlideShow.txt') is None:
        return
    logger = logging.getLogger(_PROJECT)
    productname  = 'Products.CMFPublicator'
    site = context.getSite()
    qi_tool = getToolByName(site,'portal_quickinstaller')

    if qi_tool.isProductInstallable(productname):
        ''' is the product directory present and ready for installation '''
        if qi_tool.isProductInstalled(productname):
            ''' checks wether a product is installed (by name) '''
            add_publicator_box(site)
        else:
            qi_tool.installProducts([productname],)
            add_publicator_box(site)
        msg = "Ran %s step for %s " %(productname, _PROJECT)
    else:
        msg = "Error in PloneslideShow - Install and configurate publicator step: %s is required " %(productname)

    logger.info(msg)
