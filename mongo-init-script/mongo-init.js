print("Running mongo-init.js script");
db.createCollection("client_portfolios");

const data = cat('/test-data/client_portfolio.json');

// Parse the JSON data
const jsonData = JSON.parse(data);

// Insert the JSON data into the collection
db.client_portfolios.insertMany(jsonData);
