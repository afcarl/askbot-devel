"""
Social sharing settings
"""
from askbot.conf.settings_wrapper import settings
from askbot.deps.livesettings import ConfigurationGroup, BooleanValue
from django.utils.translation import ugettext as _

SOCIAL_SHARING = ConfigurationGroup(
            'SOCIAL_SHARING',
            _('Sharing content on social networks'), 
        )

settings.register(
    BooleanValue(
        SOCIAL_SHARING,
        'ENABLE_SHARING_TWITTER',
        default=True,
        description=_('Check to enable sharing of questions on Twitter')
    )
)

settings.register(
    BooleanValue(
        SOCIAL_SHARING,
        'ENABLE_SHARING_FACEBOOK',
        default=True,
        description=_('Check to enable sharing of questions on Facebook')
    )
)

settings.register(
    BooleanValue(
        SOCIAL_SHARING,
        'ENABLE_SHARING_LINKEDIN',
        default=True,
        description=_('Check to enable sharing of questions on LinkedIn')
    )
)

settings.register(
    BooleanValue(
        SOCIAL_SHARING,
        'ENABLE_SHARING_GOOGLE',
        default=True,
        description=_('Check to enable sharing of questions on Google+')
    )
)
