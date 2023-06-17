from lms.envs.tutor.production import *

# Enable LTI by default if not set in config
if 'ENABLE_LTI_PROVIDER' not in ENV_TOKENS:
    FEATURES['ENABLE_LTI_PROVIDER'] = True
    INSTALLED_APPS.append('lms.djangoapps.lti_provider.apps.LtiProviderConfig')
    AUTHENTICATION_BACKENDS.append('lms.djangoapps.lti_provider.users.LtiBackend')

FEATURES['ENABLE_CHANGE_USER_PASSWORD_ADMIN'] = True