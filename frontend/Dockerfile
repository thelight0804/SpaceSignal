# base image
FROM node:24.13.0-alpine

# set work directory
WORKDIR /app

# install app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# install app
COPY . .

# final configuration
EXPOSE 5173
CMD ["npm", "run", "dev"]