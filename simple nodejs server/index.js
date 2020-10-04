const express = require('express');
const bodyParser = require('body-parser');
const morgan = require("morgan");
const cors = require("cors")
const app = express();

app.use(cors())
app.use(morgan('tiny'))
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json())
require('./controllers/')(app);

const PORT = 3000;

app.listen(PORT, () => console.log('Servidor rodando na porta ' + PORT));