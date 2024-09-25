function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
	throw new Error('Jobs is not an array');
    }
    for (const job of jobs) {
	const newJob = queue.create('push_notification_code_3', job);
	newJob.save((err) => {
	    if (err) {
	    }
	    else {
		console.log(`Notification job created: ${newJob.id}`);
	    }
	});
	newJob.on('completed', (res) => {
	    console.log(`Notification job ${newJob.id} completed`);
	});

	newJob.on('failed', (err) => {
	    console.log(`Notification job ${newJob.id} failed: ${err}`);
	});

	newJob.on('progress', (percent) => {
	    console.log(`Notification job ${newJob.id} ${percent}% complete`);
	});
    }
}

export default createPushNotificationsJobs;
