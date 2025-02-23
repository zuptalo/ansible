# Generate SSH key for ansible

```shell
ssh-keygen -f ~/.ssh/ansible -N ''
```

---

# Vagrant

- Start test VMs

```shell
vagrant up
```

- Suspend test VMs

```shell
vagrant suspend
```

- Resume test VMs

```shell
vagrant resume
```

- Destroy test VMs

```shell
vagrant destroy -f
```

---

# Ansible

---

- First lets see if we can ping all the hosts after vagrant up is finished

```shell
ansible all -m ping -u vagrant
```

- Now lets bootstrap all the hosts in inventory by updating everything to latest and setting up the ansible as a user on all

```shell
ansible-playbook bootstrap.yml -u vagrant
```

- Now that we have the hosts bootstrapped, lets set the site up

```shell
ansible-playbook site.yml
```

---

# Sample Ansible Commands

- Check connection to all the hosts in inventory

```shell
ansible all -m ping
```

- See all the servers defined in inventory

```shell
ansible all --list-hosts
```

- Gather all the facts about all the hosts in inventory

```shell
ansible all -m gather_facts
```

- Gather all the facts about a specified host in inventory

```shell
ansible all -m gather_facts --limit 10.0.1.150
```

- Update packages' index on all the hosts in inventory

```shell
ansible all -m package -a update_cache=true --become --ask-become-pass
```

- Install tmux on all the hosts in inventory

```shell
ansible all -m package -a name=tmux --become
```

- Update snapd package to latest version on all the hosts in inventory

```shell
ansible all -m package -a "name=snapd state=latest" --become
```

- Upgrade distro on db_servers the hosts in inventory

```shell
ansible db_servers -m apt -a "upgrade=dist" --become
```

---

# Python

- Create the virtual environment

```shell
python3 -m venv .venv
```

- Activate the virtual environment

```shell
source .venv/bin/activate
```

- Generate project context JSON to be used when chatting with AI

```shell
python ai.py
```