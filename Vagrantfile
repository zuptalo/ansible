Vagrant.configure("2") do |config|
  # Ubuntu server 1
  config.vm.define "ubuntu1" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu1"
    ubuntu.vm.network "public_network", ip: "10.0.1.150", bridge: "en0: Wi-Fi (AirPort)"

    ubuntu.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        mkdir -p /home/vagrant/.ssh
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
        chmod 700 /home/vagrant/.ssh
        chmod 600 /home/vagrant/.ssh/authorized_keys
        chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end

    ubuntu.vm.provider "virtualbox" do |vb|
      vb.name = "Ubuntu1 Ansible Node"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

  # Ubuntu server 2
  config.vm.define "ubuntu2" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu2"
    ubuntu.vm.network "public_network", ip: "10.0.1.151", bridge: "en0: Wi-Fi (AirPort)"

    ubuntu.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        mkdir -p /home/vagrant/.ssh
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
        chmod 700 /home/vagrant/.ssh
        chmod 600 /home/vagrant/.ssh/authorized_keys
        chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end

    ubuntu.vm.provider "virtualbox" do |vb|
      vb.name = "Ubuntu2 Ansible Node"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

  # Ubuntu server 3
  config.vm.define "ubuntu3" do |ubuntu|
    ubuntu.vm.box = "ubuntu/focal64"
    ubuntu.vm.hostname = "ubuntu3"
    ubuntu.vm.network "public_network", ip: "10.0.1.152", bridge: "en0: Wi-Fi (AirPort)"

    ubuntu.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        mkdir -p /home/vagrant/.ssh
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
        chmod 700 /home/vagrant/.ssh
        chmod 600 /home/vagrant/.ssh/authorized_keys
        chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end

    ubuntu.vm.provider "virtualbox" do |vb|
      vb.name = "Ubuntu3 Ansible Node"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

  # CentOS server
  config.vm.define "centos" do |centos|
    centos.vm.box = "generic/centos9s"
    centos.vm.hostname = "centos"
    centos.vm.network "public_network", ip: "10.0.1.153", bridge: "en0: Wi-Fi (AirPort)"

    centos.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        # Update system and install Python 3
        dnf install -y python3

        mkdir -p /home/vagrant/.ssh
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
        chmod 700 /home/vagrant/.ssh
        chmod 600 /home/vagrant/.ssh/authorized_keys
        chown -R vagrant:vagrant /home/vagrant/.ssh
      SHELL
    end

    centos.vm.provider "virtualbox" do |vb|
      vb.name = "CentOS Ansible Node"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end
end
