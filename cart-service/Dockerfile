FROM node:18

WORKDIR /app
COPY index.js .
RUN npm init -y
RUN npm init -y && npm install express

EXPOSE 5002
CMD ["node", "index.js"]
