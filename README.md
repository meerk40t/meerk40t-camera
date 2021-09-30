# meerk40t-camera
MeerK40t camera plugin. If you have meerk40t installed you can install the camera plugin. This gives the user access to cameras through the opencv module in Python. This plugin's job is to mediate the interactions between MeerK40t and OpenCV.

# Installing

## Pip

Since the plugin's value depends on interactions through the plugin api for MeerK40t it must be installed through pip.

* `$ pip install meerk40t-camera[cv]`

This installs the meerk40t-camera and  opencv-python-headless. 
The headless version of opencv provides all the functionality Meerk40t needs, 
so unless you are using opencv with other software that requires X11 
this is the package recommended to you to install.  

If you have a non-Meerk40t requirement for the additional functionality in one of the following opencv packages, 
then you can install the opencv-python package of your choice separately and install meerk40t camera
using the following:

* `$ pip install meerk40t-camera`

If you are installing opencv-python yourself then you can do so using one of the following commands: 

* `$ pip install opencv-python`
* `$ pip install opencv-python-headless`
* `$ pip install opencv-contrib-python`
* `$ pip install opencv-contrib-python-headless`

**Note:** Only one opencv-python package should be installed at any one time. 
If you have installed multiple versions, then you need to uninstall **all** of them
and reinstall the one you want.

## Directly

* Download into a directory:
* `$ pip install .`

## Development

To do development of meerk40t-camera you would need to load the plugin in edit mode for pip. This is because the running of Meerk40t depends on the plugin and utilizing the edits without reinstalling the plugin is extremely useful in that workflow.

* Download into a directory:
* `$ pip install -e .`

Changing something that directly changes the the registered parts of the plugins (like the `meerk40t.plugin` values). Cases where you need to force the update by pip.
* `$ pip install -U -e .`



# Plugin

Once installed access is done through the CameraInterface window in meerk40t which is part of MeerK40t rather than meerk40t-camera. This is so that the meerk40t-camera plugin can interact with pure console interactions and does not require a gui.

```
--- image-array Commands ---
image           image <operation>*

  --- Base Commands ----
 camera\d*       camera commands and modifiers.
  
  --- camera Commands ---
background      set background image
export          export camera image
fisheye         fisheye subcommand
list            list camera settings
perspective     perspective (set <#> <value>|reset)
set             set a particular setting in the camera
start           Start Camera.
stop            Stop Camera
```

Are the relevant camera commands. The image of type image-array is because the `export` camera command has an image-array type which is a non-PIL image format (since pil is not a requirement) but a simple numpy array (which is part of opencv).

```
export 
 	(camera) -> export -> (image-array)
```
This sends the image to the scene, but if you wish to modify it or save it to disk you need the `image` command to convert the output here to a PIL image.

The base command takes an index for the camera. This can be any index and it will make any number of non-overlapping camera settings within that profile. Omitting the number uses the default that was used last time. `camera start stop` for example would turn on the camera and turn it back off. You can also set the `perspective` and `fisheye` values for the camera. 

The `set` command passes particular settings to the opencv instance which permits setting a number of different values. This passes the setting to the camera but does little beyond trying to figure out the meaning and it's highly camera dependent as to whether that setting is used or does anything.
