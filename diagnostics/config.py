import os
from vm_test import *
from vn_test import *
from ipam_test import *
from floating_ip import *
from project_test import *
from vdns_fixture import *

class Base(object):
    def __init__(self, connections):
        self.connections = connections
        self.verify_on_delete = False

    def fq_name(self, uuid=None):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = self.get_fixture(uuid=uuid)
        return self.fixture.get_fq_name()

    def uuid(self):
        return self.fixture.get_uuid()

class Project(Base):
    def create(self, name):
        self.fixture = ProjectFixture(project_name=name, connections=self.connections)
        self.fixture.setUp()
        project_id = self.fixture.get_uuid()
        self.add_user_to_tenant(project_id)
        return project_id

    def add_user_to_tenant(self, uuid):
        kc = self.connections.get_auth_h().get_keystone_h()
        user_id = kc.get_user_dct(self.connections.inputs.stack_user)
        role_id = kc.get_role_dct('admin')
        kc._add_user_to_tenant(uuid.replace('-', ''), user_id, role_id)

    def update_default_sg(self, uuid=None):
        project_fixture= self.get_fixture(uuid=uuid)
        project_fixture.set_sec_group_for_allow_all()

    def get_connections(self, uuid=None):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = self.get_fixture(uuid=uuid)
        return self.fixture.get_project_connections()

    def delete(self, uuid):
        project_fixture= self.get_fixture(uuid=uuid)
        project_fixture.delete(verify=self.verify_on_delete)

    def verify(self, uuid):
        self.fixture= self.get_fixture(uuid=uuid)
        assert self.fixture.verify_on_setup()

    def get_fixture(self, uuid):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = ProjectFixture(connections=self.connections, uuid=uuid)
        return self.fixture

class vDNS(Base):
    def create(self, name):
        self.fixture = VdnsFixture(connections=self.connections, name=name)
        self.fixture.setUp()
        return self.fixture.get_uuid()

    def delete(self, uuid):
        vdns_fixture = self.get_fixture(uuid=uuid)
        vdns_fixture.delete(verify=self.verify_on_delete)

    def verify(self, uuid):
        vdns_fixture = self.get_fixture(uuid=uuid)
        assert vdns_fixture.verify_on_setup()

    def get_fixture(self, uuid):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = VdnsFixture(connections=self.connections, uuid=uuid)
        return self.fixture

class IPAM(Base):
    def create(self, name, vdns_id=None):
        vdns_obj=None
        if vdns_id:
            vnc = self.connections.get_vnc_lib_h().get_handle()
            vdns_obj = vnc.virtual_DNS_read(id=vdns_id)
        self.fixture = IPAMFixture(connections=self.connections,
                                   name=name, vdns_obj=vdns_obj)
        self.fixture.setUp()
        return self.fixture.get_uuid()

    def delete(self, uuid):
        ipam_fixture = self.get_fixture(uuid=uuid)
        ipam_fixture.delete(verify=self.verify_on_delete)

    def update(self, uuid, vdns_id):
        if vdns_id:
            vnc = self.connections.get_vnc_lib_h().get_handle()
            vdns_obj = vnc.virtual_DNS_read(id=vdns_id)
            self.fixture = self.get_fixture(uuid=uuid)
            self.fixture.update_vdns(vdns_obj)

    def verify(self, uuid):
        ipam_fixture = self.get_fixture(uuid=uuid)
        assert ipam_fixture.verify_on_setup()

    def get_fixture(self, uuid):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = IPAMFixture(connections=self.connections, uuid=uuid)
        return self.fixture

class VN(Base):
    def create(self, name, subnets=[], ipam_id=None, external=False):
        kwargs = dict()
        if ipam_id:
            kwargs['ipam_fq_name'] = IPAM(self.connections).fq_name(ipam_id)
        if external:
            kwargs['shared'] = True
            kwargs['router_external'] = True
        self.fixture = VNFixture(connections=self.connections, vn_name=name,
                                 subnets=subnets, **kwargs)
        self.fixture.setUp()
        return self.fixture.get_uuid()

    def delete(self, uuid, subnets=[]):
        if not subnets:
            subnets = self.get_subnets(uuid)
        vn_fixture = self.get_fixture(uuid=uuid, subnets=subnets)
        vn_fixture.delete(verify=self.verify_on_delete)

    def get_subnets(self, uuid):
        quantum_h = self.connections.get_network_h()
        return quantum_h.get_subnets_of_vn(uuid)
        return list(map(lambda x: x['id'], quantum_h.get_subnets_of_vn(uuid)))

    def verify(self, uuid, subnets=[]):
        if not subnets:
            subnets = self.get_subnets(uuid)
        vn_fixture = self.get_fixture(uuid=uuid, subnets=subnets)
        assert vn_fixture.verify_on_setup()

    def get_fixture(self, uuid, subnets=[]):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = VNFixture(connections=self.connections,
                                     uuid=uuid, subnets=subnets)
        return self.fixture

