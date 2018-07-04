#!/usr/bin/python3

#port for indexing server
serv_port=5016

#port and shared directory pair for upto 6 clients

peer_1_port=6025
peer_1_path='peer_1_sharedFolder/*'

peer_2_port=6026	
peer_2_path='peer_2_sharedFolder/*'

peer_3_port=6027
peer_3_path='peer_3_sharedFolder/*'


#PS edit port if they are already used in the system
# serv_port is for indexing server
# peer_1_port for all client/peer port