# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.154.2/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Node.js
ARG INSTALL_NODE="true"
ARG NODE_VERSION="lts/*"
RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi


ENV VIRTUAL_ENV=/workspaces/beam
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN curl -sSL https://sdk.cloud.google.com > /tmp/install.sh && bash /tmp/install.sh --install-dir=/workspaces --disable-prompts

RUN echo "" >> /home/vscode/.bashrc
RUN echo "# The next line updates PATH for the Google Cloud SDK." >> /home/vscode/.bashrc
RUN echo "if [ -f '/workspaces/google-cloud-sdk/path.bash.inc' ]; then . '/workspaces/google-cloud-sdk/path.bash.inc'; fi" >> /home/vscode/.bashrc
RUN echo "" >> /home/vscode/.bashrc
RUN echo "# The next line enables shell command completion for gcloud." >> /home/vscode/.bashrc
RUN echo "if [ -f '/workspaces/google-cloud-sdk/completion.bash.inc' ]; then . '/workspaces/google-cloud-sdk/completion.bash.inc'; fi" >> /home/vscode/.bashrc

ENV PATH $PATH:/workspaces/google-cloud-sdk/bin

WORKDIR /workspaces