class VM(Base):
    def create(self, name, vn_ids, image='ubuntu'):
        self.fixture = VMFixture(connections=self.connections, vn_ids=vn_ids,
                                 vm_name=name, image_name=image, node_name='disable')
        self.fixture.setUp()
        return self.fixture.get_uuid()

    def get_vm_creds(self):
        return (self.fixture.get_vm_username(),
                self.fixture.get_vm_password())

    def delete(self, uuid, vn_ids=[]):
        vm_fixture = self.get_fixture(uuid=uuid, vn_ids=vn_ids)
        verify= self.verify_on_delete if vn_ids else False
        vm_fixture.delete(verify=verify)

    def verify(self, uuid, vn_ids=[], username='ubuntu', password='ubuntu'):
        vm_fixture = self.get_fixture(uuid=uuid, vn_ids=vn_ids)
        vm_fixture.set_vm_creds(username, password)
        assert vm_fixture.verify_on_setup()

    def vm_ip(self, uuid, vn_name=None):
        orch_h = self.connections.get_orch_h()
        vm_obj = orch_h.get_vm_by_id(vm_id=uuid)
        return orch_h.get_vm_ip(vm_obj, vn_name)[0][0]

    def vm_name(self, uuid):
        orch_h = self.connections.get_orch_h()
        vm_obj = orch_h.get_vm_by_id(vm_id=uuid)
        return vm_obj.name

    def ping(self, uuid, dst, username='ubuntu', password='ubuntu'):
        vm_fixture = self.get_fixture(uuid=uuid)
        vm_fixture.set_vm_creds(username, password)
        return vm_fixture.ping_to_ip(dst, count=3)

    def wait_till_up(self, uuid, username='ubuntu', password='ubuntu'):
        vm_fixture = self.get_fixture(uuid=uuid)
        vm_fixture.set_vm_creds(username, password)
        assert vm_fixture.wait_till_vm_is_up(), 'VM didnt come up'

    def copy_file_to_vm(self, uuid, localfile, dst='/tmp/',
                        username='ubuntu', password='ubuntu'):
        vm_fixture = self.get_fixture(uuid=uuid)
        vm_fixture.set_vm_creds(username, password)
        vm_fixture.copy_file_to_vm(localfile, dst)

    def get_fixture(self, uuid, vn_ids=[]):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = VMFixture(connections=self.connections,
                                     uuid=uuid, vn_ids=vn_ids)
        return self.fixture

    def tcpecho(self, uuid, dst, dport=50000,
                username='ubuntu', password='ubuntu'):
        vm_fixture = self.get_fixture(uuid=uuid)
        vm_fixture.set_vm_creds(username, password)
        tcpclient = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                 '../', 'tcutils', 'tcpechoclient.py')
        self.copy_file_to_vm(uuid, tcpclient, '/tmp/',
                             username, password)
        cmd = 'python /tmp/tcpechoclient.py '+\
              ' --servers %s --dports %s --count 5'%(dst, dport)
        output = vm_fixture.run_cmd_on_vm(cmds=[cmd], as_sudo=True)
        if not output or not output[cmd]:
             print 'retry to workaround fab issues'
             output = vm_fixture.run_cmd_on_vm(cmds=[cmd], as_sudo=True)
        assert output[cmd], 'Connection timedout'
        exp = 'sent and received 5'
        if exp not in output[cmd]:
            print output[cmd]
            assert False, 'TCP Echo failure'
        return True

    def curl(self, uuid, dst, username='ubuntu', password='ubuntu', port=8000):
        vm_fixture = self.get_fixture(uuid=uuid)
        vm_fixture.set_vm_creds(username, password)
        cmd = 'curl -s http://%s:%d'%(dst, port)
        output = vm_fixture.run_cmd_on_vm(cmds=[cmd])[cmd]
        return output.strip() if output else output

    def web_server(self, uuid, username='ubuntu', password='ubuntu', port=8000):
        vm_fixture = self.get_fixture(uuid=uuid)
        vm_fixture.set_vm_creds(username, password)
        vm_fixture.wait_for_ssh_on_vm()
        ip = self.vm_ip(uuid)
        cmd = 'echo %s >& index.html'%ip
        self.run_cmd(uuid, cmd)
        cmd = 'python -m SimpleHTTPServer %d &> /dev/null '%port
        self.run_cmd(uuid, cmd, daemon=True)

    def run_cmd(self, uuid, cmd, sudo=False, daemon=False):
        vm_fixture = self.get_fixture(uuid)
        vm_fixture.run_cmd_on_vm(cmds=[cmd], as_sudo=sudo, as_daemon=daemon)

