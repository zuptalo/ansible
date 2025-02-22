# Vagrant

### Start test VMs
```shell
vagrant up
```

### Destroy test VMs
```shell
vagrant destroy -f
```

---

# Ansible (some sample commands)

---

### Check connection to all the hosts in inventory

```shell
ansible all -m ping
```

### See all the servers defined in inventory

```shell
ansible all --list-hosts
```

### Gather all the facts about all the hosts in inventory

```shell
ansible all -m gather_facts
```

### Gather all the facts about a specified host in inventory

```shell
ansible all -m gather_facts --limit 10.0.1.240
```

### Update apt cache on all the hosts in inventory

```shell
ansible all -m apt -a update_cache=true --become --ask-become-pass
```

### Install tmux on all the hosts in inventory

```shell
ansible all -m apt -a name=tmux --become
```

### Update snapd package to latest version on all the hosts in inventory

```shell
ansible all -m apt -a "name=snapd state=latest" --become
```

### Upgrade distro on all the hosts in inventory

```shell
ansible all -m apt -a "upgrade=dist" --become
```

### Install apache server on all the hosts in inventory

```shell
ansible-playbook install_apache.yml
```

### Remove apache server from all the hosts in inventory

```shell
ansible-playbook remove_apache.yml
```