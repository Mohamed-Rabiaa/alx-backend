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
        console.error(`Error setting ${schoolName}: ${err}`);
	}
    }

    
    async function displaySchoolValue(schoolName) {
        const value = await client.get(schoolName);
        console.log(value);
    }
    
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