class FloatingIPPool(Base):
    def create(self, vn_id, name=None):
        self.fixture = FloatingIPFixture(connections=self.connections,
                                         pool_name=name, vn_id=vn_id)
        self.fixture.setUp()
        return self.fixture.get_uuid()

    def delete(self, uuid):
        fip_fixture = self.get_fixture(uuid=uuid)
        fip_fixture.delete(verify=self.verify_on_delete)

    def associate_fip(self, uuid, vm_id, vm_connections,
                      username='ubuntu', password='ubuntu'):
        self.fixture = self.get_fixture(uuid=uuid)
        tcpserver = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                 '../', 'tcutils', 'tcpechoserver.py')
        vm = VM(vm_connections)
        vm.wait_till_up(vm_id, username, password)
        vm.copy_file_to_vm(vm_id, tcpserver, '/tmp/', username, password)
        cmd = 'python /tmp/tcpechoserver.py'
        vm.run_cmd(vm_id, cmd, sudo=True, daemon=True)
        return self.fixture.create_and_assoc_fip(vm_id=vm_id)

    def disassociate_fip(self, uuid, fip_id):
        self.fixture = self.get_fixture(uuid=uuid)
        self.fixture.disassoc_and_delete_fip(fip_id)

    def get_fip_from_id(self, fip_id):
        quantum_h = self.connections.get_network_h()
        return quantum_h.get_floatingip(fip_id)['floatingip']['floating_ip_address']

    def verify_fip(self, uuid, fip_id, vm_id, vn_ids, vm_connections):
        fip_fixture = self.get_fixture(uuid=uuid)
        fvn_fixture = VNFixture(connections=self.connections,
                                uuid=fip_fixture.get_vn_id())
        vm_fixture = VMFixture(connections=vm_connections, uuid=vm_id, vn_ids=vn_ids)
        assert fip_fixture.verify_fip(fip_id, vm_fixture, fvn_fixture)

    def verify_no_fip(self, uuid, fip_id, vm_id, fip=None):
        fip_fixture = self.get_fixture(uuid=uuid)
        fvn_fixture = VNFixture(connections=self.connections,
                                uuid=fip_fixture.get_vn_id())
        assert fip_fixture.verify_no_fip(fip_id, fvn_fixture, fip)

    def verify(self, uuid):
        fip_fixture = self.get_fixture(uuid=uuid)
        assert fip_fixture.verify_on_setup()

    def get_associated_fips(self, uuid):
        fip_fixture = self.get_fixture(uuid=uuid)
        return fip_fixture.get_associated_fips()

    def get_fip_pool_id(self, fip_id):
        vnc = self.connections.get_vnc_lib_h().get_handle()
        return vnc.floating_ip_read(id=fip_id).parent_uuid

    def get_fixture(self, uuid):
        if not getattr(self, 'fixture', None):
            assert uuid, 'ID cannot be None'
            self.fixture = FloatingIPFixture(connections=self.connections, uuid=uuid)
        return self.fixture

class LogicalRouter(Base):
    def create(self, name, vn_ids=[], gw=None):
        quantum_h = self.connections.get_network_h()
        response = quantum_h.check_and_create_router(name)
        self.uuid = response['id']
        self.fqname = response['contrail:fq_name']
        if gw:
            self.set_gw(self.uuid, gw)
        for vn_id in vn_ids:
            self.attach_vn(self.uuid, vn_id)
        return self.uuid

    def set_gw(self, uuid, gw):
        quantum_h = self.connections.get_network_h()
        quantum_h.router_gateway_set(uuid, gw)

    def clear_gw(self, uuid):
        quantum_h = self.connections.get_network_h()
        quantum_h.router_gateway_clear(uuid)

    def attach_vn(self, uuid, vn_id=None, subnet_id=None):
        quantum_h = self.connections.get_network_h()
        if not subnet_id and vn_id:
            subnet_id = quantum_h.get_vn_obj_from_id(vn_id)['network']['subnets'][0]
        quantum_h.add_router_interface(router_id=uuid, subnet_id=subnet_id)

    def detach_vn(self, uuid, vn_id=None, subnet_id=None):
        quantum_h = self.connections.get_network_h()
        if not subnet_id and vn_id:
            subnet_id = quantum_h.get_vn_obj_from_id(vn_id)['network']['subnets'][0]
        quantum_h.delete_router_interface(router_id=uuid, subnet_id=subnet_id)

    def delete(self, uuid):
        quantum_h = self.connections.get_network_h()
        ports = quantum_h.get_router_interfaces(uuid)
        for port in ports:
            quantum_h.delete_router_interface(router_id=uuid, port_id=port['id'])
        quantum_h.delete_router(uuid)

    def list_subnets(self, uuid):
        quantum_h = self.connections.get_network_h()
        subnets = list()
        for ports in quantum_h.get_router_interfaces(uuid):
            subnets.append(port['fixed_ips']['subnet_id'])
        return subnets

    def uuid(self):
        return self.uuid

    def fq_name(self, uuid=None):
        if not getattr(self, 'fqname', None):
            if not uuid:
                assert False, 'uuid has to be specified'
            quantum_h = self.connections.get_network_h()
            router_obj = quantum_h.show_router(router_id=uuid)
            self.fqname = router_obj['contrail:fq_name']
        return self.fqname

