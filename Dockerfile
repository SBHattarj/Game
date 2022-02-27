FROM gitpod/workspace-full-vnc:branch-jx-ubuntu-focal


# install dependencies
RUN apt-get update \
    && apt-get install -y libx11-dev libxkbfile-dev libsecret-1-dev libgconf2-dev libnss3 libgtk-3-dev libasound2-dev twm \
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* \
    && cd /home/gitpod/.pyenv/plugins/python-build/../.. && git pull && cd - \
    && pyenv install 3.10.2 && pyenv local 3.10.2 \
    && pip install pygame mypy numpy \
