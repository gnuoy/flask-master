#!/usr/bin/python3

import os
import sys

sys.path.insert(0, os.path.join(os.environ['CHARM_DIR'], 'lib'))

import charmhelpers.core.hookenv as hookenv  # noqa: E402

hooks = hookenv.Hooks()
log = hookenv.log


@hooks.hook('install')
def install():
    pass


@hooks.hook('config-changed')
def config_changed():
    for rid in hookenv.relation_ids('flask-master'):
        flask_slave_joined(rid)


@hooks.hook('flask-master-relation-joined')
def flask_slave_joined(rid=None):
    elaborate = hookenv.config('elaborate')
    motd = hookenv.config('motd')
    if elaborate:
        # motd = "Our amazing MOTD is '{}'".format(motd)
        motd = 'the motd is, err, broken'
    hookenv.relation_set(relation_id=rid, motd=motd)


@hooks.hook('start')
def start():
    pass


@hooks.hook('stop')
def stop():
    pass


@hooks.hook('upgrade-charm')
@hooks.hook('flask-master-relation-broken')
@hooks.hook('flask-master-relation-departed')
@hooks.hook('flask-master-relation-changed')
def noop():
    pass

if __name__ == "__main__":
    # execute a hook based on the name the program is called by
    hooks.execute(sys.argv)
