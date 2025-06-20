#!/usr/bin/env python3

import ansible_runner

def process_event(event):
    # Process the event here
    if 'event' in event:
        if event['event'] == 'runner_on_ok':
            print(f"Task succeeded: {event['event_data']['task']}")
            # You can add additional processing logic here
        elif event['event'] == 'runner_on_failed':
            print(f"Task failed: {event['event_data']['task']}")
            # Additional failure handling logic
        elif event['event'] == 'runner_on_skipped':
            print(f"Task skipped: {event['event_data']['task']}")
            # Additional skipped handling logic

# Run the Ansible playbook
r = ansible_runner.run(private_data_dir='config', playbook='playbook.yaml', event_handler=process_event)
print(f"Playbook finished with status: {r.status}, return code: {r.rc}")

#r = ansible_runner.run(private_data_dir='config', playbook='playbook.yaml')

#print("{}: {}".format(r.status, r.rc))
#
#print(r.events)
#
#for each_host_event in r.events:
#    print(each_host_event['event'])
#
#print("Final status:")
#print(r.stats)
