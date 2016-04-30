FROM debian
# Step 2 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject && touch /root/.bash_history
# Step 3 done
WORKDIR /myproject
# Step 4 done
RUN git clone https://github.com/ianmiell/git-clone-reset-tutorial && echo 'git clone https://github.com/ianmiell/git-clone-reset-tutorial && cd /myproject/git-clone-reset-tutorial' >> /root/.bash_history
# Step 5 done
WORKDIR /myproject/git-clone-reset-tutorial
# Step 6 done
RUN mkdir /myproject/git-clone-reset-tutorial-clone && echo 'mkdir /myproject/git-clone-reset-tutorial-clone && cd /myproject/git-clone-reset-tutorial-clone' >> /root/.bash_history
# Step 7 done
WORKDIR /myproject/git-clone-reset-tutorial-clone
# Step 8 done
RUN git clone /myproject/git-clone-reset-tutorial && echo 'git clone /myproject/git-clone-reset-tutorial' >> /root/.bash_history
# Step 9 done
WORKDIR /myproject/git-clone-reset-tutorial-clone/git-clone-reset-tutorial
# Step 10 done
RUN rm -rf * && echo 'rm -rf *' >> /root/.bash_history
# Step 11 done
RUN git add . && echo 'git add .' >> /root/.bash_history
# Step 12 done
RUN git reset --soft && echo 'git reset --soft' >> /root/.bash_history
# Step 13 done
RUN git reset --hard && echo 'git reset --hard' >> /root/.bash_history
# Step 14 done
CMD /bin/bash
# Step n done
