#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

if (!url) {
  console.log('Error: no URL');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    process.exit(1);
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach((task) => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
