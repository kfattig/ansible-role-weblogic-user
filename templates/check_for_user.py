import sys

connect('{{ weblogic_admin }}','{{ weblogic_password }}','{{ t3_url }}')
edit()
serverConfig()

cd('/SecurityConfiguration/{{ domain_name }}/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
sys.exit(cmo.userExists('{{ username }}'))
disconnect()
exit()