class LoadBalancer(Base):
    def create(self, name, lb_method='ROUND_ROBIN', protocol='HTTP',
               port=8000, subnet=None, members=[], vip_name=None, vip_ip=None, vip_subnet=None):
        quantum_h = self.connections.get_network_h()
        response = quantum_h.create_lb_pool(name, lb_method, protocol, subnet)
        self.uuid = response['id']
        try:
            self.create_lb_members(members, port, self.uuid)
        except:
#            self.delete_lb_members(self.get_lb_members(self.uuid))
#            self.delete(self.uuid)
#            return None
             pass
        if vip_name:
            if not vip_subnet:
                vip_subnet = subnet
            self.create_vip(vip_name, vip_subnet, self.uuid, protocol, port, vip_ip)
        return self.uuid

    def delete(self, uuid):
        quantum_h = self.connections.get_network_h()
        quantum_h.delete_lb_pool(uuid)

    def get_lb_members(self, uuid):
        quantum_h = self.connections.get_network_h()
        return [x['id'] for x in quantum_h.list_lb_members(pool_id=uuid, fields='id')]

    def create_lb_members(self, members, port, pool_id):
        quantum_h = self.connections.get_network_h()
        member_ids = list()
        for member in members:
            obj = quantum_h.create_lb_member(member, port, pool_id)
            member_ids.append(obj['id'])
        return member_ids

    def delete_lb_members(self, members):
        quantum_h = self.connections.get_network_h()
        for member in members:
            quantum_h.delete_lb_member(member)

    def get_lb_member_ip(self, member):
        quantum_h = self.connections.get_network_h()
        return quantum_h.show_lb_member(member)['address']

    def create_vip(self, name, subnet, pool_id, protocol='HTTP', port=8000, vip_ip=None):
        quantum_h = self.connections.get_network_h()
        return quantum_h.create_vip(name, protocol, port, subnet, pool_id, vip_ip)['id']

    def delete_vip(self, uuid=None, name=None):
        quantum_h = self.connections.get_network_h()
        if not uuid:
            if name:
                uuid = quantum_h.list_vips(name=name, fields='id')[0]['id']
        if uuid:
            quantum_h.delete_vip(uuid)

    def get_vip_ip(self, uuid=None, name=None):
        quantum_h = self.connections.get_network_h()
        if uuid:
            return quantum_h.list_vips(id=uuid, fields='address')[0]['address']
        if not name:
            return None
        return quantum_h.list_vips(name=name, fields='address')[0]['address']

    def get_vip_id(self, name):
        quantum_h = self.connections.get_network_h()
        return quantum_h.list_vips(name=name, fields='id')[0]['id']

    def get_vip_port_id(self, uuid):
        quantum_h = self.connections.get_network_h()
        return quantum_h.list_vips(id=uuid, fields='port_id')[0]['port_id']

    def get_vip_subnet_id(self, uuid):
        quantum_h = self.connections.get_network_h()
        return quantum_h.show_vip(uuid, fields='subnet_id')['subnet_id']

    def get_pool_subnet_id(self, uuid):
        quantum_h = self.connections.get_network_h()
        return quantum_h.get_lb_pool(uuid, fields='subnet_id')['pool']['subnet_id']

    def uuid(self):
        return self.uuid

    def fq_name(self, uuid=None):
        if not getattr(self, 'fqname', None):
            if not uuid:
                assert False, 'uuid has to be specified'
            quantum_h = self.connections.get_network_h()
            obj = quantum_h.get_lb_pool(uuid)['pool']
            self.fqname = self.connections.get_project_fq_name() + [obj['name']]
        return self.fqname
