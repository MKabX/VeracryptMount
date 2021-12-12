# VeracryptMount

Plugin for [fman.io](https://fman.io) that enables you to mount and unmount Veracrypt containers directly from [fman.io](https://fman.io).

You can install this plugin by pressing `<shift+cmd+p>` to open the command pallet. Then type `install plugin`. Look for the `VeracryptMount` plugin and select it.

## Disclaimer

In theory this plugin works on every operation system, however I only tested it under MacOS. If there are issues under Linux or Windows please post an Issue.

## Mount a Veracrypt Container

The functions are all available via the Command Pallete. Search for the container file you want to mount. Then just press `<shift+cmd+p>` and search for `Mount veracrypt volume`. If the container you want to mount is a Truecrypt container `Mount veracrypt volume in true crypt mode` is available. A dialogue will pop up where you can enter the password of the container. If the password was correct, the container should be mounted.

## Unmount a Vercraypt Container

To unmount a container, enter the Command Pallete by pressing `<shift+cmd+p>` and searching for `Unmount veracrypt volume`. A dialogue will appear that lists all your currently mounted container files. Select the one you would like to dismount and it will be dismounted.

## Unmount all Vercraypt Container

As a convenience feature `Unmount all veracrypt volumes` is available which will unmount all currently mounted containers.