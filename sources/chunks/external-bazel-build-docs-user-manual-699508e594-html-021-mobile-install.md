---
source_name: "External Linked Documentation"
source_url: "https://bazel.build/docs/user-manual"
source_path: "sources/raw/external/bazel-build-docs-user-manual-699508e594.html"
license_ref: ""
---

## Miscellaneous commands and options

### `mobile-install`

The `mobile-install` command installs apps to mobile devices. Currently only Android devices running ART are supported.

See bazel mobile-install for more information.
 **Note:** This command does not install the same thing that `bazel build` produces: Bazel tweaks the app so that it can be built, installed and re-installed quickly. This should, however, be mostly transparent to the app.
The following options are supported:

#### `--incremental`

If set, Bazel tries to install the app incrementally, that is, only those parts that have changed since the last build. This cannot update resources referenced from `AndroidManifest.xml`, native code or Java resources (such as those referenced by `Class.getResource()`). If these things change, this option must be omitted. Contrary to the spirit of Bazel and due to limitations of the Android platform, it is the **responsibility of the user** to know when this command is good enough and when a full install is needed.

If you are using a device with Marshmallow or later, consider the `--split_apks` flag.

#### `--split_apks`

Whether to use split apks to install and update the application on the device. Works only with devices with Marshmallow or later. Note that the `--incremental` flag is not necessary when using `--split_apks`.

#### `--start_app`

Starts the app in a clean state after installing. Equivalent to `--start=COLD`.

#### `--debug_app`

Waits for debugger to be attached before starting the app in a clean state after installing. Equivalent to `--start=DEBUG`.

#### `--start=_start_type_`

How the app should be started after installing it. Supported _start_type_s are:

- `NO` Does not start the app. This is the default.
- `COLD` Starts the app from a clean state after install.
- `WARM` Preserves and restores the application state on incremental installs.
- `DEBUG` Waits for the debugger before starting the app in a clean state after install.
 **Note:** If more than one of `--start=_start_type_`, `--start_app` or `--debug_app` is set, the last value is used.
#### `--adb=path`

Indicates the `adb` binary to be used.

The default is to use the adb in the Android SDK specified by `--android_sdk`.

#### `--adb_arg=serial`

Extra arguments to `adb`. These come before the subcommand in the command line and are typically used to specify which device to install to. For example, to select the Android device or emulator to use:

```go
% bazel mobile-install --adb_arg=-s --adb_arg=deadbeef

```

invokes `adb` as

```go

adb -s deadbeef install ...

```

#### `--incremental_install_verbosity=number`

The verbosity for incremental install. Set to 1 for debug logging to be printed to the console.
