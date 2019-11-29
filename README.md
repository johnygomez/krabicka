# How to start

1. Create new virtualenv (pyenv)
1. `pip install -r requirements.txt`
1. `python manage.py migrate`
1. `python manage.py runserver`

This starts a webserver running on <http://127.0.0.1:8000>

# How to use

1. Create a superuser: `python manage.py createsuperuser`
1. Enter <http://127.0.0.1:8000/admin> where you can login using your superuser credentials
1. Create new OID application in _OPENID CONNECT PROVIDER_ section, which will generate Client ID/Secret you can use in your client application
1. In your client application, point to `http://127.0.0.1:8000/openid` as oidc provider

### LDAP

Application is configured to use test LDAP server <https://www.forumsys.com/tutorials/integration-how-to/ldap/online-ldap-test-server/>
so out-of-box you should be able to login with e.g. `gauss:password`. After successful login, LDAP user is added
to Django User list. It's also possible to automatically populate groups and permissions.
Note: You can use the LDAP user to login to app, but not to admin site, for that you'd have to
set `AUTH_LDAP_USER_FLAGS_BY_GROUP` in <krabicka/settings.py>.

More info at <https://django-auth-ldap.readthedocs.io/en/latest/users.html#easy-attributes>
