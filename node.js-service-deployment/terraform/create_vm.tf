resource "vsphere_virtual_machine" "test_vm" {
  name             = "test-node.js"
  resource_pool_id = data.vsphere_compute_cluster.cluster.resource_pool_id
  datastore_id     = data.vsphere_datastore.datastore.id
  num_cpus         = 2
  memory           = 4096
  guest_id         = "ubuntu64Guest"
  network_interface {
    network_id = data.vsphere_network.network_91.id
  }
  disk {
    label = "disk"
    size  = 300
  }
  clone {
    template_uuid = data.vsphere_virtual_machine.template.id
    customize {
      linux_options { # Linux 운영 체제의 사용자 정의와 관련
        host_name = "test-node"
        domain    = "smrc.klab-a"
      }
      network_interface {
        ipv4_address = "10.10.91.4"
        ipv4_netmask = 24
      }
      ipv4_gateway    = "10.10.91.1"
      dns_server_list = ["10.10.92.201"] # 리스트 형태로 해주어야 IP로 입력 가능
    }
  }

  provisioner "remote-exec" {

    connection { # connection 해당 옵션이 inline 보다 앞에와야지 ssh 접속이 원활하게 됩니다.
      type     = "ssh"
      user     = "root"
      password = "1234"
      host     = "10.10.91.4"
    }
    
    inline = [
      "mkdir -p /root/.ssh",
      "echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP57+TY2n0a0bcZqZ0I4VfD2lsKSHpcLNWW+bHWPlhYq han@S2300289' >> /root/.ssh/authorized_keys",
      "chmod 600 /root/.ssh/authorized_keys",
      "chmod 700 /root/.ssh"
    ]
  }
}
