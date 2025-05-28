const express = require('express');
const mqtt = require('mqtt');
const WebSocket = require('ws');
const fs = require('fs');

const app = express();
const wss = new WebSocket.Server({ port: 8080 });
//const client = mqtt.connect('mqtt://localhost:1883'); // DOCKER
const client = mqtt.connect('mqtt://192.168.0.177:1883');   // LAPTOP

app.use(express.json());

client.on('connect', () => {
  console.log('Connected to MQTT broker');

  client.subscribe(['temperature', 'humidity', 'tank', 'video'], (err) => {
    if (err) {
      console.error('Failed to subscribe:', err);
    } else {
      console.log('Subscribed to topics');
    }
  });
});

client.on('error', (err) => {
  console.error('MQTT connection error:', err);
});

client.on('close', () => {
  console.log('MQTT connection closed');
});

client.on('message', (topic, message) => {
  switch (topic) {
    case 'temperature': {
      const payload = message.toString();
      wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify({
            type: 'temperature',
            data: payload
          }));
        }
      });
      break;
    }
    case 'humidity': {
      const payload = message.toString();
      wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify({
            type: 'humidity',
            data: payload
          }));
        }
      });
      break;
    }
    case 'tank': {
      console.log("received tank data")
      const payload = message.toString();
      wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(JSON.stringify({
            type: 'tank',
            data: payload
          }));
        }
      });
      break;
    }
    case 'video': {
      //latestImage = message;
      fs.writeFileSync('src/assets/received.jpg', message);
      break;
    }
  }
});

/*
setInterval(() => {
  if (latestImage) {
    fs.writeFileSync('src/assets/received.jpg', latestImage);
    latestImage = null;
  }
}, 1000);
*/

module.exports = app;
