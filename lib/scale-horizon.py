import horizon

# remove the 'change password panel'
settings_dashboard = horizon.get_dashboard("settings")
password_panel = settings_dashboard.get_panel("password")
settings_dashboard.unregister(password_panel.__class__)

