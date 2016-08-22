
export LC_ALL=C
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./:./vnc_api:./cfgm_common:/usr/lib/python2.7/dist-packages/
rm logs/tor-scale.log.log


python diagnostics/systemtest.full.py --global_yaml_config_file diagnostics/csol1.global.yaml --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_name=ALL
