import inspect, os, subprocess

filename = inspect.getframeinfo(inspect.currentframe()).filename
exec_path = os.path.dirname(os.path.abspath(filename))
execfile(os.path.join(exec_path, 'helpers.py'))

parent_dirs = ['/media/Windows/Mozilla']

commands = {
    'branch': 'git branch',
    'fetch': 'git fetch upstream',
    'merge': 'git merge upstream/master',
    'checkout': 'git checkout master',
}


def repo_update(dir_name):
    print 'Entering', dir_name
    os.chdir(dir_name)
    if not os.path.exists(os.path.join(dir_name, '.git')):
        print "Not a 'git' repository! Getting out...\n"
        return

    out = exec_cmd(commands['branch'])
    idx = out.find('*')
    if 'master' not in out:
        print "'master' branch unavailable!"
        return

    if not out[idx:].startswith('* master'):
        print 'This looks like another branch. Trying to checkout to master...'
        out = exec_cmd(commands['checkout'])
        if 'Switched to branch' not in out:
            print '\033[91m Repo sync failed! Unable to switch branch!\033[0m'
            return

    out = exec_cmd(commands['fetch'])
    if 'fatal' in out:
        print '\033[91m Repo sync failed! Unable to fetch!\033[0m'
        return

    out = exec_cmd(commands['merge'])


if __name__ == '__main__':
    for parent_dir in parent_dirs:
        for repo in os.listdir(parent_dir):
            try:
                repo_update(os.path.join(parent_dir, repo))
            except KeyboardInterrupt:
                exit('Interrupted!')
