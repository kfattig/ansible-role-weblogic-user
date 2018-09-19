import sys

connect('{{ weblogic_admin }}','{{ weblogic_password }}','{{ t3_url }}')
edit()
serverConfig()

cd('/SecurityConfiguration/{{ domain_name }}/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
sys.exit(cmo.isMember('{{ group_name }}','{{ username }}',true))
disconnect()
exit()
