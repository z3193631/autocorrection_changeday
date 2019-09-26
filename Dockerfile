FROM python:3.6-slim-stretch

# Configure build
ARG VERSION=0.0.1
ARG HOME=/usr/local/flask
ARG USER=flask
ARG PORT=5000
ARG EXTRA_PIPENV_ARGS=""


ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm-256color
ENV PIP_NO_CACHE_DIR false

WORKDIR ${HOME}

# Create .bashrc
RUN touch .bashrc \
    && echo "alias ls='ls --color=auto'\n \
    alias ll='ls -l --color=auto'\n \
    alias grep='grep --color=auto'\n \
    alias egrep='egrep --color=auto'" | awk '{$1=$1}1' > .bashrc

# Install dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        build-essential \
    && useradd -s /bin/bash -d ${HOME} ${USER} \
    && chown -R ${USER}: ${HOME} \
    && pip install pip -U \
    && pip install pipenv==2018.5.18

COPY Pipfile* ./
RUN pipenv install --system --deploy ${EXTRA_PIPENV_ARGS}
RUN python -m spacy download en_core_web_md

# Purge unecessaries
RUN apt-get purge --auto-remove -yqq build-essential \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base

COPY . ${HOME}/

EXPOSE ${PORT}

USER ${USER}

ENV FLASK_APP ${HOME}/app/app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--no-reload"]
