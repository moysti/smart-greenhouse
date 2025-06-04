const express = require('express');
const mqtt = require('mqtt');
const WebSocket = require('ws');
const fs = require('fs');
const cors = require('cors');

const app = express();
const wss = new WebSocket.Server({ port: 8080 });
//const client = mqtt.connect('mqtt://localhost:1883'); // DOCKER
const client = mqtt.connect('mqtt://192.168.0.177:1883');   // LAPTOP

app.use(express.json());
app.use(cors({
  origin: 'http://localhost:5173',
  methods: ['GET', 'POST'],
  credentials: true,
}));

client.on('connect', () => {
  console.log('Connected to MQTT broker');

  client.subscribe(['greenhouse/temp', 'greenhouse/humidity', 'greenhouse/waterlevel', 'video'], (err) => {
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
    case 'greenhouse/temp': {
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
    case 'greenhouse/humidity': {
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
    case 'greenhouse/waterlevel': {
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

app.post('/publish', (req, res) => {
  const { topic, message } = req.body;

  if (!topic || !message.toString()) {
    return res.status(400).json({ error: 'Missing topic or message' });
  }

  client.publish(topic, message.toString(), (err) => {
    if (err) {
      console.error('MQTT publish error: ', err);
      return res.status(500).json({ error: 'MQTT publish failed' });
    }
    res.json({ success: true });
  });
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
