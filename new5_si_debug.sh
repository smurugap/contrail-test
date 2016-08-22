
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

ulimit -n 65535
  python diagnostics/systemtest.full.debug.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --delete --tenant_count 1 --tenant_index_range 320:330
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --create --tenant_count 1 --tenant_index_range 320:330
  python diagnostics/systemtest.full.debug.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --delete --tenant_count 1 --tenant_index_range 320:330
exit
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v6.yaml --delete --tenant_count 1 --tenant_index_range 330:340
exit
while true;
do
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --delete --tenant_count 1 --tenant_index_range 320:330
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v6.yaml --delete --tenant_count 1 --tenant_index_range 330:340
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --create --tenant_count 1 --tenant_index_range 320:330
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v6.yaml --create --tenant_count 1 --tenant_index_range 330:340
  
   python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v4.yaml --traffic_only --tenant_index_range 320:330  --tenant_count 1 --loop_count 10
   python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.si.v6.yaml --traffic_only --tenant_index_range 330:340  --tenant_count 1 --loop_count 10
sleep 10
done


