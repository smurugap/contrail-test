
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailNetworkIpam(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, DISPLAY_NAME, IPAM_SUBNET_METHOD, NETWORK_IPAM_MGMT, NETWORK_IPAM_MGMT_IPAM_METHOD, NETWORK_IPAM_MGMT_IPAM_DNS_METHOD, NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS, NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME, NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME, NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE, NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES, NETWORK_IPAM_MGMT_CIDR_BLOCK, NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX, NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN, NETWORK_IPAM_MGMT_HOST_ROUTES, NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX, NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP, NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, IPAM_SUBNETS, IPAM_SUBNETS_SUBNETS, IPAM_SUBNETS_SUBNETS_SUBNET, IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX, IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN, IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY, IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS, IPAM_SUBNETS_SUBNETS_SUBNET_UUID, IPAM_SUBNETS_SUBNETS_ENABLE_DHCP, IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS, IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START, IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END, IPAM_SUBNETS_SUBNETS_ADDR_FROM_START, IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME, IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE, IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES, IPAM_SUBNETS_SUBNETS_HOST_ROUTES, IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX, IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP, IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE, IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE, IPAM_SUBNETS_SUBNETS_SUBNET_NAME, IPAM_SUBNETS_SUBNETS_ALLOC_UNIT, VIRTUAL_DNS_REFS, PROJECT
    ) = (
        'name', 'fq_name', 'display_name', 'ipam_subnet_method', 'network_ipam_mgmt', 'network_ipam_mgmt_ipam_method', 'network_ipam_mgmt_ipam_dns_method', 'network_ipam_mgmt_ipam_dns_server', 'network_ipam_mgmt_ipam_dns_server_tenant_dns_server_address', 'network_ipam_mgmt_ipam_dns_server_tenant_dns_server_address_ip_address', 'network_ipam_mgmt_ipam_dns_server_virtual_dns_server_name', 'network_ipam_mgmt_dhcp_option_list', 'network_ipam_mgmt_dhcp_option_list_dhcp_option', 'network_ipam_mgmt_dhcp_option_list_dhcp_option_dhcp_option_name', 'network_ipam_mgmt_dhcp_option_list_dhcp_option_dhcp_option_value', 'network_ipam_mgmt_dhcp_option_list_dhcp_option_dhcp_option_value_bytes', 'network_ipam_mgmt_cidr_block', 'network_ipam_mgmt_cidr_block_ip_prefix', 'network_ipam_mgmt_cidr_block_ip_prefix_len', 'network_ipam_mgmt_host_routes', 'network_ipam_mgmt_host_routes_route', 'network_ipam_mgmt_host_routes_route_prefix', 'network_ipam_mgmt_host_routes_route_next_hop', 'network_ipam_mgmt_host_routes_route_next_hop_type', 'network_ipam_mgmt_host_routes_route_community_attributes', 'network_ipam_mgmt_host_routes_route_community_attributes_community_attribute', 'ipam_subnets', 'ipam_subnets_subnets', 'ipam_subnets_subnets_subnet', 'ipam_subnets_subnets_subnet_ip_prefix', 'ipam_subnets_subnets_subnet_ip_prefix_len', 'ipam_subnets_subnets_default_gateway', 'ipam_subnets_subnets_dns_server_address', 'ipam_subnets_subnets_subnet_uuid', 'ipam_subnets_subnets_enable_dhcp', 'ipam_subnets_subnets_dns_nameservers', 'ipam_subnets_subnets_allocation_pools', 'ipam_subnets_subnets_allocation_pools_start', 'ipam_subnets_subnets_allocation_pools_end', 'ipam_subnets_subnets_addr_from_start', 'ipam_subnets_subnets_dhcp_option_list', 'ipam_subnets_subnets_dhcp_option_list_dhcp_option', 'ipam_subnets_subnets_dhcp_option_list_dhcp_option_dhcp_option_name', 'ipam_subnets_subnets_dhcp_option_list_dhcp_option_dhcp_option_value', 'ipam_subnets_subnets_dhcp_option_list_dhcp_option_dhcp_option_value_bytes', 'ipam_subnets_subnets_host_routes', 'ipam_subnets_subnets_host_routes_route', 'ipam_subnets_subnets_host_routes_route_prefix', 'ipam_subnets_subnets_host_routes_route_next_hop', 'ipam_subnets_subnets_host_routes_route_next_hop_type', 'ipam_subnets_subnets_host_routes_route_community_attributes', 'ipam_subnets_subnets_host_routes_route_community_attributes_community_attribute', 'ipam_subnets_subnets_subnet_name', 'ipam_subnets_subnets_alloc_unit', 'virtual_dns_refs', 'project'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        IPAM_SUBNET_METHOD: properties.Schema(
            properties.Schema.STRING,
            _('IPAM_SUBNET_METHOD.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_IPAM_MGMT: properties.Schema(
            properties.Schema.MAP,
            _('NETWORK_IPAM_MGMT.'),
            update_allowed=True,
            required=False,
            schema={
                NETWORK_IPAM_MGMT_IPAM_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('NETWORK_IPAM_MGMT_IPAM_METHOD.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'dhcp', u'fixed']),
                    ],
                ),
                NETWORK_IPAM_MGMT_IPAM_DNS_METHOD: properties.Schema(
                    properties.Schema.STRING,
                    _('NETWORK_IPAM_MGMT_IPAM_DNS_METHOD.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.AllowedValues([u'none', u'default-dns-server', u'tenant-dns-server', u'virtual-dns-server']),
                    ],
                ),
                NETWORK_IPAM_MGMT_IPAM_DNS_SERVER: properties.Schema(
                    properties.Schema.MAP,
                    _('NETWORK_IPAM_MGMT_IPAM_DNS_SERVER.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS: properties.Schema(
                            properties.Schema.MAP,
                            _('NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS.'),
                            update_allowed=True,
                            required=False,
                            schema={
                                NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS: properties.Schema(
                                    properties.Schema.LIST,
                                    _('NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        ),
                        NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME: properties.Schema(
                            properties.Schema.STRING,
                            _('NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                NETWORK_IPAM_MGMT_DHCP_OPTION_LIST: properties.Schema(
                    properties.Schema.MAP,
                    _('NETWORK_IPAM_MGMT_DHCP_OPTION_LIST.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION: properties.Schema(
                            properties.Schema.LIST,
                            _('NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION.'),
                            update_allowed=True,
                            required=False,
                            schema=properties.Schema(
                                properties.Schema.MAP,
                                schema={
                                    NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            )
                        ),
                    }
                ),
                NETWORK_IPAM_MGMT_CIDR_BLOCK: properties.Schema(
                    properties.Schema.MAP,
                    _('NETWORK_IPAM_MGMT_CIDR_BLOCK.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX: properties.Schema(
                            properties.Schema.STRING,
                            _('NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX.'),
                            update_allowed=True,
                            required=False,
                        ),
                        NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN: properties.Schema(
                            properties.Schema.INTEGER,
                            _('NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN.'),
                            update_allowed=True,
                            required=False,
                        ),
                    }
                ),
                NETWORK_IPAM_MGMT_HOST_ROUTES: properties.Schema(
                    properties.Schema.MAP,
                    _('NETWORK_IPAM_MGMT_HOST_ROUTES.'),
                    update_allowed=True,
                    required=False,
                    schema={
                        NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE: properties.Schema(
                            properties.Schema.LIST,
                            _('NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE.'),
                            update_allowed=True,
                            required=False,
                            schema=properties.Schema(
                                properties.Schema.MAP,
                                schema={
                                    NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                        properties.Schema.STRING,
                                        _('NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                        update_allowed=True,
                                        required=False,
                                        constraints=[
                                            constraints.AllowedValues([u'service-instance', u'ip-address']),
                                        ],
                                    ),
                                    NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                        properties.Schema.MAP,
                                        _('NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                        update_allowed=True,
                                        required=False,
                                        schema={
                                            NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                properties.Schema.LIST,
                                                _('NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
                                                update_allowed=True,
                                                required=False,
                                            ),
                                        }
                                    ),
                                }
                            )
                        ),
                    }
                ),
            }
        ),
        IPAM_SUBNETS: properties.Schema(
            properties.Schema.MAP,
            _('IPAM_SUBNETS.'),
            update_allowed=True,
            required=False,
            schema={
                IPAM_SUBNETS_SUBNETS: properties.Schema(
                    properties.Schema.LIST,
                    _('IPAM_SUBNETS_SUBNETS.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            IPAM_SUBNETS_SUBNETS_SUBNET: properties.Schema(
                                properties.Schema.MAP,
                                _('IPAM_SUBNETS_SUBNETS_SUBNET.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX: properties.Schema(
                                        properties.Schema.STRING,
                                        _('IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                    IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN: properties.Schema(
                                        properties.Schema.INTEGER,
                                        _('IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN.'),
                                        update_allowed=True,
                                        required=False,
                                    ),
                                }
                            ),
                            IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY: properties.Schema(
                                properties.Schema.STRING,
                                _('IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS: properties.Schema(
                                properties.Schema.STRING,
                                _('IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_SUBNET_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('IPAM_SUBNETS_SUBNETS_SUBNET_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_ENABLE_DHCP: properties.Schema(
                                properties.Schema.BOOLEAN,
                                _('IPAM_SUBNETS_SUBNETS_ENABLE_DHCP.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS: properties.Schema(
                                properties.Schema.LIST,
                                _('IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS: properties.Schema(
                                properties.Schema.LIST,
                                _('IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS.'),
                                update_allowed=True,
                                required=False,
                                schema=properties.Schema(
                                    properties.Schema.MAP,
                                    schema={
                                        IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START: properties.Schema(
                                            properties.Schema.STRING,
                                            _('IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                        IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END: properties.Schema(
                                            properties.Schema.STRING,
                                            _('IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END.'),
                                            update_allowed=True,
                                            required=False,
                                        ),
                                    }
                                )
                            ),
                            IPAM_SUBNETS_SUBNETS_ADDR_FROM_START: properties.Schema(
                                properties.Schema.BOOLEAN,
                                _('IPAM_SUBNETS_SUBNETS_ADDR_FROM_START.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST: properties.Schema(
                                properties.Schema.MAP,
                                _('IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION: properties.Schema(
                                        properties.Schema.LIST,
                                        _('IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION.'),
                                        update_allowed=True,
                                        required=False,
                                        schema=properties.Schema(
                                            properties.Schema.MAP,
                                            schema={
                                                IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                            }
                                        )
                                    ),
                                }
                            ),
                            IPAM_SUBNETS_SUBNETS_HOST_ROUTES: properties.Schema(
                                properties.Schema.MAP,
                                _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES.'),
                                update_allowed=True,
                                required=False,
                                schema={
                                    IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE: properties.Schema(
                                        properties.Schema.LIST,
                                        _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE.'),
                                        update_allowed=True,
                                        required=False,
                                        schema=properties.Schema(
                                            properties.Schema.MAP,
                                            schema={
                                                IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP.'),
                                                    update_allowed=True,
                                                    required=False,
                                                ),
                                                IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE: properties.Schema(
                                                    properties.Schema.STRING,
                                                    _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    constraints=[
                                                        constraints.AllowedValues([u'service-instance', u'ip-address']),
                                                    ],
                                                ),
                                                IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES: properties.Schema(
                                                    properties.Schema.MAP,
                                                    _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES.'),
                                                    update_allowed=True,
                                                    required=False,
                                                    schema={
                                                        IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE: properties.Schema(
                                                            properties.Schema.LIST,
                                                            _('IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE.'),
                                                            update_allowed=True,
                                                            required=False,
                                                        ),
                                                    }
                                                ),
                                            }
                                        )
                                    ),
                                }
                            ),
                            IPAM_SUBNETS_SUBNETS_SUBNET_NAME: properties.Schema(
                                properties.Schema.STRING,
                                _('IPAM_SUBNETS_SUBNETS_SUBNET_NAME.'),
                                update_allowed=True,
                                required=False,
                            ),
                            IPAM_SUBNETS_SUBNETS_ALLOC_UNIT: properties.Schema(
                                properties.Schema.INTEGER,
                                _('IPAM_SUBNETS_SUBNETS_ALLOC_UNIT.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        VIRTUAL_DNS_REFS: properties.Schema(
            properties.Schema.LIST,
            _('VIRTUAL_DNS_REFS.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        IPAM_SUBNET_METHOD: attributes.Schema(
            _('IPAM_SUBNET_METHOD.'),
        ),
        NETWORK_IPAM_MGMT: attributes.Schema(
            _('NETWORK_IPAM_MGMT.'),
        ),
        IPAM_SUBNETS: attributes.Schema(
            _('IPAM_SUBNETS.'),
        ),
        VIRTUAL_DNS_REFS: attributes.Schema(
            _('VIRTUAL_DNS_REFS.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT):
            try:
                parent_obj = self.vnc_lib().project_read(id=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except:
                parent_obj = None

        if parent_obj is None:
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None:
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.NetworkIpam(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.IPAM_SUBNET_METHOD) is not None:
            obj_0.set_ipam_subnet_method(self.properties.get(self.IPAM_SUBNET_METHOD))
        if self.properties.get(self.NETWORK_IPAM_MGMT) is not None:
            obj_1 = vnc_api.IpamType()
            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_METHOD) is not None:
                obj_1.set_ipam_method(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_METHOD))
            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_METHOD) is not None:
                obj_1.set_ipam_dns_method(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_METHOD))
            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER) is not None:
                obj_2 = vnc_api.IpamDnsAddressType()
                if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS) is not None:
                    obj_3 = vnc_api.IpAddressesType()
                    if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS) is not None:
                        for index_3 in range(len(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS))):
                            obj_3.add_ip_address(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS)[index_3])
                    obj_2.set_tenant_dns_server_address(obj_3)
                if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME) is not None:
                    obj_2.set_virtual_dns_server_name(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME))
                obj_1.set_ipam_dns_server(obj_2)
            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST) is not None:
                obj_2 = vnc_api.DhcpOptionsListType()
                if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                    for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION))):
                        obj_3 = vnc_api.DhcpOptionType()
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                            obj_3.set_dhcp_option_name(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                            obj_3.set_dhcp_option_value(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                            obj_3.set_dhcp_option_value_bytes(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                        obj_2.add_dhcp_option(obj_3)
                obj_1.set_dhcp_option_list(obj_2)
            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK) is not None:
                obj_2 = vnc_api.SubnetType()
                if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX) is not None:
                    obj_2.set_ip_prefix(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX))
                if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN) is not None:
                    obj_2.set_ip_prefix_len(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN))
                obj_1.set_cidr_block(obj_2)
            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES) is not None:
                obj_2 = vnc_api.RouteTableType()
                if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE) is not None:
                    for index_2 in range(len(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE))):
                        obj_3 = vnc_api.RouteType()
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX) is not None:
                            obj_3.set_prefix(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX))
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                            obj_3.set_next_hop(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP))
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                            obj_3.set_next_hop_type(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                        if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                            obj_4 = vnc_api.CommunityAttributes()
                            if self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                for index_4 in range(len(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                    obj_4.add_community_attribute(self.properties.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_4])
                            obj_3.set_community_attributes(obj_4)
                        obj_2.add_route(obj_3)
                obj_1.set_host_routes(obj_2)
            obj_0.set_network_ipam_mgmt(obj_1)
        if self.properties.get(self.IPAM_SUBNETS) is not None:
            obj_1 = vnc_api.IpamSubnets()
            if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS) is not None:
                for index_1 in range(len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS))):
                    obj_2 = vnc_api.IpamSubnetType()
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX))
                        if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN))
                        obj_2.set_subnet(obj_3)
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY) is not None:
                        obj_2.set_default_gateway(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY))
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS) is not None:
                        obj_2.set_dns_server_address(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS))
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_UUID) is not None:
                        obj_2.set_subnet_uuid(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_UUID))
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ENABLE_DHCP) is not None:
                        obj_2.set_enable_dhcp(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ENABLE_DHCP))
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS) is not None:
                        for index_2 in range(len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS))):
                            obj_2.add_dns_nameservers(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS)[index_2])
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS) is not None:
                        for index_2 in range(len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS))):
                            obj_3 = vnc_api.AllocationPoolType()
                            if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START) is not None:
                                obj_3.set_start(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START))
                            if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END) is not None:
                                obj_3.set_end(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END))
                            obj_2.add_allocation_pools(obj_3)
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ADDR_FROM_START) is not None:
                        obj_2.set_addr_from_start(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ADDR_FROM_START))
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST) is not None:
                        obj_3 = vnc_api.DhcpOptionsListType()
                        if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                            for index_3 in range(len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION))):
                                obj_4 = vnc_api.DhcpOptionType()
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                                    obj_4.set_dhcp_option_name(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                                    obj_4.set_dhcp_option_value(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                                    obj_4.set_dhcp_option_value_bytes(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                                obj_3.add_dhcp_option(obj_4)
                        obj_2.set_dhcp_option_list(obj_3)
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES) is not None:
                        obj_3 = vnc_api.RouteTableType()
                        if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE) is not None:
                            for index_3 in range(len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE))):
                                obj_4 = vnc_api.RouteType()
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                    obj_4.set_prefix(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX))
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                    obj_4.set_next_hop(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP))
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                    obj_4.set_next_hop_type(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                    obj_5 = vnc_api.CommunityAttributes()
                                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                        for index_5 in range(len(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                            obj_5.add_community_attribute(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                    obj_4.set_community_attributes(obj_5)
                                obj_3.add_route(obj_4)
                        obj_2.set_host_routes(obj_3)
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_NAME) is not None:
                        obj_2.set_subnet_name(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_NAME))
                    if self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOC_UNIT) is not None:
                        obj_2.set_alloc_unit(self.properties.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOC_UNIT))
                    obj_1.add_subnets(obj_2)
            obj_0.set_ipam_subnets(obj_1)

        # reference to virtual_DNS_refs
        if self.properties.get(self.VIRTUAL_DNS_REFS):
            for index_0 in range(len(self.properties.get(self.VIRTUAL_DNS_REFS))):
                try:
                    ref_obj = self.vnc_lib().virtual_DNS_read(
                        id=self.properties.get(self.VIRTUAL_DNS_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().virtual_DNS_read(
                        fq_name_str=self.properties.get(self.VIRTUAL_DNS_REFS)[index_0]
                    )
                obj_0.add_virtual_DNS(ref_obj)

        try:
            obj_uuid = super(ContrailNetworkIpam, self).resource_create(obj_0)
        except:
            raise Exception(_('network-ipam %s could not be created.') % self.name)

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().network_ipam_read(
                id=self.resource_id
            )
        except:
            raise Exception(_('network-ipam %s not found.') % self.name)

        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.IPAM_SUBNET_METHOD) is not None:
            obj_0.set_ipam_subnet_method(prop_diff.get(self.IPAM_SUBNET_METHOD))
        if prop_diff.get(self.NETWORK_IPAM_MGMT) is not None:
            obj_1 = vnc_api.IpamType()
            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_METHOD) is not None:
                obj_1.set_ipam_method(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_METHOD))
            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_METHOD) is not None:
                obj_1.set_ipam_dns_method(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_METHOD))
            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER) is not None:
                obj_2 = vnc_api.IpamDnsAddressType()
                if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS) is not None:
                    obj_3 = vnc_api.IpAddressesType()
                    if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS) is not None:
                        for index_3 in range(len(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS))):
                            obj_3.add_ip_address(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_TENANT_DNS_SERVER_ADDRESS_IP_ADDRESS)[index_3])
                    obj_2.set_tenant_dns_server_address(obj_3)
                if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME) is not None:
                    obj_2.set_virtual_dns_server_name(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER, {}).get(self.NETWORK_IPAM_MGMT_IPAM_DNS_SERVER_VIRTUAL_DNS_SERVER_NAME))
                obj_1.set_ipam_dns_server(obj_2)
            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST) is not None:
                obj_2 = vnc_api.DhcpOptionsListType()
                if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                    for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION))):
                        obj_3 = vnc_api.DhcpOptionType()
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                            obj_3.set_dhcp_option_name(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                            obj_3.set_dhcp_option_value(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                            obj_3.set_dhcp_option_value_bytes(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST, {}).get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_2].get(self.NETWORK_IPAM_MGMT_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                        obj_2.add_dhcp_option(obj_3)
                obj_1.set_dhcp_option_list(obj_2)
            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK) is not None:
                obj_2 = vnc_api.SubnetType()
                if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX) is not None:
                    obj_2.set_ip_prefix(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX))
                if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN) is not None:
                    obj_2.set_ip_prefix_len(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK, {}).get(self.NETWORK_IPAM_MGMT_CIDR_BLOCK_IP_PREFIX_LEN))
                obj_1.set_cidr_block(obj_2)
            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES) is not None:
                obj_2 = vnc_api.RouteTableType()
                if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE) is not None:
                    for index_2 in range(len(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE))):
                        obj_3 = vnc_api.RouteType()
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX) is not None:
                            obj_3.set_prefix(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_PREFIX))
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                            obj_3.set_next_hop(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP))
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                            obj_3.set_next_hop_type(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                        if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                            obj_4 = vnc_api.CommunityAttributes()
                            if prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                for index_4 in range(len(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                    obj_4.add_community_attribute(prop_diff.get(self.NETWORK_IPAM_MGMT, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE, {})[index_2].get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.NETWORK_IPAM_MGMT_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_4])
                            obj_3.set_community_attributes(obj_4)
                        obj_2.add_route(obj_3)
                obj_1.set_host_routes(obj_2)
            obj_0.set_network_ipam_mgmt(obj_1)
        if prop_diff.get(self.IPAM_SUBNETS) is not None:
            obj_1 = vnc_api.IpamSubnets()
            if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS) is not None:
                for index_1 in range(len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS))):
                    obj_2 = vnc_api.IpamSubnetType()
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET) is not None:
                        obj_3 = vnc_api.SubnetType()
                        if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX) is not None:
                            obj_3.set_ip_prefix(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX))
                        if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN) is not None:
                            obj_3.set_ip_prefix_len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET, {}).get(self.IPAM_SUBNETS_SUBNETS_SUBNET_IP_PREFIX_LEN))
                        obj_2.set_subnet(obj_3)
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY) is not None:
                        obj_2.set_default_gateway(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DEFAULT_GATEWAY))
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS) is not None:
                        obj_2.set_dns_server_address(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_SERVER_ADDRESS))
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_UUID) is not None:
                        obj_2.set_subnet_uuid(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_UUID))
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ENABLE_DHCP) is not None:
                        obj_2.set_enable_dhcp(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ENABLE_DHCP))
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS) is not None:
                        for index_2 in range(len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS))):
                            obj_2.add_dns_nameservers(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DNS_NAMESERVERS)[index_2])
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS) is not None:
                        for index_2 in range(len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS))):
                            obj_3 = vnc_api.AllocationPoolType()
                            if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START) is not None:
                                obj_3.set_start(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_START))
                            if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END) is not None:
                                obj_3.set_end(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS, {})[index_2].get(self.IPAM_SUBNETS_SUBNETS_ALLOCATION_POOLS_END))
                            obj_2.add_allocation_pools(obj_3)
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ADDR_FROM_START) is not None:
                        obj_2.set_addr_from_start(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ADDR_FROM_START))
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST) is not None:
                        obj_3 = vnc_api.DhcpOptionsListType()
                        if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION) is not None:
                            for index_3 in range(len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION))):
                                obj_4 = vnc_api.DhcpOptionType()
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME) is not None:
                                    obj_4.set_dhcp_option_name(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_NAME))
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE) is not None:
                                    obj_4.set_dhcp_option_value(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE))
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES) is not None:
                                    obj_4.set_dhcp_option_value_bytes(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST, {}).get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_DHCP_OPTION_LIST_DHCP_OPTION_DHCP_OPTION_VALUE_BYTES))
                                obj_3.add_dhcp_option(obj_4)
                        obj_2.set_dhcp_option_list(obj_3)
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES) is not None:
                        obj_3 = vnc_api.RouteTableType()
                        if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE) is not None:
                            for index_3 in range(len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE))):
                                obj_4 = vnc_api.RouteType()
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX) is not None:
                                    obj_4.set_prefix(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_PREFIX))
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP) is not None:
                                    obj_4.set_next_hop(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP))
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE) is not None:
                                    obj_4.set_next_hop_type(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_NEXT_HOP_TYPE))
                                if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES) is not None:
                                    obj_5 = vnc_api.CommunityAttributes()
                                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE) is not None:
                                        for index_5 in range(len(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE))):
                                            obj_5.add_community_attribute(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE, {})[index_3].get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES, {}).get(self.IPAM_SUBNETS_SUBNETS_HOST_ROUTES_ROUTE_COMMUNITY_ATTRIBUTES_COMMUNITY_ATTRIBUTE)[index_5])
                                    obj_4.set_community_attributes(obj_5)
                                obj_3.add_route(obj_4)
                        obj_2.set_host_routes(obj_3)
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_NAME) is not None:
                        obj_2.set_subnet_name(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_SUBNET_NAME))
                    if prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOC_UNIT) is not None:
                        obj_2.set_alloc_unit(prop_diff.get(self.IPAM_SUBNETS, {}).get(self.IPAM_SUBNETS_SUBNETS, {})[index_1].get(self.IPAM_SUBNETS_SUBNETS_ALLOC_UNIT))
                    obj_1.add_subnets(obj_2)
            obj_0.set_ipam_subnets(obj_1)

        # reference to virtual_DNS_refs
        ref_obj_list = []
        if self.VIRTUAL_DNS_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.VIRTUAL_DNS_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().virtual_DNS_read(
                        id=prop_diff.get(self.VIRTUAL_DNS_REFS)[index_0]
                    )
                except:
                    ref_obj = self.vnc_lib().virtual_DNS_read(
                        fq_name_str=prop_diff.get(self.VIRTUAL_DNS_REFS)[index_0]
                    )
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_virtual_DNS_list(ref_obj_list)
            # End: reference to virtual_DNS_refs

        try:
            self.vnc_lib().network_ipam_update(obj_0)
        except:
            raise Exception(_('network-ipam %s could not be updated.') % self.name)

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().network_ipam_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('network_ipam %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().network_ipam_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::NetworkIpam': ContrailNetworkIpam,
    }
