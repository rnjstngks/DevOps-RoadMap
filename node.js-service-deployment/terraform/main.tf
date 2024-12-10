# provider 정의
provider "vsphere" {
  user           = "<vCenter 사용자>"
  password       = "<vCenter 사용자의 패스워드>"
  vsphere_server = "<vCenter 주소>"

  # SSL 인증서 무시
  allow_unverified_ssl = true
}

# 데이터 소스 정의 시작

# 데이터센터 이름 정의
data "vsphere_datacenter" "datacenter" {
  name = "Datacenter"
}

# 데이터스토어 이름 정의
data "vsphere_datastore" "datastore" {
  name          = "COMM_vsanDatastore"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 클러스터 이름 정의
data "vsphere_compute_cluster" "cluster" {
  name          = "COMM-CL01"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 분산스위치 정의
data "vsphere_distributed_virtual_switch" "distributed_switch" {
  name          = "COMM-CL01-vDS"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 네트워크 어댑터 정의
data "vsphere_network" "network_91" {
  name          = "LS-OV-10.10.91.x-DMZ"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}

# 가상머신 생성을 위한 템플릿 지정
data "vsphere_virtual_machine" "template" {
  name          = "dgx-default-template"
  datacenter_id = data.vsphere_datacenter.datacenter.id
}
 