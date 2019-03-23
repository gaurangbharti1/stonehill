var mqtt = require('mqtt'); // Framework for Node
var my_topic_name = 'CryogenicPlanet/feeds/moistureValue';

var client = mqtt.connect('mqtts://io.adafruit.com', {
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

client.on('message', function(topic, message) {
    // Do some sort of thing here.
    // Could be GPIO related, or in my case running system commands to
    // trigger the omxplayer app to play a certain file.

    console.log(message.toString()); // for demo purposes.
});