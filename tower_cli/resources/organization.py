# Copyright 2015, Ansible, Inc.
# Luke Sneeringer <lsneeringer@ansible.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click

from tower_cli import models, resources
from tower_cli.cli import types


class Resource(models.Resource):
    cli_help = 'Manage organizations within Ansible Tower.'
    endpoint = '/organizations/'
    deprecated_methods = ['associate_project', 'disassociate_project']

    name = models.Field(unique=True)
    description = models.Field(required=False, display=False)

    @resources.command(use_fields_as_options=False)
    @click.option('--organization', type=types.Related('organization'),
                  required=True)
    @click.option('--user', type=types.Related('user'), required=True)
    def associate(self, organization, user):
        """Associate a user with this organization.

        =====API DOCS=====
        Associate a user with this organization.

        :param organization: Primary key or name of the organization to associate to.
        :type organization: str
        :param user: Primary key or name of the user to be associated.
        :type user: str
        :returns: Dictionary of only one key "changed", which indicates whether the association succeeded.
        :rtype: dict

        =====API DOCS=====
        """
        return self._assoc('users', organization, user)

    @resources.command(use_fields_as_options=False)
    @click.option('--organization', type=types.Related('organization'),
                  required=True)
    @click.option('--user', type=types.Related('user'), required=True)
    def associate_admin(self, organization, user):
        """Associate an admin with this organization.

        =====API DOCS=====
        Associate an admin with this organization.

        :param organization: Primary key or name of the organization to associate to.
        :type organization: str
        :param user: Primary key or name of the user to be associated.
        :type user: str
        :returns: Dictionary of only one key "changed", which indicates whether the association succeeded.
        :rtype: dict

        =====API DOCS=====
        """
        return self._assoc('admins', organization, user)

    @resources.command(use_fields_as_options=False)
    @click.option('--organization', type=types.Related('organization'),
                  required=True)
    @click.option('--user', type=types.Related('user'), required=True)
    def disassociate(self, organization, user):
        """Disassociate a user from this organization.

        =====API DOCS=====
        Disassociate a user from this organization.

        :param organization: Primary key or name of the organization to disassociate from.
        :type organization: str
        :param user: Primary key or name of the user to be disassociated.
        :type user: str
        :returns: Dictionary of only one key "changed", which indicates whether the disassociation succeeded.
        :rtype: dict

        =====API DOCS=====
        """
        return self._disassoc('users', organization, user)

    @resources.command(use_fields_as_options=False)
    @click.option('--organization', type=types.Related('organization'),
                  required=True)
    @click.option('--user', type=types.Related('user'), required=True)
    def disassociate_admin(self, organization, user):
        """Disassociate an admin from this organization.

        =====API DOCS=====
        Disassociate an admin from this organization.

        :param organization: Primary key or name of the organization to disassociate from.
        :type organization: str
        :param user: Primary key or name of the user to be disassociated.
        :type user: str
        :returns: Dictionary of only one key "changed", which indicates whether the disassociation succeeded.
        :rtype: dict

        =====API DOCS=====
        """
        return self._disassoc('admins', organization, user)

    @resources.command(use_fields_as_options=False)
    @click.option('--organization', type=types.Related('organization'),
                  required=True)
    @click.option('--project', type=types.Related('project'), required=True)
    def associate_project(self, organization, project):
        """Associate a project with this organization.

        =====API DOCS=====
        Associate a project with this organization.

        :param organization: Primary key or name of the organization to associate to.
        :type organization: str
        :param project: Primary key or name of the project to be associated.
        :type project: str
        :returns: Dictionary of only one key "changed", which indicates whether the association succeeded.
        :rtype: dict

        =====API DOCS=====
        """
        return self._assoc('projects', organization, project)

    @resources.command(use_fields_as_options=False)
    @click.option('--organization', type=types.Related('organization'),
                  required=True)
    @click.option('--project', type=types.Related('project'), required=True)
    def disassociate_project(self, organization, project):
        """Disassociate a project from this organization.

        =====API DOCS=====
        Disassociate a project from this organization.

        :param organization: Primary key or name of the organization to disassociate from.
        :type organization: str
        :param project: Primary key or name of the project to be disassociated.
        :type project: str
        :returns: Dictionary of only one key "changed", which indicates whether the disassociation succeeded.
        :rtype: dict

        =====API DOCS=====
        """
        return self._disassoc('projects', organization, project)
