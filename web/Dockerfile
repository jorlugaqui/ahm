FROM node:lts-alpine

ENV NODE_ENV development
ENV VUE_APP_API_HOST ${VUE_APP_API_HOST}

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json package.json 
RUN npm install
RUN npm install -g @vue/cli

COPY . /app
WORKDIR /app

CMD ["npm", "run", "serve"]
