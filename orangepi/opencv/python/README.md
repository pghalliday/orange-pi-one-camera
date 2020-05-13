# python

Some tests of OpenCV using python

## Accessing the camera using `cv2.VideoCapture(0)`

This doesn't work directly so we use a video loopback driver from https://github.com/umlaeute/v4l2loopback

```
git clone https://github.com/umlaeute/v4l2loopback
cd v4l2loopback/
make
sudo make install
sudo depmod -a
sudo modprobe v4l2loopback
```

This will add a `/dev/video1` device

We also add the following lines to our `/etc/rc.local` to load on reboot

```
sleep 5
modprobe v4l2loopback
```

Then we'll use `vidcopy` to create a virtual video output that `cv2.VideoCapture` can read

```
sudo apt install libv4l-dev
git clone https://github.com/lhelontra/vidcopy
cd vidcopy/
gcc vidcopy.c -o vidcopy
```

It is then possible to copy the video output from `/dev/video0` to `/dev/video1` using

```
./vidcopy -w 800 -h 600 -r 30 -i /dev/video0 -o /dev/video1 -f UYVY
```
