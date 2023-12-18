FROM node:18-alpine

WORKDIR /app

COPY package*.json .

ARG NODE_ENV 

RUN if [ "$NODE_ENV" = "production" ]; then npm ci --only=production; else npm ci; fi

COPY . .

# This EXPOSE is entirely for documentation purposes. This doesn't actually force the PORT to be 3000.
EXPOSE $PORT

CMD ["npm","run","prod"]