# -*- coding:utf-8 -*-
from zope.schema import Bool, Int, TextLine, Tuple, Choice
from zope.component import adapts
from zope.interface import Interface, implements

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFPlone.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty, SchemaAdapterBase

from zope.formlib.form import FormFields
from plone.app.controlpanel.form import ControlPanelForm
from plone.fieldsets.fieldsets import FormFieldsets

from Products.PloneSlideShow import MessageFactory as _

class IProvidersSchema(Interface):
    """ General Configurations """ 

    withcollection = Bool(
        title=_(u"Slide using Plone collection criteria"),
        description=_(u'help_withcollection',
            default=u"If set to true, do not use the CMFPublicator",
        ),
        default=False,
        required=False
    )
                          
class BaseControlPanelAdapter(SchemaAdapterBase):
    """ Base control panel adapter """
   
    def __init__(self, context):
        super(BaseControlPanelAdapter, self).__init__(context)
        portal_properties = getToolByName(context, 'portal_properties')
        self.context = portal_properties.ploneslideshow_properties

class SlideShowControlPanelAdapter(BaseControlPanelAdapter):
    """ control panel adapter """
    adapts(IPloneSiteRoot)
    implements(IProvidersSchema)
    
    withcollection = ProxyFieldProperty(IProvidersSchema['withcollection'])

baseset = FormFieldsets(IProvidersSchema)
baseset.id = 'baseset'
baseset.label = _(u'SlideShow Configuration')

class ProvidersControlPanel(ControlPanelForm):
    """ """
    form_fields = FormFieldsets(baseset)
    
    label = _('SlideShow Settings')
    description = _('Configure settings for Products.PloneSlideShow.')
    form_name = _('SlideShow Configuration')
