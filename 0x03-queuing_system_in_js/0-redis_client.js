import { createClient } from 'redis';

const client = createClient()
      .on('error', (err) => {
	  console.log(`Redis client not connected to the server: ${err.toString()}`);
      })
      .on('connect', () => {
	  console.log('Redis client connected to the server');
      })
      .connect();
