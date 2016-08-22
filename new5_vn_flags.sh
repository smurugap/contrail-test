
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log
rm ping_result_symantec.Tenant.175.txt

ulimit -n 65535

if [ "$1" = 'feature_ping_only' ];
then
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.vn_flags.yaml --create --tenant_count 1 --tenant_index_range 175:180
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.vn_flags.yaml --traffic_only --tenant_index_range 175:180  --tenant_count 1 --loop_count 5 --feature_ping_only
exit
fi

while true;
do
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.vn_flags.yaml --delete --tenant_count 1 --tenant_index_range 175:180
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.vn_flags.yaml --create --tenant_count 1 --tenant_index_range 175:180
for i in {1..10}
do
  python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --global_yaml_config_file diagnostics/csol1.global.yaml --yaml_config_file diagnostics/symantec.tor2.vn_flags.yaml --traffic_only --tenant_index_range 175:180  --tenant_count 1 --loop_count 5
sleep 10
done
done

