import ldap
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion

AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_SERVER_URI = "{{cookiecutter.ldap_server}}"
AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
    LDAPSearch("{{cookiecutter.ldap_user_dn}}", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
)
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {}
AUTH_LDAP_ALWAYS_UPDATE_USER = True
