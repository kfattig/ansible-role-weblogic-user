Weblogic User
=========

This role creates users, and updates their group memberships

Requirements
------------

This role requires WLST on the target host.  It's designed to be run on the AdminServer host, but could be run anywhere with WLST installed.

Role Variables
--------------
Name|Description
---|---
weblogic_username|Username to authenticate with Weblogic
weblogic_password|Password to authenticate with Weblogic
username|Username to create
password|Password to set for created user (Use vault!)


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
