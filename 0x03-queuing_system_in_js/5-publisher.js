import { createClient } from 'redis';


(async () => {
    const publisher = createClient();
    
    async function setUpPublisher() {
	publisher.on('connect', () => {
	    console.log('Redis client connected to the server');
	});
	publisher.on('error', (err) => {
	    console.log(`Redis client not connected to the server: ${err.toString()}`);
	});
	await publisher.connect();
    }
    
    async function publishMessage(message, time) {
	setTimeout(() => {
	    console.log(`About to send ${message}`);
	}, time);
	await publisher.publish('holberton school channel', message);
    }

    await setUpPublisher();
    await publishMessage("Holberton Student #1 starts course", 100);
    await publishMessage("Holberton Student #2 starts course", 200);
    await publishMessage("KILL_SERVER", 300);
    await publishMessage("Holberton Student #3 starts course", 400);

    publisher.quit();
})();
