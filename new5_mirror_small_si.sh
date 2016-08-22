
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log

python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/mirror.yaml --create --tenant_count 1 --tenant_index_range 400:410
exit

ulimit -n 65535
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/small_si.yaml --delete --tenant_count 10 --tenant_index_range 400:410
exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/small_si.yaml --create --tenant_count 10 --tenant_index_range 400:410
while true;
do
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/small_si.yaml --traffic_only --tenant_index_range 400:410  --tenant_count 10
sleep 10
done
exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --delete --tenant_count 10 --tenant_index_range 600:610
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --create --tenant_count 10 --tenant_index_range 600:610
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/small_si.yaml --update --tenant_count 1 --tenant_index_range 600:610
#xit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.v6.yaml --create --tenant_count 1 --tenant_index_range 700:710
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml  --create_global
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml --delete --tenant_count 2 --tenant_index_range 600:710
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml --traffic_only --tenant_index_range 600:610  --tenant_count 1
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml --delete --tenant_count 1 --tenant_index_range 600:610
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml --create --tenant_count 1 --tenant_index_range 600:610
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml --traffic_only --tenant_index_range 600:610  --tenant_count 1
#exit
#python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.tor2.si.yaml --create --tenant_count 1 --tenant_index_range 600:610
#exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --delete --tenant_index_range 600:610  --tenant_count 10
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --create --tenant_index_range 600:610  --tenant_count 10

while true;
do
 python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/v4_si.yaml --traffic_only --tenant_index_range 600:610  --tenant_count 10
sleep 10
done


