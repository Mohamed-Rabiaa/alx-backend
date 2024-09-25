import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
	queue.testMode.clear(); 
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should display an error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(Error, 'Jobs is not an array');
    });

    it('should create two new jobs to the queue', () => {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234' },
            { phoneNumber: '4153518781', message: 'This is the code 5678' }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });

    it('should log the job creation and completion', (done) => {
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234' },
            { phoneNumber: '4153518781', message: 'This is the code 5678' }
        ];

        const log = console.log;
        const logMessages = [];
        console.log = (message) => logMessages.push(message);

        createPushNotificationsJobs(jobs, queue);

        expect(logMessages).to.include(`Notification job created: 1`);
        expect(logMessages).to.include(`Notification job created: 2`);

        console.log = log;

        done();
    });
});
