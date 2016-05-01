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
			'3f72901f994d963b000568ce81189a5d',
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
			'''Create a new folder called /myproject/git-clone-reset-tutorial-clone and move into it. ''',
			'1d38b5774769d2d582f8c37630013b6f',
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
			'''Now clone the repository from the previous folder (/myproject/git-clone-reset-tutorial), and move into the newly-created copy.

Do not clone from the https address! Clone from the local folder directly.''',
			'98302ef7635896b19319e126d146ad66',
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
			'8080dd76e8d1363731040828f88983a6',
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
			'19c23679dc326fd54455dcb2996b6436',
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
			'f04cfe65eca750dcfd949b275db358f6',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git reset --soft'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(git status -s) <(pwd)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_12',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_12'
			}
		)
		shutit.challenge(
			'''That didn't do very much at all! 
A soft reset doesn't do anything other than reset the HEAD to the commit you last checked out.
It doesn't unstage changes added, and doesn't affect your working folders or the git repository itself.
Now do a standard git reset.
''',
			'5686a4f9c4c502cd2df6fbca7dc700e4',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git reset'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(git status -s) <(pwd)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_12',
				'ok_container_name':'imiell/git-clone-reset-tutorial:step_14'
			}
		)
		shutit.challenge(
			'''That took your changes out of the staging area, but did not affect the files in your working directory at all!
Your working directory is unchanged. To revert your working directory to its pristine state, do a hard reset. Then run git status to see what happened.
''',
			'a60d881b2d0442baacd3b3e0d1e86a1e',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git reset --hard'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(ls) <(git status -s) <(pwd)',
				'context':'docker',
				'reset_container_name':'imiell/git-clone-reset-tutorial:step_14',
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
