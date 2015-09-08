import yaml
import sys
import string
import argparse
from tcutils.cfgparser import parse_cfg_file
from common.contrail_test_init import ContrailTestInit
from common.connections import ContrailConnections
from tcutils.db import TestDB
from config import *

def random_string(prefix):
    return prefix+''.join(random.choice(string.hexdigits) for _ in range(6))

def sig_handler(_signo, _stack_frame):
    raise KeyboardInterrupt

def setup_test_infra(testbed_file):
    import logging
    from common.log_orig import ContrailLogger
    logging.getLogger('urllib3.connectionpool').setLevel(logging.WARN)
    logging.getLogger('paramiko.transport').setLevel(logging.WARN)
    logging.getLogger('keystoneclient.session').setLevel(logging.WARN)
    logging.getLogger('keystoneclient.httpclient').setLevel(logging.WARN)
    logging.getLogger('neutronclient.client').setLevel(logging.WARN)
    logger = ContrailLogger('delete')
    logger.setUp()
    mylogger = logger.logger
    inputs = ContrailTestInit(testbed_file, logger=mylogger)
    inputs.setUp()
    connections = ContrailConnections(inputs=inputs, logger=mylogger)
    return connections

class delete(object):
    def __init__(self, args):
        self.args = args
        self.connections = setup_test_infra(args.testbed_file)
        self.db = None
        if args.db_file:
            self.db = TestDB(args.db_file)

    def get_vdns_ids(self):
        if not self.args.delete_vdns or self.args.tenant:
            return []
        vdns = []
        if self.args.vdns_id:
            return self.args.vdns_id
        if self.db:
            for fqname in self.db.list_vdns():
                vdns.append(self.db.get_vdns_id(fqname))
        return vdns

    def get_fip_pool_ids(self):
        if not self.args.delete_fip_pool or self.args.tenant:
            return []
        fip_pools = []
        if self.args.fip_pool_id:
            return self.args.fip_pool_id
        if self.db:
            for fqname in self.db.list_fip_pools():
                fip_pools.append(self.db.get_fip_pool_id(fqname))
        return fip_pools

    def get_tenant_fqnames(self):
        if self.args.tenant:
            return [':'.join([self.connections.inputs.domain_name, self.args.tenant])]
        if self.db:
            return self.db.list_projects()
        return []

    def get_ipam_ids(self, project_fqname):
        ipams = []
        if not self.args.delete_ipam or self.args.vn_name:
            return ipams
        if self.args.ipam_id:
            return self.args.ipam_id
        if self.db:
            for fqname in self.db.list_ipams(project_fqname):
                ipams.append(self.db.get_ipam_id(fqname))
        return ipams

    def get_vn_ids(self, project_fqname, connections):
        if self.args.vm_id:
            return []
        if self.args.vn_name:
            vn_id = connections.get_network_h().get_vn_id(self.args.vn_name)
            assert vn_id, 'Unable to fetch ID of vn_name '+ self.args.vn_name
            return [vn_id]
        vns = []
        if self.db:
            for fqname in self.db.list_virtual_networks(project_fqname):
                vn_id = self.db.get_virtual_network_id(fqname)
                vns.append(vn_id)
        return vns

    def get_vm_details(self, vm_name, project_fqname, connections):
        if self.args.vm_id:
            vn_id = connections.get_network_h().get_vn_id(self.args.vn_name)
            return (self.args.vm_id, [vn_id], '', '')
        if self.db:
            return self.db.get_virtual_machine(vm_name, project_fqname)
        return None

    def get_vm_names(self, project_fqname):
        if self.args.vm_id:
            return [self.args.vm_id]
        if self.db:
            return self.db.list_virtual_machines(project_fqname)
        return []

    def get_router_ids(self, project_fqname):
        if not self.args.delete_snat or self.args.vn_name:
            return []
        if self.args.router_id:
            return [self.args.router_id]
        if self.db:
            rtr_ids = []
            for rtr in self.db.list_logical_routers():
                if project_fqname not in rtr:
                    continue
                rtr_ids.append(self.db.get_logical_router_id(rtr))
            return rtr_ids
        return []

    def get_project_id(self, fqname):
        if self.db:
            return self.db.get_project_id(fqname)
        else:
            return self.connections.get_auth_h().get_project_id(fqname[-1])

    def get_fip_ids(self, vm_name, project_fqname):
        if self.db:
            return self.db.get_fip_id_assoc(vm_name, project_fqname)
        return []

    def _delete(self, tenant_fqname, connections):

        for vm_name in self.get_vm_names(tenant_fqname):
            (vm_id, vn_ids, username, password) = \
                    self.get_vm_details(vm_name, tenant_fqname, connections)
            obj = VM(connections)
            if self.args.vm_id:
                vm_name = obj.fq_name(vm_id)
            for fip_id in self.get_fip_ids(vm_name, tenant_fqname):
                fip_obj = FloatingIPPool(self.connections)
                fip_pool_id = fip_obj.get_fip_pool_id(fip_id)
                fip = fip_obj.get_fip_from_id(fip_id)
                fip_obj.disassociate_fip(fip_pool_id, fip_id)
                fip_obj.verify_no_fip(fip_pool_id, fip_id, vm_id, fip)
                if self.db:
                    self.db.delete_fip(fip_obj.fq_name(), fip_id)
                    self.db.disassociate_fip_from_vm(vm_name, tenant_fqname, fip_id)
            obj.delete(vm_id, vn_ids)
            if self.db:
                self.db.delete_virtual_machine(vm_name, tenant_fqname)

        for router_id in self.get_router_ids(tenant_fqname):
            router_obj = LogicalRouter(connections)
            fqname = router_obj.fq_name(router_id)
            router_obj.delete(router_id)
            if self.db:
                self.db.delete_logical_router(fqname)
