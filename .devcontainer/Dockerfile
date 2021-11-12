FROM ltuml/ml-dev:vsc1-ubuntu20.04-python3.9

# linux requirements [optional]
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends build-essential

# VSC live share - I guess temporary
RUN wget -O ~/vsls-reqs https://aka.ms/vsls-linux-prereq-script && chmod +x ~/vsls-reqs && ~/vsls-reqs

# Python requirements
COPY requirements-src.txt /tmp/pip-tmp/requirements-src.txt
RUN python -m pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements-src.txt \
    && rm -rf /tmp/pip-tmp

# Python requirements for test
COPY requirements-tests.txt /tmp/pip-tmp/requirements-tests.txt
RUN python -m pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements-tests.txt \
    && rm -rf /tmp/pip-tmp

# Python requirements for visual studio code
COPY requirements-vscode.txt /tmp/pip-tmp/requirements-vscode.txt
RUN python -m pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements-vscode.txt \
    && rm -rf /tmp/pip-tmp

ENV PYTHONPATH=/home/vscode/workspace/src

USER vscode

CMD while sleep 1000; do :; done
