resource "vsphere_virtual_machine" "test_vm" {
  name             = "automated-db-backups"
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
            host_name = "automated-db-backups"
            domain = "smrc.klab-a"
        }
        network_interface {
            ipv4_address = "10.10.99.7"
            ipv4_netmask = 24
      }
      ipv4_gateway = "10.10.99.1"
    }
  }
}
