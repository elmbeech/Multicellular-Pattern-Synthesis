# Multicellular Pattern Synthesis Docker

## Short Description

This container replicates the computational environemet for the publication: Briers, Libby,Haghighi, Joy, Conklin, Belta, and McDevitt

## Container Contributors (alphabetical order)
- [Demarcus Briers](https://github.com/dmarcbriers)
- Iman Haghighi
- David Joy
- Ashley Libby


## Quickstart
If you already have docker installed on your computer you can run the following commands to pull a docker image from dockerhub. If you are not familiar with docker there is a cheetsheet [here](https://github.com/wsargent/docker-cheat-sheet): To pull the image from dockerhub make sure your create a free account, then enter you login credential from the command line using:

```docker login -u <username> -p```

Once you have entered you login credential on the docker command line, make sure you are in the root folder of the repository to have access to all files from inside the docker container.

```docker pull dmarcbriers/mc-pattern-synthesis:latest ```

If that command was sucessful you can launcha docker container using the command below. Note, sometimes being on a VPN prevents docker from working so try disconnecting from your VPN client if docker is not working.

```docker run --rm -v ${PWD}:/home/ubuntu/:rw -it dmarcbriers/mc-pattern-synthesis:latest /bin/bash```

This will launch an interactive terminal with all necessary software. See the README in the model directiory for further instructions on running simulations.

## Build Instructions
If a ready made image was not avaible from dockerhub, you can quickly rebuild the image using the command (make sure you are inside of the docker directory when running the build command, and dont forget the period at the end). This took about 10 minutes to build on a latpop with i7 processor, 32GB RAM, and a WiFi conenction:

```docker build --tag="dmarcbriers/mc-pattern-synthesis:latest" .```

```cd ../ ```

```docker run --rm -v ${PWD}:/home/ubuntu/:rw  -it dmarcbriers/mc-pattern-synthesis:latest /bin/bash```

If docker was successful you will notice a `#` sign at the enf of your terminal prompt. Since the user of this docker is `ubuntu` change to the users home folder to access local files on your systems.

`cd /home/ubuntu/`

Now you can pull up the help documentation to run a simulation from the model folder:
```python3 MorpheusSetup.py -h ```

You can also perform other analysis from our paper in the `image_segmentation/` and `synthesis/` folders.
