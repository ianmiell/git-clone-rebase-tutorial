FROM debian
# Step 2 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject && touch /root/.bash_history
# Step 3 done
WORKDIR /myproject
# Step 4 done
RUN git clone https://github.com/ianmiell/jenkins-phoenix && echo 'git clone https://github.com/ianmiell/jenkins-phoenix && cd /myproject/jenkins-phoenix' >> /root/.bash_history
# Step 5 done
WORKDIR /myproject/jenkins-phoenix
# Step 6 done
RUN mkdir /myproject/jenkins-phoenix-clone && echo 'mkdir /myproject/jenkins-phoenix-clone && cd /myproject/jenkins-phoenix-clone' >> /root/.bash_history
# Step 7 done
WORKDIR /myproject/jenkins-phoenix-clone
# Step 8 done
RUN git clone /myproject/jenkins-phoenix && echo 'git clone /myproject/jenkins-phoenix' >> /root/.bash_history
# Step 9 done
WORKDIR /myproject/jenkins-phoenix-clone/jenkins-phoenix
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
