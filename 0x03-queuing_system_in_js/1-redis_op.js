import { createClient, print } from 'redis';

(async () => {
  const client = createClient();

  client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

  await client.connect();

  function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
  }

  function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
      if (err) {
        console.error(`Error retrieving value for ${schoolName}: ${err}`);
      } else {
        console.log(value);
      }
    });
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
})();

