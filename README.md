# ansible
My Ansible Playground


# Check connection to all the hosts in inventory
```shell
ansible all -m ping
```

# See all the servers defined in inventory
```shell
ansible all --list-hosts
```

# Get all the facts about all the hosts in inventory
```shell
ansible all -m gather_facts
```

# Get all the facts about a specified host in inventory
```shell
ansible all -m gather_facts --limit 10.0.1.240
```