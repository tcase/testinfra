# coding: utf-8
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

from __future__ import unicode_literals

import importlib
import sys


def _import_modules():
    modules = {
        'PipPackage': __name__ + '.pip',
        'Facter': __name__ + '.puppet',
        'PuppetResource': __name__ + '.puppet',
    }
    for name in (
        'Ansible', 'Command', 'File', 'Group', 'Interface', 'MountPoint',
        'Package', 'Process', 'Salt', 'Service', 'Socket', 'Sudo',
        'Supervisor', 'Sysctl', 'SystemInfo', 'User'
    ):
        modules[name] = __name__ + '.' + name.lower()
    mod = sys.modules[__name__]
    for name, modname in modules.items():
        module = importlib.import_module(modname)
        setattr(mod, name, getattr(module, name))
    return modules.keys()

__all__ = _import_modules()
