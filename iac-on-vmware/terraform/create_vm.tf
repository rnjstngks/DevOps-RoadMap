resource "vsphere_virtual_machine" "test_vm" {
  name             = "<가상머신의 이름>"
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
        linux_options {
            host_name = "<가상머신의 호스트명>"
            domain = "<가상머신의 도메인 명>"
        }
        network_interface {
            ipv4_address = "<가상머신의 IP>"
            ipv4_netmask = 24
      }
      ipv4_gateway = "<사용되는 네트워크 어댑터의 게이트웨이 주소>"
    }
  }
}