//Environment Variables
var port = 8080; // Port of server
//var dbPassword = process.env.Db;
//Libraries
var getenv = require('getenv'); // Library for Enviroment Variables, Used for Db Conn
var mysql = require('promise-mysql'); // Mysql Library, With Node Promises
var sha512 = require('sha512'); // Sha512 Library, Sha512 is a hash
var bodyParser = require('body-parser'); // Library for parsing data
var jsonParser = bodyParser.json(); // Using Data type Json
var cors = require("cors"); // Library for handling access headers
var express = require('express');
var mqtt = require('mqtt');// Framework for Node
//Server Setup
var app = express(); // Establishing Express App
app.use(express.logger()); // Logging Connections
app.use(cors()); // Cors to Handle Url Authentication
app.set('view engine', 'ejs');

app.use(bodyParser.json()); // Using Body Parser
app.set('jwtTokenSecret', '95FEE00F5ED3C7650C40286EE4FB44DC38C55DDFAD1B692D80443F21F4007E2146547E4F04D1EE4495D6CD597DBD70545B6AFA6F219BAC5D2E700A7DFDD3D474'); // JWT Secret
var server = app.listen(port); // Set Port
var  my_topic_name = 'CryogenicPlanet/feeds/moistureValue';
var lastestMoisture,timeRecorded;

   

  var client = mqtt.connect('mqtts://io.adafruit.com',{
    port: 8883,
    username: 'CryogenicPlanet',
    password: '26a4330925734fa2b13956ab640a066c'
  });

  client.on('connect', () => {
    client.subscribe(my_topic_name)
  });

  client.on('error', (error) => {
    console.log('MQTT Client Errored');
    console.log(error);
  });

  client.on('message', function (topic, message) {
    // Do some sort of thing here.
    // Could be GPIO related, or in my case running system commands to
    // trigger the omxplayer app to play a certain file.

    console.log(message.toString()); // for demo purposes.
    lastestMoisture = message.toString();
    timeRecorded = new Date();
  });
app.use('/',express.static("./client/"))