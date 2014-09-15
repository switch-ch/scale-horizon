=============
Scale-Horizon
=============

The Scale-Horizon module is an OpenStack Horizon customization module.

Installation
============

To install, first install the module:::

   python setup.py install


Then edit the Horizon configuration file ```/etc/openstack-dashboard/local_settings.py```
to include the ```customization_module``` line:::


    HORIZON_CONFIG = {
        'dashboards': ('project', 'admin', 'settings',),
        'default_dashboard': 'project',
        'user_home': 'openstack_dashboard.views.get_user_home',
        'ajax_queue_limit': 10,
        'auto_fade_alerts': {
            'delay': 3000,
            'fade_duration': 1500,
            'types': ['alert-success', 'alert-info']
        },
        'help_url': "http://docs.openstack.org",
        'exceptions': {'recoverable': exceptions.RECOVERABLE,
                       'not_found': exceptions.NOT_FOUND,
                       'unauthorized': exceptions.UNAUTHORIZED},
        'customization_module': 'switch.scale-horizon',
    }

Restart Apache for the changes to take effect.

Customizations
==============

The ```scale-horizon``` module currently does the following customizations:

* Remove the ```change password``` panel (we manage users through a different system)


Build
=====

To build a distribution source package, run:::

    python setup.py sdist

