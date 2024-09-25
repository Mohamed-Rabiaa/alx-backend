const kue = require('kue');
const queue = kue.createQueue({name: 'push_notification_code'});

const data = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', data);
job.save((err) => {
    if (err) {
	console.log('Failed to create the job:', err);
    } else {
	console.log(`Notification job created: ${job.id}`);
    }
});
job.on('failed', (err) => {
    console.log('Notification job failed');
});

job.on('complete', (res) => {
    console.log('Notification job completed');
});