#ToDo: msenthil - Link LR and VNs

        for vn_id in self.get_vn_ids(tenant_fqname, connections):
            obj = VN(connections)
            fqname = obj.fq_name(vn_id)
            obj.delete(vn_id)
            if self.db:
                self.db.delete_virtual_network(fqname)

        ipam_ids = self.get_ipam_ids(tenant_fqname)
        for ipam_id in ipam_ids:
            obj = IPAM(connections)
            fqname = obj.fq_name(ipam_id)
            obj.delete(ipam_id)
            if self.db:
                self.db.delete_ipam(fqname)

    def delete(self):
        for tenant_fqname in self.get_tenant_fqnames():
            if tenant_fqname == ':'.join(self.connections.get_project_fq_name()):
                continue
            project_obj = Project(self.connections)
            project_id = self.get_project_id(tenant_fqname)
            connections = project_obj.get_connections(project_id)
            self._delete(tenant_fqname, connections)
            if not self.args.vn_name and self.args.delete_ipam:
                project_obj.delete(project_id)
                if self.db:
                    self.db.delete_project(tenant_fqname)

        fip_pool_ids = self.get_fip_pool_ids()
        for fip_pool in fip_pool_ids:
            obj = FloatingIPPool(self.connections)
            fqname = obj.fq_name(fip_pool)
            obj.delete(fip_pool)
            if self.db:
                self.db.delete_fip_pool(fqname)

        if not self.args.tenant or self.args.tenant == self.connections.project_name:
            self._delete(':'.join(self.connections.get_project_fq_name()),
                         self.connections)

            vdns_ids = self.get_vdns_ids()
            for vdns_id in vdns_ids:
                obj = vDNS(self.connections)
                fqname = obj.fq_name(vdns_id)
                obj.delete(vdns_id)
                if self.db:
                    self.db.delete_vdns(fqname)

def validate_args(args):
    for key, value in args.__dict__.iteritems():
        if type(value) is str:
            if value.lower() == 'none':
                args.__dict__[key] = None
            if value.lower() == 'false':
                args.__dict__[key] = False
            if value.lower() == 'true':
                args.__dict__[key] = True

    if (args.vm_id or args.vn_name) and not args.tenant:
        raise Exception('Need tenant name too. use --tenant <tenant_name>')

    if not args.testbed_file:
        args.testbed_file = os.path.join(os.path.abspath(
                                         os.path.dirname(__file__)),
                                         '../', 'sanity_params.ini')
