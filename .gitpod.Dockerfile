FROM gitpod/workspace-full

RUN sudo apt-get update && \
    sudo apt-get install -y python3-sphinx && \
    pip install --upgrade pip && \
    pip install setuptools wheel tox twine sphinx sphinx-rtd-theme && \
    pip install flask flask-restful requests && \
    sudo rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]