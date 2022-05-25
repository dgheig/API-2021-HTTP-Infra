'use strict';

const express = require('express');
const Chance = require('chance');
const chance = new Chance();

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

function generateStudents() {
  var numberOfStudents = chance.integer({
    min: 0,
    max: 10,
  });
  // console.log(numberOfStudents);
  var students = [];
  for(let i = 0; i < numberOfStudents; ++i) {
    var gender = chance.gender();
    var birthyear = chance.year({
      min: 1986,
      max: 1996,
    });
    students.push({
      firstName: chance.first({gender: gender}),
      lastName: chance.last(),
      gender: gender,
      birthday: chance.birthday({year: birthyear})
    });
  }
  // console.log(students);
  return students;
};

// App
const app = express();
app.get('/', (req, res) => {
  console.log("Requested")
  res.send(generateStudents());
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
