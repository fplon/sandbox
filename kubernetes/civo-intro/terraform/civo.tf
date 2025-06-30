data "civo_size" "xsmall" {
	filter {
		key = "name"
		values = ["g4s.kube.xsmall"]
		match_by = "re"
	}
}

resource "civo_kubernetes_cluster" "k8s_intro" {
	name = "k8s_intro"
	applications = ""
	firewall_id = civo_firewall.fw_intro.id
	pools {
		label = "pools_intro"
		size = element(data.civo_size.xsmall.sizes, 0).name
		node_count = 3
	}
}

resource "civo_network" "network_intro" {
	label = "network_intro"
}

	resource "civo_firewall" "fw_intro" {
	name = "fw_intro"
	network_id = civo_network.network_intro.id
	create_default_rules = false
	ingress_rule {
		label = "http"
		protocol = "tcp"
		port_range = "80"
		cidr = ["0.0.0.0/0"]
		action = "allow"
	}
	ingress_rule {
		label = "https"
		protocol = "tcp"
		port_range = "443"
		cidr = ["0.0.0.0/0"]
		action = "allow"
	}
	ingress_rule {
		label = "api"
		protocol = "tcp"
		port_range = "6443"
		cidr = ["0.0.0.0/0"]
		action = "allow"
	}
}

# resource "civo_firewall_rule" "kubernetes_http" {
# 	firewall_id = civo_firewall.fw_intro.id
# 	protocol = "tcp"
# 	start_port = "80"
# 	end_port= "80"
# 	cidr = ["0.0.0.0/0"]
# 	direction = "ingress"
# 	action = "allow"
# 	label = "kubernetes_http"
# }
#
# resource "civo_firewall_rule" "kubernetes_https" {
# 	firewall_id = civo_firewall.fw_intro.id
# 	protocol = "tcp"
# 	start_port = "443"
# 	end_port= "443"
# 	cidr = ["0.0.0.0/0"]
# 	direction = "ingress"
# 	action = "allow"
# 	label = "kubernetes_https"
# }
#
# resource "civo_firewall_rule" "kubernetes_api" {
# 	firewall_id = civo_firewall.fw_intro.id
# 	protocol = "tcp"
# 	start_port = "6443"
# 	end_port= "6443"
# 	cidr = ["0.0.0.0/0"]
# 	direction = "ingress"
# 	action = "allow"
# 	label = "kubernetes_api"
# }

