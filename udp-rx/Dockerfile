# Larger linux distro (but has bash)
FROM python:3.8

# Alpine is a smaller Linux distro (but no bash)
# FROM python:3.8-alpine	

WORKDIR '/app'
ADD ./udp-rx.py ./

# Set port arg for python script using env vars
# -u option for Pyton allows print to terminal that runs container
CMD python -u udp-rx.py $myport



