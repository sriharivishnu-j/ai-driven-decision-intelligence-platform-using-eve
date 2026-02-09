# Milvus Initialization
from pymilvus import connections, Milvus

connections.connect("default", host="localhost", port="19530")
milvus_client = Milvus("default")

# TODO: Initialize collection