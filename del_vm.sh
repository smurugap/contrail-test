nova list --all-tenants | awk -F \| '{print $2}' | xargs nova delete 
