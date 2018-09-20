Weblogic User
=========

This role creates users, and updates their group memberships

Requirements
------------

This role requires WLST on the target host.  It's designed to be run on the AdminServer host, but could be run anywhere with WLST installed.

Role Variables
--------------

Below are the variables in use,  see the defaults file for defaults.

Name|Description
---|---
weblogic_admin|Username to authenticate with Weblogic (must be Admin user)
weblogic_password|Password to authenticate with Weblogic
username|Username to create
password|Password to set for created user (Use vault!)
t3_url|T3 URL to connect to Weblogic AdminServer
script_temp_location|Location to stage WLST scripts
oracle_user|User that owns weblogic installation (used for ownership of WLST scripts)
oracle_group|Group that owns weblogic installation (used for ownership of WLST scripts)
domain_name|Name of the weblogic domain
wlst_script|Path to WLST script
update_memberships|Boolean to enable/disable group membership update
create_user|Boolean to enable/disable user creation
description|Description to use for the user in weblogic.


Dependencies
------------

No Dependencies

Example Playbook
----------------

This sample creates an Admin user called 'testuser'

    - name: create testuser
    hosts: weblogic_admin_host
    become: yes
    become_user: mwadmin
    roles:
    - role: weblogic_user
    vars:
      create_user: True
      update_memberships: True
      username: testuser
      password: password1234
      group_name: Administrators
      weblogic_admin: weblogic
      weblogic_password: weblogic1234
      domain_name: MyDomain


Author Information
------------------

kyle.fattig@zirous.com
