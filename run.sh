
. /etc/contrail/openstackrc
export PYTHONPATH=./fixtures:./scripts:./
rm logs/tor-scale.log.log

# following params used from yaml if not mentioned thru CLI.
# --tenant_count 
# --tenant_index_range default value: 0-64K
# --tenant_name_prefix

#1.create and delete global configuration
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --create_global

exit
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete_global

#2.create tenant with specific name.to be safe tenant_name should be in the format tenant_name_prefix + "." + random_int
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --create --tenant_name=symantec.5

#3.create tenants as per yaml configuration
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --create 

#4.create n tenants as per yaml.index starts from 0.
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --create --tenant_count n 

#5.create n tenants as per yaml.index starts from 50.
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --create --tenant_count n --tenant_index_range 50 

#6.create n tenants as per yaml.index will be random
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --create --tenant_count n --tenant_index_range 50:100 --tenant_index_random

#7.delete all tenants except standard tenants like admin,invisible
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_name=ALL

#8.delete tenant with specific name.to be safe tenant_name should be in the format tenant_name_prefix + "." + random_int
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_name=symantec.5

#9.delete tenants as per yaml configuration
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete

#10.delete n tenants as per yaml.index starts from 0.
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_count n

#11.delete n tenants as per yaml.index starts from 0.
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_count n --tenant_index_random

#12.delete n tenants as per yaml.index starts from 50.
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_count n --tenant_index_range 50

#12.create n tenants as per yaml.index will be random
python diagnostics/systemtest.full.py --ini_file diagnostics/global_params.ini --yaml_config_file diagnostics/symantec.full.yaml --delete --tenant_count n --tenant_index_range 50:100 --tenant_index_random

