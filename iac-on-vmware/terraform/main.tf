# provider 정의
provider "vsphere" {
  user           = "<vCenter ID>"
  password       = "<vCenter PW>"
  vsphere_server = "<vCenter Domain>"

  # SSL 인증서 무시
  allow_unverified_ssl = true
}

# 데이터 소스 정의 시작

# 데이터센터 이름 정의
data "vsphere_datacenter" "datacenter" {
  name = "<가상머신을 생성할 데이터센터 이름>"
}

# 데이터스토어 이름 정의
data "vsphere_datastore" "datastore" {
  name          = "<가상머신을 생성할 데이터스토어 이름>"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 클러스터 이름 정의
data "vsphere_compute_cluster" "cluster" {
  name          = "<가상머신을 생성할 클러스터 이름>"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 분산스위치 정의
data "vsphere_distributed_virtual_switch" "distributed_switch" {
  name          = "COMM-CL01-vDS"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 네트워크 어댑터 정의
data "vsphere_network" "network_91" {
  name          = "<가상머신 생성할 때 사용할 네트워크 어댑터 이름>"
  datacenter_id = data.vsphere_datacenter.datacenter.id
#   filter {
#     network_type = "Network"
#   }
}

# 가상머신 생성을 위한 템플릿 지정
data "vsphere_virtual_machine" "template" {
  name          = "<가상머신을 생성할 때 사용되는 템플릿 이름>"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}
