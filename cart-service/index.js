const express = require('express');
const app = express();
const port = 5002;

app.get('/cart', (req, res) => {
  res.json({ cart: ["Laptop", "Phone"] });
});

app.listen(port, () => {
  console.log(`Cart service running on port ${port}`);
});
