#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""Add ip_version to AddressScope

Revision ID: c3a73f615e4
Revises: 13cfb89f881a
Create Date: 2015-10-08 17:34:32.231256

"""

# revision identifiers, used by Alembic.
revision = 'c3a73f615e4'
down_revision = 'dce3ec7a25c9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('address_scopes',
                  sa.Column('ip_version', sa.Integer(), nullable=False))
