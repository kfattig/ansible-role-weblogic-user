import sys

connect('{{ weblogic_admin }}','{{ weblogic_password }}','{{ t3_url }}')
edit()
serverConfig()

cd('/SecurityConfiguration/{{ domain_name }}/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
cmo.createUser('{{ username }}','{{ password }}','{{ description }}')
disconnect()
exit()

