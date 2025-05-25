const express = require('express');
const mqtt = require('mqtt');
const client = mqtt.connect('mqtt://192.168.0.177:1883');
const app = express();

const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

app.use(express.json());

client.on('connect', () => {
  console.log('Connected to MQTT broker');

  client.subscribe(['temperature', 'humidity', 'light', 'tank', 'video'], (err) => {
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
    case 'light': {
      console.log('Received light data JSON!');
      break;
    }
    case 'tank': {
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
      console.log('Received video data!');
      break;
    }
    default: {
      console.log('Received unknown data.')
    }
  }
});

module.exports = app;
