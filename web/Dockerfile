FROM node:lts-alpine

ENV NODE_ENV development

ENV PATH /app/node_modules/.bin:$PATH
COPY package.json package.json 
RUN npm install
RUN npm install -g @vue/cli

COPY . /app
WORKDIR /app

CMD ["npm", "run", "serve"]
