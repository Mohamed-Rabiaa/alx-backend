import { createClient } from 'redis';

(async () => {
    const client = createClient();
    
    client.on('error', (err) => {
        console.log(`Redis client not connected to the server: ${err.toString()}`);
    });
    
    client.on('connect', () => {
        console.log('Redis client connected to the server');
    });
    
    await client.connect();
    
    async function setNewSchool(schoolName, value) {
	try {
            const result = await client.set(schoolName, value);
            console.log('Reply:', result);
	} catch (err) {
        console.error(`Error setting ${schoolName}: ${err.toString()}`);
	}
    }

    async function displaySchoolValue(schoolName) {
        return client.get(schoolName);
    }
    
    const value1 = await displaySchoolValue('Holberton');
    console.log(value1);
    await setNewSchool('HolbertonSanFrancisco', '100');
    const value2 = await displaySchoolValue('HolbertonSanFrancisco');
    console.log(value2);

    const key = 'HolbertonSchools';
    
    async function setHashValues(key, field, value) {
	try {
	    const result = client.hSet(key, field, value);
	    console.log('Replay: 1');
	} catch (err) {
	    console.log(`Error setting hashvalue: ${value} for field: ${field} on key: ${key}`);
	}
    }

    async function getAllHashValues(key) {
	const allValues = await client.hGetAll(key);
	console.log(allValues);
    }

    await setHashValues(key, 'Portland', 50);
    await setHashValues(key, 'Seattle', 80);
    await setHashValues(key, 'New York', 20);
    await setHashValues(key, 'Bogota', 20);
    await setHashValues(key, 'Cali', 40);
    await setHashValues(key, 'Paris', 2);

    await getAllHashValues(key);
})();
