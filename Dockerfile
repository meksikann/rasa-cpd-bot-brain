FROM python:2.7-slim

# Run updates, install basics and cleanup
 # - build-essential: Compile specific dependencies
 # - git-core: Checkout git repos
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core openssl libssl-dev libffi6 libffi-dev curl  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# use bash always
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# workdir
WORKDIR /app
COPY . /app

# rasa stack
## rasa nlu
RUN pip install -r alt_requirements/requirements_full.txt

## spacy models
RUN pip install rasa_nlu[spacy]
CMD [ "python", "-m spacy download en_core_web_md" ]
CMD [ "python", "-m spacy link en_core_web_md en" ]

## rasa core
RUN pip install rasa_core

# volumes
VOLUME ["/app/data", "/app/models"]


EXPOSE 5005

CMD [ "python", "-m rasa_core.server -d models/current/dialogue -u models/current/nlu -o out.log" ]
