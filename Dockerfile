FROM ubuntu
WORKDIR /ramalo_directory
RUN touch file{1..88}.txt
CMD ["echo","hello world"]