#    if not args.db_file:
#        args.db_file = os.path.join('/var/tmp/', 'test.db')

    if type(args.vdns_id) is str:
       args.vdns_id = [args.vdns_id]
    if type(args.ipam_id) is str:
       args.ipam_id = [args.ipam_id]
    if type(args.fip_pool_id) is str:
       args.fip_pool_id = [args.fip_pool_id]

    if args.vdns_id == True:
        args.vdns_id = None
    if args.router_id == True:
        args.router_id = None
    if args.ipam_id == True:
        args.ipam_id = None
    if args.fip_pool_id == True:
        args.fip_pool_id = None

def parse_cli(args):
    '''Define and Parse arguments for the script'''
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--testbed_file', default=None,
                        help='Specify testbed ini file', metavar="FILE")
    parser.add_argument('--db_file', default=None,
                        help='Specify database file', metavar="FILE")

    parser.add_argument('--tenant', default=None,
                        help='Tenant name []')
    parser.add_argument('--vdns_id', default=None,
                        help='UUID of virtual DNS')
    parser.add_argument('--ipam_id', default=None,
                        help='IPAM UUID')
    parser.add_argument('--router_id', default=None,
                        help='UUID of Logical Router(snat)')
    parser.add_argument('--vn_name', default=None,
                        help='Name of virtual network')

    parser.add_argument('--vm_id', default=None,
                        help='UUID of Virtual Machine')
    parser.add_argument('--fip_pool_id', default=None,
                        help='UUID of Floating IP Pool')

    args = dict(parser.parse_known_args(args)[0]._get_kwargs())
    return create_per_tenant_args(args['tenant'], dict(), dict(), args)

def populate_args(args):
    args['delete_vdns'] = False
    args['delete_snat'] = False
    args['delete_ipam'] = False
    args['delete_fip_pool'] = False
    if args['vdns_id']:
        args['delete_vdns'] = True
    if args['router_id']:
        args['delete_snat'] = True
    if args['ipam_id']:
        args['delete_ipam'] = True
    if args['fip_pool_id']:
        args['delete_fip_pool'] = True

def create_per_tenant_args(name, default_args, global_args, tenant_args=None):
    tenant = default_args.copy()
    if tenant_args:
        tenant.update(tenant_args)
        populate_args(tenant)
    tenant['tenant'] = name
    tenant.update(global_args)
    return tenant

def parse_yaml(conf, cli_args):
    config = yaml.load(open(conf, 'r'))
    if cli_args:
        update_args(config['default'], cli_args)
    n_tenants = config['default'].get('n_tenants', 0) or 0
    pargs = dict()
    populate_args(config['default'])
#    for index in range(n_tenants):
#        name = (config['default']['name'] or 'TestProject') + str(index)
#        pargs[name] = create_per_tenant_args(name, config['default'],
#                                             config['global'])
    for entry in config['tenant']:
        name = entry.keys()[0]
        pargs[name] = create_per_tenant_args(name, config['default'],
                                             config['global'], entry[name])
    if cli_args['tenant'] in pargs.keys():
        update_args(pargs[name], cli_args)
    return pargs

def update_args(ini_args, cli_args):
    for key in cli_args.keys():
        if cli_args[key]:
            ini_args[key] = cli_args[key]
    return ini_args

class Struct(object):
    def __init__(self, entries):
        self.__dict__.update(entries)

    def __getattr__(self, attrib):
        print ' am i here'
        return getattr(self, attrib, None)

def main():
    signal.signal(signal.SIGTERM, sig_handler)
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-c", "--config", help="Specify conf file", metavar="FILE")
    pargs, remaining_argv = parser.parse_known_args(sys.argv[1:])
    cli_args = parse_cli(remaining_argv)
    if pargs.config:
        cargs = parse_yaml(pargs.config, cli_args)
    else:
        cargs = {None: cli_args}
    for key, tenant in cargs.iteritems():
        tenant_args = Struct(tenant)
        validate_args(tenant_args)
        obj = delete(tenant_args)
        obj.delete()

if __name__ == "__main__":
    main()
