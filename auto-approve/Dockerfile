FROM node:22-alpine
LABEL description="Auto-approve OpenClaw device pairing requests"

# Install openclaw globally (match host version)
RUN npm install -g openclaw@2026.6.6

# Copy polling script
COPY poller.cjs /usr/local/bin/poller.cjs

WORKDIR /root

CMD ["node", "/usr/local/bin/poller.cjs"]
