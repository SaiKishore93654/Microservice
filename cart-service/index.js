const express = require('express');
const cors = require('cors');
const app = express();
const port = 5002;

app.use(cors());

app.get('/cart', (req, res) => {
  res.json({ cart: ["Laptop", "Phone"] });
});

app.listen(port, () => {
  console.log(`Cart service running on port ${port}`);
});
