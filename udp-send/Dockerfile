# Larger linux distro
FROM python:3.8

# Alpine is a smaller Linux distro
# FROM python:3.8-alpine	

WORKDIR '/app'
ADD ./udp-send.py ./

# Set ip and port args for python script using env vars
# -u option for Pyton allows print to terminal that runs container
CMD python -u udp-send.py $destip $destport


