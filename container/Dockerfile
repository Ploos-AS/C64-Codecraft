FROM debian:13-slim

RUN sed -i 's/Components: main/Components: main contrib/' /etc/apt/sources.list.d/debian.sources \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      64tass \
      acme \
      cc65 \
      make \
      python3 \
      xvfb \
      default-jre-headless \
      vice \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY tools/c64cc /usr/local/bin/c64cc
RUN chmod +x /usr/local/bin/c64cc

CMD ["c64cc", "doctor"]
