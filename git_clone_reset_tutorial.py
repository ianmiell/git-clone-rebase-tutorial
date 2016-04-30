from shutit_module import ShutItModule

class git_clone_reset_tutorial(ShutItModule):


	def build(self, shutit):
		shutit.send('cd /myproject')
		shutit.challenge(
			'''In this tutorial you will be asked to clone a git repo, will mess
it up by deleting items, and then be asked to restore state using git reset.

You have a full bash shell, so can use vi, less, man etc..

If any tools are missing or there are bugs raise a github request or contact
@ianmiell on twitter.

CTRL-] (right angle bracket) to continue.
''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['Hit CTRL-]'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'echo 1',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_4',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_4'
			}
		)
		shutit.challenge('''Clone this repo: https://github.com/ianmiell/git-clone-reset-tutorial move into the git-clone-reset-tutorial folder.
''',
			'6e778f4feb9b52c05058b5a9f1a492a3',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['Hit CTRL-]'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(git status) <(pwd)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_4',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_6'
			}
		)
		shutit.challenge(
			'''Create a folder called /myproject/git-clone-reset-tutorial and move into it. ''',
			'763444ab57fa9c117159456634396f86',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['mkdir /myproject/git-clone-reset-tutorial-clone && cd /myproject/git-clone-reset-tutorial-clone'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(pwd)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_6',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_8'
			}
		)
		shutit.challenge(
			'''Now clone the repository from the previous folder (/myproject/git-clone-reset-tutorial), and move into the newly-created copy.''',
			'838c4ec4d8b3a5eaad3b6134f3c03314',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git clone /myproject/git-clone-reset-tutorial && cd git-clone-reset-tutorial'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(git status) <(cat .git/config | grep -w url)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_8',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_10'
			}
		)
		shutit.challenge(
			'''Now run rm -rf *. Go on, I dare you!''',
			'6074e2d7436c87ac94159582f178e024',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['rm -rf *'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(pwd) <(git status)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_10',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_11'
			}
		)
		shutit.challenge(
			'''git add your changes ready to commit!
Then run git status to see what can be committed.
''',
			'1',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git add .'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'git status -s',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_11',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_12'
			}
		)
		shutit.challenge(
			'''Do a soft git reset, then run git status to see what happened.
''',
			'1',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git reset --soft'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'git status -s',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_12',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_13'
			}
		)
		shutit.challenge(
			'''That only took your changes out of the staging area! Your working directory is unchanged. To revert your working directory to its pristine state, do a hard reset. Then run git status to see what happened.
''',
			'1',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git reset --hard'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'echo 1',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_13',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_14'
			}
		)
		shutit.pause_point('Tutorial complete! Feel free to mess around at the back :)')
		return True


def module():
	return git_clone_reset_tutorial(
		'tk.shutit.git_clone_reset_tutorial', 1845506479.0001,
		description='',
		maintainer='',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)
