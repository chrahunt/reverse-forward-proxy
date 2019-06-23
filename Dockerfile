FROM python:3.7

COPY docker/entrypoint /entrypoint

COPY . /src

RUN pip install --upgrade pip \
 && pip install /src

ENTRYPOINT ["/entrypoint"]

CMD ["/usr/local/bin/reverse-forward-proxy"]
