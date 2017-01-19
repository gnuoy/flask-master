#!/usr/bin/python3

import os
import sys

sys.path.insert(0, os.path.join(os.environ['CHARM_DIR'], 'lib'))

import charmhelpers.core.hookenv as hookenv

hooks = hookenv.Hooks()
log = hookenv.log

@hooks.hook('install')
def install():
    pass

@hooks.hook('config-changed')
def config_changed():
    for rid in hookenv.relation_ids('flask-slave'):
        flask_slave_joined(rid)


@hooks.hook('flask-slave-relation-joined')
def flask_slave_joined(rid=None):
    hookenv.relation_set(relation_id=rid,
                         motd=hookenv.config('motd'))

@hooks.hook('start')
def start():
    pass

@hooks.hook('stop')
def stop():
    pass

if __name__ == "__main__":
    # execute a hook based on the name the program is called by
    hooks.execute(sys.argv)
