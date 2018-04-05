CONTRAIL_SERVICES_CONTAINER_MAP = {
    'api-server': ['config_api', 'contrail-config-api'],
    'schema': ['config_schema', 'contrail-schema-transformer'],
    'svc-monitor': ['config_svcmonitor', 'contrail-svc-monitor'],
    'device-manager': ['config_devicemgr', 'contrail-devicemgr'],
    'control': ['control_control', 'contrail-control'],
    'dns': ['control_dns', 'contrail-dns'],
    'named': ['control_named', 'contrail-named'],
    'analytics-api': ['analytics_api', 'contrail-analytics-api'],
    'alarm-gen': ['analytics_alarm-gen', 'contrail-alarm-gen'],
    'query-engine': ['analytics_query-engine', 'contrail-query-engine'],
    'topology': ['analytics_topology', 'contrail-topology'],
    'collector': ['analytics_collector', 'contrail-collector'],
    'snmp-collector': ['analytics_snmp-collector', 'contrail-snmp-collector'],
    'agent': ['contrail-agent', 'vrouter-agent', 'contrail-vrouter-agent'],
    'webui': ['webui_web', 'contrail-webui'],
    'webui-middleware': ['webui_job', 'contrail-webui-middleware'],
    'config-rabbitmq': ['configdatabase_rabbitmq', 'rabbitmq'],
    'config-zookeeper': ['configdatabase_zookeeper',
                         'contrail-config-zookeeper'],
    'config-cassandra': ['configdatabase_cassandra', 'contrail-configdb'],
    'analytics-kafka': ['analyticsdatabase_kafka', 'contrail-kafka'],
    'analytics-zookeeper': ['analyticsdatabase_zookeeper',
                            'contrail-analytics-zookeeper'],
    'analytics-cassandra': ['analyticsdatabase_cassandra',
                            'contrail-analyticsdb'],
    'nova': ['nova_api', 'nova-api-osapi'],
    'nova-compute': ['nova_compute', 'nova-compute'],
    'nova-conductor': ['nova_conductor', 'nova-conductor'],
    'nova-scheduler': ['nova_scheduler', 'nova-scheduler'],
    'glance': ['glance_api', 'glance-api'],
    'rabbitmq': ['rabbitmq'],
    'haproxy': ['haproxy'],
    'keystone': ['keystone-api', 'keystone'],
    'neutron': ['neutron', 'neutron-server'],
    'mysql': ['mariadb'],
    'redis': ['webui_redis', 'webui-redis'],
    'vrouter-nodemgr': ['vrouter_nodemgr', 'vrouter-nodemgr'],
    'config-nodemgr': ['config_nodemgr', 'config-nodemgr'],
    'analytics-nodemgr': ['analytics_nodemgr', 'analytics-nodemgr'],
    'control-nodemgr': ['control_nodemgr', 'control-nodemgr'],
    'analyticsdb-nodemgr': ['analyticsdatabase_nodemgr',
                            'analyticsdatabase-nodemgr'],
    'contrail-kube-manager': ['contrail-kube-manager', 'kubemanager'],
}

CONTRAIL_PODS_SERVICES_MAP = {
    'vrouter' : ['vrouter-nodemgr', 'agent'],
    'control' : ['control-nodemgr',
                 'control',
                 'named',
                 'dns'],
    'config' : ['config-nodemgr',
                'api-server',
                'schema',
                'svc-monitor',
                'device-manager'],
    'config-database' : ['config-cassandra',
                         'config-zookeeper',
                         'config-rabbitmq'],
    'analytics' : ['analytics-nodemgr',
                   'analytics-api',
                   'collector',
                   'query-engine',
                   'alarm-gen',
                   'snmp-collector',
                   'topology'],
    'analytics-database' : ['analytics-cassandra',
                            'analyticsdb-nodemgr',
                            'analytics-zookeeper',
                            'analytics-kafka'],
    'webui' : ['webui', 'webui-middleware', 'redis'],
    'kubernetes' : ['contrail-kube-manager'],
}

BackupImplementedServices = ["schema",
                             "svc-monitor",
                             "device-manager",
                             "contrail-kube-manager"]
ServiceHttpPortMap = {
    "agent" : 8085,
    "control" : 8083,
    "collector" : 8089,
    "query-engine" : 8091,
    "analytics-api" : 8090,
    "dns" : 8092,
    "api-server" : 8084,
    "schema" : 8087,
    "svc-monitor" : 8088,
    "device-manager" : 8096,
    "analytics-nodemgr" : 8104,
    "vrouter-nodemgr" : 8102,
    "control-nodemgr" : 8101,
    "analyticsdb-nodemgr" : 8103,
    "config-nodemgr" : 8100,
    "alarm-gen" : 5995,
    "snmp-collector" : 5920,
    "topology" : 5921,
    "contrail-kube-manager" : 8108,
}

