FROM node:18

WORKDIR /app
COPY index.js .

RUN npm init -y && npm install express cors

EXPOSE 5002
CMD ["node", "index.js"]
